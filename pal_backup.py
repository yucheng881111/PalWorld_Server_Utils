import shutil
import os
from datetime import datetime
import time
from collections import deque

def copy_and_rename_folder(source_path, destination_path):
    if not os.path.exists(source_path):
        print(f"Error: Cannot find '{source_path}'")
        return

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_folder_name = f"Saved_{current_time}"
    new_folder_path = os.path.join(destination_path, new_folder_name)

    try:
        shutil.copytree(source_path, new_folder_path)
        print(f"Success, Save to '{new_folder_path}'")
    except Exception as e:
        print(f"Error: {e}")
    
    return new_folder_path

if __name__ == "__main__":
    max_folders_to_keep = 20
    deq = deque(maxlen=max_folders_to_keep)
    while True:
        source_folder_path = r"C:\Program Files (x86)\Steam\steamapps\common\PalServer\Pal\Saved"
        destination_path = r"C:\Users\yucheng\Documents\Pal_backup"
        if len(deq) == max_folders_to_keep:
            folder_to_rm = deq[0]
            try:
                shutil.rmtree(folder_to_rm)
                print(f"Success, delete '{folder_to_rm}'")
            except Exception as e:
                print(f"Error: {e}")


        new_folder_path = copy_and_rename_folder(source_folder_path, destination_path)    
        deq.append(new_folder_path) 
        time.sleep(1800)
