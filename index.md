---
layout: default
title: DevSecOps20 - Complete Course
---

<style>
/* Modern Theme Variables */
:root {
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --secondary: #ec4899;
  --accent: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  --dark: #0f172a;
  --dark-lighter: #1e293b;
  --dark-card: #334155;
  --text-primary: #f1f5f9;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --border: #475569;
  --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
}

/* Reset and Base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--dark);
  color: var(--text-primary);
  line-height: 1.6;
  overflow-x: hidden;
}

/* Hero Section */
.hero {
  background: linear-gradient(135deg, var(--dark) 0%, var(--dark-lighter) 100%);
  padding: 80px 20px;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(236, 72, 153, 0.1) 0%, transparent 50%);
  pointer-events: none;
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 1200px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 4rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 20px;
  animation: fadeInUp 0.8s ease;
}

.hero-subtitle {
  font-size: 1.5rem;
  color: var(--text-secondary);
  margin-bottom: 40px;
  animation: fadeInUp 0.8s ease 0.2s both;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 60px;
  margin-top: 60px;
  animation: fadeInUp 0.8s ease 0.4s both;
}

.stat {
  text-align: center;
}

.stat-number {
  font-size: 3rem;
  font-weight: 700;
  color: var(--primary);
  display: block;
}

.stat-label {
  color: var(--text-secondary);
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Navigation Tabs */
.nav-tabs {
  background: var(--dark-lighter);
  padding: 20px;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.nav-tab {
  padding: 12px 24px;
  background: var(--dark-card);
  border: 2px solid transparent;
  border-radius: 12px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  position: relative;
  overflow: hidden;
}

.nav-tab::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--gradient-1);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.nav-tab:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
}

.nav-tab.active {
  border-color: var(--primary);
  color: var(--text-primary);
}

.nav-tab.active::before {
  opacity: 0.1;
}

.nav-icon {
  display: inline-block;
  margin-right: 8px;
}

/* Content Sections */
.content-section {
  display: none;
  animation: fadeIn 0.5s ease;
}

.content-section.active {
  display: block;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
}

/* Section Headers */
.section-header {
  text-align: center;
  margin-bottom: 60px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 15px;
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.section-description {
  font-size: 1.2rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
}

/* Grid Layout */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

/* Cards */
.card {
  background: var(--dark-lighter);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 30px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--gradient-1);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  border-color: var(--primary);
}

