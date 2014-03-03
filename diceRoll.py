from random import randint


#sides=99
#Entering 0 for both prompts will commence dice rolling

def diceRoll():
    sides=99
    total=0
    result=0
    cup={}
    while int(sides) !=0:
        print("Enter the number of sides")
        sides = input()
        #print(sides)
        if sides==0:
            continue
        else:
            print("Enter number of dice of size ", sides)
            number = input()
            cup[sides]=number

    #roll cup
    for key in cup:
        for i in range(1,int(cup[key])+1):
            result = randint(1,int(key))
            print(key," sided die rolled a ", result)
            total = total+result
    print ("And the total is ", total)
    total = 0
    print("Would you like to reroll?  y/n")
    cont = input()
    if cont=="y":
        while cont=="y":
            #roll cup
            for key in cup:
                for i in range(1,int(cup[key])+1):
                    result = randint(1,int(key))
                    print(key," sided die rolled a ", result)
                    total = total+result
            print ("And the total is ", total)
            total = 0
            print("Would you like to reroll?  y/n")
            cont = input()
        #endwhile
    elif cont == "n":
        diceRoll()
    return total
  #exit


#if __name__ == "__main__":
#    diceRoll()
