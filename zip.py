import subprocess
import os

def zip_file(file_to_archive, output_rar):
    winrar = r"C:\Users\Asus\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\WinRAR\WinRAR.lnk"
    if not os.path.exists(winrar):
        print(f"WinRAR executable not found at {winrar}")
        return
    
    command = [winrar, "a", output_rar, file_to_archive]
    subprocess.run(command, check=True)