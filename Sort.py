import os

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.webm'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Code': ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css', '.json', '.xml'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg'],
}

files = os.listdir('.')
# current directory

for file in files:
    if os.path.isdir(file):
        continue
    # if the file is a directory, then check the next file

    _, ext = os.path.splitext(file)
    ext = ext.lower()

    category = 'Others'
    for cat, exts in FILE_TYPES.items():
        if ext in exts:
            category = cat
            break

    print(f'{file} → {category}')