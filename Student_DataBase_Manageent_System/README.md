🎓 Student Database Management System (Python)

A simple menu-driven Student Database Management System built using Python and JSON for data storage. This project helps beginners understand file handling, JSON operations, functions, and basic CRUD operations in Python.

📌 Features

➕ Add student details (ID, Name, Age, Course, Marks)

📋 Display all student records

🔍 Search student by ID

✏️ Update student details

❌ Delete student by ID

💾 Save & load data using a JSON file

🧭 Menu-based user interaction

🛠️ Technologies Used

Python 3

JSON (for data storage)

📂 Project Structure
Student_DataBase_Management_System/
│
├── student.py        # Main Python program
├── student.json      # Stores student data (auto-created)
└── README.md         # Project documentation

▶️ How to Run the Project

Clone the repository or download the source code

Make sure Python 3 is installed

Open a terminal in the project folder

Run the program:

python student.py

📖 Menu Options
==== StudentDB Menu ====
1. Add Students
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Save & Exit

🧪 Sample Output
Enter Student ID : 101
Enter Student Name : Alice
Enter Student Age : 20
Enter Student Course : CSE
Enter Student Marks : 85
Student Added Successfully

💾 Data Storage Format (student.json)
[
    {
        "id": "101",
        "name": "Alice",
        "age": "20",
        "course": "CSE",
        "marks": "85"
    }
]

🚀 Future Improvements

Input validation (age & marks as numbers)

Prevent duplicate student IDs

Better UI formatting

Convert to OOP (class-based approach)

Add sorting and filtering options

👨‍💻 Author

Jahid
BTech CSE (AI) | Python Developer
Beginner-friendly mini project 🚀
