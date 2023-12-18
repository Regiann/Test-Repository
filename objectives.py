'''
https://www.101computing.net/average-nights-sleep-survey/
'''

carryOn = "y"
totalHours = 0
numberOfStudents = 0

while carryOn == "y":
  hours = int(input("How many hours do you sleep in a night?: "))
  totalHours = totalHours + hours
  numberOfStudents = numberOfStudents + 1
  average = totalHours / numberOfStudents
  print("For", numberOfStudents, "student/s the average is: ", average)
  carryOn = str(input("Would you like to continue adding data?"))

print("Total Students: ", numberOfStudents)
