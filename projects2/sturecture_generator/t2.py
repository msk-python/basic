import os
import sys

def print_tree(startpath, prefix="", last=True, file=None, max_depth=None, current_depth=0, include_hidden=False):
    # List all items in the directory
    items = os.listdir(startpath)
    
    # If we want to exclude hidden files, filter them out
    if not include_hidden:
        items = [item for item in items if not item.startswith('.')]

    items.sort()  # Sort items to get consistent ordering
    
    for index, item in enumerate(items):
        # Create full path
        path = os.path.join(startpath, item)
        
        # Check if it is the last item for correct prefix
        is_last_item = (index == len(items) - 1)
        connector = "└── " if is_last_item else "├── "

        # Write directory or file name to the file
        file.write(prefix + connector + item + (
            "/" if os.path.isdir(path) else "") + "\n")

        # Only recurse into directories if we haven't reached the maximum depth
        if os.path.isdir(path) and (max_depth is None or current_depth < max_depth):
            new_prefix = prefix + ("    " if is_last_item else "│   ")
            print_tree(path, new_prefix, last=is_last_item, file=file, max_depth=max_depth, current_depth=current_depth + 1, include_hidden=include_hidden)


def main():
    # Get the current working directory (the folder open in VS Code)
    root_directory = os.getcwd()
    
    # Specify the output file
    output_file = 'directory_structure.txt'
    
    # Get user inputs
    max_depth = input("Enter max depth level (or press Enter for no limit): ")
    max_depth = int(max_depth) if max_depth.isdigit() else None
    
    include_hidden = input("Include hidden files? (y/n): ").lower() == 'y'

    # Open the output file in write mode with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        print_tree(root_directory, file=file, max_depth=max_depth, include_hidden=include_hidden)
    
    print(f"Directory structure saved to {output_file}")

if __name__ == "__main__":
    main()