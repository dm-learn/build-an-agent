import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        valid_target = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target:
            raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        if not os.path.isdir(target_dir):
            raise ValueError(f'Error: "{directory}" is not a directory')
        
        target_contents = os.listdir(target_dir)

        content_metadata = []
        for item in target_contents:
            item_path = os.path.join(target_dir, item)
            content_metadata.append(
                f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            )

        all_metadata = "\n".join(content_metadata)
        return all_metadata

    except Exception as exc:
        return f"Error: getting file info: {exc}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
