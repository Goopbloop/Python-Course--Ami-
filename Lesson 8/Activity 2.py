print("Enter a Number(Numerator):")
numN = int(input())
print("Enter a Number(Demionator):")
numD = int(input())

if numN % numD == 0:
    print(str(numN) + " is divisible by " + str(numD))
else: 
    print(str(numN) + " is not divisible by " + str(numD))
