from pathlib import Path

def check_if_valid_directory(directory: Path)->bool:
    if not directory.exists():
        print("Error: path doesn't exist")
        return False

    if not directory.is_dir():
        print("Error: input path is not a directory")
        return False

    return True

def display_directory(directory: Path)->None:
    print("\nOrion File Explorer")
    print(f"Current Directory: {directory.absolute()}\n")

    for item in directory.iterdir():
         item_type = "Directory" if item.is_dir() else "File"
         item_size = item.stat().st_size
         item_name = item.name.rstrip()

         print(f'Name:{item_name}\tType:{item_type}\tSize:{item_size} Bytes')
