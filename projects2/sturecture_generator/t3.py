import os

def print_tree(startpath, prefix="", last=True, file=None, max_depth=None, current_depth=0):
    # List all items in the directory
    items = os.listdir(startpath)

    # Exclude hidden files and folders
    items = [item for item in items if not item.startswith('.')]
    
    items.sort()  # Sort items to get consistent ordering
    
    for index, item in enumerate(items):
        # Create full path
        path = os.path.join(startpath, item)

        # Check if it is the last item for correct prefix
        is_last_item = (index == len(items) - 1)
        connector = "└── " if is_last_item else "├── "

        # Write directory or file name to the file
        if os.path.isdir(path):
            file.write(prefix + connector + item + "/\n")
        else:
            file.write(prefix + connector + item + "\n")

        # Only recurse into directories if we haven't reached the maximum depth
        if os.path.isdir(path) and (max_depth is None or current_depth < max_depth):
            new_prefix = prefix + ("    " if is_last_item else "│   ")
            print_tree(path, new_prefix, last=is_last_item, file=file, max_depth=max_depth, current_depth=current_depth + 1)


def main():
    # Get the current working directory (the Django project root directory)
    root_directory = os.getcwd()
    
    # Specify the output file
    output_file = 'django_project_structure.txt'
    
    # Get user inputs for maximum depth
    max_depth = input("Enter max depth level (or press Enter for no limit): ")
    max_depth = int(max_depth) if max_depth.isdigit() else None

    # Open the output file in write mode with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Directory structure for Django project at: {root_directory}\n\n")
        # Write the current directory name as a header
        current_folder_name = os.path.basename(root_directory)
        file.write(f"{current_folder_name}/\n")

        # Start printing the directory structure
        print_tree(root_directory, file=file, max_depth=max_depth)
    
    print(f"Django project structure saved to {output_file}")

if __name__ == "__main__":
    main()