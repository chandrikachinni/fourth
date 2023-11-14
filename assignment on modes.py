# f=open("student.txt","w")
# while True:
#     name=input("Enter the name:")
#     roll_no=input("Enter the roll no:")
#     marks=input("Enter the marks:")
#     f.write("{}\t{}\t{}\n".format(name,roll no,marks))
#     another = input("Add another student (yes/no): ")
#     if another.lower()!= "yes":
#         break

# f = open("student.txt", "r")
# for line in f:
#     name,roll no,marks = line.strip().split('\t')
#     print("Name: {}, Roll Number: {}, Marks: {}".format(name, roll no, marks))
# f.close()

########################################################

# f = open("chandu.txt", 'w')
# n = 5
# for i in range(n):
#     grades = input(f"Enter grades for student {i + 1}: ")
#     f.write(grades + '\n')
# f.close() 

# f = open("chandu.txt", 'r')
# lines = f.readlines()
# f.close()

# print("Total number of students:", len(lines))

# for i, line in enumerate(lines):
#     grades = line.split()
#     print("Student number:", i + 1)
#     print("Grades:", grades)
#     total_marks = sum(map(int, grades))
#     percentage = (total_marks /(len(grades)  *100))  *100
#     print("Total marks:", total_marks)
#     print("Percentage:", percentage)
#     print()










