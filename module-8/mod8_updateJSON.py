# Garvin Stewart
# CSD-325 | Module 8 Assignment
# 5/4/2026

"""
Program: Load a student JSON file, print the original list, append a new
         student record, print the updated list, then dump the updated data
         back to the JSON file.
"""

import json

# ── Constants ────────────────────────────────────────────────────────────────
JSON_FILE = "student.json"


# ── Helper Functions ─────────────────────────────────────────────────────────

def print_students(student_list):
    """
    Loop through the class list and print each student's information
    in the format: Last, First : ID = ###### , Email = address
    """
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} "
              f": ID = {student['Student_ID']} "
              f", Email = {student['Email']}")


# ── Main Program ─────────────────────────────────────────────────────────────

def main():
    # Step 1: Load the JSON file into a Python list using json.load()
    with open(JSON_FILE, "r") as file:
        class_list = json.load(file)

    # Step 2: Print the original student list
    print("=" * 60)
    print("  Original Student List")
    print("=" * 60)
    print_students(class_list)

    # Step 3: Append your own record to the list
    new_student = {
        "F_Name": "Garvin",
        "L_Name": "Stewart",
        "Student_ID": 99001,           # Fictional student ID
        "Email": "gstewart@gmail.com"
    }
    class_list.append(new_student)

    # Step 4: Print the updated student list
    print()
    print("=" * 60)
    print("  Updated Student List")
    print("=" * 60)
    print_students(class_list)

    # Step 5: Dump the updated list back to the JSON file using json.dump()
    # 'w' mode overwrites the file with the full updated list (which now
    # includes the appended record).  indent=4 keeps the file human-readable.
    with open(JSON_FILE, "w") as file:
        json.dump(class_list, file, indent=4)

    # Step 6: Notify the user that the file has been updated
    print()
    print("=" * 60)
    print(f"  {JSON_FILE} has been updated successfully.")
    print("=" * 60)


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
