from os import listdir, path, makedirs, rename, environ, path, name
import getpass
from time import sleep
from rich.progress import track
from rich import print

# Get directory to organize (windows-nt, mac-posix)
if name == 'nt':
    get_dir = input("Enter your folder path: ")
    directory = path.join(environ['USERPROFILE'], get_dir)
else:
    get_dir = input("Enter your folder path: ")
    directory = path.join(environ['HOME'], get_dir)

# All possible type Extentions
extentions = {
    "Adobe": ['.psd', '.bmp', '.psb', '.ct', '.tiff', '.tif', '.eps', '.svg', '.ai', '.webp'],
    "Applications": ['.exe'],
    "Archives": ['.zip', '.rar', '.7zip', '.tar', '.iso', '.tar.gz', 'bz2'],
    "Code": ['.py', '.java', '.c', '.cpp', '.rb', '.asm', '.php', '.html', '.css', '.js', '.lua', '.jar', '.o', '.obj', '.r', '.go', '.ts', 'sh', '.bat'],
    "Documents": ['.docx', '.doc', '.pdf', '.txt', '.ppt', '.pptx', '.ppsx', '.pptm',
                  '.docm', '.dotx', '.dotm', '.docb', '.xlsx', '.xlsm', '.xltx',
                  '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw',
                  '.ACCDB', '.ACCDE', '.ACCDT', '.ACCDR', '.pub',
                  '.potx', '.potm', '.ppam', '.ppsm', '.sldx', '.sldm', '.ext', '.epub'],
    "Music": ['.mp3', '.ogg', '.wav'],
    "Pictures": ['.jpg', '.jpeg', '.png', '.bmp', '.gif'],
    "Raws": ['.CR2'],
    "Videos": ['.mp4', '.3gp', '.avi', '.mov', '.mkv', '.wmv', '.flv']
}

# If you have no '/' in the end
if not directory.endswith('/'):
    directory += '/'

# progress bar
process_step = track(range(len(listdir(directory))),
                     description="Processing...")

# Check each file in the directory
for step, fil in zip(process_step, listdir(directory)):
    for typ, lis in extentions.items():
        for ex in lis:
            if fil.endswith(ex) or fil.endswith(ex.upper()):
                if not path.exists(directory+typ+'/'):
                    makedirs(directory+typ+'/')
                rename(directory+fil, directory+typ+'/'+fil)
print("Process [bold magenta]done![/bold magenta]")
