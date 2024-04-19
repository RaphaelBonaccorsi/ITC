from main import initialize_graph

def test_initialize_graph_empty_transitions():
    transitions = []
    assert initialize_graph(transitions) == {}

def test_initialize_graph_single_transition():
    transitions = ['0 a 1']
    expected_graph = {'0': ['a 1']}
    assert initialize_graph(transitions) == expected_graph

def test_initialize_graph_multiple_transitions():
    transitions = ['0 a 1', '0 b 1', '1 a 1', '1 b 2', '2 a 0', '2 b 2']
    expected_graph = {'0': ['a 1', 'b 1'], '1': ['a 1', 'b 2'], '2': ['a 0', 'b 2']}
    assert initialize_graph(transitions) == expected_graph
