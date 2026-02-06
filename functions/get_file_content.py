import os
from google.genai import types


MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    
    try:
        wd_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(wd_abs, file_path))

        if os.path.commonpath([wd_abs, file_path_abs]) != wd_abs:
            raise ValueError(f"Error: cannot access {file_path} because it is outside the permitted working directory.")
        
        if not os.path.isfile(file_path_abs):
            raise ValueError(f"Error: {file_path} is not a file.")
        
        with open(file_path_abs, "r") as f:
            file_content = f.read(MAX_CHARS)

            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    
        return file_content
    
    except Exception as exc:
        return f"Error: getting file content: {exc}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns a string containing the content of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)