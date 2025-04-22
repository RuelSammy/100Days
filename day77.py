#Write a script to automate file renaming.
import os

def rename_files(directory, prefix='', suffix='', new_name=None, start_number=1, extension_filter=None):
    """
    Rename files in a directory with optional prefix, suffix, or completely new name.

    Parameters:
    - directory (str): Path to the target directory.
    - prefix (str): Text to add before the file name.
    - suffix (str): Text to add after the file name (before extension).
    - new_name (str): If given, all files will be renamed to this base name with numbers.
    - start_number (int): Starting number if using new_name.
    - extension_filter (str): Only rename files with this extension (e.g., '.txt').
    """
    files = sorted(os.listdir(directory))
    count = start_number

    for filename in files:
        file_path = os.path.join(directory, filename)

        if not os.path.isfile(file_path):
            continue

        base, ext = os.path.splitext(filename)

        if extension_filter and ext != extension_filter:
            continue

        if new_name:
            new_filename = f"{new_name}_{count}{ext}"
            count += 1
        else:
            new_filename = f"{prefix}{base}{suffix}{ext}"

        new_file_path = os.path.join(directory, new_filename)
        os.rename(file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

# Example usage
rename_files(
    directory="path/to/your/files",
    prefix="IMG_",
    suffix="_2025",
    new_name=None,
    extension_filter=".jpg"
)
