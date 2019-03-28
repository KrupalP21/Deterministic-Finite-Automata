dfa = {}
states = []
symbols = []
start = []
final = []
truth = 1
while (truth == 1):
    try:
        currentInput = input()
        currentInput = currentInput.split()
    except EOFError:
        break
    
    if (currentInput[0] == "states:"):
        for i in range(1, len(currentInput)):
            states.append(currentInput[i])
    if (currentInput[0] == "symbols:"):
        for i in range(1, len(currentInput)):
            symbols.append(currentInput[i])
    if (currentInput[0] == "start:"):
        for i in range(1, len(currentInput)):
            start.append(currentInput[i])
    if (currentInput[0] == "final:"):
        for i in range(1, len(currentInput)):
            final.append(currentInput[i])
        truth = 0
    if (currentInput[0] == "begin_rules"):
        yellow = 1
        while(yellow == 1):
            currentInput = input()
            currentInput = currentInput.split()
            if (currentInput[0] == "end_rules"):
                yellow = 0
                break
            if(currentInput[0] in dfa):
                dfa[currentInput[0]][currentInput[4]] = currentInput[2]
            else:
                dfa[currentInput[0]] = {}
                dfa[currentInput[0]][currentInput[4]] = currentInput[2]

truth = 1
currentState = start[0]
while truth == 1:
    currentState = start[0]
    flag = 0
    try:
    	currentString = input()
    except EOFError:
        break
    
    for i in range(len(currentString)):
        if currentState not in dfa:
            flag = 1
            break
        if (currentString[i] in dfa[currentState]):
            currentState = dfa[currentState][currentString[i]]
    if (currentState in final) & (flag == 0):
        print("accepted")
    else:
        print("rejected")       
