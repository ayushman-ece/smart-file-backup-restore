# 💾 Smart File Backup & Restore System

## 📌 Project Overview

The **Smart File Backup & Restore System** is a Python command-line application that creates compressed backups of files and folders and allows users to restore them later.

The application uses Python's built-in `zipfile` module to create timestamped ZIP backups, manage backup files, and restore data to a selected destination.

## 🎯 Objectives

- Create backups of files and folders.
- Store backups in a dedicated directory.
- Generate timestamped backup files.
- List available backups.
- Restore backups to a chosen destination.
- Validate paths and handle errors.

## ⚙️ Features

- **File Backup:** Back up individual files.
- **Folder Backup:** Back up files from folders and subfolders.
- **ZIP Compression:** Store backups in compressed ZIP format.
- **Timestamped Backups:** Prevent backup filenames from being reused.
- **Backup Listing:** View available backup archives.
- **Restore Functionality:** Restore files from selected backups.
- **Path Validation:** Validate source paths and backup files.
- **Basic Security Validation:** Detect unsafe paths inside backup archives.
- **Error Handling:** Handle invalid paths, selections, and corrupted archives.

## 🧠 Workflow

1. Select an operation from the menu.
2. Provide a source file or folder path.
3. Create a timestamped ZIP archive.
4. Store the archive in the backups directory.
5. List available backup archives.
6. Select a backup for restoration.
7. Specify the restoration destination.
8. Extract the selected backup after validation.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pathlib | Path management |
| zipfile | ZIP creation and extraction |
| datetime | Timestamp generation |
| os | File system operations |

## 📊 Backup Information

Backups are stored inside the `backups/` directory.

Each backup filename contains a timestamp:

```text
backup_YYYYMMDD_HHMMSS.zip
```

## 🔍 Technical Concepts

### 1. File Handling

Uses `pathlib` to manage file and directory paths.

### 2. ZIP Compression

Uses `zipfile.ZipFile` with ZIP compression to create backup archives.

### 3. Recursive File Processing

Uses `Path.rglob()` to find files inside nested folders.

### 4. Timestamped Naming

Uses `datetime` to generate unique timestamp-based backup names.

### 5. Restore Operations

Extracts archived files into a selected destination directory.

### 6. Path Validation

Checks archive paths before extraction to reduce path traversal risks.

## 📁 Project Structure

```text
smart-file-backup-restore/
│
├── main.py
├── backup_manager.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── backups/             # Generated backup archives
```

## 🚀 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/smart-file-backup-restore.git
```

### 2. Navigate into the project

```bash
cd smart-file-backup-restore
```

### 3. Install dependencies

This project uses Python's standard library. No external dependencies are required.

### 4. Run the application

```bash
python main.py
```

## 📚 Key Concepts Learned

- File and directory management
- Python pathlib
- Recursive file traversal
- ZIP compression
- File restoration
- Exception handling
- Path validation
- Timestamp generation
- Modular programming

## ⚠️ Limitations

- Backups are stored locally.
- There is no scheduled automatic backup.
- The application does not support cloud storage.
- It does not currently provide backup encryption.
- Restoring files may overwrite files with the same names.
- Backups are not incremental.

## 🔮 Future Improvements

- Add scheduled automatic backups.
- Implement incremental backups.
- Add backup encryption.
- Support cloud storage.
- Add backup verification.
- Provide a graphical interface.
- Add backup retention policies.
- Add file integrity checking using hashes.

## 👨‍💻 Author

**Ayushman Tiwari**

B.Tech – Electronics and Communication Engineering

GitHub: https://github.com/ayushman-ece

---

⭐ If you find this project useful, consider giving it a star!