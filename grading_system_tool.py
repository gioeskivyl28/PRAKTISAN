#I'm Gio and this is my grading system trial creation hehe
name = str(input("Enter your name\n--> "))
g1 = float(input("enter your grade in the subject EU1 -->"))
g2 = float(input("enter your grade in the subject ITCS101 -->"))
g3 = float(input("enter your grade in the subject ITCS102 -->"))
g4 = float(input("enter your grade in the subject ITPS101 -->"))
g5 = float(input("enter your grade in the subject MMW -->"))
g6 = float(input("enter your grade in the subject NSTP -->"))
g7 = float(input("enter your grade in the subject PCOM -->"))
g8 = float(input("enter your grade in the subject PE1 -->"))
g9 = float(input("enter your grade in the subject STS -->"))

final_grade = g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 
final_grade = final_grade / 9
print("Your final grade is", final_grade)

result = ""
if final_grade >= 90:
    result = "With honors"
    print("The result of your grade is", result)
elif final_grade >= 80 and final_grade < 90:
    result = "Passed"
    print("The result of your grade is", result)
else:
    result = "Failed"
    print("The result of your grade is", result)
print("Thank you for using our software Mr./ Ms.", name)