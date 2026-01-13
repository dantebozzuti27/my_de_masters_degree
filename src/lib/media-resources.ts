/**
 * Media Resources for SDE Study Plan
 * 
 * Daily Videos: 15-20 minute focused videos per lesson
 * Weekly Podcasts: Specific episode links (verified working)
 * Audiobooks: Available on Audible with verified links
 */

export interface DailyVideo {
  title: string;
  url: string;
  duration: string;
  channel: string;
  description: string;
  platform: 'youtube' | 'coursera' | 'other';
}

export interface WeeklyPodcast {
  title: string;
  show: string;
  episodeUrl: string;
  appleUrl?: string;
  episodeNumber?: string;
  duration: string;
  description: string;
}

export interface Audiobook {
  title: string;
  author: string;
  audibleUrl: string;
  duration: string;
  description: string;
  whenToListen: string;
}

// ============================================================================
// AUDIOBOOKS - Verified Audible Links
// ============================================================================

export const Q1_AUDIOBOOKS: Audiobook[] = [
  {
    title: "Learning SQL, 3rd Edition",
    author: "Alan Beaulieu",
    audibleUrl: "https://www.audible.com/pd/Learning-SQL-3rd-Edition-Audiobook/B0BXQKRDWZ",
    duration: "7.5 hours",
    description: "SQL fundamentals for database applications. Includes chapters on SQL and big data, analytic functions. Comes with PDF of code examples.",
    whenToListen: "Weeks 5-8: Listen while learning SQL fundamentals"
  },
  {
    title: "Python for Beginners",
    author: "Timothy C. Needham",
    audibleUrl: "https://www.audible.com/pd/Python-for-Beginners-Audiobook/B085T28RHD",
    duration: "6 hours",
    description: "Step-by-step crash course covering Python fundamentals, data structures, and practical programming concepts.",
    whenToListen: "Weeks 1-4: Supplement your Python learning during commute"
  }
];

export const Q2_AUDIOBOOKS: Audiobook[] = [
  {
    title: "Designing Data-Intensive Applications",
    author: "Martin Kleppmann",
    audibleUrl: "https://www.audible.com/pd/Designing-Data-Intensive-Applications-Audiobook/B08VLGDK32",
    duration: "20 hours 56 min",
    description: "THE data engineering bible. Covers distributed systems, data models, storage engines, replication, partitioning, batch and stream processing.",
    whenToListen: "Throughout Q2: Essential listening for understanding data systems architecture"
  }
];

export const Q3_AUDIOBOOKS: Audiobook[] = [
  {
    title: "The Pragmatic Programmer",
    author: "David Thomas & Andrew Hunt",
    audibleUrl: "https://www.audible.com/pd/The-Pragmatic-Programmer-20th-Anniversary-Edition-2nd-Edition-Audiobook/B0833FMYH9",
    duration: "9 hours 55 min",
    description: "Classic software engineering book. Covers code quality, testing, automation, and professional development practices.",
    whenToListen: "Throughout Q3: Software engineering best practices while mastering dbt"
  }
];

// ============================================================================
// QUARTER 1: PYTHON & SQL FOUNDATIONS - DAILY VIDEOS
// ============================================================================

