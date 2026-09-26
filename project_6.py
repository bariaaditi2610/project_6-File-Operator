import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def create_file(self):
        try:
            with open(self.filename, "x") as file:
                pass
        except FileExistsError:
            pass
        except PermissionError:
            print("Error: Permission denied.")


    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")

            if entry.strip() == "":
                print("Entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write("[" + timestamp + "]\n")
                file.write(entry + "\n")
                file.write("\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied.")


    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            if data.strip() == "":
                print("No journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("")
                print(data)

        except FileNotFoundError:
            print("Error: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied.")


    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                lines = file.readlines()

            found = False
            current_entry = []

            print("\nMatching Entries:")
            print("")

            for line in lines:

                if line.startswith("["):
                    current_entry = [line]

                elif line.startswith("-"):
                    current_entry.append(line)

                    complete_entry = "".join(current_entry)

                    if keyword.lower() in complete_entry.lower():
                        print(complete_entry)
                        found = True

                    current_entry = []

                else:
                    current_entry.append(line)

            if not found:
                print("No entries were found for the keyword:", keyword)

        except FileNotFoundError:
            print("Error: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied.")


    def delete_all_entries(self):
        try:

            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return

            confirmation = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if confirmation.lower() == "yes":

                with open(self.filename, "w") as file:
                    file.write("")

                os.remove(self.filename)

                print("All journal entries have been deleted.")

            else:
                print("Deletion cancelled.")

        except FileNotFoundError:
            print("No journal entries to delete.")

        except PermissionError:
            print("Error: Permission denied.")


    def menu(self):

        while True:

            print("\n ")
            print("      PERSONAL JOURNAL MANAGER")
            print("")

            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            print("")

            choice = input("Please select an option: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_all_entries()

            elif choice == "5":
                print("Thank you for using Personal Journal Manager.")
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please select a valid option.")


journal = JournalManager()

journal.create_file()

journal.menu()