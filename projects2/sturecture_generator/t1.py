import os

def print_tree(startpath, prefix="", last=True, file=None):
    # List all items in the directory
    items = os.listdir(startpath)
    items.sort()  # Sort items to get consistent ordering
    
    for index, item in enumerate(items):
        # Create full path
        path = os.path.join(startpath, item)
        
        # Check if it is the last item for correct prefix
        is_last_item = (index == len(items) - 1)
        connector = "└── " if is_last_item else "├── "
        
        if os.path.isdir(path):
            # Write the directory name to the file with appropriate connector
            file.write(prefix + connector + item + "/\n")
            # Recursive call for nested directories
            new_prefix = prefix + ("    " if is_last_item else "│   ")
            print_tree(path, new_prefix, last=is_last_item, file=file)
        else:
            # Write the file name to the file with appropriate connector
            file.write(prefix + connector + item + "\n")



if __name__ == "__main__":
    # Get the current working directory (the folder open in VS Code)
    root_directory = os.getcwd()
    
    # Specify the output file
    output_file = 'directory_structure.txt'
    
    # Open the output file in write mode with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        print_tree(root_directory, file=file)
    
    print(f"Directory structure saved to {output_file}")