from functions.get_file_content import get_file_content


def main():
    
    files = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

    for file in files:
        content = get_file_content("calculator", file)
        print(content)


if __name__ == "__main__":
    main()
