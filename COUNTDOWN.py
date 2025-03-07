import time
choice = input("Do you want to print a countdown?(Yes or No):")

while True:
    if choice== "Yes":
        for i in range(10,0,-1):
            time.sleep(0.5)
            print(i)
            time.sleep(0.5)
        print("Happy New Year!")
        break
    else:
        print("Maybe next time!")
        break