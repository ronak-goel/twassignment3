def grossSalary(grade):
    if(grade == "A"):
        gross = (1+0.20+0.50-0.11)*10000 + 1700
    elif(grade == "B"):
        gross = (1+0.20+0.50-0.11)*4567 + 1500
    return gross

grade = input("Enter grade(A or B): ")
grossS = grossSalary(grade)
print("Gross Salary is: ",grossS)