payPerHr = input("Enter your hourly pay rate: ")
hoursWorked = input("Enter the number of hours you work on one day: ")

if not isinstance(payPerHr, int):
    print("Your pay rate must be a number")
    exit()

if not isinstance(hoursWorked, int):
    print("Your work hours must be a number")
    exit()

payPerHr = int(payPerHr)
hoursWorked = int(hoursWorked)


if payPerHr < 0:
    print("You can't have a negative pay rate!")
    exit()

if hoursWorked < 0:
    print("You can't work negative hours!")
    exit()

salaryPerDay = payPerHr * hoursWorked
salaryPerWeek = salaryPerDay * 5
salaryPerMonth = salaryPerWeek * 4
salaryPerYear = salaryPerMonth * 12

print("Your salary per day is: " + str(salaryPerDay) + '€')
print("Your salary per week is: " + str(salaryPerWeek) + '€')
print("Your salary per month is: " + str(salaryPerMonth) + '€')
print("Your salary per year is: " + str(salaryPerYear) + '€')

input("Press enter to exit")