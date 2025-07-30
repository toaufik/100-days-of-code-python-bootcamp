print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("🏝️ Welcome to **Treasure Island**! 🗺️")
print("Your mission is to **find the treasure**. Good luck, adventurer!\n")

choice1 = input('You\'re at a crossroad. Where do you want to go?\nType "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('\nYou\'ve come to a lake. There is an island in the middle of the lake.\n'
                    'Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    
    if choice2 == "wait":
        choice3 = input('\nYou arrive safely on the island. 🏝️\n'
                        'There is a house with 3 doors: one **red**, one **yellow**, and one **blue**.\n'
                        'Which door do you choose? ').lower()
        
        if choice3 == "red":
            print("\n🔥 You were burned by fire. Game Over.")
        elif choice3 == "blue":
            print("\n🐻 You were eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("\n🎉 You found the treasure! You Win! 🪙")
        else:
            print("\n🚪 You chose a door that doesn't exist. Game Over.")
    
    else:
        print("\n🐟 You were attacked by a giant trout. Game Over.")

elif choice1 == "right":
    print("\n🕳️ You fell into a hole. Game Over.")
else:
    print("\n❗Invalid choice. You wander off and are never seen again. Game Over.")