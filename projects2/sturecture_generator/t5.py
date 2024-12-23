import os

def print_tree(startpath, prefix="", last=True, file=None, skip_folders=None, only_folders=False, current_depth=0):
    # List all items in the directory
    items = os.listdir(startpath)

    # Exclude hidden files and folders
    items = [item for item in items if not item.startswith('.')]
    
    # Skip specified folders
    if skip_folders:
        items = [item for item in items if item not in skip_folders]

    items.sort()  # Sort items to get consistent ordering
    
    for index, item in enumerate(items):
        # Create full path
        path = os.path.join(startpath, item)

        # Check if it is the last item for correct prefix
        is_last_item = (index == len(items) - 1)
        connector = "└── " if is_last_item else "├── "

        # Write directory or file name to the file only based on the option provided
        if os.path.isdir(path):
            file.write(prefix + connector + item + "/\n")
            # Only recurse into directories if only_folders is not set
            if not only_folders:
                new_prefix = prefix + ("    " if is_last_item else "│   ")
                print_tree(path, new_prefix, last=is_last_item, file=file, skip_folders=skip_folders, only_folders=only_folders, current_depth=current_depth + 1)

        elif not only_folders:  # If not only folders, log files as well
            file.write(prefix + connector + item + "\n")

def main():
    # Get the current working directory (the Django project root directory)
    root_directory = os.getcwd()
    
    # Specify the output file
    output_file = 'django_project_structure.txt'
    
    # Get user inputs for maximum depth, skip folders, and only folders
    max_depth = input("Enter max depth level (or press Enter for no limit): ")
    max_depth = int(max_depth) if max_depth.isdigit() else None

    skip_folders_input = input("Enter comma-separated folder names to skip (or press Enter for none): ")
    skip_folders = [folder.strip() for folder in skip_folders_input.split(',')] if skip_folders_input else []

    only_folders_input = input("Do you want to list only folders? (y/n): ")
    only_folders = only_folders_input.lower() == 'y'

    # Open the output file in write mode with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write the current directory name as a header
        current_folder_name = os.path.basename(root_directory)
        file.write(f"{current_folder_name}/\n")
        
        # Start printing the directory structure
        print_tree(root_directory, file=file, skip_folders=skip_folders, only_folders=only_folders)
    
    print(f"Django project structure saved to {output_file}")

if __name__ == "__main__":
    main()