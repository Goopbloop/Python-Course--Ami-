print("Input your marks for 5 subjects!")
MarkOne = int(input())
MarkTwo = int(input())
MarkThree = int(input())
MarkFour = int(input())
MarkFive = int(input())

tot = MarkOne + MarkTwo + MarkThree + MarkFour + MarkFive
avg = tot / 5 

if avg >= 80 and avg <= 100:
    print("Your grade is A!")
elif avg >= 65 and avg <= 79:
    print("Your grade is B!")
elif avg >= 50 and avg <= 64:
    print("Your grade is a C-!")
else :
    print("Your grade is F! You failed!")