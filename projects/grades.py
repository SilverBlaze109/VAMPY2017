
f = open("Grades.txt", "w")

name = input("What is your name? ")

grade = float(input("Enter your test Grades: "))

f.write( name + "\n ================ \nAverage: " + str(grade))
