import os
import time
import random
import rich
from rich import print as rprint
from rich.spinner import Spinner
from rich.live import Live

try:

    if os.environ.get('RAN_BEFORE') == "true":
        ranBefore = True
    else:
        ranBefore = False

    print("")

    rprint("[bold red]Roll the Dice![/bold red]")
    rprint("[bold yellow]*d4, d6, d8, d10, d12, d20, coin flip*[/bold yellow]")

    print("")

    whichDice = input("Which dice would you like to roll? ")
    diceCount = ""
    if whichDice != "coin flip":
        diceCount = input("How many dice would you like to roll? (press enter to continue with one) ")
        
        if diceCount == "":
            diceCount = 1

    dice = str(diceCount) + str(whichDice)
    rollMessage = f"Rolling dice...{dice}"

    def coinFlip():
        coinFlip = random.choice(["heads", "tails"])
        return coinFlip

    def d4():
        d4 = sum(random.randint(1,4) for _ in range(int(diceCount)))
        return d4

    def d6():
        d6 = sum(random.randint(1,6) for _ in range(int(diceCount)))
        return d6

    def d8():
        d8 = sum(random.randint(1,8) for _ in range(int(diceCount)))
        return d8

    def d10():
        d10 = sum(random.randint(0,9) for _ in range(int(diceCount)))
        return d10

    def d12():
        d12 = sum(random.randint(1,12) for _ in range(int(diceCount)))
        return d12
    def d20():
        d20 = sum(random.randint(1,20) for _ in range(int(diceCount)))
        return d20

    def addAllNumbers():
        resultVars = {}

        for env_name, env_value in os.environ.items():
            if env_name.startswith('RESULT_'):
                numberPart = env_name[7:]
                if len(numberPart) == 3 and numberPart.isdigit():
                    resultVars[env_name] = env_value
        
        integerValues = []

        for var_name, string_value in resultVars.items():
            try:
                intValue = int(string_value)
                integerValues.append(intValue)
            except ValueError:
                rprint(f"[bold red]WARNING:{var_name} contains '{string_value}' which cannot be converted to an integer[/bold red]")
        
        totalSum = sum(integerValues)
        return totalSum, integerValues

    if whichDice == "coin flip":
        rollMessage = "Flipping a coin..."
        result = coinFlip()
    elif whichDice == "d4":
        result = d4()
    elif whichDice == "d6":
        result = d6()
    elif whichDice == "d8":
        result = d8()
    elif whichDice == "d10":
        result = d10()
    elif whichDice == "d12":
        result = d12()
    elif whichDice == "d20":
        result = d20()
    else:
        print("")
        rprint("[bold red]ERROR: Please enter a valid dice number[/bold red]")
        exit()

    print("")
    rollTime = Spinner("dots2", text= rollMessage)
    with Live(rollTime):
        time.sleep(2)
    print("")

    print(f"Your result is...{result}!")
    if whichDice != "coin flip":
        os.environ[f'RESULT_{str(random.randint(100,999))}'] = str(result)

    if ranBefore == True:
        sumAll = input("Would you like to sum all of your results together? (Y/n) ").strip()
        if sumAll.lower() in ["","y","yes"]:
            total, individualValues = addAllNumbers()
            rollTime = Spinner("dots2", text="Adding all results...")
            with Live(rollTime):
                time.sleep(3)
            print("")
            print(f"The sum of all the results is {total}, summed from {individualValues}")
        else:
            print("")

    rollAgain = input("Would you like to roll again? (Y/n)").strip()

    if rollAgain.lower() in ["","y","yes"]:
        os.environ['RAN_BEFORE'] = str("true")
        filePath = os.path.abspath(__file__)
        os.system(f"python3 {filePath}")
    else:
        exit()

except KeyboardInterrupt:
    print("\n")
    rprint("Goodbye [bold yellow]:))[/bold yellow]")