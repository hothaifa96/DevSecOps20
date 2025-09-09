---
layout: default
title: DevSecOps lessons
---

# DevSecOps lessons

Welcome to the DevSecOps course lessons! Click on any lesson topic below to explore the available lessons and materials.

<style>
.lesson-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin: 30px 0;
    align-items: start;
}
.lesson-card {
    background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
    border-radius: 15px;
    padding: 25px;
    color: white;
    transition: all 0.3s ease;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    position: relative;
    overflow: hidden;
    height: fit-content;
    align-self: start;
}
.lesson-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}
.lesson-card h3 {
    margin: 0 0 15px 0;
    font-size: 1.5em;
    font-weight: 600;
}
.lesson-card p {
    margin: 0;
    opacity: 0.9;
    line-height: 1.5;
}
.lesson-files {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 15px;
    margin-top: 15px;
    backdrop-filter: blur(10px);
}
.lesson-files h4 {
    margin: 0 0 10px 0;
    font-size: 1.1em;
    color: #fff;
}
.file-list {
    list-style: none;
    padding: 0;
    margin: 0;
}
.file-list li {
    padding: 8px 12px;
    margin: 5px 0;
    background: rgba(255,255,255,0.1);
    border-radius: 6px;
    border-left: 3px solid #fff;
    transition: all 0.2s ease;
}
.file-list li:hover {
    background: rgba(255,255,255,0.2);
    transform: translateX(5px);
}
.file-list a {
    color: white;
    text-decoration: none;
    display: block;
}
.file-list a:hover {
    text-decoration: underline;
}
.lesson-links {
    display: flex;
    gap: 10px;
    margin-top: 5px;
}
.btn-link {
    background: rgba(255,255,255,0.15);
    color: #fff;
    padding: 4px 10px;
    border-radius: 5px;
    text-decoration: none;
    font-size: 0.95em;
    transition: background 0.2s;
}
.btn-link:hover {
    background: rgba(255,255,255,0.3);
    text-decoration: underline;
}
</style>

<div class="lesson-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
  <h3>🔬 Hands-On Labs</h3>
  <p>Apply your knowledge with practical exercises, real-world scenarios, and interactive challenges. Master DevSecOps through hands-on experience.</p>
  <div class="lesson-files">
    <a href="{{ site.baseurl }}/labs/" class="btn-link" style="font-size:1.1em; font-weight:bold;">Access Labs</a>
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
        <span>Lesson 4: Linux Basics 4(networks)</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Linux-basics/04-linux-basics/" class="btn-link">Start Lesson</a>
        </div>
      </li>
    </ul>
  </div>
</div>

<!-- Python Card -->
<div class="lesson-card">
  <h3>🐍 Python</h3>
  <p>Automate tasks and build tools with Python scripting for DevOps workflows.</p>
  <div class="lesson-files">
    <h4>Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: input,print and datatypes</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/05-python-lesson1.py/" class="btn-link">Start Lesson</a>
          <a href="https://github.com/hothaifa96/DevSecOps20/blob/main/lessons/Python/05-python-lesson1.py/class_code.py" class="btn-link">Class Code</a>
          <a href="{{ site.baseurl }}/lessons/Python/05-python-lesson1.py/python1.pdf" class="btn-link">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 2: Strings and Lists</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/cheatsheet.webp" class="btn-link">Cheatsheet</a>
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/python2.pdf" class="btn-link">PDF</a>
        </div>
      </li>
       <li>
        <span>Lesson 3: If statement </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/07-python-lesson3.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/06-python-lesson2.py/python3.pdf" class="btn-link">PDF</a>
        </div>
      </li>
      <li>
        <span>Lesson 4: Lists,Tuples,sets and for loop </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/python4.drawio.pdf" class="btn-link">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4.py/list.md" class="btn-link">list methods</a>
          <a href="{{ site.baseurl }}/lessons/Python/08-python-lesson4/class_code.py" class="btn-link">class code </a>
        </div>
      </li>
      <li>
        <span>Lesson 5: while and for loops </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/09-python-lesson5.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/09-python-lesson4.py/python5.drawio.pdf" class="btn-link">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/09-python-lesson5.py/classcode.py" class="btn-link">class code </a>
        </div>
      </li>
       <li>
        <span>Lesson 6: JSON, while pip and RESTful API </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/python6.drawio.pdf" class="btn-link">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/10-python-lesson6.py/classcode.py" class="btn-link">class code </a>
        </div>
      </li>
      <li>
        <span>Lesson 7: functions and RESTful API </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/python7.pdf" class="btn-link">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/11-python-lesson7.py/classcode.py" class="btn-link">class code </a>
        </div>
      </li>

       <li>
        <span>Lesson 8: classes and OOP </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/python8.pdf" class="btn-link">PDF</a>
          <a href="{{ site.baseurl }}/lessons/Python/12-python-lesson8.py/classcode.md" class="btn-link">class code </a>
        </div>
      </li>

       <li>
        <span>Lesson 9: OOP,imports and GIT </span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Python/Python/13-python-lesson9.py/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Python/Python/13-python-lesson9.py/python9.pdf" class="btn-link">PDF</a>
          <a href="https://github.com/hothaifa96/DevSecOps20/tree/main/lessons/Python/13-python-lesson9.py/app" class="btn-link">class code </a>
        </div>
      </li>
    </ul>

  </div>
</div>

<!-- Git Card -->
<div class="lesson-card">
  <h3>🔄 GIT</h3>
  <p>Mastering Git and Github </p>
  <div class="lesson-files">
    <h4>Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: basics and configs</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/GIT/lesson1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/GIT/lesson1/GIT1.pdf" class="btn-link">PDF</a>
        </div>
      </li>
    </ul>
  </div>
</div>
</div>

<!-- Bash SCripting Card -->
<div class="lesson-card">
  <h3> Bash</h3>
  <p>Bashing and scripting </p>
  <div class="lesson-files">
    <h4>Available lessons:</h4>
    <ul class="file-list">
      <li>
        <span>Lesson 1: basics and variables</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/commands.txt" class="btn-link">basics commands</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/demo1.sh" class="btn-link">demo1</a>
        </div>
      </li>
        <li>
        <span>Lesson 2: if and conditions</span>
        <div class="lesson-links">
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/" class="btn-link">Start Lesson</a>
          <a href="{{ site.baseurl }}/lessons/Bash-scripting/bash-scripting-1/class-code.md" class="btn-link">class code</a>
        </div>
      </li>
    </ul>
  </div>
</div>
</div>
