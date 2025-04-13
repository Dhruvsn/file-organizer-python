import os
import shutil

def organize_files(directory):
    # Ensure the given directory exists
    if not os.path.isdir(directory):
        print(f"⚠️ The directory '{directory}' doesn't exist!")
        return

    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Only proceed if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Get the file extension (without the dot)
            file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'

            # Create a folder for the extension if it doesn't exist
            folder_name = os.path.join(directory, file_extension)
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"✔️ Created folder: {folder_name}")

            # Move the file into the corresponding folder
            shutil.move(file_path, os.path.join(folder_name, filename))
            print(f"✔️ Moved '{filename}' to '{folder_name}'")

# Use this function to organize files in your directory
directory = input("Enter the path of the directory you want to organize: ")
organize_files(directory)
