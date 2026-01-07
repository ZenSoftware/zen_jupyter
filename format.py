import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Replace LaTex escapes with with KaTex in a file."
    )
    parser.add_argument("file_path", help="Path to the file you want to modify")

    args = parser.parse_args()
    file_path = args.file_path

    # Read the file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # print(repr(content[:500]))

    # Perform the replacement
    updated = content.replace(r"\\[", "$$")
    updated = updated.replace(r"\\]", "$$")
    updated = updated.replace(r"\\(", "$")
    updated = updated.replace(r"\\)", "$")

    # Write back to the same file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated)


if __name__ == "__main__":
    main()
