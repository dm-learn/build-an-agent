from functions.get_files_info import get_files_info


def main():

    directories = [".", "pkg", "/bin", ".."]
    for directory in directories:
        files_info = get_files_info("calculator", directory)

        print(f"Result for '{"current" if directory == "." else directory}' directory:\n{files_info}")

if __name__ == "__main__":
    main()
