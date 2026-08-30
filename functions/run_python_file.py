import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        wd_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(wd_abs, file_path))

        if os.path.commonpath([wd_abs, file_path_abs]) != wd_abs:
            raise ValueError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.isfile(file_path_abs):
            raise ValueError(f'Error: "{file_path}" does not exist or is not a regular file')
        
        if os.path.splitext(file_path_abs)[-1] != ".py":
            raise ValueError(f'Error: "{file_path}" is not a Python file')
        
        command = ["python", file_path_abs]
        if args is not None:
            command += args
        
        result = subprocess.run(
            command,
            cwd=os.getcwd(),
            capture_output=True,
            timeout=30,
            text=True,
        )
        
        output_str = ""
        return_code = result.returncode
        if return_code != 0:
            output_str += f"Process exited with code {return_code}"

        stdout = result.stdout
        if stdout:
            output_str += f"STDOUT: {stdout}"

        stderr = result.stderr
        if stderr:
            output_str += f"STDERR: {stderr}"

        if not stdout and not stderr:
            output_str += f"No output produced."

        return output_str

    except Exception as exc:
        return f"Error: executing Python file: {exc}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a Python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to run, relative to the working directory"
                },
                "args": {
                    "type": "array",
                    "description": "A list of positional arguments to the file. The arguments must be strings"
                }
            },
            "required": ["file_path"]
        },
    },
}
