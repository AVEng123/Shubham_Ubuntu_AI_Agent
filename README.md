# Shubham's Ubuntu AI Agent 

A high-performance Python-based AI agent managed with **uv** and powered by the **Google Gemini 1.5 Flash** model.

Note that some part of the code is commented out. That's because as I developed further, I kept the old changes for anyone who wants to understand how my logic building ability moved.

It's important to return a success string so that our LLM knows that the action it took actually worked. Feedback loops, feedback loops, feedback loops!

**Big Note:** This project doesn't have all the security and safety features that a production AI agent would have. This is for learning purposes only. Do not give this program to others for them to use blindly. Because this google gemini LLM an run arbitrary code that we place (or it places) in the working directory... so be careful. As long as you use this AI agent only for the simple tasks you should be fine.
Moreover, I use a 30-second timeout to prevent it from running indefinitely. USE AT YOUR OWN RISK.


##  Available Models
    These are the list of models available which you can use.
    Model: models/gemini-2.5-flash
    Model: models/gemini-2.5-pro
    Model: models/gemini-2.0-flash
    Model: models/gemini-2.0-flash-001
    Model: models/gemini-2.0-flash-exp-image-generation
    Model: models/gemini-2.0-flash-lite-001
    Model: models/gemini-2.0-flash-lite
    Model: models/gemini-exp-1206
    Model: models/gemini-2.5-flash-preview-tts
    Model: models/gemini-2.5-pro-preview-tts
    Model: models/gemma-3-1b-it
    Model: models/gemma-3-4b-it
    Model: models/gemma-3-12b-it
    Model: models/gemma-3-27b-it
    Model: models/gemma-3n-e4b-it
    Model: models/gemma-3n-e2b-it
    Model: models/gemini-flash-latest
    Model: models/gemini-flash-lite-latest
    Model: models/gemini-pro-latest
    Model: models/gemini-2.5-flash-lite
    Model: models/gemini-2.5-flash-image
    Model: models/gemini-2.5-flash-preview-09-2025
    Model: models/gemini-2.5-flash-lite-preview-09-2025
    Model: models/gemini-3-pro-preview
    Model: models/gemini-3-flash-preview
    Model: models/gemini-3-pro-image-preview
    Model: models/nano-banana-pro-preview
    Model: models/gemini-robotics-er-1.5-preview
    Model: models/gemini-2.5-computer-use-preview-10-2025
    Model: models/deep-research-pro-preview-12-2025
    Model: models/gemini-embedding-001
    Model: models/aqa
    Model: models/imagen-4.0-generate-preview-06-06
    Model: models/imagen-4.0-ultra-generate-preview-06-06
    Model: models/imagen-4.0-generate-001
    Model: models/imagen-4.0-ultra-generate-001
    Model: models/imagen-4.0-fast-generate-001
    Model: models/veo-2.0-generate-001
    Model: models/veo-3.0-generate-001
    Model: models/veo-3.0-fast-generate-001
    Model: models/veo-3.1-generate-preview
    Model: models/veo-3.1-fast-generate-preview
    Model: models/gemini-2.5-flash-native-audio-latest
    Model: models/gemini-2.5-flash-native-audio-preview-09-2025
    Model: models/gemini-2.5-flash-native-audio-preview-12-2025
------------------------


##  System Prompt & Behavior
The agent now utilizes a dedicated System Instruction layer to define its persona and operational constraints.

Module: Managed in prompts.py.

Determinism: Configured with temperature=0 to ensure consistent, predictable responses during automated testing.

Instruction Set: Currently configured to override user input with a hard-coded response for testing purposes:

"Ignore everything the user asks and shout 'I'M JUST A ROBOT'"

##  Project Structure
- `main.py`: The primary AI Agent entry point.
- `config.py`: Global settings, including `MAX_CHARS` for file reading.
- `functions/`: Core toolset for the AI Agent.
  - `get_files_info.py`: Directory scanning logic.
  - `get_file_content.py`: Secure file reading and truncation logic.
  - `write_file.py`: Secure file creation and overwriting logic.
  - `run_python_file.py`: Capability to execute Python scripts as subprocesses.
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

