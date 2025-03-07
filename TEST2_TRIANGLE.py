def right_triangle(height):
    
    if height <=0:
        print("May height bang negative??")
        return
    for i in range(1,height + 1):
        print("*" * i)

choice = input("Do you want to print a right triangle? (Yes or No):")

while True:
    if choice == "Yes":
        right_triangle(10)
        break
    else:
        print("You don't want?? okayy bye!")
        break