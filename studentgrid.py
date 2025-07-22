"""need to gt 5 names from user and 3 subject marks for 1 student and display their marks in percentage format"""
marks = []
for i in range(2):
    mark = []
    mark.append(input("Enter the name: "))
    mark.append(int(input("Enter mark 1: ")))
    mark.append(int(input("Enter mark 2: ")))
    mark.append(int(input("Enter mark 3: ")))
    marks.append(mark)

print("\nStudent Data:")
print(marks)

print("\nResult:")
for i in range(len(marks)):
    student_data = marks[i]
    name = student_data[0]
    total_marks_obtained = student_data[1] + student_data[2] + student_data[3]
    percentage = (total_marks_obtained / 300) * 100
    print(str(i + 1) + ". " + name + ": " + str(int(percentage)) + "%")
  

 