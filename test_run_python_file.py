from functions.run_python_file import run_python_file


def main():
    
    run_files = ["main.py", "main.py", "tests.py", "../main.py", "nonexistent.py", "lorem.txt"]
    files_args = [None, ["3 + 5"], None, None, None, None]
    for i in range(len(run_files)):
        run_file = run_files[i]
        file_args = files_args[i]
        result = run_python_file("calculator", run_file, file_args)
        print(f"Result for {run_files[i]} with args {file_args if files_args is not None else 'None'}...\n{result}")


if __name__ == "__main__":
    main()
