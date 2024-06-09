import os

def list_files_in_folder(folder_path):
    try:
        # returns all the files in the folder
        files = os.listdir(folder_path)
        return files
    except FileNotFoundError:
        return f"The folder {folder_path} does not exist."
    except PermissionError:
        return f"Permission denied to access the folder {folder_path}."





# main routine
def main_routine():
    # Accessing the file
    folder_path = 'wa_res/WakaNats2017'
    files = list_files_in_folder(folder_path)
    print(files)

main_routine()