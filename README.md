# AI Code Review Agent

An AI-powered Python code review agent that compresses code context 
and provides automated feedback based on best practices.

---

# Problem Statement
Manual code reviews are time-consuming and they are often error-prone. This project helps to automate the code review process by analyzing Python source code, compressing relevant context, and generating intelligent feedback using AI-driven logic.

---

# System Architecture
Python Code
↓
AST Parser
↓
Context Compressor
↓
AI Reviewer
↓
Review Feedback

---

# Features
- Parses Python code using AST
- Extracts structural context (functions, loops, conditionals)
- Compresses code context into a concise summary
- Generates automated, human-like review feedback
- Modular and extensible design

---

# Project Structure
ai-code-review-agent/
│
├── src/
│ ├── parser.py
│ ├── context_compressor.py
│ ├── ai_reviewer.py
│ └── main.py
│
├── examples/
│ └── sample_code.py
│
├── docs/
│
├── requirements.txt
└── README.md

---

# How to Run
```bash
cd src
python main.py
```

# AI Code Review Feedback:
- Function 'example' has many parameters. Consider using a data structure or keyword arguments.
- High number of loops detected. Consider refactoring to improve readability and performance.

# Creative Feature
Context-Aware Review Summary
The system compresses large codebases into a minimal structural summary before generating feedback, improving efficiency and accuracy.

# Future Enhancements
Multi-file project analysis
Real LLM API integration
GitHub PR review automation
Code quality scoring



