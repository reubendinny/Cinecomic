import shutil
import os

def copy_and_rename_file(source_file, destination_folder, new_file_name):

    destination_path = os.path.join(destination_folder, new_file_name)

    try:
        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            os.remove(destination_path)  # Remove the existing file
            
        # Copy the file from source to destination
        shutil.copy(source_file, destination_path)
        os.rename(destination_path, os.path.join(destination_folder, new_file_name))

        
        print(f"File '{source_file}' copied and renamed to '{new_file_name}' in '{destination_folder}'.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")



