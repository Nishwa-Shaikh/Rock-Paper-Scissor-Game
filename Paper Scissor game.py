print("Let's start Paper, Scissor and Rock game ")
print("Instruction: \n1.This is only 2 players game\n2.Names of both players should not be same\n3.Do not write your choice completely, just write the first letter\n4.If you want to exit press 'e'.\nEnjoy!!")

PointsOfPlayer1 = 0
PointsOfPlayer2 = 0
exit_game = False

while True:
    Name1 = input('Enter name of player1: ')
    Name2 = input('Enter name of player2: ')
    if Name1 == Name2: 
        print("Names should not be same")
        continue
    break 

while True:
    Player1 = input(f"Enter {Name1}'s choice: ").upper()
    if Player1 == 'E':
        exit_game = True
        break
    Player2 = input(f"Enter {Name2}'s choice: ").upper()
    if Player2 == 'E':
        exit_game = True
        break 

    if Player1 == Player2:
        print('Tie')
    elif Player1 == 'P' and Player2 == 'S':
        print(f"{Name2} won")
        PointsOfPlayer2 += 1
    elif Player2 == 'P' and Player1 == 'S':
        print(f"{Name1} won")
        PointsOfPlayer1 += 1
    elif Player1 == 'P' and Player2 == 'R':
        print(f"{Name1} won")
        PointsOfPlayer1 += 1        
    elif Player1 == 'R' and Player2 == 'P':
        print(f'{Name2} won')
        PointsOfPlayer2 += 1
    elif Player1 == 'R' and Player2 == 'S':
        print(f'{Name1} won')
        PointsOfPlayer1 += 1
    elif Player1 == 'S' and Player2 == 'R':
        print(f'{Name2} won')
        PointsOfPlayer2 += 1
    else:
        print('Please enter correct data')
        
    if exit_game:
        break

print(f"Points of {Name1}: {PointsOfPlayer1}")
print(f"Points of {Name2}: {PointsOfPlayer2}")
if PointsOfPlayer1>PointsOfPlayer2:
    print(f"{Name1} won!!")
elif PointsOfPlayer2>PointsOfPlayer1:
    print(f"{Name2} won!!")
else:
    print('Tie')