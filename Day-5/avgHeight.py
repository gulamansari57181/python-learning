
students_height = input("Please enter list of students height :").split(" ")
print(students_height)

sum_height=0
for i in range(0,len(students_height)):
    students_height[i] = int(students_height[i])
    sum_height += students_height[i]
    
    
print(f"Sum of Students Height is : {sum_height}")
print(f"Average Height of Students is : {(sum_height/len(students_height)):0.2f} ")