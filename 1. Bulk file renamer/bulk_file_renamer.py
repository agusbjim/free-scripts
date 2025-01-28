import os

def bulk_rename(directory, new_name):
    """
    Renames all files in the specified directory to follow a new naming pattern.
    
    Parameters:
        directory (str): Path to the folder containing files to rename.
        new_name (str): Base name for renamed files.
    """
    try:
        files = os.listdir(directory)
        for i, file in enumerate(files):
            extension = os.path.splitext(file)[1]
            new_file_name = f"{new_name}_{i+1}{extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
        print("Files renamed successfully.")
    except Exception as e:
        print(f"Error: {e}")
