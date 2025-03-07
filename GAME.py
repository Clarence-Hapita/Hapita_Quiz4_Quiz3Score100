name = input("Enter your character's name:")
print(f"Welcome, {name}! Do you want to play a mini adventure? (Yes or No)")
    
play = input(">")
if play == "Yes":
        print("Welcome to the Mini-Clarence Adventure!")
        print ("while walking...")
elif play == "no":
        print("Aww what a bummer!")
else:
        print("Invalid choice.")
        
def play_game():
    health = 100
    inventory = []

    # Level 1: The Secret Forest
    print("You found a secret forest. You see a path leading east and a cave to the north.")
    choice1 = input("Go east (e) or north (n)? ").lower()
    if choice1 == "e":
        print("You encounter a friendly but ugly villager. They offer you a lame sword.")
        inventory.append("lame sword")
        health += 20 #gain health
    elif choice1 == "n":
        print("You enter the cave and find a chest containing 2 apples.")
        inventory.extend(["apple", "apple"])
        health += 10 # gain health

    #Level 2: The mysterious cave or secretive Path?
    if "lame sword" in inventory:
      print("You continue east with your lame sword. You encounter a zombie")
      choice2 = input("Attack (a) or run (r)? ").lower()
      if choice2 == "a":
        print("You defeat the zombie! You find a rainbow apple in its chest.")
        inventory.append("rainbow apple")
        health += 30
      elif choice2 == "r":
        print("You escape the zombie, but the zombie attacks you behind! you lose 10 health points.")
        health -= 10

    elif "rainbow apple" in inventory:
        print("You continue north through the cave. You find a hidden path leading to a treasure chest.")
        choice3 = input("Open the chest(o) or leave it(l)? ").lower()
        if choice3 == "o":
            print("You found a ruby! You gain 50 health points.")
            inventory.append("ruby")
            health += 50
        elif choice3 == "l":
            print("You decide not to open the chest. A unicorn is dissapointed. You lose 5 health points.")
            health -= 5

    else:
        print("You are lost and weak. LOL Game Over.")
        return


    # Level 3: Village or Mine
    if health > 50:
        print("You reach a village. You can either trade with the villagers(t) or explore the mine(m).")
        choice4 = input("Trade(t) or mine(m)? ").lower()
        if choice4 == "t":
            print("You trade for a healing potion. Your health is fully restored.")
            health = 100
        elif choice4 == "m":
            print("You enter the mine. You find a powerful weapon but get injured. You gain a powerful weapon but lose 30 health points.")
            inventory.append("powerful weapon")
            health -= 30
    else:
        print("You are too weak to continue. LMAO Game Over.")
        return

    # Level 4: Final Challenge
    if "powerful weapon" in inventory:
        print("You face the final boss! A feisty Papyrus! You use your powerful weapon.")
        choice5 = input("Attack the boss(a) or run away (r)? ").lower()
        if choice5 == "a":
          print("You defeat the boss! Congratulations, You win the game!")
        else:
          print("You failed to defeat the boss. LOL Game Over!")

    elif health > 0:
        print("You've survived, but the adventure continues...")  


    print("Game Over. Health:", health)
    print("Inventory:", inventory)


play_game()