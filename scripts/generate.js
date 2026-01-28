#!/usr/bin/env node
/**
 * Generate All Derived Files
 * 
 * Single source of truth: data/curriculum.json + data/progress.json
 * Generates:
 *   - src/lib/workspace-manifest.json (for Next.js dashboard)
 *   - CURRICULUM.md (for human reading)
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const CURRICULUM_FILE = path.join(ROOT, 'data', 'curriculum.json');
const PROGRESS_FILE = path.join(ROOT, 'data', 'progress.json');
const MANIFEST_OUTPUT = path.join(ROOT, 'src', 'lib', 'workspace-manifest.json');
const MARKDOWN_OUTPUT = path.join(ROOT, 'CURRICULUM.md');

function load(file) {
  return JSON.parse(fs.readFileSync(file, 'utf-8'));
}

function generateManifest(curriculum, progress) {
  const completedSet = new Set(progress.completed);
  
  const manifest = {
    generatedAt: new Date().toISOString(),
    meta: curriculum.meta,
    summary: {
      totalDays: curriculum.meta.totalDays,
      completedDays: progress.completed.length,
      completionRate: Math.round((progress.completed.length / curriculum.meta.totalDays) * 100)
    },
    months: {},
    dayStatus: {}
  };

  for (const month of curriculum.months) {
    manifest.months[month.id] = {
      name: month.name,
      weeks: {}
    };

    for (const week of month.weeks) {
      manifest.months[month.id].weeks[week.week] = {
        title: week.title,
        days: week.days.map(d => ({
          day: d.day,
          topic: d.topic,
          complete: completedSet.has(d.day)
        }))
      };

      for (const d of week.days) {
        manifest.dayStatus[d.day] = {
          complete: completedSet.has(d.day),
          topic: d.topic,
          month: month.id,
          week: week.week
        };
      }
    }
  }

  return manifest;
}

function generateMarkdown(curriculum, progress) {
  const completedSet = new Set(progress.completed);
  const lines = [];

  lines.push(`# ${curriculum.meta.title.toUpperCase()}`);
  lines.push(`## Goal: ${curriculum.meta.goal}`);
  lines.push('');
  lines.push(`**Schedule:** ${curriculum.meta.hoursPerWeek} hours/week`);
  lines.push(`**Duration:** 24 weeks (${curriculum.meta.totalDays} days)`);
  lines.push(`**Start Date:** February 2026`);
  lines.push(`**Target End Date:** July 2026`);
  lines.push('');
  lines.push('---');
  lines.push('');

  // Current Progress
  lines.push('## Current Progress');
  lines.push('');
  lines.push(`**${progress.completed.length}/${curriculum.meta.totalDays} days complete**`);
  lines.push('');

  // Find next incomplete day
  let nextDay = null;
  for (let i = 1; i <= curriculum.meta.totalDays; i++) {
    if (!completedSet.has(i)) {
      nextDay = i;
      break;
    }
  }

  if (nextDay) {
    const dayInfo = findDay(curriculum, nextDay);
    if (dayInfo) {
      lines.push(`**Next:** Day ${nextDay} - ${dayInfo.topic}`);
    }
  }
  lines.push('');
  lines.push('---');
  lines.push('');

  // Each month
  for (const month of curriculum.months) {
    lines.push(`## MONTH ${month.id}: ${month.name.toUpperCase()}`);
    lines.push('');

    if (month.project) {
      lines.push(`**Project:** ${month.project.name}`);
      lines.push(`**Stack:** ${month.project.stack.join(', ')}`);
      lines.push('');
    }

    if (month.certification) {
      lines.push(`**Certification:** ${month.certification.name} (Day ${month.certification.day})`);
      lines.push('');
    }

    for (const week of month.weeks) {
      lines.push(`### Week ${week.week}: ${week.title}`);
      lines.push('');
      lines.push('| Day | Topic | Status |');
      lines.push('|-----|-------|--------|');

      for (const d of week.days) {
        const status = completedSet.has(d.day) ? 'Done' : (d.day === nextDay ? 'Next' : '');
        lines.push(`| ${d.day} | ${d.topic} | ${status} |`);
      }
      lines.push('');
    }

    lines.push('---');
    lines.push('');
  }

  return lines.join('\n');
}

function findDay(curriculum, dayNum) {
  for (const month of curriculum.months) {
    for (const week of month.weeks) {
      for (const d of week.days) {
        if (d.day === dayNum) return d;
      }
    }
  }
  return null;
}

function main() {
  console.log('Loading data sources...');
  const curriculum = load(CURRICULUM_FILE);
  const progress = load(PROGRESS_FILE);

  console.log('Generating manifest...');
  const manifest = generateManifest(curriculum, progress);
  fs.writeFileSync(MANIFEST_OUTPUT, JSON.stringify(manifest, null, 2));

  console.log('Generating CURRICULUM.md...');
  const markdown = generateMarkdown(curriculum, progress);
  fs.writeFileSync(MARKDOWN_OUTPUT, markdown);

  console.log('');
  console.log(`Progress: ${progress.completed.length}/${curriculum.meta.totalDays} days (${manifest.summary.completionRate}%)`);
  console.log('');
  console.log('Generated:');
  console.log(`  ${MANIFEST_OUTPUT}`);
  console.log(`  ${MARKDOWN_OUTPUT}`);
}

main();
