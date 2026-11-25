
from backup_manager import (
    create_backup,
    list_backups,
    restore_backup
)


def main():
    while True:
        print("\n===== SMART BACKUP & RESTORE =====")
        print("1. Create Backup")
        print("2. List Backups")
        print("3. Restore Backup")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                source = input("Enter file/folder path: ").strip()

                backup_path = create_backup(source)

                print("\nBackup created successfully!")
                print("Backup Location:", backup_path)

            elif choice == "2":
                backups = list_backups()

                if not backups:
                    print("No backups found.")
                else:
                    print("\nAvailable Backups:")
                    for index, backup in enumerate(backups, start=1):
                        print(f"{index}. {backup}")

            elif choice == "3":
                backups = list_backups()

                if not backups:
                    print("No backups available.")
                    continue

                print("\nAvailable Backups:")
                for index, backup in enumerate(backups, start=1):
                    print(f"{index}. {backup}")

                try:
                    number = int(input("Select backup number: "))

                    if number < 1 or number > len(backups):
                        print("Invalid backup selection.")
                        continue

                    selected_backup = backups[number - 1]

                    destination = input(
                        "Enter restore destination folder: "
                    ).strip()

                    result = restore_backup(
                        selected_backup,
                        destination
                    )

                    print("\nRestore completed successfully!")
                    print("Restored to:", result)

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                print("Exiting Backup System.")
                break

            else:
                print("Invalid choice.")

        except (OSError, ValueError, zipfile.BadZipFile) as error:
            print("\nError:", error)


if __name__ == "__main__":
    import zipfile
    main()
