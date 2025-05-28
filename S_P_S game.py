# Write code below 💖
import random
print("===================")
print("ROCK PAPER SCISSORS")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🖖")
print("5) 🦎")

while True:

  player = int(input("Pick a number: "))


  if player ==1:
    print("You chose: ✊")
  elif player==2:
    print("You chose: ✋")
  elif player==3:
    print("You chose: ✌️")
  elif player==4:
    print("You chose: 🖖")
  elif player==5:
    print("You chose: 🦎")
  else:
      print("Invalid choice.")

  computer=random.randint(1,5)

  if computer==1:
    print("CPU chose: ✊")
  elif computer==2:
    print("CPU chose: ✋")
  elif computer==3:
    print("CPU chose: ✌️")
  elif computer==4:
    print("CPU chose: 🖖")
  else:
    print("CPU chose: 🦎")

  if player==1 and computer==1 or player==2 and computer==2 or player==3 and computer==3 or player==4 and computer==4 or player==5 and computer==5:
    print("Tie. Nobody won")
  elif player==2 and computer==3 or player==5 and computer==3 or player==1 and computer==2 or player==4 and computer==2 or player==5 and computer==1 or player==3 and computer==1 or player==4 and computer==5 or player==2 and computer==5 or player==3 and computer==4 or player==1 and computer==4:
    print("CPU wins")
    break
  else:
    print("Player wins")
    break
