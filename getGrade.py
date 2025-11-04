
for i in range(3):
    degree = float(input("Enter your degree: "))

    if degree >= 90:
        print("Grade: A")
    elif degree >= 80:
        print("Grade: B")
    elif degree >= 70:
        print("Grade: C")
    elif degree >= 60:
        print("Grade: D")
    else:
        print("Fail")



count = 1

while count <= 3:
    degree = float(input("Enter your degree "))

    if degree >= 90:
        grade = "A"
    elif degree >= 80:
        grade = "B"
    elif degree >= 70:
        grade = "C"
    elif degree >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", {grade})
    count += 1