.card:hover::before {
  transform: scaleX(1);
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.card-icon {
  width: 48px;
  height: 48px;
  background: var(--gradient-1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-size: 1.5rem;
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
}

.card-description {
  color: var(--text-secondary);
  margin-bottom: 25px;
  line-height: 1.6;
}

/* Content Lists */
.content-list {
  list-style: none;
}

.content-item {
  background: var(--dark);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 15px;
  transition: all 0.3s ease;
}

.content-item:hover {
  background: var(--dark-card);
  border-color: var(--primary);
  transform: translateX(5px);
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.item-title {
  font-weight: 600;
  color: var(--text-primary);
}

.item-badge {
  background: var(--primary);
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.item-description {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-bottom: 15px;
}

.item-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.item-link {
  background: var(--dark-card);
  color: var(--text-primary);
  padding: 8px 16px;
  border-radius: 8px;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.3s ease;
  border: 1px solid var(--border);
}

.item-link:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
}

/* Special Cards for Different Sections */
.lessons .card-icon { background: var(--gradient-1); }
.labs .card-icon { background: var(--gradient-2); }
.projects .card-icon { background: var(--gradient-3); }

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
  }
  
  .hero-stats {
    gap: 30px;
  }
  
  .stat-number {
    font-size: 2rem;
  }
  
  .nav-container {
    gap: 10px;
  }
  
  .nav-tab {
    padding: 10px 16px;
    font-size: 0.9rem;
  }
  
  .grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .container {
    padding: 40px 15px;
  }
}

/* Loading Animation */
.loading {
  text-align: center;
  padding: 40px;
  color: var(--text-muted);
}

.loading::after {
  content: '...';
  animation: dots 1.5s infinite;
}

@keyframes dots {
  0%, 20% { content: '.'; }
  40% { content: '..'; }
  60%, 100% { content: '...'; }
}

/* Search Bar */
.search-container {
  max-width: 600px;
  margin: 0 auto 40px;
  position: relative;
}

.search-input {
  width: 100%;
  padding: 15px 20px 15px 50px;
  background: var(--dark-lighter);
  border: 2px solid var(--border);
  border-radius: 12px;
  color: var(--text-primary);
  font-size: 1rem;
  transition: all 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.search-icon {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
}

/* Tags */
.tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 15px;
}

.tag {
  background: var(--dark-card);
  color: var(--text-secondary);
  padding: 4px 10px;
  border-radius: 15px;
  font-size: 0.8rem;
  border: 1px solid var(--border);
}

</style>

<!-- Hero Section -->
<div class="hero">
  <div class="hero-content">
    <h1>DevSecOps20</h1>
    <p class="hero-subtitle">Master DevSecOps with Hands-On Learning Experience</p>
    
    <div class="hero-stats">
      <div class="stat">
        <span class="stat-number" id="lessonsCount">0</span>
        <span class="stat-label">Lessons</span>
      </div>
      <div class="stat">
        <span class="stat-number" id="labsCount">0</span>
        <span class="stat-label">Labs</span>
      </div>
      <div class="stat">
        <span class="stat-number" id="projectsCount">0</span>
        <span class="stat-label">Projects</span>
      </div>
    </div>
  </div>
</div>

<!-- Navigation Tabs -->
<div class="nav-tabs">
  <div class="nav-container">
    <button class="nav-tab active" onclick="showSection('lessons')">
      <span class="nav-icon">📚</span>Lessons
    </button>
    <button class="nav-tab" onclick="showSection('labs')">
      <span class="nav-icon">🔬</span>Labs
    </button>
    <button class="nav-tab" onclick="showSection('projects')">
      <span class="nav-icon">🚀</span>Projects
    </button>
  </div>
</div>

<!-- Lessons Section -->
<div id="lessons" class="content-section active">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">📚 Comprehensive Lessons</h2>
      <p class="section-description">Master DevSecOps fundamentals through structured learning paths</p>
    </div>
    
    <div class="search-container">
      <span class="search-icon">🔍</span>
      <input type="text" class="search-input" placeholder="Search lessons..." onkeyup="filterContent('lessons', this.value)">
    </div>
    
    <div class="grid lessons" id="lessonsGrid">
      <div class="loading">Loading lessons</div>
    </div>
  </div>
</div>

<!-- Labs Section -->
<div id="labs" class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">🔬 Hands-On Labs</h2>
      <p class="section-description">Apply your knowledge with practical exercises and real-world scenarios</p>
    </div>
    
    <div class="search-container">
      <span class="search-icon">🔍</span>
      <input type="text" class="search-input" placeholder="Search labs..." onkeyup="filterContent('labs', this.value)">
    </div>
    
    <div class="grid labs" id="labsGrid">
      <div class="loading">Loading labs</div>
    </div>
  </div>
</div>

<!-- Projects Section -->
<div id="projects" class="content-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">🚀 Real Projects</h2>
      <p class="section-description">Build impressive projects to showcase your DevSecOps skills</p>
    </div>
    
    <div class="search-container">
      <span class="search-icon">🔍</span>
      <input type="text" class="search-input" placeholder="Search projects..." onkeyup="filterContent('projects', this.value)">
    </div>
    
    <div class="grid projects" id="projectsGrid">
      <div class="loading">Loading projects</div>
    </div>
  </div>
</div>

<script>
// Content data structure
const contentData = {
  lessons: [
    {
      title: "🐧 Linux Basics",
      description: "Master command-line, file systems, permissions, and process control",
      icon: "🐧",
      items: [
        {
          title: "Linux Basics 1",
          description: "Introduction to Linux command line and basic operations",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Linux-basics/01-linux-basics/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Linux-basics/01-linux-basics/lesson1.drawio.pdf" }
          ]
        },
        {
          title: "Linux Basics 2",
          description: "Advanced commands and file system navigation",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Linux-basics/02-linux-basics/" },
            { text: "Cheatsheet", url: "{{ site.baseurl }}/lessons/Linux-basics/02-linux-basics/cheatsheet.md" }
          ]
        },
        {
          title: "Linux Basics 3",
          description: "Process management and system monitoring",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Linux-basics/03-linux-basics/" },
            { text: "Cheatsheet", url: "{{ site.baseurl }}/lessons/Linux-basics/03-linux-basics/cheatsheet.md" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Linux-basics/03-linux-basics/lesson3.drawio.pdf" }
          ]
        },
        {
          title: "Linux Networks",
          description: "Networking fundamentals and troubleshooting",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Linux-basics/04-linux-basics/" }
          ]
        }
      ],
      tags: ["fundamentals", "linux", "cli"]
    },
    {
      title: "📜 Bash Scripting",
      description: "Automate tasks and create powerful scripts with bash programming",
      icon: "📜",
      items: [
        {
          title: "Basics and Variables",
          description: "Introduction to bash scripting and variable handling",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" },
            { text: "Commands", url: "{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/commands.txt" },
            { text: "Demo", url: "{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/demo1.sh" }
          ]
        },
        {
          title: "If Statements and Conditions",
          description: "Control flow and conditional logic in bash",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" },
            { text: "Class Code", url: "{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/class-code.md" }
          ]
        }
      ],
      tags: ["automation", "scripting", "bash"]
    },
    {
      title: "🐍 Python",
      description: "Automate tasks and build tools with Python scripting for DevOps workflows",
      icon: "🐍",
      items: [
        {
          title: "Input, Print and Datatypes",
          description: "Python fundamentals and basic data types",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/05-python-lesson1.py/" },
            { text: "Class Code", url: "https://github.com/hothaifa96/DevSecOps20/blob/main/lessons/Python/05-python-lesson1.py/class_code.py" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/05-python-lesson1.py/python1.pdf" }
          ]
        },
        {
          title: "Strings and Lists",
          description: "Working with strings and lists in Python",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/" },
            { text: "Cheatsheet", url: "{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/cheatsheet.webp" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/python2.pdf" }
          ]
        },
        {
          title: "If Statement",
          description: "Conditional logic and decision making",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/07-python-lesson3.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/python3.pdf" }
          ]
        },
        {
          title: "Lists, Tuples, Sets and For Loop",
          description: "Data structures and iteration",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/python4.drawio.pdf" },
            { text: "List Methods", url: "{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/list.md" },
            { text: "Class Code", url: "{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/class_code.py" }
          ]
        },
        {
          title: "While and For Loops",
          description: "Looping constructs and patterns",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/09-python-lesson5.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/09-python-lesson4.py/python5.drawio.pdf" },
            { text: "Class Code", url: "{{ site.baseurl }}/lessons/Python/09-python-lesson5.py/classcode.py" }
          ]
        },
        {
          title: "JSON, PIP and RESTful API",
          description: "Working with APIs and package management",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/python6.drawio.pdf" },
            { text: "Class Code", url: "{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/classcode.py" }
          ]
        },
        {
          title: "Functions and RESTful API",
          description: "Advanced functions and API integration",
          badge: "Advanced",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/python7.pdf" },
            { text: "Class Code", url: "{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/classcode.py" }
          ]
        },
        {
          title: "Classes and OOP",
          description: "Object-oriented programming concepts",
          badge: "Advanced",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/python8.pdf" },
            { text: "Class Code", url: "{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/classcode.md" }
          ]
        },
        {
          title: "OOP, Imports and GIT",
          description: "Advanced OOP and version control integration",
          badge: "Advanced",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Python/Python/13-python-lesson9.py/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Python/Python/13-python-lesson9.py/python9.pdf" },
            { text: "Class Code", url: "https://github.com/hothaifa96/DevSecOps20/tree/main/lessons/Python/13-python-lesson9.py/app" }
          ]
        }
      ],
      tags: ["programming", "python", "automation"]
    },
    {
      title: "🔄 Git",
      description: "Master version control with Git and GitHub for collaborative development",
      icon: "🔄",
      items: [
        {
          title: "Basics and Configs",
          description: "Git fundamentals and initial setup",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/GIT/lesson1/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/GIT/lesson1/GIT1.pdf" }
          ]
        },
        {
          title: "Branching and Merging",
          description: "Advanced Git workflows and collaboration",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/GIT/Lesson2/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/GIT/Lesso2/Git3.drawio.pdf" }
          ]
        },
        {
          title: "GitHub and Git",
          description: "Remote repositories and GitHub features",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/GIT/Lesson3/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/GIT/Lesson3/lesson3.pdf" }
          ]
        }
      ],
      tags: ["version-control", "git", "collaboration"]
    },
    {
      title: "🐳 Docker",
      description: "Containerize and run all applications with Docker",
      icon: "🐳",
      items: [
        {
          title: "Docker Architecture and Run Command",
          description: "Understanding Docker containers and basic commands",
          badge: "Beginner",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/Docker/Lession1/" },
            { text: "Commands", url: "{{ site.baseurl }}/lessons/Docker/Lession1/CheatSheet.md" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/Docker/Lession1/Docker1.pdf" }
          ]
        }
      ],
      tags: ["containers", "docker", "virtualization"]
    },
    {
      title: "☸️ Kubernetes",
      description: "Master container orchestration with Kubernetes",
      icon: "☸️",
      items: [
        {
          title: "Architecture and Main Components",
          description: "Understanding Kubernetes cluster architecture",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/kubernetes/lesson1/" },
            { text: "PDF", url: "{{ site.baseurl }}/lessons/kubernetes/lesson1/GIT1.pdf" }
          ]
        }
      ],
      tags: ["kubernetes", "orchestration", "containers"]
    },
    {
      title: "🔧 Jenkins",
      description: "CI/CD pipeline automation with Jenkins",
      icon: "🔧",
      items: [
        {
          title: "Jenkins Fundamentals",
          description: "Setting up Jenkins and basic pipeline concepts",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/jenkins/" },
            { text: "Tutorials", url: "{{ site.baseurl }}/lessons/jenkins/toturials/" }
          ]
        }
      ],
      tags: ["ci-cd", "jenkins", "automation"]
    },
    {
      title: "📊 Monitoring",
      description: "Comprehensive monitoring with Prometheus, Grafana, and more",
      icon: "📊",
      items: [
        {
          title: "Grafana Tutorial",
          description: "Create stunning dashboards with Grafana",
          badge: "Intermediate",
          links: [
            { text: "Tutorial", url: "{{ site.baseurl }}/lessons/monitoring/tutorials/01-grafana-tutorial.md" }
          ]
        },
        {
          title: "Prometheus Architecture",
          description: "Understanding Prometheus monitoring system",
          badge: "Intermediate",
          links: [
            { text: "Tutorial", url: "{{ site.baseurl }}/lessons/monitoring/tutorials/02-prometheus-architecture.md" }
          ]
        },
        {
          title: "PromQL Tutorial",
          description: "Query language for Prometheus metrics",
          badge: "Advanced",
          links: [
            { text: "Tutorial", url: "{{ site.baseurl }}/lessons/monitoring/tutorials/03-promql-tutorial.md" }
          ]
        },
        {
          title: "Prometheus Exporters",
          description: "Export metrics from various systems",
          badge: "Intermediate",
          links: [
            { text: "Tutorial", url: "{{ site.baseurl }}/lessons/monitoring/tutorials/04-prometheus-exporter.md" }
          ]
        },
        {
          title: "Python Prometheus Client",
          description: "Instrument Python applications with Prometheus",
          badge: "Advanced",
          links: [
            { text: "Tutorial", url: "{{ site.baseurl }}/lessons/monitoring/tutorials/05-python-prometheus-code.md" }
          ]
        },
        {
          title: "Prometheus Configuration",
          description: "Complete guide to prometheus.yml configuration",
          badge: "Intermediate",
          links: [
            { text: "Tutorial", url: "{{ site.baseurl }}/lessons/monitoring/tutorials/06-prometheus-yml.md" }
          ]
        }
      ],
      tags: ["monitoring", "prometheus", "grafana", "observability"]
    },
    {
      title: "🏗️ Terraform",
      description: "Infrastructure as Code with Terraform",
      icon: "🏗️",
      items: [
        {
          title: "Terraform Fundamentals",
          description: "Infrastructure provisioning and management",
          badge: "Intermediate",
          links: [
            { text: "Start Lesson", url: "{{ site.baseurl }}/lessons/terraform/" }
          ]
        }
      ],
      tags: ["terraform", "iac", "infrastructure"]
    }
  ],
  labs: [
    {
      title: "🔬 Linux Basics Labs",
      description: "Hands-on exercises for Linux command line mastery",
      icon: "🐧",
      items: [
        {
          title: "Linux Command Line Lab",
          description: "Practice essential Linux commands and operations",
          badge: "Hands-on",
          links: [
            { text: "Start Lab", url: "{{ site.baseurl }}/labs/linux-basics/" }
          ]
        }
      ],
      tags: ["linux", "hands-on", "cli"]
    },
    {
      title: "🔬 Python Programming Labs",
      description: "Practical Python exercises for DevOps automation",
      icon: "🐍",
      items: [
        {
          title: "Python Automation Lab",
          description: "Build automation scripts with Python",
          badge: "Hands-on",
          links: [
            { text: "Start Lab", url: "{{ site.baseurl }}/labs/python/" }
          ]
        }
      ],
      tags: ["python", "automation", "programming"]
    },
    {
      title: "🔬 Docker Labs",
      description: "Containerization exercises and best practices",
      icon: "🐳",
      items: [
        {
          title: "Docker Container Lab",
          description: "Build and manage Docker containers",
          badge: "Hands-on",
          links: [
            { text: "Start Lab", url: "{{ site.baseurl }}/labs/docker/" }
          ]
        }
      ],
      tags: ["docker", "containers", "hands-on"]
    },
    {
      title: "🔬 Kubernetes Labs",
      description: "Real-world Kubernetes deployment scenarios",
      icon: "☸️",
      items: [
        {
          title: "Kubernetes Deployment Lab",
          description: "Deploy applications on Kubernetes cluster",
          badge: "Advanced",
          links: [
            { text: "Start Lab", url: "{{ site.baseurl }}/labs/kubernetes/" }
          ]
        }
      ],
      tags: ["kubernetes", "deployment", "advanced"]
    },
    {
      title: "🔬 Jenkins CI/CD Labs",
      description: "Build and deploy automation pipelines",
      icon: "🔧",
      items: [
        {
          title: "Jenkins Pipeline Lab",
          description: "Create automated CI/CD pipelines",
          badge: "Hands-on",
          links: [
            { text: "Start Lab", url: "{{ site.baseurl }}/labs/jenkins/" }
          ]
        }
      ],
      tags: ["jenkins", "ci-cd", "automation"]
    }
  ],
  projects: [
    {
      title: "🚀 Kubernetes Projects",
      description: "Real-world Kubernetes deployment projects",
      icon: "☸️",
      items: [
        {
          title: "Microservices Deployment",
          description: "Deploy a complete microservices architecture on K8s",
          badge: "Advanced",
          links: [
            { text: "View Project", url: "{{ site.baseurl }}/projects/k8s/" }
          ]
        },
        {
          title: "Kubernetes Operators",
          description: "Build custom Kubernetes operators",
          badge: "Expert",
          links: [
            { text: "View Project", url: "{{ site.baseurl }}/projects/k8s/operators/" }
          ]
        }
      ],
      tags: ["kubernetes", "microservices", "advanced"]
    },
    {
      title: "🚀 Python DevOps Projects",
      description: "Automation and tooling projects with Python",
      icon: "🐍",
      items: [
        {
          title: "DevOps Automation Toolkit",
          description: "Build a complete DevOps automation toolkit",
          badge: "Intermediate",
          links: [
            { text: "View Project", url: "{{ site.baseurl }}/projects/python/" }
          ]
        }
      ],
      tags: ["python", "automation", "toolkit"]
    },
    {
      title: "🚀 Final Capstone Project",
      description: "Comprehensive DevOps pipeline project",
      icon: "🎯",
      items: [
        {
          title: "End-to-End DevOps Pipeline",
          description: "Build a complete CI/CD pipeline from scratch",
          badge: "Capstone",
          links: [
            { text: "View Project", url: "{{ site.baseurl }}/projects/final/" }
          ]
        }
      ],
      tags: ["capstone", "comprehensive", "production"]
    }
  ]
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
  renderContent('lessons');
  renderContent('labs');
  renderContent('projects');
  updateStats();
});