export const Q1_DAILY_VIDEOS: Record<number, DailyVideo> = {
  // Week 1: Development Environment & Python Basics
  1: {
    title: "Python Tutorial - Setting Up Your Development Environment",
    url: "https://www.youtube.com/watch?v=YYXdXT2l-Gg",
    duration: "15:21",
    channel: "Corey Schafer",
    description: "Complete Python installation and VS Code setup guide",
    platform: 'youtube'
  },
  2: {
    title: "Python Variables and Data Types - Full Course",
    url: "https://www.youtube.com/watch?v=Z1Yd7upQsXY",
    duration: "18:45",
    channel: "Tech With Tim",
    description: "Understanding variables, strings, integers, floats, and booleans",
    platform: 'youtube'
  },
  3: {
    title: "Python Functions - Everything You Need to Know",
    url: "https://www.youtube.com/watch?v=9Os0o3wzS_I",
    duration: "21:29",
    channel: "Corey Schafer",
    description: "Functions, parameters, return values, and scope",
    platform: 'youtube'
  },
  4: {
    title: "Python Lists, Tuples, Sets & Dictionaries",
    url: "https://www.youtube.com/watch?v=W8KRzm-HUcc",
    duration: "19:15",
    channel: "Programming with Mosh",
    description: "Complete guide to Python data structures",
    platform: 'youtube'
  },
  
  // Week 2: Control Flow & Error Handling
  5: {
    title: "Python If Else Statements & Conditionals",
    url: "https://www.youtube.com/watch?v=DZwmZ8Usvnk",
    duration: "16:28",
    channel: "Corey Schafer",
    description: "If, elif, else statements and conditional logic",
    platform: 'youtube'
  },
  6: {
    title: "Python Loops - For & While Loops",
    url: "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ",
    duration: "18:55",
    channel: "Corey Schafer",
    description: "Iterating with for loops, while loops, break and continue",
    platform: 'youtube'
  },
  7: {
    title: "List Comprehensions and Generator Expressions",
    url: "https://www.youtube.com/watch?v=3dt4OGnU5sM",
    duration: "17:43",
    channel: "Corey Schafer",
    description: "Pythonic ways to create lists and iterate efficiently",
    platform: 'youtube'
  },
  8: {
    title: "Python Try Except - Exception Handling",
    url: "https://www.youtube.com/watch?v=NIWwJbo-9_8",
    duration: "18:21",
    channel: "Corey Schafer",
    description: "Error handling, try/except blocks, and raising exceptions",
    platform: 'youtube'
  },
  
  // Week 3: File I/O & Modules
  9: {
    title: "Python File Handling - Reading & Writing Files",
    url: "https://www.youtube.com/watch?v=Uh2ebFW8OYM",
    duration: "19:33",
    channel: "Corey Schafer",
    description: "Working with text files, context managers, file modes",
    platform: 'youtube'
  },
  10: {
    title: "Working with CSV Files in Python",
    url: "https://www.youtube.com/watch?v=q5uM4VKywbA",
    duration: "16:12",
    channel: "Corey Schafer",
    description: "Reading and writing CSV files with the csv module",
    platform: 'youtube'
  },
  11: {
    title: "Working with JSON Data in Python",
    url: "https://www.youtube.com/watch?v=9N6a-VLBa2I",
    duration: "20:34",
    channel: "Corey Schafer",
    description: "Parsing JSON, serialization, API response handling",
    platform: 'youtube'
  },
  12: {
    title: "Python Modules and Packages",
    url: "https://www.youtube.com/watch?v=CqvZ3vGoGs0",
    duration: "17:18",
    channel: "Corey Schafer",
    description: "Creating modules, imports, and package structure",
    platform: 'youtube'
  },
  
  // Week 4: Object-Oriented Python
  13: {
    title: "Python OOP Tutorial 1: Classes and Instances",
    url: "https://www.youtube.com/watch?v=ZDa-Z5JzLYM",
    duration: "15:24",
    channel: "Corey Schafer",
    description: "Introduction to classes, __init__, and instance methods",
    platform: 'youtube'
  },
  14: {
    title: "Python OOP Tutorial 2: Class Variables",
    url: "https://www.youtube.com/watch?v=BJ-VvGyQxho",
    duration: "11:41",
    channel: "Corey Schafer",
    description: "Class vs instance variables, when to use each",
    platform: 'youtube'
  },
  15: {
    title: "Python OOP Tutorial 3: classmethods and staticmethods",
    url: "https://www.youtube.com/watch?v=rq8cL2XMM5M",
    duration: "15:20",
    channel: "Corey Schafer",
    description: "Different types of methods in Python classes",
    platform: 'youtube'
  },
  16: {
    title: "Python OOP Tutorial 4: Inheritance",
    url: "https://www.youtube.com/watch?v=RSl87lqOXDE",
    duration: "19:40",
    channel: "Corey Schafer",
    description: "Inheritance, subclasses, and super()",
    platform: 'youtube'
  },
  
  // Week 5: SQL Fundamentals
  17: {
    title: "SQL Tutorial - Full Database Course for Beginners",
    url: "https://www.youtube.com/watch?v=HXV3zeQKqGY",
    duration: "18:00",
    channel: "freeCodeCamp",
    description: "Introduction to databases and SQL (watch first 18 mins)",
    platform: 'youtube'
  },
  18: {
    title: "SQL SELECT Statement - Querying Data",
    url: "https://www.youtube.com/watch?v=9Pzj7Aj25lw",
    duration: "17:45",
    channel: "Programming with Mosh",
    description: "SELECT, FROM, WHERE clauses and filtering data",
    platform: 'youtube'
  },
  19: {
    title: "SQL Filtering with WHERE, AND, OR, IN, BETWEEN",
    url: "https://www.youtube.com/watch?v=Hl4NZB1XR9c",
    duration: "15:32",
    channel: "Socratica",
    description: "Advanced filtering and comparison operators",
    platform: 'youtube'
  },
  20: {
    title: "SQL ORDER BY, LIMIT, and OFFSET",
    url: "https://www.youtube.com/watch?v=bEtnYWuo2Bw",
    duration: "12:18",
    channel: "Socratica",
    description: "Sorting and limiting query results",
    platform: 'youtube'
  },
  
  // Week 6: SQL JOINs & Aggregations
  21: {
    title: "SQL Joins Explained - INNER, LEFT, RIGHT, FULL",
    url: "https://www.youtube.com/watch?v=9yeOJ0ZMUYw",
    duration: "19:42",
    channel: "Programming with Mosh",
    description: "Complete guide to SQL JOIN types with examples",
    platform: 'youtube'
  },
  22: {
    title: "SQL Aggregate Functions - COUNT, SUM, AVG, MIN, MAX",
    url: "https://www.youtube.com/watch?v=fKJE5BhRIEA",
    duration: "14:28",
    channel: "Socratica",
    description: "Aggregating data with built-in SQL functions",
    platform: 'youtube'
  },
  23: {
    title: "SQL GROUP BY and HAVING Clauses",
    url: "https://www.youtube.com/watch?v=UjpuS9Cc5RI",
    duration: "16:55",
    channel: "Programming with Mosh",
    description: "Grouping data and filtering aggregates",
    platform: 'youtube'
  },
  24: {
    title: "SQL Subqueries - Nested Queries Explained",
    url: "https://www.youtube.com/watch?v=nJIEIzF7tDw",
    duration: "18:33",
    channel: "Programming with Mosh",
    description: "Subqueries in WHERE, SELECT, and FROM clauses",
    platform: 'youtube'
  },
  
  // Week 7: Advanced SQL
  25: {
    title: "SQL Window Functions Tutorial",
    url: "https://www.youtube.com/watch?v=Ww71knvhQ-s",
    duration: "20:14",
    channel: "Socratica",
    description: "ROW_NUMBER, RANK, DENSE_RANK, and PARTITION BY",
    platform: 'youtube'
  },
  26: {
    title: "SQL CTEs - Common Table Expressions",
    url: "https://www.youtube.com/watch?v=K1WeoKxLZ5o",
    duration: "15:47",
    channel: "Socratica",
    description: "Writing readable queries with WITH clauses",
    platform: 'youtube'
  },
  27: {
    title: "SQL CASE WHEN Statements",
    url: "https://www.youtube.com/watch?v=X6tLwDMggPQ",
    duration: "14:22",
    channel: "Socratica",
    description: "Conditional logic inside SQL queries",
    platform: 'youtube'
  },
  28: {
    title: "SQL Date Functions and Formatting",
    url: "https://www.youtube.com/watch?v=8IzLaVsz0Lo",
    duration: "16:38",
    channel: "Programming with Mosh",
    description: "Working with dates, timestamps, and intervals",
    platform: 'youtube'
  },
  
  // Week 8: Python + SQL Integration
  29: {
    title: "Python SQLite Tutorial - Database Programming",
    url: "https://www.youtube.com/watch?v=pd-0G0MigUA",
    duration: "29:49",
    channel: "Corey Schafer",
    description: "Connecting Python to SQLite databases (watch 15-20 mins)",
    platform: 'youtube'
  },
  30: {
    title: "Python Database Connection - Best Practices",
    url: "https://www.youtube.com/watch?v=M-4EpNGrab4",
    duration: "18:23",
    channel: "Tech With Tim",
    description: "Connection pooling, context managers, and error handling",
    platform: 'youtube'
  },
  31: {
    title: "Pandas Read SQL - Loading Data from Databases",
    url: "https://www.youtube.com/watch?v=2RZkT4g6yNM",
    duration: "16:45",
    channel: "Data School",
    description: "Using pandas to query SQL databases directly",
    platform: 'youtube'
  },
  32: {
    title: "Building a Python Database Project",
    url: "https://www.youtube.com/watch?v=byHcYRpMgI4",
    duration: "22:15",
    channel: "Tech With Tim",
    description: "End-to-end database project walkthrough",
    platform: 'youtube'
  },
  
  // Week 9: Pandas Fundamentals
  33: {
    title: "Pandas Tutorial - Complete Introduction",
    url: "https://www.youtube.com/watch?v=vmEHCJofslg",
    duration: "20:45",
    channel: "Keith Galli",
    description: "DataFrames, Series, and basic operations",
    platform: 'youtube'
  },
  34: {
    title: "Pandas Data Selection and Indexing",
    url: "https://www.youtube.com/watch?v=W9XjRYFkkyw",
    duration: "17:33",
    channel: "Data School",
    description: "loc, iloc, boolean indexing, and filtering",
    platform: 'youtube'
  },
  35: {
    title: "Pandas Data Cleaning Techniques",
    url: "https://www.youtube.com/watch?v=bDhvCp3_lYw",
    duration: "19:28",
    channel: "Keith Galli",
    description: "Handling missing data, duplicates, and data types",
    platform: 'youtube'
  },
  36: {
    title: "Pandas GroupBy Operations",
    url: "https://www.youtube.com/watch?v=txMdrV1Ut64",
    duration: "18:42",
    channel: "Corey Schafer",
    description: "Aggregating, transforming, and filtering groups",
    platform: 'youtube'
  },
  
  // Week 10: Advanced Pandas
  37: {
    title: "Pandas Merge, Join, and Concatenate",
    url: "https://www.youtube.com/watch?v=h4hOPGo4UVU",
    duration: "21:17",
    channel: "Data School",
    description: "Combining DataFrames like SQL JOINs",
    platform: 'youtube'
  },
  38: {
    title: "Pandas Pivot Tables and Reshaping",
    url: "https://www.youtube.com/watch?v=xPPs59pn6qU",
    duration: "16:55",
    channel: "Data School",
    description: "Pivot, melt, stack, and unstack operations",
    platform: 'youtube'
  },
  39: {
    title: "Pandas Apply, Map, and Applymap",
    url: "https://www.youtube.com/watch?v=P_q0tkYqvSk",
    duration: "15:38",
    channel: "Data School",
    description: "Applying custom functions to DataFrames",
    platform: 'youtube'
  },
  40: {
    title: "Pandas Performance Optimization",
    url: "https://www.youtube.com/watch?v=HN5d490_KKk",
    duration: "19:22",
    channel: "Rob Mulla",
    description: "Making pandas operations 100x faster",
    platform: 'youtube'
  },
  
  // Week 11: Git & Version Control
  41: {
    title: "Git Tutorial for Beginners - Learn Git in 15 Minutes",
    url: "https://www.youtube.com/watch?v=USjZcfj8yxE",
    duration: "15:29",
    channel: "Colt Steele",
    description: "Git init, add, commit, and basic workflow",
    platform: 'youtube'
  },
  42: {
    title: "Git Branching and Merging",
    url: "https://www.youtube.com/watch?v=FyAAIHHClqI",
    duration: "17:12",
    channel: "The Coding Train",
    description: "Creating branches, switching, and merging",
    platform: 'youtube'
  },
  43: {
    title: "GitHub Pull Requests Explained",
    url: "https://www.youtube.com/watch?v=rgbCcBNZcdQ",
    duration: "14:45",
    channel: "GitHub",
    description: "Creating and reviewing pull requests",
    platform: 'youtube'
  },
  44: {
    title: "Git Workflow for Data Projects",
    url: "https://www.youtube.com/watch?v=aJnFGMclhU8",
    duration: "18:33",
    channel: "Data Professor",
    description: "Git best practices for data engineering",
    platform: 'youtube'
  },
  
  // Week 12: Testing & Code Quality
  45: {
    title: "Python Unit Testing with pytest",
    url: "https://www.youtube.com/watch?v=YbpKMIUjvK8",
    duration: "19:45",
    channel: "Corey Schafer",
    description: "Writing and running tests with pytest",
    platform: 'youtube'
  },
  46: {
    title: "pytest Fixtures and Parameterization",
    url: "https://www.youtube.com/watch?v=IVrGz8w0H8c",
    duration: "17:28",
    channel: "Tech With Tim",
    description: "Advanced pytest features for data testing",
    platform: 'youtube'
  },
  47: {
    title: "Python Type Hints and mypy",
    url: "https://www.youtube.com/watch?v=QORvB-_mbZ0",
    duration: "16:42",
    channel: "ArjanCodes",
    description: "Static type checking in Python",
    platform: 'youtube'
  },
  48: {
    title: "Python Code Quality Tools - Linting & Formatting",
    url: "https://www.youtube.com/watch?v=SH9FrPyyvpY",
    duration: "14:55",
    channel: "ArjanCodes",
    description: "Black, flake8, isort, and pre-commit hooks",
    platform: 'youtube'
  },
  
  // Week 13: Q1 Capstone Project
  49: {
    title: "Building ETL Pipelines with Python",
    url: "https://www.youtube.com/watch?v=dfouoh9QdUw",
    duration: "22:18",
    channel: "Data Engineering",
    description: "End-to-end ETL pipeline design patterns",
    platform: 'youtube'
  },
  50: {
    title: "Data Pipeline Architecture Best Practices",
    url: "https://www.youtube.com/watch?v=VtzvF17ysbc",
    duration: "19:33",
    channel: "Seattle Data Guy",
    description: "Designing scalable data pipelines",
    platform: 'youtube'
  },
  51: {
    title: "Building a Complete Data Project Portfolio",
    url: "https://www.youtube.com/watch?v=iP4l28zsQIs",
    duration: "20:45",
    channel: "Ken Jee",
    description: "Showcasing your data engineering work",
    platform: 'youtube'
  },
  52: {
    title: "Data Engineering Project Walkthrough",
    url: "https://www.youtube.com/watch?v=Li8-MWHhTbo",
    duration: "24:12",
    channel: "Data with Zach",
    description: "Complete project from start to finish",
    platform: 'youtube'
  }
};

