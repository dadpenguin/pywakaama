import os




class scoring_component():
    def __init__(self,folder_path):
        self.folder_path = folder_path

    # public methods
    def get_files(self):
        try:
            # returns all the files in the folder
            files = os.listdir(self.folder_path)
            return files
        except FileNotFoundError:
            os.error(f"The folder {self.folder_path} does not exist.")
        except PermissionError:
            os.error(f"Permission denied to access the folder{self.folder_path}.")





# main routine
def main_routine():
    # Accessing the file
    folder_path = 'wa_res/WakaNats2017'
    files = list_files_in_folder(folder_path)
    

main_routine()