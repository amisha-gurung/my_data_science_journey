sc = input("Enter your score: ")
score = int(sc)

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Great job!")
elif score >= 70:
    print("C - Good work!")
elif score >= 60:
    print("D - You passed")
else:  
    print("F - Need improvement")