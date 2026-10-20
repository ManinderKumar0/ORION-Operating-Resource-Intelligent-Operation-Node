from pathlib import Path
from file_manager import check_if_valid_directory, display_directory

def main():
    while True:
        initial_path = input("Enter Path (or q to quit): ")

        if initial_path == 'q':
            return

        current_directory = Path(initial_path)

        if check_if_valid_directory(current_directory):
            break

    while True:
        display_directory(current_directory)

        command = input("\nEnter item to open, q to quit or .. to go to parent: ")

        if command == 'q':
            break

        if command == '..':
            current_directory = current_directory.parent
            continue

        target = current_directory / command

        valid_directory = check_if_valid_directory(target)

        if not valid_directory:
            continue

        current_directory = target

if __name__ == "__main__":
    main()
