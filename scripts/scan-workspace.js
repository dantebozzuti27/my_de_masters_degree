#!/usr/bin/env node
/**
 * Workspace Scanner
 * 
 * Scans the workspace folder and generates a manifest of completed exercises.
 * This runs at BUILD TIME so progress is based on actual committed code.
 * 
 * Completion criteria:
 * - Template placeholder values have been replaced with real implementations
 * - Empty strings, zeros, and placeholder returns are NOT complete
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const WORKSPACE_DIR = path.join(__dirname, '..', 'workspace');
const OUTPUT_FILE = path.join(__dirname, '..', 'src', 'lib', 'workspace-manifest.json');

function hashFile(content) {
  return crypto.createHash('md5').update(content).digest('hex').substring(0, 8);
}

// Patterns that indicate INCOMPLETE code (placeholders)
const INCOMPLETE_PATTERNS = [
  // Empty variable assignments meant to be filled in
  /^\s*my_name\s*=\s*""\s*#/m,
  /^\s*my_age\s*=\s*0\s*#/m,
  /^\s*my_height\s*=\s*0\.0\s*#/m,
  /^\s*is_learning_python\s*=\s*False\s*#/m,
  /^\s*name\s*=\s*""\s*#.*Replace/m,
  
  // Pass statements indicating TODO
  /^\s*pass\s*$/m,  // Just 'pass' on its own line
  /^\s*pass\s*#/m,  // pass with comment
  
  // Return statements with placeholder values
  /return\s*\{\s*\}/,  // return {}
  /return\s*\[\s*\]/,  // return []
  
  // Empty list/dict variable followed by return
  /result\s*=\s*\[\s*\]\s*\n\s*return\s+result/m,
  /result\s*=\s*\{\s*\}\s*\n\s*return\s+result/m,
  
  // Return dicts with empty string values (template pattern)
  /'uppercase':\s*''/,
  /'lowercase':\s*''/,
  /'as_int':\s*0,/,
  /'sum':\s*0,/,
  /'count':\s*0,/,
  
  // Generic placeholder returns
  /return\s*""\s*$/m,
  /return\s*''\s*$/m,
  /return\s*None\s*$/m,
];

// Patterns that indicate COMPLETE code
const COMPLETE_PATTERNS = [
  // Actual return with computed value
  /return\s+\w+\s*\+/,  // return a + b
  /return\s+\w+\s*%/,   // return n % 2
  /return\s+\w+\s*\*/,  // return a * b
  /return\s+text\./,    // return text.upper() etc
  /return\s+\[.*for/,   // list comprehension
  /return\s+\{.*for/,   // dict comprehension
  /return\s+True|False\s*$/m,  // explicit boolean return
  /return\s+f["']/,     // f-string return
];

function analyzeExerciseFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    
    // Count incomplete patterns found
    let incompleteCount = 0;
    for (const pattern of INCOMPLETE_PATTERNS) {
      if (pattern.test(content)) {
        incompleteCount++;
      }
    }
    
    // Count complete patterns found  
    let completeCount = 0;
    for (const pattern of COMPLETE_PATTERNS) {
      if (pattern.test(content)) {
        completeCount++;
      }
    }
    
    // Count functions with actual implementations vs placeholders
    const functionMatches = content.match(/^def \w+\(/gm) || [];
    const totalFunctions = functionMatches.length;
    
    // Look for functions with real implementations
    let completedFunctions = 0;
    const funcRegex = /def (\w+)\([^)]*\):[^]*?(?=\ndef |\n# ===|$)/g;
    let match;
    
    while ((match = funcRegex.exec(content)) !== null) {
      const funcBody = match[0];
      const funcName = match[1];
      
      // Skip test/helper functions
      if (funcName.startsWith('run_') || funcName.startsWith('check_') || 
          funcName.startsWith('test_') || funcName === 'main') {
        continue;
      }
      
      // Check if this function has placeholder patterns
      let hasPlaceholder = false;
      for (const pattern of INCOMPLETE_PATTERNS) {
        if (pattern.test(funcBody)) {
          hasPlaceholder = true;
          break;
        }
      }
      
      // Check if this function has real implementation patterns
      let hasRealCode = false;
      for (const pattern of COMPLETE_PATTERNS) {
        if (pattern.test(funcBody)) {
          hasRealCode = true;
          break;
        }
      }
      
      // Also check for real variable assignments
      if (!hasRealCode) {
        // Look for actual name assignment (not empty)
        if (/name\s*=\s*["'][^"']+["']/.test(funcBody)) {
          hasRealCode = true;
        }
      }
      
      if (hasRealCode && !hasPlaceholder) {
        completedFunctions++;
      }
    }
    
    // Determine overall completion
    // Complete if: more complete patterns than incomplete, OR specific functions done
    const isComplete = (completeCount > 0 && incompleteCount === 0) || 
                       (completedFunctions > 0 && incompleteCount < 2);
    
    return {
      complete: isComplete,
      totalFunctions,
      completedFunctions,
      incompletePatterns: incompleteCount,
      completePatterns: completeCount,
      hash: hashFile(content),
      lines: lines.length,
      path: path.relative(WORKSPACE_DIR, filePath),
      modifiedAt: fs.statSync(filePath).mtime.toISOString()
    };
  } catch (error) {
    return { 
      complete: false, 
      reason: 'File not found or unreadable',
      error: error.message
    };
  }
}

function scanWeek(weekPath) {
  const exercises = {};
  const exercisesDir = path.join(weekPath, 'exercises');
  
  if (!fs.existsSync(exercisesDir)) {
    return exercises;
  }
  
  const files = fs.readdirSync(exercisesDir).filter(f => f.endsWith('.py'));
  
  for (const file of files) {
    const filePath = path.join(exercisesDir, file);
    exercises[file] = analyzeExerciseFile(filePath);
  }
  
  return exercises;
}

function scanQuarter(quarterPath) {
  const weeks = {};
  
  if (!fs.existsSync(quarterPath)) {
    return weeks;
  }
  
  const weekDirs = fs.readdirSync(quarterPath)
    .filter(d => d.startsWith('week-'))
    .sort();
  
  for (const weekDir of weekDirs) {
    const weekPath = path.join(quarterPath, weekDir);
    const weekNum = parseInt(weekDir.replace('week-', ''));
    
    weeks[weekNum] = {
      exercises: scanWeek(weekPath)
    };
  }
  
  return weeks;
}

function scanWorkspace() {
  const manifest = {
    generatedAt: new Date().toISOString(),
    quarters: {},
    summary: {
      totalExercises: 0,
      completedExercises: 0,
      completionRate: 0
    },
    dayStatus: {}
  };
  
  const quarterDirs = [
    'q1-python-sql',
    'q2-etl-quality', 
    'q3-dbt-mastery',
    'q4-aws-foundations',
    'q5-orchestration',
    'q6-aws-advanced',
    'q7-system-design',
    'q8-interview-prep'
  ];
  
  for (const quarterDir of quarterDirs) {
    const quarterPath = path.join(WORKSPACE_DIR, quarterDir);
    const quarterNum = parseInt(quarterDir.split('-')[0].replace('q', ''));
    manifest.quarters[quarterNum] = {
      folder: quarterDir,
      weeks: scanQuarter(quarterPath)
    };
  }
  
  // Calculate summary
  for (const [qNum, quarter] of Object.entries(manifest.quarters)) {
    for (const [wNum, week] of Object.entries(quarter.weeks)) {
      for (const [fileName, exercise] of Object.entries(week.exercises)) {
        manifest.summary.totalExercises++;
        
        if (exercise.complete) {
          manifest.summary.completedExercises++;
        }
        
        // Map file to day number
        const dayMatch = fileName.match(/day(\d+)/);
        if (dayMatch) {
          const dayInWeek = parseInt(dayMatch[1]);
          const weekNum = parseInt(wNum);
          const quarterNum = parseInt(qNum);
          const weeksBeforeThisQuarter = (quarterNum - 1) * 13;
          const absoluteDay = (weeksBeforeThisQuarter + weekNum - 1) * 4 + dayInWeek;
          
          manifest.dayStatus[absoluteDay] = {
            complete: exercise.complete,
            file: exercise.path
          };
        }
      }
    }
  }
  
  manifest.summary.completionRate = manifest.summary.totalExercises > 0
    ? Math.round((manifest.summary.completedExercises / manifest.summary.totalExercises) * 100)
    : 0;
  
  return manifest;
}

function main() {
  console.log('📂 Scanning workspace for completed exercises...\n');
  
  const manifest = scanWorkspace();
  
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(manifest, null, 2));
  
  console.log('📊 Workspace Summary:');
  console.log(`   Total Exercises: ${manifest.summary.totalExercises}`);
  console.log(`   Completed: ${manifest.summary.completedExercises}`);
  console.log(`   Completion Rate: ${manifest.summary.completionRate}%\n`);
  
  // Show status
  for (const [qNum, quarter] of Object.entries(manifest.quarters)) {
    for (const [wNum, week] of Object.entries(quarter.weeks)) {
      for (const [fileName, exercise] of Object.entries(week.exercises)) {
        const status = exercise.complete ? '✅' : '⬜';
        console.log(`   ${status} Q${qNum}/W${wNum}: ${fileName}`);
        if (!exercise.complete && exercise.incompletePatterns) {
          console.log(`      └─ ${exercise.incompletePatterns} placeholder patterns found`);
        }
      }
    }
  }
  
  console.log(`\n✅ Manifest: ${OUTPUT_FILE}`);
}

main();
