<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevSecOps Lessons</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            color: white;
            margin-bottom: 50px;
            animation: fadeInDown 0.8s ease;
        }

        header h1 {
            font-size: clamp(2rem, 5vw, 3.5rem);
            font-weight: 800;
            margin-bottom: 15px;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            letter-spacing: -1px;
        }

        header p {
            font-size: clamp(1rem, 2vw, 1.3rem);
            opacity: 0.95;
            font-weight: 300;
        }

        /* Labs Card - Full Width Hero */
        .labs-hero {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border-radius: 25px;
            padding: 50px;
            color: white;
            margin-bottom: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
            animation: fadeIn 0.8s ease;
        }

        .labs-hero::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 15s ease-in-out infinite;
        }

        .labs-hero-content {
            position: relative;
            z-index: 1;
            text-align: center;
        }

        .labs-hero h2 {
            font-size: clamp(2rem, 4vw, 3rem);
            margin-bottom: 20px;
            font-weight: 700;
        }

        .labs-hero p {
            font-size: clamp(1rem, 2vw, 1.4rem);
            margin-bottom: 30px;
            opacity: 0.9;
        }

        .labs-btn {
            display: inline-block;
            background: white;
            color: #1e3c72;
            padding: 18px 45px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.2rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .labs-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            background: #f0f0f0;
        }

        /* Lesson Cards Grid */
        .lesson-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            animation: fadeIn 1s ease;
        }

        .lesson-card {
            background: white;
            border-radius: 20px;
            padding: 0;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            overflow: hidden;
            position: relative;
        }

        .lesson-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 60px rgba(0,0,0,0.25);
        }

        .card-header {
            padding: 35px 30px;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .card-header::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
        }

        .card-header h3 {
            font-size: 1.8rem;
            margin-bottom: 12px;
            position: relative;
            z-index: 1;
            font-weight: 700;
        }

        .card-header p {
            position: relative;
            z-index: 1;
            opacity: 0.95;
            font-size: 1.05rem;
        }

        /* Color Schemes */
        .linux { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
        .bash { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .python { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
        .git { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
        .docker { background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); }

        .card-body {
            padding: 30px;
            background: white;
        }

        .card-body h4 {
            color: #333;
            font-size: 1.2rem;
            margin-bottom: 20px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card-body h4::before {
            content: '📚';
            font-size: 1.4rem;
        }

        .lesson-list {
            list-style: none;
        }

        .lesson-item {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid #667eea;
            transition: all 0.3s ease;
        }

        .lesson-item:hover {
            background: #e9ecef;
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .lesson-title {
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 12px;
            font-size: 1.05rem;
        }

        .lesson-links {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .btn-link {
            display: inline-flex;
            align-items: center;
            padding: 8px 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        }

        .btn-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }

        .btn-link:active {
            transform: translateY(0);
        }

        /* Animations */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1) rotate(0deg);
            }
            50% {
                transform: scale(1.1) rotate(5deg);
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .lesson-grid {
                grid-template-columns: 1fr;
            }

            .labs-hero {
                padding: 35px 25px;
            }

            .card-header {
                padding: 25px 20px;
            }

            .card-body {
                padding: 20px;
            }

            .lesson-links {
                flex-direction: column;
            }

            .btn-link {
                text-align: center;
                justify-content: center;
            }
        }

        @media (max-width: 480px) {
            body {
                padding: 15px;
            }

            header {
                margin-bottom: 30px;
            }

            .lesson-item {
                padding: 15px;
            }
        }

        /* Scrollbar Styling */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255,255,255,0.1);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.3);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255,255,255,0.5);
        }

        footer {
            text-align: center;
            color: white;
            margin-top: 60px;
            padding: 30px;
            font-size: 0.95rem;
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 DevSecOps Lessons</h1>
            <p>Master DevSecOps with hands-on labs and comprehensive lessons</p>
        </header>

        <!-- Labs Hero Section -->
        <div class="labs-hero">
            <div class="labs-hero-content">
                <h2>🔬 Hands-On Labs</h2>
                <p>Apply your knowledge with practical exercises, real-world scenarios, and interactive challenges. Master DevSecOps through hands-on experience.</p>
                <a href="#" class="labs-btn">Access Labs →</a>
            </div>
        </div>

        <!-- Lesson Cards Grid -->
        <div class="lesson-grid">
            
            <!-- Linux Basics Card -->
            <div class="lesson-card">
                <div class="card-header linux">
                    <h3>🐧 Linux Basics</h3>
                    <p>Master command-line, file systems, permissions, and process control</p>
                </div>
                <div class="card-body">
                    <h4>Available Lessons</h4>
                    <ul class="lesson-list">
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 1: Linux Basics 1</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 2: Linux Basics 2</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📋 Cheatsheet</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 3: Linux Basics 3</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📋 Cheatsheet</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 4: Linux Basics 4 (Networks)</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Bash Scripting Card -->
            <div class="lesson-card">
                <div class="card-header bash">
                    <h3>📜 Bash Scripting</h3>
                    <p>Automate tasks and create powerful scripts with bash programming</p>
                </div>
                <div class="card-body">
                    <h4>Available Lessons</h4>
                    <ul class="lesson-list">
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 1: Basics and Variables</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">⌨️ Basic Commands</a>
                                <a href="#" class="btn-link">🎯 Demo1</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 2: If Statements and Conditions</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Python Card -->
            <div class="lesson-card">
                <div class="card-header python">
                    <h3>🐍 Python</h3>
                    <p>Automate tasks and build tools with Python scripting for DevOps workflows</p>
                </div>
                <div class="card-body">
                    <h4>Available Lessons</h4>
                    <ul class="lesson-list">
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 1: Input, Print and Datatypes</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 2: Strings and Lists</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📋 Cheatsheet</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 3: If Statement</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 4: Lists, Tuples, Sets and For Loop</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                                <a href="#" class="btn-link">📋 List Methods</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 5: While and For Loops</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 6: JSON, PIP and RESTful API</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 7: Functions and RESTful API</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 8: Classes and OOP</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 9: OOP, Imports and GIT</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="link">📄 PDF</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Git Card -->
            <div class="lesson-card">
                <div class="card-header git">
                    <h3>🔄 Git</h3>
                    <p>Master version control with Git and GitHub for collaborative development</p>
                </div>
                <div class="card-body">
                    <h4>Available Lessons</h4>
                    <ul class="lesson-list">
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 1: Basics and Configs</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 2: Branching and Merging</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 3: GitHub and Git</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Docker Card -->
            <div class="lesson-card">
                <div class="card-header docker">
                    <h3>🐳 Docker</h3>
                    <p>Containerize and run all applications with Docker</p>
                </div>
                <div class="card-body">
                    <h4>Available Lessons</h4>
                    <ul class="lesson-list">
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 1: Docker Architecture and Run Command</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">⌨️ Docker Commands</a>
                                <a href="#" class="btn-link">📄 PDF</a>
                            </div>
                        </li>
                        <li class="lesson-item">
                            <div class="lesson-title">Lesson 2: Advanced Docker Concepts</div>
                            <div class="lesson-links">
                                <a href="#" class="btn-link">📖 Start Lesson</a>
                                <a href="#" class="btn-link">💻 Class Code</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

        </div>

        <footer>
            <p>💡 Built with passion for DevSecOps excellence</p>
            <p>© 2025 DevSecOps Training Program</p>
        </footer>
    </div>
</body>
</html>