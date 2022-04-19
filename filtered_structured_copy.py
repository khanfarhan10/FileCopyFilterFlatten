import os, fnmatch, shutil

PATTERN = '*.txt' # Regex Pattern to Match files
INPUT_FOLDER = "A" # os.getcwd()
INPUT_FOLDER = os.path.abspath(INPUT_FOLDER)
include_input_foldername = False
prepend = "_included" if include_input_foldername else ""
OUTPUT_FOLDER = f"Structured_Copy_{os.path.basename(INPUT_FOLDER)}{prepend}"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def find(pattern, path):
    """Utility to find files wrt a regex search"""
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

all_files = find(PATTERN, INPUT_FOLDER)

for each_path in all_files:
    relative_path = os.path.relpath(each_path, os.path.dirname(INPUT_FOLDER)) if include_input_foldername else os.path.relpath(each_path, INPUT_FOLDER) 
    flattened_relative_fullpath = os.path.join(OUTPUT_FOLDER, relative_path)
    os.makedirs(os.path.dirname(flattened_relative_fullpath), exist_ok=True)
    shutil.copy(each_path, flattened_relative_fullpath)
    print(f"Copied {each_path} to {flattened_relative_fullpath}")
    
print(f"Finished Copying {len(all_files)} Files from : {INPUT_FOLDER} to : {OUTPUT_FOLDER}")