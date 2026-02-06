import os
from google.genai import types


def write_file(working_directory, file_path, content):
    
    try:
        wd_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(wd_abs, file_path))

        if os.path.commonpath([wd_abs, file_path_abs]) != wd_abs:
            raise ValueError(f"Error: cannot access {file_path} because it is outside the permitted working directory.")
        
        if os.path.isdir(file_path_abs):
            raise ValueError(f"Error: cannot write to {file_path} as it is a directory.")
        
        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        with open(file_path_abs, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
        
    except Exception as exc:
        return f"Error: writing file: {exc}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file at file_path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file"
            )
        },
        required=["file_path", "content"]
    ),
)
