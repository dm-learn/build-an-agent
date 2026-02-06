from functions.write_file import write_file


def main():
    
    files = ["lorem.txt", "pkg/morelorem.txt", "/tmp/temp.txt",]
    contents = [
        "wait, this isn't lorem ipsum",
        "lorem ipsum dolor sit amet",
        "this should not be allowed",
    ]

    for i in range(len(files)):
        result = write_file("calculator", files[i], contents[i])
        print(result)


if __name__ == "__main__":
    main()
