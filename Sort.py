import os
import shutil

DRY_RUN = True  # True = Preview only | False = Move files

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

print('=' * 50)
if DRY_RUN:
    print('🔍 DRY RUN MODE - No files will be moved')
    print('   (Change DRY_RUN to False to actually move files)')
else:
    print('📦 SORT MODE - Files WILL be moved')
print('=' * 50)
print()

# Get all files in current directory
files = os.listdir('.')

# Count the number of moved files
moved_count = 0
skipped_count = 0

for file in files:
    # Skip directories
    if os.path.isdir(file):
        skipped_count += 1
        continue

    if file == SCRIPT_NAME:
        print(f'⏭️  Skipping self: {file}')
        skipped_count += 1
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

    target_path = os.path.join(category, file)

    if DRY_RUN:
        # Preview only
        print(f'🔍 Would move: {file} → {category}/')
    else:
        # Real move
        # Create folder if not exist
        if not os.path.exists(category):
            os.makedirs(category)
            print(f'📁 Created folder: {category}')

        # Move the file
        try:
            shutil.move(file, target_path)
            print(f'✅ {file} → {category}/')
            moved_count += 1
        except Exception as e:
            print(f'❌ Failed to move {file}: {e}')

    # Final Outcomes
    print()
    print('=' * 50)
    if DRY_RUN:
        print('🔍 DRY RUN COMPLETE - No files were moved')
        print('   Set DRY_RUN = False to move files')
    else:
        print(f'✅ DONE! Moved {moved_count} files')
    print(f'   📁 {moved_count} files moved')
    print(f'   ⏭️ {skipped_count} items skipped')
    print('=' * 50)