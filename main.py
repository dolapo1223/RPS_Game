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

#Introduction to the game
print("Hello, this is ROCK, PAPER, SCISSORS game\n")
#Constants
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

#Rules of engagement
print(bold + blue + "Rules of engagement: \n"+ end)
print(italics + red + "- Rocks wins against scissors:" + end)
print(italics + red + "- Rocks wins against scissors" + end)
print(italics + red + "- Scissors wins against paper."+ end)
print(italics + red + "- Paper wins against rock\n" + end)

#game images
game_images = [rock, paper, scissors]

#user choice selection
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors: "))

#invalid number catch
if user_choice >=3 or user_choice < 0:
  print(bold + italics + red +  "\nYou entered an invalid number. You loose!" + end)
else:
  print("\nYou chose " + (game_images[user_choice]))

  #Computer choice selection
  computer_choice = random.randint(0, 2)
  print("computer chose: " + (game_images[computer_choice]))

  #Games Process

  if user_choice == 0 and computer_choice == 2:
    print(bold + green + "You WIN!" + end)
  elif computer_choice == 0 and user_choice == 2:
    print(bold + red + "You Loose" + end)
  elif user_choice > computer_choice:
    print(bold + green + "You WIN!" + end)
  elif computer_choice > user_choice:
    print(bold + red + "You Loose" + end)
  elif user_choice == computer_choice:
    print(bold + blue + "It's a Draw!" + end)



