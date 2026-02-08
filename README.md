# Shubham's Ubuntu AI Agent 

A high-performance Python-based AI agent managed with **uv** and powered by the **Google Gemini 2.0 Flash** model.

## Project Structure
- `main.py`: The primary AI Agent entry point.
- `calculator/`: A test project for the agent to interact with.
  - `main.py`: CLI entry point for the calculator.
  - `pkg/`: Core logic and JSON rendering.
  - `tests.py`: Unit tests for calculator logic.

## Quick Start

### 1. Configuration
Create a `.env` file:
```text
GEMINI_API_KEY=your_api_key_here
```

## 🛠 Tech Stack
- **Environment:** Ubuntu Linux
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (Rust-based)
- **Model:** Gemini 2.0 Flash
- **CLI Framework:** Python `argparse`

## Quick Start

### 1. Prerequisites
Ensure you have `uv` installed:
\`\`\`bash
curl -LsSf https://astral.sh/uv/install.sh | sh
\`\`\`

### 2. Configuration
Create a \`.env\` file in the root directory:
\`\`\`text
GEMINI_API_KEY=your_api_key_here
\`\`\`

### 3. Running the Agent
**Standard mode:**
\`\`\`bash
uv run main.py "Your prompt here"
\`\`\`

**Verbose mode (shows token usage):**
\`\`\`bash
uv run main.py "Your prompt here" --verbose
\`\`\`

##  Project Features
- **Fast Execution:** Leveraging \`uv\` for near-instant dependency resolution.
- **Token Tracking:** Real-time metadata monitoring for cost and performance.
- **Environment Isolation:** Uses lockfiles (\`uv.lock\`) for reproducible results.
