import os
from config import MAX_CHARS


def get_files_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    #print(f"Working directory: {abs_working_directory}")
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    #print(f"Requested file path: {abs_file_path}")
    
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Access Denied. "{abs_file_path}" is outside of "{abs_working_directory}"'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a valid file"'
    
    try:
        with open(abs_file_path, 'r') as file:
            content = file.read(MAX_CHARS)
            if len(content) >= MAX_CHARS:
                content += f"\n... (truncated to {MAX_CHARS} characters)"
        #print(f"Content of {file_path}:\n{content}\n")
        
        return content
    except Exception as e:
        return f"Error reading file: {e}"