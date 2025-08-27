def main():
    # Ask the user for input file name
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except IOError:
        print("Error: Could not read the file.")
        return

    # Modify the content (example: uppercase)
    modified_content = content.upper()

    # Create new output file
    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w", encoding="utf-8") as f:
            f.write(modified_content)
        print(f"Modified file saved as: {new_filename}")
    except IOError:
        print("Error: Could not write the modified file.")


if __name__ == "main":
    main()
