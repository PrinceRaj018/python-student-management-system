students = []

while True:
    print("=" * 40)
    print("\nWELCOME TO THE STUDENT MANAGEMENT PROGRAM\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    print("=" * 40)

    choice = int(input("Enter Your Choice: "))

    if choice == 4:
        break

    elif choice == 1:
        print("\nADD STUDENT")
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        grade = input("Enter grade: ")

        student = {
            "name": name,
            "marks": marks,
            "grade": grade
        }

        students.append(student)
        print("Student Added!")

    elif choice == 2:
        print("\nSTUDENTS LIST")

        for student in students:
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            print("=" * 40)

    elif choice == 3:
        print("\nSEARCH STUDENT")
        search = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"] == search:
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                print("Grade:", student["grade"])
                print("=" * 40)
                found = True

        if not found:
            print("Student Not Found")

    else:
        print("Invalid Choice")
