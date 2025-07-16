---
layout: default
title: DevSecOps Labs 2
---

# LAB2

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lab 2 - Linux Basics 2 | DevSecOps 20</title>
    <style>
      :root {
        --bg-primary: #0a0a0a;
        --bg-secondary: #1a1a1a;
        --text-primary: #ffffff;
        --text-secondary: #b0b0b0;
        --neon-blue: #00f5ff;
        --neon-green: #00ff41;
        --neon-purple: #8a2be2;
        --neon-pink: #ff0080;
        --neon-yellow: #ffff00;
        --cyber-gradient: linear-gradient(
          45deg,
          var(--neon-blue),
          var(--neon-purple),
          var(--neon-green)
        );
        --border-color: rgba(0, 245, 255, 0.3);
      }

      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: "Courier New", monospace;
        background: var(--bg-primary);
        color: var(--text-primary);
        line-height: 1.6;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 10px;
        padding: 30px;
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.1);
      }

      .header {
        text-align: center;
        margin-bottom: 40px;
        border-bottom: 2px solid var(--neon-blue);
        padding-bottom: 20px;
      }

      .header h1 {
        font-size: 2.5rem;
        background: var(--cyber-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 10px;
      }

      .header p {
        color: var(--text-secondary);
        font-size: 1.1rem;
      }

      .section {
        margin-bottom: 40px;
        padding: 25px;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background: rgba(0, 245, 255, 0.05);
        transition: all 0.3s ease;
      }

      .section:hover {
        border-color: var(--neon-blue);
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.2);
        transform: translateY(-2px);
      }

      .section h2 {
        color: var(--neon-blue);
        font-size: 1.8rem;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 1px solid var(--neon-blue);
        padding-bottom: 10px;
      }

      .section h3 {
        color: var(--neon-green);
        font-size: 1.4rem;
        margin: 20px 0 15px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
      }

      .task-list {
        list-style: none;
        counter-reset: task-counter;
      }

      .task-list li {
        counter-increment: task-counter;
        margin-bottom: 15px;
        padding: 15px;
        background: rgba(0, 0, 0, 0.3);
        border-left: 4px solid var(--neon-blue);
        border-radius: 5px;
        position: relative;
      }

      .task-list li::before {
        content: "TASK " counter(task-counter);
        position: absolute;
        top: -10px;
        left: 10px;
        background: var(--neon-blue);
        color: var(--bg-primary);
        padding: 2px 8px;
        font-size: 0.8rem;
        font-weight: bold;
        border-radius: 3px;
      }

      .code-block {
        background: rgba(0, 0, 0, 0.8);
        border: 1px solid var(--neon-green);
        border-radius: 5px;
        padding: 15px;
        margin: 15px 0;
        font-family: "Courier New", monospace;
        color: var(--neon-green);
        overflow-x: auto;
      }

      .highlight {
        background: rgba(0, 245, 255, 0.1);
        border: 1px solid var(--neon-blue);
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
      }

      .bonus {
        background: linear-gradient(
          45deg,
          rgba(255, 0, 128, 0.1),
          rgba(138, 43, 226, 0.1)
        );
        border: 2px solid var(--neon-pink);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
      }

      .bonus h3 {
        color: var(--neon-pink);
        text-align: center;
        font-size: 1.6rem;
        margin-bottom: 20px;
      }

      .navigation {
        text-align: center;
        margin: 30px 0;
      }

      .btn {
        display: inline-block;
        padding: 12px 24px;
        background: var(--cyber-gradient);
        color: var(--bg-primary);
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        margin: 0 10px;
      }

      .btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.6);
      }

      .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid var(--border-color);
        color: var(--text-secondary);
        font-size: 0.9rem;
      }

      @keyframes glow {
        0%,
        100% {
          box-shadow: 0 0 5px rgba(0, 245, 255, 0.5);
        }
        50% {
          box-shadow: 0 0 20px rgba(0, 245, 255, 0.8);
        }
      }

      .section:hover {
        animation: glow 2s infinite;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>🔬 Lab 2 - Linux Basics 2</h1>
        <p>
          Advanced Linux Operations: Number Systems, Users, Permissions & Text
          Processing
        </p>
      </div>

      <div class="section">
        <h2>1: Number Systems</h2>
        <p>
          Master binary, decimal, and hexadecimal conversions with practical
          exercises.
        </p>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>Convert the decimal number <code>13</code> to binary.</li>
          <li>Convert the decimal number <code>255</code> to hexadecimal.</li>
          <li>Convert the binary number <code>1101</code> to decimal.</li>
          <li>Convert the hexadecimal number <code>FF</code> to decimal.</li>
          <li>
            Write a script that takes a decimal number as input and prints its
            binary and hexadecimal equivalents.
          </li>
        </ol>
      </div>

      <div class="section">
        <h2>2: Users and Groups in Ubuntu</h2>
        <p>Learn user and group management in Linux systems.</p>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>Create a new user named <code>alice</code>.</li>
          <li>Create a new group named <code>devops</code>.</li>
          <li>Add <code>alice</code> to the <code>devops</code> group.</li>
          <li>Display <code>alice</code>'s user and group information.</li>
          <li>
            Delete the user <code>alice</code> and remove their home directory.
          </li>
        </ol>
      </div>

      <div class="section">
        <h2>3: File Permissions</h2>
        <p>
          Master file permission management using both numeric and symbolic
          modes.
        </p>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>Create a new file called <code>testfile</code>.</li>
          <li>
            Set <code>testfile</code>'s permissions to <code>755</code> using
            numeric mode.
          </li>
          <li>
            Change the file's user permission to remove execute access using
            symbolic mode.
          </li>
          <li>Change the file owner to your current user.</li>
          <li>Set SUID, SGID, and sticky bits on <code>testfile</code>.</li>
        </ol>
      </div>

      <div class="section">
        <h2>4: Sudo and System Files</h2>
        <p>Understand privilege escalation and system file management.</p>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>Create a new user <code>bob</code>.</li>
          <li>Add <code>bob</code> to the <code>sudo</code> group.</li>
          <li>Use <code>sudo</code> to run a command as another user.</li>
          <li>
            View the contents of <code>/etc/passwd</code>,
            <code>/etc/group</code>, and <code>/etc/shadow</code>.
          </li>
        </ol>
      </div>

      <div class="section">
        <h2>5: Command Line I/O and Piping</h2>
        <p><strong>Objective:</strong> Practice using redirection and pipes.</p>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>Redirect a command's output to a file.</li>
          <li>Redirect error output to a separate file.</li>
          <li>
            Pipe the output of <code>ls -la</code> into <code>grep</code> to
            filter results.
          </li>
          <li>Chain commands using multiple pipes.</li>
          <li>
            Use <code>tee</code> to write output to a file and display it on the
            terminal.
          </li>
        </ol>
      </div>

      <div class="section">
        <h2>6: Text Processing Tools</h2>
        <p>
          <strong>Objective:</strong> Use tools like <code>cut</code>,
          <code>wc</code>, <code>grep</code>, <code>sort</code>, and
          <code>uniq</code>.
        </p>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>
            Use <code>cut</code> to extract the usernames from
            <code>/etc/passwd</code>.
          </li>
          <li>
            Use <code>wc</code> to count the number of lines in
            <code>/etc/passwd</code>.
          </li>
          <li>
            Use <code>grep</code> to find all lines in
            <code>/etc/passwd</code> containing <code>/bin/bash</code>.
          </li>
          <li>
            Sort and remove duplicate usernames in <code>/etc/passwd</code>.
          </li>
          <li>
            Create a command chain that shows the most frequent commands from
            your history.
          </li>
        </ol>
      </div>

      <div class="bonus">
        <h3>🎯 Bonus: Integrated Challenge</h3>
        <p>
          <strong>Scenario:</strong> You are setting up a system with the
          following requirements:
        </p>
        <ul>
          <li>
            A user <code>devuser</code> must be created and added to a group
            <code>devgroup</code>.
          </li>
          <li>
            A file <code>/tmp/devfile.txt</code> must be created with custom
            content.
          </li>
          <li>The file should have specific permissions and ownership.</li>
          <li>
            Use text processing tools to extract, filter, and analyze the file's
            contents.
          </li>
        </ul>

        <h3>Tasks:</h3>
        <ol class="task-list">
          <li>
            Create the user <code>devuser</code> and group
            <code>devgroup</code>.
          </li>
          <li>Add <code>devuser</code> to <code>devgroup</code>.</li>
          <li>
            Create the file <code>/tmp/devfile.txt</code> with at least two
            lines (e.g., containing "error" and "info" messages).
          </li>
          <li>
            Change the file's ownership to <code>devuser:devgroup</code> and set
            permissions to <code>640</code>.
          </li>
          <li>
            Use <code>grep</code>, <code>cut</code>, and <code>tee</code> to
            extract and log error messages from the file.
          </li>
        </ol>
      </div>

      <div class="navigation">
        <a href="../../index.md" class="btn">🏠 Back to Home</a>
        <a href="../" class="btn">📚 All Labs</a>
      </div>

      <div class="footer">
        <p><strong>🔒 [CLASSIFIED] DEVSECOPS 20 TRAINING MODULE</strong></p>
        <p>Clearance Level: ULTRA | Last Updated: July 2025</p>
      </div>
    </div>

    <script>
      // Enhanced interactivity
      document.addEventListener("DOMContentLoaded", function () {
        // Add click effects to sections
        const sections = document.querySelectorAll(".section");
        sections.forEach((section) => {
          section.addEventListener("click", function () {
            this.style.transform = "scale(1.02)";
            setTimeout(() => {
              this.style.transform = "";
            }, 200);
          });
        });

        // Add typing effect to code elements
        const codeElements = document.querySelectorAll("code");
        codeElements.forEach((code) => {
          code.addEventListener("mouseenter", function () {
            this.style.color = "var(--neon-yellow)";
            this.style.textShadow = "0 0 10px var(--neon-yellow)";
          });

          code.addEventListener("mouseleave", function () {
            this.style.color = "";
            this.style.textShadow = "";
          });
        });

        // Add progress tracking
        const tasks = document.querySelectorAll(".task-list li");
        tasks.forEach((task) => {
          task.addEventListener("click", function () {
            if (this.style.background.includes("rgba(0, 255, 65, 0.2)")) {
              this.style.background = "rgba(0, 0, 0, 0.3)";
              this.style.borderLeftColor = "var(--neon-blue)";
            } else {
              this.style.background = "rgba(0, 255, 65, 0.2)";
              this.style.borderLeftColor = "var(--neon-green)";
            }
          });
        });
      });
    </script>
  </body>
</html>
