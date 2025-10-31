from typing import TypedDict
from langgraph.graph import StateGraph
from typing import Annotated
from rich import print
import operator
from dataclasses import dataclass

@dataclass
# Definir estado do grafo
class State:
    nodes_path: Annotated[list[str], operator.add] 
    
# Definir o node A
def node_a(state: State) -> State:
    output_state: State = State(nodes_path=["A"]) 
    print('> node_a', f"{state}", f"{output_state}") 
    return output_state

# Definir o node B
def node_b(state: State) -> State:
    output_state: State = State(nodes_path=["B"]) 
    print('> node_b', f"{state}", f"{output_state}") 
    return output_state

# Definir o builder do grafo
builder = StateGraph(State)

builder.add_node('A', node_a)
builder.add_node('B', node_b)

# Conectar as edges (arestas)
builder.add_edge('__start__', 'A')
builder.add_edge('A', 'B')
builder.add_edge('B', '__end__')

# Compilar o grafo
graph = builder.compile()

# Pegar o resultado
response = graph.invoke(State(nodes_path=[]))


print()
print(f"{response} ")
