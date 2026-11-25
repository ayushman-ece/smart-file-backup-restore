
import os
import zipfile
from datetime import datetime
from pathlib import Path


BACKUP_DIR = Path("backups")


def create_backup(source_path):
    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError("Source path does not exist.")

    BACKUP_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = BACKUP_DIR / backup_name

    with zipfile.ZipFile(backup_path, "w",
                         zipfile.ZIP_DEFLATED) as zip_file:

        if source.is_file():
            zip_file.write(source, arcname=source.name)

        else:
            for file_path in source.rglob("*"):
                if file_path.is_file():
                    arcname = file_path.relative_to(source)
                    zip_file.write(file_path, arcname=arcname)

    return backup_path


def list_backups():
    BACKUP_DIR.mkdir(exist_ok=True)

    backups = list(BACKUP_DIR.glob("*.zip"))
    backups.sort(reverse=True)

    return backups


def restore_backup(backup_path, destination):
    backup = Path(backup_path)
    destination = Path(destination)

    if not backup.exists():
        raise FileNotFoundError("Backup file not found.")

    destination.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(backup, "r") as zip_file:

        # Security check against path traversal
        for member in zip_file.namelist():
            target = (destination / member).resolve()

            if not target.is_relative_to(destination.resolve()):
                raise ValueError("Unsafe file path detected in backup.")

        zip_file.extractall(destination)

    return destination
