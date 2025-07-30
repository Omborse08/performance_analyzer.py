from SecondFile import line as l

def gradesystem(y):
    if y > 85.00:
        return ("A")
    elif y > 70.00:
        return ("B")
    elif y > 50.00:
        return ("C")
    else:
        return ("F")

print("Welcome To Student Performance Analyzer")
Students = {}
Grade = set()
while True:
    print("""
\n1. Add Student Data
2. View All Reports
3. Show Subject Toppers
4. Show Failed Students
5. Exit
""")
    choose_option = (input("=> Choose Option: "))
    try:
        match choose_option:
            case "1":
                many = (input("Enter How Many Students Wanted to Add: "))
                try:
                    for s in range(int(many)):
                        student_name = input("\n> Enter Student Name: ")
                        student_marks = input("> Enter Student Marks: ").split(" ")
                        Students1 = {
                            student_name:student_marks
                        }
                        Students.update(Students1)
                        print(">>> Student Info Added Successfully")
                except Exception:
                    print("❌❌❌ Invalid Output! ❌❌❌")

            case "2":
                a = "Students Reports"
                print(a.center(50))
                print(l)
                AVGE = 0
                f = 0
                p = 0
                for list in Students.items():
                    print(f"\nName: {list[0]}")
                    print(f"Marks: {list[1]}")
                    sum = list[1]
                    total = int(sum[0]) + int(sum[1]) + int(sum[2])
                    print(f"Total: {total} ")
                    AVG1 = (total/300) * 100
                    AVGE += AVG1
                    print(f"Average: {AVG1:.2f}%")
                    if AVG1 > 35:
                        print("Passed")
                        p += 1
                    else:
                        print("Failed")
                        f += 1
                    a = gradesystem(AVG1)
                    Grade.update(a)
                    print("Grade:",gradesystem(AVG1))
                    n = 0
                    for j in sum:
                        if int(j) < 35:
                            n += 1
                    if n != 0:
                        print(f"❌ Student Failed in {n} Subjects")
                    else:
                        pass
                print("\n           Class Average: ")
                print(l)
                c_avg = (AVGE/(len(Students)*100)) * 100
                print(f"📌Class Average Marks : {c_avg}")
                print(f"🎓 Unique Grades      : {Grade}")
                print(f"📉 Failed Students    : {f}")
                print(f"📈 Passed Students    : {p}")
                input("\n> Press any key to continue....")
            
            case "3":
                print("\n              Shows Subjects Toppers")
                print(l)
                for subject_index in range(3):
                    top_score = -1
                    topper = ""
                    for student_named, student_mark in Students.items():
                        mark = int(student_mark[subject_index])
                        if mark > top_score:
                            top_score = mark
                            topper = student_named
                    print(f"🏆 Subject {subject_index + 1} Topper: {topper} ({top_score})")
                input("\n> Press any key to continue....")
            
            case "4":
                print("\n              Shows Failed Students")
                print(l)
                fail = 0
                for m,n in Students.items():
                    failed = 0
                    for numbers in n:
                        if int(numbers) < 35:
                            failed += 1
                    if failed > 0:
                        print(f"\nName: {m}")
                        print(f"Marks: {n}")
                        print(f"❌ Failed in {failed} subjects")
                        fail += 1
                print(l)
                print(f"\nTotal Failed Student is {fail}")
                input("> Press any key to continue! ")

            case "5":
                print(l)
                print("Thank You For Using My Code! ")
                break

            case _:
                print("❌❌❌ Invalid Check Again! ❌❌❌")
    except Exception:
        print("❌❌❌ Invalid Result ❌❌❌")



