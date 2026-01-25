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
// More conservative to avoid false positives on legitimate error handling code
const INCOMPLETE_PATTERNS = [
  // Empty variable assignments with comments indicating they need to be filled
  /^\s*my_name\s*=\s*""\s*#/m,
  /^\s*my_age\s*=\s*0\s*#/m,
  /^\s*my_height\s*=\s*0\.0\s*#/m,
  /^\s*is_learning_python\s*=\s*False\s*#/m,
  /^\s*name\s*=\s*""\s*#.*Replace/m,
  
  // Explicit placeholder markers ONLY if followed by pass or nothing
  // This avoids false positives when user fills in code but leaves the comment
  /# YOUR CODE HERE\s*\n\s*pass\s*$/m,
  
  // Standalone completion markers (for terminal-based exercises)
  /^# YOUR CODE HERE - DELETE/m,
  
  // Bare pass statements in functions (at first indent level only)
  // Match pass that is exactly 4 spaces indented (top of function), not nested
  /^    pass\s*$/m,  // Exactly 4 spaces = likely incomplete function
  
  // Empty result variable followed immediately by return (template pattern)
  /result\s*=\s*\[\s*\]\s*\n\s*return\s+result\s*$/m,
  /result\s*=\s*\{\s*\}\s*\n\s*return\s+result\s*$/m,
  
  // Return dicts with empty string values (template pattern - specific placeholders)
  /'uppercase':\s*''\s*,/,
  /'lowercase':\s*''\s*,/,
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
    
    // Count incomplete patterns found (count actual occurrences, not just patterns)
    let incompleteCount = 0;
    for (const pattern of INCOMPLETE_PATTERNS) {
      const globalPattern = new RegExp(pattern.source, 'gm');
      const matches = content.match(globalPattern) || [];
      incompleteCount += matches.length;
    }
    
    // Special case: allow up to 2 pass statements (exception classes are OK)
    // But if there are many pass statements, clearly incomplete
    const passMatches = content.match(/^\s{4}pass\s*$/gm) || [];
    if (passMatches.length > 3) {
      incompleteCount = passMatches.length;  // Override with actual count
    } else if (passMatches.length <= 2) {
      // Likely just exception classes - don't count as incomplete
      incompleteCount = Math.max(0, incompleteCount - passMatches.length);
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
    // Complete if: has complete patterns AND zero incomplete patterns
    // The DELETE marker must be removed for terminal-based exercises
    const isComplete = (completeCount > 0 && incompleteCount === 0);
    
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
  
  // 6-month aggressive plan structure
  const monthDirs = [
    'month1-foundations',    // Feb 2026: Days 1-35
    'month2-dbt',            // Mar 2026: Days 36-63
    'month3-airflow',        // Apr 2026: Days 64-91
    'month4-aws-cert',       // May 2026: Days 92-119
    'month5-interviews',     // Jun 2026: Days 120-147
    'month6-close'           // Jul 2026: Days 148-168
  ];
  
  for (const monthDir of monthDirs) {
    const monthPath = path.join(WORKSPACE_DIR, monthDir);
    
    // Extract month number from folder name (month1, month2, etc.)
    const numMatch = monthDir.match(/\d+/);
    const monthNum = numMatch ? parseInt(numMatch[0]) : 0;
    
    if (!fs.existsSync(monthPath)) continue;
    
    manifest.quarters[monthNum] = {
      folder: monthDir,
      weeks: scanQuarter(monthPath)
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
        // Filenames use ABSOLUTE day numbers (day1, day2, ..., day52, etc.)
        // NOT day-within-week, so we just extract the number directly
        const dayMatch = fileName.match(/day(\d+)/);
        if (dayMatch) {
          const absoluteDay = parseInt(dayMatch[1]);
          
          // If we already have a complete status for this day, don't overwrite with incomplete
          // This handles cases where old curriculum files exist alongside new ones
          const existingStatus = manifest.dayStatus[absoluteDay];
          if (!existingStatus || 
              exercise.complete || 
              (!existingStatus.complete && !exercise.complete)) {
            // Prioritize month1-foundations files over old q1- files
            const isNewCurriculum = exercise.path.startsWith('month');
            const existingIsNew = existingStatus?.file?.startsWith('month');
            
            if (!existingStatus || exercise.complete || isNewCurriculum || !existingIsNew) {
              manifest.dayStatus[absoluteDay] = {
                complete: exercise.complete,
                file: exercise.path
              };
            }
          }
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
        console.log(`   ${status} M${qNum}/W${wNum}: ${fileName}`);
        if (!exercise.complete && exercise.incompletePatterns) {
          console.log(`      └─ ${exercise.incompletePatterns} placeholder patterns found`);
        }
      }
    }
  }
  
  console.log(`\n✅ Manifest: ${OUTPUT_FILE}`);
}

main();
