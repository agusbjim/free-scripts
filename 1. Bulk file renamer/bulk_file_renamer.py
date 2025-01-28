## 1. Bulk File Renamer
### Code:
```python
import os

def bulk_rename(directory, new_name):
    try:
        files = os.listdir(directory)
        for i, file in enumerate(files):
            extension = os.path.splitext(file)[1]
            new_full_name = f"{new_name}_{i+1}{extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_full_name))
        print("Files renamed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Usage
# bulk_rename("directory_path", "new_name")
```