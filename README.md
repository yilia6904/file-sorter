# 🍐📂 File Sorter

Automatically organize messy folders by sorting files into categorized directories.
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

# ✨ Features
- 📁 Automatically sorts files into categories: Images, Documents, Archives, Videos, Music, Code, Installers
- 🔍 **Dry run mode** – preview before you actually move files
- 🛡️ Skip script itself 
- 📊 Shows summary of moved files
- 🎨 Colorful emoji output for easy reading
- 🐍 Pure Python – no external dependencies

## 🚀 Quick Start
### Prerequisites
- Python 3.6 or higher
### Clone & Run
This project uses only Python standard libraries (os, shutil).
No external dependencies required.

```bash
git clone https://github.com/yilia6904/file-sorter.git
cd file-sorter
```
# 📚Usage
## 1. Preview Mode (Dry Run for Default)
The script runs in preview mode by default. It shows what would be moved without actually moving anything.
```bash
python Sort.py
```
### Example Output:
```bash
==================================================
🔍 DRY RUN MODE - No files will be moved
   (Change DRY_RUN to False to actually move files)
==================================================

⏭️  Skipping self: sort.py
🔍 Would move: report.pdf → Documents/
🔍 Would move: photo.jpg → Images/

==================================================
🔍 DRY RUN COMPLETE - No files were moved
   Set DRY_RUN = False to move files
   📁 0 files moved
   ⏭️ 4 items skipped
==================================================
```
## 2. Run for Real
Open `Sort.py` and change:
```bash
DRY_RUN = True  # True = Preview only | False = Move files
```
Then run again:
```bash
python Sort.py
```
### Example Output:
```bash
==================================================
📦 SORT MODE - Files will be moved
==================================================

📁 Created folder: Documents
✅ report.pdf → Documents/
✅ photo.jpg → Images/

==================================================
✅ DONE! Moved 2 files
   📁 2 files moved
   ⏭️ 4 items skipped
==================================================
```

## 📂 Supported File Types

| Category | Extensions |
| :------- | :--------- |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg` |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.md` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2` |
| **Videos** | `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.webm` |
| **Music** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg` |
| **Code** | `.py`, `.java`, `.c`, `.cpp`, `.js`, `.html`, `.css`, `.json`, `.xml` |
| **Installers** | `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm` |
| **Others** | Anything not listed above |

--> You can easily customize the `FILE_TYPES` dictionary in `sort.py`.

# 🤝 Contributing
Issues and Pull Requests are welcome!

# 📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

# 👤 Author
Yilia Sun
GitHub: @yilia6904

