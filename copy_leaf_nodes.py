import os
import shutil


def is_leaf_directory(path):
    return os.path.isdir(path) and not any(os.path.isdir(os.path.join(path, item)) for item in os.listdir(path))

def copy_leaf_directories(source_root, destination_root):
    for root, dirs, files in os.walk(source_root, topdown=True):
        # Exclude .git folder from the walk
        dirs[:] = [d for d in dirs if d != '.git']

        if is_leaf_directory(root):
            leaf_dir_name = os.path.basename(root)
            destination_path = os.path.join(destination_root, leaf_dir_name)

            # If a directory with the same name already exists in the destination,
            # append a number to make it unique
            counter = 1
            while os.path.exists(destination_path):
                destination_path = os.path.join(destination_root, f"{leaf_dir_name}_{counter}")
                counter += 1

            shutil.copytree(root, destination_path)
            print(f"Copied: {leaf_dir_name} to {destination_path}")

# Set the source and destination directories
source_directory = "./"
destination_directory = "leaf_nodes"

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Copy the leaf directories
copy_leaf_directories(source_directory, destination_directory)

print("Leaf directory copying completed.")
