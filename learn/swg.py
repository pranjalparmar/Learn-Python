import random
x = ["snake","water","gun"]
y = ["s","w","g"]

myscore = 0
compscore = 0
for count in range (1,10):
    comp = random.choice(x)
    i = input("Choose from s, w, g\n")
    if i not in y:
        print("Invalid Choice! ", "\nPlease Enter Valid Choice from 's','w','g'")

    if i == "s":
        if comp == "snake":
            print("draw")
        elif comp == "water":
            print("you win")
            myscore = myscore + 1
        elif comp == "gun":
            print("computer wins")
            compscore = compscore + 1

    if i == "w":
        if comp == "water":
            print("draw")
        elif comp == "gun":
            print("you win")
            myscore = myscore + 1
        elif comp == "snake":
            print("computer wins")
            compscore = compscore + 1

    if i == "g":
        if comp == "gun":
            print("draw")
        elif comp == "water":
            print("you win")
            myscore = myscore + 1
        elif comp == "snake":
            print("computer wins")
            compscore = compscore + 1




print("yourscore = ",myscore)
print("computer's score = ",compscore)

if myscore > compscore:
    print("YOU WIN")
elif myscore == compscore:
    print("MATCH DRAW")
else:
    print("YOU LOST")