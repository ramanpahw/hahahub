from langgraph.graph import StateGraph, START, END
from character_identifier import character_identifier_node
from dialogue_generator import dialogue_generator_node
from graph_state import GraphState

class ScriptGraph:
  """Class ScriptGraph: Creates the graph and exposes method to invoke the graph."""
  def __init__(self):
    # Start building a new graph.
    self.graph_builder = StateGraph(GraphState)

    #Add the nodes to the graph
    self.graph_builder.add_node("character_identifier", character_identifier_node)
    self.graph_builder.add_node("dialogue_generator", dialogue_generator_node)

    # Start with the chatbot again.
    self.graph_builder.add_edge(START, "character_identifier")
    self.graph_builder.add_edge("character_identifier", "dialogue_generator")
    self.graph_builder.add_edge("dialogue_generator", END)

    # Complie the graph
    self.graph = self.graph_builder.compile()
  
  def create_script(self, text):
    """This method creates the base state and invoke the graph."""
    base_state = {
      "text": text,
      "characters": []
    }

    state = self.graph.invoke(base_state)
    #print(state["characters"])
    #print(state["dialogues"])
    return state["dialogues"]
