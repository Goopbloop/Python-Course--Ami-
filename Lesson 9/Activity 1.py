print("Are you eligable to attend the school exam?")

MedicalReason = input("Is there a medical reason why you cannot attend the exam? Please write true or false")

Attendance = int(input("Please input your attendance level if you do not have a medical reason to skip the exam."))

if MedicalReason == "true":
    print("You are eligable to skip the exam")
else: 
    if Attendance > 75:
        print("You are eligable to take exam")

    else:
        print("You are not eligable to partake in the exam.")