// Render content for a section
function renderContent(section) {
  const grid = document.getElementById(section + 'Grid');
  const data = contentData[section];
  
  let html = '';
  
  data.forEach(category => {
    html += `
      <div class="card" data-section="${section}" data-title="${category.title.toLowerCase()}">
        <div class="card-header">
          <div class="card-icon">${category.icon}</div>
          <h3 class="card-title">${category.title}</h3>
        </div>
        <p class="card-description">${category.description}</p>
        
        <ul class="content-list">
    `;
    
    category.items.forEach(item => {
      html += `
        <li class="content-item">
          <div class="item-header">
            <span class="item-title">${item.title}</span>
            <span class="item-badge">${item.badge}</span>
          </div>
          <p class="item-description">${item.description}</p>
          <div class="item-links">
      `;
      
      item.links.forEach(link => {
        html += `<a href="${link.url}" class="item-link">${link.text}</a>`;
      });
      
      html += `
          </div>
        </li>
      `;
    });
    
    html += `
        </ul>
        <div class="tags">
    `;
    
    category.tags.forEach(tag => {
      html += `<span class="tag">${tag}</span>`;
    });
    
    html += `
        </div>
      </div>
    `;
  });
  
  grid.innerHTML = html;
}

// Update statistics
function updateStats() {
  let totalLessons = 0;
  let totalLabs = 0;
  let totalProjects = 0;
  
  contentData.lessons.forEach(category => {
    totalLessons += category.items.length;
  });
  
  contentData.labs.forEach(category => {
    totalLabs += category.items.length;
  });
  
  contentData.projects.forEach(category => {
    totalProjects += category.items.length;
  });
  
  // Animate counters
  animateCounter('lessonsCount', totalLessons);
  animateCounter('labsCount', totalLabs);
  animateCounter('projectsCount', totalProjects);
}

// Animate counter
function animateCounter(id, target) {
  const element = document.getElementById(id);
  const duration = 2000;
  const step = target / (duration / 16);
  let current = 0;
  
  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      element.textContent = target;
      clearInterval(timer);
    } else {
      element.textContent = Math.floor(current);
    }
  }, 16);
}

// Show section
function showSection(section) {
  // Hide all sections
  document.querySelectorAll('.content-section').forEach(s => {
    s.classList.remove('active');
  });
  
  // Remove active class from all tabs
  document.querySelectorAll('.nav-tab').forEach(t => {
    t.classList.remove('active');
  });
  
  // Show selected section
  document.getElementById(section).classList.add('active');
  
  // Add active class to clicked tab
  event.target.classList.add('active');
}

// Filter content
function filterContent(section, searchTerm) {
  const cards = document.querySelectorAll(`#${section}Grid .card`);
  const term = searchTerm.toLowerCase();
  
  cards.forEach(card => {
    const title = card.dataset.title;
    const content = card.textContent.toLowerCase();
    
    if (title.includes(term) || content.includes(term)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>
