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


##  Tooling: Get Files Info
The agent has been granted the ability to scan directory structures within a restricted scope. This ensures the AI can explore the codebase without accessing sensitive system files.

###  Security Guardrails
We use `os.path.commonpath` to ensure the `target_dir` always resides within the `working_directory`.
- **Valid:** `calculator/pkg` -> Allowed.
- **Invalid:** `/bin` or `../` -> Blocked with an `Error: Access Denied` message.

### Manual Testing & Debugging
The `main.py` script contains several pre-configured test cases for the `get_files_info` tool. To verify specific behaviors, you must **uncomment** the relevant lines in the `main()` function:

```python
# --- Manual Test Suite ---
# 1. Test current directory
print(get_files_info("calculator", "."))

# 2. Test sub-directory
print(get_files_info("calculator", "pkg"))

# 3. Test security (Outside working dir)
print(get_files_info("calculator", "/bin"))

Expected Outputs
When running these tests via uv run main.py, you should see results similar to these:

Current Directory (.):
- main.py: file_size=740 bytes, is_dir=False
- pkg: file_size=4096 bytes, is_dir=True
- tests.py: file_size=1353 bytes, is_dir=False

Security Violation (/bin):
Error: Access Denied. "/bin" is outside of "/home/shubham/.../calculator"


Functions Directory
functions/get_files_info.py: Contains the logic for path normalization and directory iteration.
functions/__init__.py: Required for Python package resolution.