print("1 = Red")
print("2 = Yellow")
print("3 = Green")
print("4 = Pedestrian Crossing")
print("5 = Emergency Vehicle")

choice = int(input("Enter number: "))

if choice == 1:
    print("STOP - Vehicles must stop")
elif choice == 2:
    print("WAIT - Get ready")
elif choice == 3:
    print("GO - Vehicles can move")
elif choice == 4:
    print("Pedestrian Crossing - Let people walk")
elif choice == 5:
    print("Emergency Mode - Give way immediately")
else:
    print("Wrong choice")

print("END OF THIS PROGRAM")
