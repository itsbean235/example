from random import randint 
print("Please enter all choices in lower case:")
print("rock...")
print("paper...")
print("scissor...")
print("Enter your choice:")
pl=input().lower()
ran=randint(0,2)
if ran==0:
	com="rock"
elif ran==1:
	com="paper"
else:
	com="scissor"
print(f"computer played {com}")
if pl!="rock" and pl!="paper" and pl!="scissor":
	print("You entered something else")
if com==pl:
	print("This  match is tie")
if pl=='rock' and com=='paper':
	print("computer wins")
if pl=='rock' and com=='scissor':
	print("you win")
if pl=='paper' and com=='rock':
	print("you win")
if pl=='paper' and com=='scissor':
	print("computer win")
if pl=="scissor" and com=='rock':
	print("computer win")
if pl=='scissor' and com=='paper':
	print("you win")