import os
import shutil
import string

def move_files():
    folder = "Alphabet_Files"
    if not os.path.exists(folder):
        os.makedirs(folder)

    for letter in string.ascii_uppercase: 
        file_name = f"{letter}.txt"
        if os.path.exists(file_name):
            shutil.move(file_name, os.path.join(folder, file_name))

    print(f"All files moved to '{folder}'.")

move_files()