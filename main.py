def receive_input():
    numberOfStates = receive_numberOfStates()
    numberOfTerminalSymbols, terminalSymbols = receive_terminalSymbols()

def receive_numberOfStates():
    while True:
        numberOfStates = input() # Number of states, first input
        try:
            int(numberOfStates)
        except:
            print("Number of states should be a number\nPlease, try again.")
            continue

        if int(numberOfStates) >= 1 and int(numberOfStates) <= 10:
            numberOfStates = int(numberOfStates)
            break
        else:
            print("Number of states should be between 1 and 10\nPlease, try again.")
            continue

    return numberOfStates

def receive_terminalSymbols(): # Criar try except para verificar se o primeiro input é numero (semelhante a função acima), criar casos de teste
    while True:
        terminalSymbols = input().split() # Receive the terminal symbols
        try:
            numberOfTerminalSymbols = int(terminalSymbols[0]) # Get the number of terminal symbols
        except:
            print("Number of terminal symbols should be a number\nPlease, try again.")
            continue
        terminalSymbols = terminalSymbols[1:] # Remove the first element of the list
        if len(terminalSymbols) > 10:
            print("Too much terminal symbols")
            continue
    return numberOfTerminalSymbols, terminalSymbols


def receive_AcceptanceStates():
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
            
def receive_Transitions():
    numberOfTransitions = int(input())
    return numberOfTransitions

def receive_InitialFinal_Transitions():
    transitions = []
    for i in range(numberOfTransitions):
        transitions = input(format(i+1))
        transitions.append(transitions.split())
    return transitions
     

if __name__ == "__main__": # Main function
    receive_input()
