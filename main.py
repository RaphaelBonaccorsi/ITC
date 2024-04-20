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
        if len(chain) > 20 or len(chain) < 1:
            print("Invalid chain length")
            exit(0)
        chains.append(chain)
    if len(chains) != numberOfChains:
        print("Invalid number of chains")
        exit(0)
    return chains
 
def initialize_graph(transitions):
    graph = {}
    for i in transitions:
        key = i[0]
        value = i[2:]
        graph[key] = graph.get(key, []) + [value]
    return graph
    
def is_AFN(graph):
    for state, transitions in graph.items():
        transition_dict = {}
        for transition in transitions:
            symbol, next_state = transition.split()
            if symbol in transition_dict:
                if next_state != transition_dict[symbol]:
                    return True  # Encontramos um AFN
            else:
                transition_dict[symbol] = next_state
    return False  # Não encontramos nenhum AFN

def convert(graph, caracters):
    translate = {}
    afd = {}
    total_states = 0
    start_state = '0'  # Estado inicial do DFA
    to_check = [start_state]  # Lista de estados para verificar

    # Mapeia o estado inicial do NFA para o estado inicial do DFA
    translate[start_state] = total_states
    afd[total_states] = []
    total_states += 1

    # Loop principal para converter estados
    while to_check:
        cur = to_check.pop()

        for cur_caracter in caracters:
            new_state = []
            for i in cur.strip():
                for j in graph[i]: 
                    caracter, next_state = j.split()
                    if cur_caracter == caracter:
                        if next_state not in new_state:
                            new_state.append(next_state)
            new_state.sort()                

            # Ordena os novos estados

            # Adiciona o novo estado ao DFA se ainda não estiver mapeado
            if "".join(new_state) not in translate:
                to_check.append("".join(new_state))
                translate["".join(new_state)] = total_states
                afd[total_states] = []
                total_states += 1

        # Adiciona a transição ao DFA
            afd[translate[cur]].append(cur_caracter + " " + str(translate["".join(new_state)]))


    return afd

def is_accepted(graph, chain, acceptanceStates):
    current_state = '0'
    for symbol in chain:
        transitions = graph.get(current_state)
        if transitions is None:
            return False
        next_state = None
        for transition in transitions:
            if transition.startswith(symbol):
                next_state = transition[len(symbol)+1:]
                break
        if next_state is None:
            return False
        current_state = next_state
    if int(current_state) in acceptanceStates:
        return True
    else:
        return False

if __name__ == "__main__": # Main function
    numberOfStates = receive_numberOfStates()
    numberOfTerminalSymbols, terminalSymbols = receive_terminalSymbols()
    numberOfAcceptanceStates, acceptanceStates = receive_AcceptanceStates()
    numberOfTransitions = receive_Transitions()
    transitions = receive_InitialFinal_Transitions()
    numberOfChains = receive_numberOfChains()
    chains = receive_Chains(numberOfChains)
    graph = initialize_graph(transitions)

    #if not is_AFN(graph):
    #    graph = convert(graph, terminalSymbols)

    with open('/home/raphael/Desktop/ITC/output.txt', 'w') as file:
        for chain in chains:
            if is_accepted(graph, chain, acceptanceStates):
                file.write("aceita\n")
            else:
                file.write("rejeita\n")

    
