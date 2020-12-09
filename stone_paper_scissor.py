import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("___________Welcome to the Rock-Paper-Scissors!!!___________")
choice = int(input("\nWhat do you chooose? \n\tType '0' for 'Rock' \n\t\tType '1' for 'Paper' \n\t\t\tType '2' for 'Scissors'\n "))
game_list = [rock,paper,scissors]

print(game_list[choice])

print("Computer chose:")
list_length = len(game_list)
computer_choice = random.randint(0,list_length-1)

print(game_list[computer_choice])

if choice >= 3:
  print("You chose an invalid number,You lose!!")
elif choice == 0 and computer_choice == 2:
  print("You win!!")
elif computer_choice > choice :
  print("You lose!!")
elif choice > computer_choice:
  print("You win!!")
elif choice == computer_choice:
  print("It's a draw!!")
