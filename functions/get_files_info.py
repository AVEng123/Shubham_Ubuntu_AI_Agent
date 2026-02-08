import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    
    if directory is None or directory == ".":
        abs_directory = abs_working_directory
    else:
        abs_directory = os.path.abspath(directory)
    
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Access Denied. "{abs_directory}" is outside of "{abs_working_directory}"'
    
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a valid directory"'
    
    final_response = ""
    
    contents = os.listdir(abs_directory)
    for content_item in contents:
        content_path = os.path.join(abs_directory, content_item)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        print(f"{content_item} - {'Directory' if is_dir else 'File'}")
        final_response += f"- {content_item}: file_size= {size} bytes, is_directory={is_dir}\n"
    return final_response