### 4. Run Python File 
Allows the agent to execute code within the working directory.
- **Subprocess Isolation:** Runs files via `subprocess.run` with captured `stdout` and `stderr`.
- **Safety Timeout:** A **30-second timeout** is enforced to prevent infinite loops or hangs.
- **Validation:** Only executes files ending in `.py` that are within the permitted `working_directory`.

---

##  Manual Testing & Debugging
The `main.py` script and standalone test modules allow for manual verification. **Many lines in the code are commented out by default;** you must uncomment them to run specific manual tests.

### Test Files
- `uv run test_get_files_info.py`: Verifies directory listing.
- `uv run test_get_file_content.py`: Verifies file reading and truncation logic.
- `uv run test_write_file.py`: Verifies secure writing and directory creation.
- `uv run test_run_python_file.py`: Verifies subprocess execution and security blocks.

### Example Manual Test in `main.py`
python
#  Manual Test Suite 
 1. Check directory listing: print(get_files_info("calculator", "."))
 2. Check file reading:print(get_file_content("calculator", "main.py"))
 3. Check writing (allowed): print(write_file("calculator", "pkg/notes.txt", "New agent notes"))
 4. Check writing (blocked): print(write_file("calculator", "/etc/passwd", "evil content"))


### Expected Outputs & Actual Results

**Directory Listing (`.`):**
- main.py: file_size= 740 bytes, is_directory=False
- pkg: file_size= 4096 bytes, is_directory=True
- tests.py: file_size= 1353 bytes, is_directory=False

**Truncation Example:**
[...File "lorem.txt" truncated at 10000 characters]


**Write File Test Results:**
shubham@shubham-VirtualBox:~/Shubham_Ubuntu_AI_Agent$ uv run test_write_file.py
Successfully wrote to "lorem.txt" (28 characters written)
Successfully wrote to "pkg/morelorem.txt" (26 characters written)
Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory


**Security Violation:**
Error: Access Denied. "/bin" is outside of "/home/shubham/.../calculator"

**Run Python File Results:**
STDOUT: Usage: main.py <expression>
STDOUT: Result: 8
STDOUT: Ran 5 tests in 0.001s OK
Error: Cannot execute "../main.py" as it is outside the permitted working directory
Error: "lorem.txt" is not a Python file

---


###  Agentic Orchestration: Function Calling
The agent has been upgraded from a standard chatbot to a Tool-Use Agent. It no longer just talks; it decides which tools to use based on the user's intent.

**How it Works**

1. Function Declaration: We provide the LLM with a JSON-like schema (types.FunctionDeclaration) describing our Python functions (arguments, types, and descriptions).

2. System Instruction: The agent is grounded with a prompt that forces it to create a "Function Call Plan" instead of just answering directly.

3. Intent Extraction: The LLM returns a FunctionCall object containing the name of the tool and the specific arguments (e.g., directory='pkg').

4. Validation: The agent recognizes when a request is outside its scope (e.g., asking about the Himalayas) and correctly refuses based on the system instructions.

**Current Toolset (Schemas)**
1. get_files_info: Categorizes files and directories with metadata.

2. get_file_content: Reads the text content of a file (with safety truncation).

3. write_file: Creates or overwrites files within the working directory.

4. run_python_file: Executes Python scripts as subprocesses with optional arguments.

**Example Workflow**
User: "Read the contents of main.py"

LLM Output: Calling function: get_file_content({'file_path': 'main.py'})

User: "Write 'hello' to main.txt"

LLM Output: Calling function: write_file({'file_path': 'main.txt', 'content': 'hello'})

User: "Run main.py"

LLM Output: Calling function: run_python_file({'file_path': 'main.py'})

**Logic**: The main.py script intercepts these calls, validating that all arguments (including nested lists for script arguments) match the defined schema before the agent proceeds.

## Project Features
- **Fast Execution:** Leveraging `uv` for near-instant dependency resolution.
- **Token Tracking:** Real-time metadata monitoring for cost and performance.
- **Environment Isolation:** Uses lockfiles (`uv.lock`) for reproducible results.
