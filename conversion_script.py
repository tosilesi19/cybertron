import os
import shutil

# Set the directory path where your .py files are located
dir_path = "/Users/tosilesi/Documents/forConversion"

# Loop through all files in the directory
for file_name in os.listdir(dir_path):
    if file_name.endswith(".py"):
        # Create the new file name with .md extension
        new_file_name = os.path.splitext(file_name)[0] + ".md"
        # Construct the full file paths for the old and new files
        old_file_path = os.path.join(dir_path, file_name)
        new_file_path = os.path.join(dir_path, new_file_name)
        # Rename the file by copying it to the new file name
        shutil.copy(old_file_path, new_file_path)
        # Remove the old file
        os.remove(old_file_path)
