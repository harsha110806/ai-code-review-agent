# Architecture Documentation

The AI Code Review Agent is designed using a modular pipeline architecture. Each module handles a specific responsibility such as parsing, context compression, and review generation. This separation improves maintainability and scalability.

The system leverages Python's AST for static analysis and applies AI-inspired reasoning on compressed context to generate feedback efficiently.
