
f = open("Grades.txt", "w")

name = input("What is your name? ")

grade = float(input("Enter your test Grades: "))

test_count = 0
test_sum = 0;

while grade != -1:
	grade = float(input("Enter your test Grades: "))
	test_count = test_sum + 1
	test_sum = test_sum + grade

f.write( name + "\n ================\nAverage: " + str(test_sum/test_count))
