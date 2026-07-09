import os
import shutil

# File type classification rules
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.webm'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Code': ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css', '.json', '.xml'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
}

SCRIPT_NAME = os.path.basename(__file__)

# Get all files in current directory
files = os.listdir('.')

# Count the number of moved files
moved_count = 0

for file in files:
    # Skip directories
    if os.path.isdir(file):
        continue

    if file == SCRIPT_NAME:
        continue

    # Get file extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()

    # Find the category
    category = 'Others'
    for cat, exts in FILE_TYPES.items():
        if ext in exts:
            category = cat
            break

    # Create category folder if it doesn't exist
    if not os.path.exists(category):
        os.makedirs(category)
        print(f'Created folder: {category}')

    # Then move the file
    try:
        shutil.move(file, os.path.join(category, file))
        print(f'✅ {file} → {category}')
        moved_count += 1
    except Exception as e:
        print(f'❌ Failed to move {file}: {e}')

print(f'Moved {moved_count} files.')