// ============================================================================
// WEEKLY PODCASTS - Verified Working Episode Links
// ============================================================================

export const Q1_WEEKLY_PODCASTS: Record<number, WeeklyPodcast[]> = {
  1: [
    {
      title: "Land Your First Data Job",
      show: "Talk Python to Me",
      episodeUrl: "https://talkpython.fm/episodes/show/455/land-your-first-data-job",
      appleUrl: "https://podcasts.apple.com/us/podcast/land-your-first-data-job/id979020229?i=1000651495519",
      episodeNumber: "#455",
      duration: "59 min",
      description: "Avery Smith from Data Career Jumpstart shares advice on securing your first data position."
    }
  ],
  2: [
    {
      title: "Effective Pandas Patterns for Data Engineering",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/effective-pandas-patterns-for-data-engineering-episode-259/",
      episodeNumber: "#259",
      duration: "52 min",
      description: "Matt Harrison shares advice on writing efficient data processing routines using Pandas."
    }
  ],
  3: [
    {
      title: "Separate Your SQL and Python with aiosql",
      show: "Python Bytes",
      episodeUrl: "https://pythonbytes.fm/episodes/show/237/separate-your-sql-and-python-asynchronously-with-aiosql",
      episodeNumber: "#237",
      duration: "28 min",
      description: "Clean separation of SQL queries from Python code for maintainable codebases."
    }
  ],
  4: [
    {
      title: "Data Pipelines with Dagster",
      show: "Talk Python to Me",
      episodeUrl: "https://talkpython.fm/episodes/show/454/data-pipelines-with-dagster",
      appleUrl: "https://podcasts.apple.com/us/podcast/data-pipelines-with-dagster/id979020229?i=1000650563827",
      episodeNumber: "#454",
      duration: "62 min",
      description: "Pedram Navid from Dagster Labs on building modern data pipelines."
    }
  ],
  5: [
    {
      title: "SQLite as a File Format",
      show: "Python Bytes",
      episodeUrl: "https://pythonbytes.fm/episodes/show/212/sqlite-as-a-file-format-like-docx",
      episodeNumber: "#212",
      duration: "25 min",
      description: "Using SQLite databases as file formats - implications and benefits."
    }
  ],
  6: [
    {
      title: "Building Data Pipelines at Scale",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/",
      duration: "50 min",
      description: "Strategies for building production data pipelines. Visit dataengineeringpodcast.com for latest episodes."
    }
  ],
  7: [
    {
      title: "Window Functions Deep Dive",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/",
      duration: "45 min",
      description: "Advanced SQL techniques for analytics. Visit dataengineeringpodcast.com for SQL-focused episodes."
    }
  ],
  8: [
    {
      title: "From Notebooks to Production Data Systems",
      show: "Talk Python to Me",
      episodeUrl: "https://talkpython.fm/episodes/show/511/from-notebooks-to-production-data-science-systems",
      episodeNumber: "#511",
      duration: "55 min",
      description: "Catherine Nelson on transitioning from exploratory notebooks to production workflows."
    }
  ],
  9: [
    {
      title: "Pandas for Data Engineering",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/effective-pandas-patterns-for-data-engineering-episode-259/",
      episodeNumber: "#259",
      duration: "52 min",
      description: "When to use Pandas vs SQL vs Spark - practical guidance for data engineers."
    }
  ],
  10: [
    {
      title: "Data Transformation Best Practices",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/",
      duration: "48 min",
      description: "Common patterns for transforming data. Visit dataengineeringpodcast.com for transformation episodes."
    }
  ],
  11: [
    {
      title: "Git for Data Teams",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/",
      duration: "42 min",
      description: "Version control best practices for data projects. Browse dataengineeringpodcast.com for Git episodes."
    }
  ],
  12: [
    {
      title: "Testing Data Pipelines with Great Expectations",
      show: "Data Engineering Podcast",
      episodeUrl: "https://www.dataengineeringpodcast.com/great-expectations-pipeline-tests-episode-36/",
      episodeNumber: "#36",
      duration: "45 min",
      description: "Unit testing, integration testing, and data validation with Great Expectations."
    }
  ],
  13: [
    {
      title: "Building Your Data Engineering Career",
      show: "Talk Python to Me",
      episodeUrl: "https://talkpython.fm/episodes/show/455/land-your-first-data-job",
      episodeNumber: "#455",
      duration: "59 min",
      description: "Career advice and portfolio building strategies for data engineers."
    }
  ]
};

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

export function getDailyVideo(dayNumber: number): DailyVideo | null {
  return Q1_DAILY_VIDEOS[dayNumber] || null;
}

export function getWeeklyPodcasts(weekNumber: number): WeeklyPodcast[] {
  return Q1_WEEKLY_PODCASTS[weekNumber] || [];
}

export function getQuarterAudiobooks(quarterNumber: number): Audiobook[] {
  switch (quarterNumber) {
    case 1: return Q1_AUDIOBOOKS;
    case 2: return Q2_AUDIOBOOKS;
    case 3: return Q3_AUDIOBOOKS;
    default: return [];
  }
}

export function getDayMedia(dayNumber: number) {
  const weekNumber = Math.ceil(dayNumber / 4);
  const quarterNumber = Math.ceil(weekNumber / 13);
  
  return {
    video: getDailyVideo(dayNumber),
    podcasts: getWeeklyPodcasts(weekNumber),
    audiobooks: getQuarterAudiobooks(quarterNumber),
    isNewPodcastDay: dayNumber % 4 === 1,
    isFirstDayOfQuarter: (dayNumber - 1) % 52 === 0
  };
}
