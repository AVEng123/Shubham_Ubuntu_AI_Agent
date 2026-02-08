# Shubham's Ubuntu AI Agent 

A high-performance Python-based AI agent managed with **uv** and powered by the **Google Gemini 2.0 Flash** model.

Based on: https://www.boot.dev/courses/build-ai-agent-python 

Note that some part of the code is commented out. That's because as I developed further, I kept the old changes for anyone who wants to understand how my logic building ability moved.

It's important to return a success string so that our LLM knows that the action it took actually worked. Feedback loops, feedback loops, feedback loops!

##  Project Structure
- `main.py`: The primary AI Agent entry point.
- `config.py`: Global settings, including `MAX_CHARS` for file reading.
- `functions/`: Core toolset for the AI Agent.
  - `get_files_info.py`: Directory scanning logic.
  - `get_file_content.py`: Secure file reading and truncation logic.
  - `write_file.py`: Secure file creation and overwriting logic.
- `calculator/`: A test project for the agent to interact with.
  - `main.py`: CLI entry point for the calculator.
  - `lorem.txt`: 20KB test file for truncation verification.

##  Tech Stack
- **Environment:** Ubuntu Linux
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (Rust-based)
- **Model:** Gemini 2.0 Flash
- **CLI Framework:** Python `argparse`

##  Quick Start

### 1. Prerequisites
Ensure you have `uv` installed:
bash
curl -LsSf https://astral.sh/uv/install.sh | sh


### 2. Configuration
Create a `.env` file in the root directory:
text
GEMINI_API_KEY=your_api_key_here


### 3. Running the Agent
**Standard mode:**
bash
uv run main.py "Your prompt here"


**Verbose mode (shows token usage):**
bash
uv run main.py "Your prompt here" --verbose


---

##  AI Tools & Capabilities

### 1. Get Files Info
Scans directory structures within a restricted scope to ensure the AI explores the codebase safely.
- **Security:** Uses `os.path.commonpath` to prevent access to system directories like `/bin`.

### 2. Get File Content
Allows the agent to read file contents as a string for analysis.
- **Truncation:** Automatically caps reads at **10,000 characters** (configurable in `config.py`) to protect token limits.
- **Validation:** Only allows reading files within the permitted `working_directory`.

### 3. Write File 
Empowers the agent to create new files or overwrite existing ones.
- **Directory Auto-Creation:** Automatically builds parent directories using `os.makedirs(exist_ok=True)` if they don't exist.
- **Safety Checks:** Prevents overwriting actual directories and blocks any write attempts outside the `working_directory`.
- **Feedback Loop:** Returns a clear success message including the character count to confirm the operation.



---

##  Manual Testing & Debugging
The `main.py` script and standalone test modules allow for manual verification. **Many lines in the code are commented out by default;** you must uncomment them to run specific manual tests.

### Test Files
- `uv run test_get_files_info.py`: Verifies directory listing.
- `uv run test_get_file_content.py`: Verifies file reading and truncation logic.
- `uv run test_write_file.py`: Verifies secure writing and directory creation.

### Example Manual Test in `main.py`
python
# --- Manual Test Suite ---
# 1. Check directory listing:
# print(get_files_info("calculator", "."))

# 2. Check file reading:
# print(get_file_content("calculator", "main.py"))

# 3. Check writing (allowed):
# print(write_file("calculator", "pkg/notes.txt", "New agent notes"))

# 4. Check writing (blocked):
# print(write_file("calculator", "/etc/passwd", "evil content"))


### Expected Outputs & Actual Results

**Directory Listing (`.`):**
- main.py: file_size= 740 bytes, is_directory=False
- pkg: file_size= 4096 bytes, is_directory=True
- tests.py: file_size= 1353 bytes, is_directory=False

**Truncation Example:**
text
[...File "lorem.txt" truncated at 10000 characters]


**Write File Test Results:**
text
shubham@shubham-VirtualBox:~/Shubham_Ubuntu_AI_Agent$ uv run test_write_file.py
Successfully wrote to "lorem.txt" (28 characters written)
Successfully wrote to "pkg/morelorem.txt" (26 characters written)
Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory


**Security Violation:**
text
Error: Access Denied. "/bin" is outside of "/home/shubham/.../calculator"


---

## Project Features
- **Fast Execution:** Leveraging `uv` for near-instant dependency resolution.
- **Token Tracking:** Real-time metadata monitoring for cost and performance.
- **Environment Isolation:** Uses lockfiles (`uv.lock`) for reproducible results.
