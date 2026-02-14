def calculate_grade(avg):
    if avg >= 90:
        return "A \n Excellent"
    elif avg >= 75: 
        return "B \n Very Good"
    elif avg >= 60:
        return "C \n Good"
    elif avg >= 40:
        return "D \n Pass"
    else:
        return "F \n Fail"

marks = []
subjects =  int(input("enter the number of subjects: "))

for i in range(subjects):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)
    total = sum(marks)
average = total / subjects
grade = calculate_grade(average)
print("Marks entered:", marks)
print("Total : ",total)
print("Average: ",average)
print("Grade: ",grade)
