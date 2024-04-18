def receive_input():
    numberOfStates = receive_numberOfStates()
    numberOfTerminalSymbols, terminalSymbols = receive_terminalSymbols()
    numberOfAcceptanceStages, AcceptanceStages = receive_AcceptanceStates()
    numberOfTransitions = receive_Transitions()
    transitions = receive_InitialFinal_Transitions()
    numberOfChains = receive_numberOfChains()
    chains = receive_Chains(numberOfChains)

def receive_numberOfStates(): # First input, number of states
    while True:
        numberOfStates = input() # Number of states, first input
        try:
            numberOfStates = int(numberOfStates)
            if int(numberOfStates) >= 1 and int(numberOfStates) <= 10:
                numberOfStates = int(numberOfStates)
                break
            else:
                print("Number of states should be between 1 and 10\nPlease, try again.")
                continue
        except:
            print("Number of states should be a number\nPlease, try again.")
            continue

    return numberOfStates

def receive_terminalSymbols(): # Second input, number of terminal symbols and terminal symbols
    while True:
        terminalSymbols = input().split() # Receive the terminal symbols
        try:
            numberOfTerminalSymbols = int(terminalSymbols[0]) # Get the number of terminal symbols
            terminalSymbols = terminalSymbols[1:] # Remove the first element of the list
            if len(terminalSymbols) > 10:
                print("Too much terminal symbols")
                continue
            else:
                break
        except:
            print("Number of terminal symbols should be a number\nPlease, try again.")
            continue
        
        
    return numberOfTerminalSymbols, terminalSymbols

def receive_AcceptanceStates():# Third input, number of acceptance states and acceptance states
    inputStages = input()
    try:
        AcceptanceStages = inputStages.split()

        numberOfAcceptanceStages = int(AcceptanceStages[0])
        AcceptanceStages = AcceptanceStages[1:]

        for i in range(len(AcceptanceStages)):
            AcceptanceStages[i] = int(AcceptanceStages[i])

        return numberOfAcceptanceStages, AcceptanceStages
    except Exception as e:
        return e
            
def receive_Transitions(): # Fourth input, number of transitions
    while True:
        numberOfTransitions = input()
        try:
            numberOfTransitions = int(numberOfTransitions)
            if numberOfTransitions > 50 and numberOfTransitions < 1:
                print("Invalid transitions")
                continue
            else:
                break
        except:
            print("Number of transitions should be a number\nPlease, try again.")
            continue

    return numberOfTransitions

def receive_InitialFinal_Transitions(): # Fifth input, transitions
    transitions = []
    for i in range(numberOfTransitions):
        transition = input()
        transitions.append(transition)
    return transitions

def receive_numberOfChains(): # Number of chains
    while True:
        numberOfChains = input()
        try:
            numberOfChains = int(numberOfChains)
            if numberOfChains > 10:
                print("Too much chains")
                continue
            else:
                break
        except:
            print("Number of chains should be a number\nPlease, try again.")
            continue
    return numberOfChains

def receive_Chains(numberOfChains): # Receive chains
    chains = []
    for i in range(numberOfChains):
        chain = input()
        if len(chain) > 20:
            print("Chain too long")
            exit(0)
        chains.append(chain)
    return chains
 

if __name__ == "__main__": # Main function
    receive_input()
