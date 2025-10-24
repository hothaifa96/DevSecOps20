---
layout: default
title: DevSecOps lessons
---

# DevSecOps lessons

Welcome to the DevSecOps course lessons! Click on any lesson topic below to explore the available lessons and materials.

<style>
  /* Root Theme Variables */
:root {
  --black: #121212;
  --dark-gray: #1e1e1e;
  --mid-gray: #2a2a2a;
  --light-gray: #ccc;
  --gold: #d4af37;
  --gold-light: #f5e9c6;
}

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--black);
  color: var(--light-gray);
  line-height: 1.6;
  padding: 20px;
}

/* Link Styling */
a {
  color: var(--gold);
  text-decoration: none;
  transition: all 0.3s ease;
}
a:hover {
  text-decoration: underline;
  color: #ffd700;
}

/* Card Container */
.lesson-container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

/* Card Base Style */
.lesson-card {
  background-color: var(--dark-gray);
  border: 1px solid #2c2c2c;
  border-left: 6px solid var(--gold);
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.4);
  transition: transform 0.2s ease;
}
.lesson-card:hover {
  transform: translateY(-5px);
}

/* Card Titles */
.lesson-card h3 {
  color: var(--gold);
  font-size: 1.5em;
  margin-bottom: 10px;
}

/* Paragraphs */
.lesson-card p {
  color: var(--light-gray);
  font-size: 1em;
  margin-bottom: 20px;
}

/* Lesson Files */
.lesson-files h4 {
  color: var(--gold-light);
  font-size: 1.1em;
  margin-bottom: 10px;
}

.file-list {
  list-style: none;
  padding-left: 0;
}
.file-list li {
  background: var(--mid-gray);
  border-left: 4px solid var(--gold);
  padding: 12px;
  border-radius: 8px;
  margin-bottom: 10px;
}
.file-list li span {
  display: block;
  font-weight: bold;
  color: var(--gold-light);
  margin-bottom: 5px;
}

/* Lesson Links */
.lesson-links {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.btn-link {
  background-color: #1a1a1a;
  border: 1px solid var(--gold);
  color: var(--gold);
  padding: 8px 14px;
  font-size: 0.95em;
  border-radius: 5px;
  transition: all 0.3s ease;
}
.btn-link:hover {
  background-color: var(--gold);
  color: #1a1a1a;
  font-weight: bold;
}

  </style>

<div class="lesson-card" >
  <h3>🔬 Hands-On Labs</h3>
  <p>Apply your knowledge with practical exercises, real-world scenarios, and interactive challenges. Master DevSecOps through hands-on experience.</p>
  <div class="lesson-files">
    <a href="{{ site.baseurl }}/labs/" class="btn-link" style="font-size:1.1em; font-weight:bold;">Access Labs</a>
    <a href="{{ site.baseurl }}/quizes/Docker-quiz.html" class="btn-link">quiz docker</a>
  </div>
</div>

<div class="lesson-container">

<!-- Linux Basics Card -->
<div class="lesson-card">
  <h3>🐧 Linux Basics</h3>
  <p>Master command-line, file systems, permissions, and process control.</p>
  <div class="lesson-files">
    <h4>Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: Linux Basics 1</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Linux-basics/01-linux-basics/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Linux-basics/01-linux-basics/lesson1.drawio.pdf" class="btn-link">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 2: Linux Basics 2</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Linux-basics/02-linux-basics/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Linux-basics/02-linux-basics/cheatsheet.md" class="btn-link">Cheatsheet</a>
        </div>
      </li>
      <li>
        <span>Lesson 3: Linux Basics 3</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Linux-basics/03-linux-basics/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Linux-basics/03-linux-basics/cheatsheet.md" class="btn-link">Cheatsheet</a>
          <a href="{{ site.baseurl }}/lessons/Linux-basics/03-linux-basics/lesson3.drawio.pdf" class="btn-link">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 4: Linux Basics 4 (networks)</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Linux-basics/04-linux-basics/" class="btn-link">Start Lesson</a>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- Bash Scripting Card -->
<div class="lesson-card" >
  <h3>📜 Bash Scripting</h3>
  <p>Automate tasks and create powerful scripts with bash programming.</p>
  <div class="lesson-files">
    <h4>Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: Basics and Variables</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/commands.txt" class="btn-link">Basic Commands</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/demo1.sh" class="btn-link">Demo1</a>
        </div>
      </li>
      <li>
        <span>Lesson 2: If Statements and Conditions</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/class-code.md" class="btn-link">Class Code</a>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- Python Card -->
<div class="lesson-card" >
  <h3 style="color: #333;">🐍 Python</h3>
  <p style="color: #444;">Automate tasks and build tools with Python scripting for DevOps workflows.</p>
  <div class="lesson-files">
    <h4 style="color: #333;">Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: Input, Print and Datatypes</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/05-python-lesson1.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="https://github.com/hothaifa96/DevSecOps20/blob/main/lessons/Python/05-python-lesson1.py/class_code.py" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
          <a href="{{ site.baseurl }}/lessons/Python/05-python-lesson1.py/python1.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 2: Strings and Lists</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/cheatsheet.webp" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Cheatsheet</a>
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/python2.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 3: If Statement</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/07-python-lesson3.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/python3.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 4: Lists, Tuples, Sets and For Loop</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/python4.drawio.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/list.md" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">List Methods</a>
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4/class_code.py" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
        </div>
      </li>
      <li>
        <span>Lesson 5: While and For Loops</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/09-python-lesson5.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/09-python-lesson4.py/python5.drawio.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/09-python-lesson5.py/classcode.py" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
        </div>
      </li>
      <li>
        <span>Lesson 6: JSON, PIP and RESTful API</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/python6.drawio.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/classcode.py" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
        </div>
      </li>
      <li>
        <span>Lesson 7: Functions and RESTful API</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/python7.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/classcode.py" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
        </div>
      </li>
      <li>
        <span>Lesson 8: Classes and OOP</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/python8.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/classcode.md" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
        </div>
      </li>
      <li>
        <span>Lesson 9: OOP, Imports and GIT</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/Python/13-python-lesson9.py/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/Python/13-python-lesson9.py/python9.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
          <a href="https://github.com/hothaifa96/DevSecOps20/tree/main/lessons/Python/13-python-lesson9.py/app" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Class Code</a>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- Git Card -->
<div class="lesson-card" >
  <h3 style="color: #333;">🔄 Git</h3>
  <p style="color: #444;">Master version control with Git and GitHub for collaborative development.</p>
  <div class="lesson-files">
    <h4 style="color: #333;">Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: Basics and Configs</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/GIT/lesson1/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/GIT/lesson1/GIT1.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 2: Branching and Merging</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/GIT/Lesson2/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/GIT/Lesso2/Git3.drawio.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 3: github and git </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/GIT/Lesson3/" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/GIT/Lesson3/lesson3.pdf" class="btn-link" style="background: rgba(0,0,0,0.15); color: #333;">PDF</a>
        </div>
      </li>
    </ul>
  </div>
</div>

<div class="lesson-card" >
  <h3>📜 Docker </h3>
  <p>Containerize and run all applications</p>
  <div class="lesson-files">
    <h4>Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: Docker archeticture and Run command</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Docker/Lession1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Docker/Lession1/CheatSheet.md" class="btn-link">Docker Commands</a>
          <a href="{{ site.baseurl }}/lessons/Docker/Lession1/Docker1.pdf" class="btn-link">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 2: If Statements and Conditions</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/class-code.md" class="btn-link">Class Code</a>
        </div>
      </li>
    </ul>
  </div>
</div>

</div>
