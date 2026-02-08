import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    #print(f"abs_working_directory: {abs_working_directory}")
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        print(f'Error: Cannot write to "{file_path}" as it is a directory. Hence we make the directory and write the file there.')
        parent_directory = os.path.dirname(abs_file_path)
        try:
            os.makedirs(parent_directory, exist_ok=True)
        except Exception as e:
            return f'Error: Failed to create directory "{parent_directory}". {str(e)}'

    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{file_path}". {str(e)}'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
    ),
)
    

    