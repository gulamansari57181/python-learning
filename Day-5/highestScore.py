students_score = input("Please enter list of students score :").split(" ")
print(students_score)

highest_score = -1
for i in range(0,len(students_score)):
    students_score[i] = int(students_score[i])
    if students_score[i] >highest_score:
        highest_score=students_score[i]
        
        
print(f"Highest Score of the student is : {highest_score}")