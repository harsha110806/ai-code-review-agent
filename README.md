# AI Code Review Agent

An AI-powered Python code review agent that compresses code context, generates automated feedback, and produces a refined version of Python code based on best practices.

---

## Problem Statement
Manual code reviews are time-consuming and often error-prone. This project automates the code review process by analyzing Python source code, compressing relevant context, generating intelligent feedback, and suggesting refined code improvements using AI-driven logic.

---

## System Architecture
Python Source Code
↓
AST Parser
↓
Context Compressor
↓
AI Reviewer
↓
Code Refiner
↓
Review Feedback + Refined Code

---

## Features
- Parses Python code using Python’s AST module  
- Extracts structural context such as functions, loops, and conditional statements  
- Compresses code context into a concise and meaningful summary  
- Generates automated, human-like code review feedback  
- Produces a refined version of the input code using rule-based refactoring  
- Modular and extensible design suitable for academic use  

---

## Project Structure
ai-code-review-agent/
│
├── src/
│ ├── parser.py
│ ├── context_compressor.py
│ ├── ai_reviewer.py
│ ├── refiner.py
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

## How to Run

```bash
cd src
python main.py
```

Sample Output
AI Code Review Feedback
- Function 'process_orders' has many parameters. Consider using a data structure or keyword arguments.
- High number of loops detected. Consider refactoring to improve readability and performance.

Refined Code Output
# REFACTORED VERSION (Suggested Improvement)
# Parameters grouped into a configuration dictionary

def process_orders(orders, tax_rate, discount, shipping_fee, service_charge, region):
    ...

Creative Feature

Context-Aware Review Summary with Automated Code Refinement
The system first compresses large codebases into a minimal structural summary and then generates both review feedback and a refined version of the code using rule-based refactoring techniques.

Future Enhancements

Multi-file project analysis

Real LLM API integration

GitHub pull request review automation

Code quality and complexity scoring

Academic Note

This project demonstrates the application of static analysis, context compression, AI-assisted reasoning, and automated refactoring techniques for software engineering tasks.

---



