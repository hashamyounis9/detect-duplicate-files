import os

def exist_in_sizes(sizes : dict):
    keys = sizes.keys
        


file_and_dirs = os.listdir()
sizes = []

for file in file_and_dirs:
    if os.path.isfile(file):
        
        file_path = os.path.join(os.getcwd(), file)
        file_name = file_path[file_path.rfind('/')+1:]
        if os.path.getsize(file_path) in sizes:

            target_directory = os.path.join(os.getcwd(), "Possible Duplicates")
            if os.path.exists(target_directory):
                new_path = os.path.join(target_directory, os.path.basename(file_path))
                os.rename(file_path, new_path)
            else:
                os.mkdir("Possible Duplicates")
                new_path = os.path.join("Possible Duplicates", os.path.basename(file_path))
                os.rename(file_path, new_path)
        else:
            sizes.append(os.path.getsize(file_path))