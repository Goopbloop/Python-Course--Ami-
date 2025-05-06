Amount = int(input("Please enter the ammount you would like to withdraw :"))

note_1 = Amount // 100
note_2 = (Amount % 100) // 50
note_3 = ((Amount % 100) % 50) // 10

print("The number of 100 BDT notes needed : ", note_1)
print("The number of 50 BDT notes needed : ", note_2)
print("The number of 10 BDT notes needed : ", note_3)
