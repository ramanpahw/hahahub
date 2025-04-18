from langgraph.graph import StateGraph, START, END
from character_identifier import character_identifier_node
from dialogue_generator import dialogue_generator_node
from graph_state import GraphState
from script_graph import ScriptGraph
import os

def main():
  """Main method to test the application."""
  text = """
  Shah Rukh Khan and Kajol have been one of Bollywood’s most loved on-screen pairs, lighting up the screen with their 
  incredible chemistry in films like Dilwale Dulhania Le Jayenge, Kuch Kuch Hota Hai, and Kabhi Khushi Kabhie Gham. 
  Their last film together was Dilwale, where they reunited alongside Varun Dhawan and Kriti Sanon. 
  In a throwback interview with NDTV, they were asked if they might’ve dated each other had they both been single.
  Kajol answered honestly, saying she wasn’t sure since she was already dating Ajay Devgn during Baazigar. 
  Shah Rukh, always quick with a joke, chimed in saying, “I was also seeing Ajay at that time,” making everyone laugh.
  Their first film together, Baazigar, was a major hit and marked the beginning of a legendary on-screen partnership. 
  Shah Rukh played a complex, grey-shaded character that really stood out, while Kajol’s performance brought heart and 
  intensity. The chemistry between them was instant and unforgettable, and fans quickly fell in love with the pair.
  Over the years, their connection only got stronger on screen, turning every film they did together into something special 
  and iconic.

  Off screen, both stars have built beautiful lives for themselves. Shah Rukh married Gauri Khan even before he entered 
  the film industry, and they’ve raised three kids together — Aryan, Suhana, and AbRam. Kajol started dating Ajay Devgn 
  in the mid-90s and the two tied the knot in a simple Maharashtrian ceremony at Ajay’s home in 1999. They’re now proud 
  parents to daughter Nysa and son Yug. Despite being huge stars, both Shah Rukh and Kajol have always kept their personal
  lives fairly low-key and grounded.
  """

  # Creates object of the graph
  script_graph = ScriptGraph()
  # Calls the method
  script = script_graph.create_script(text)
  # Print the output script
  print(script)

if __name__ == "__main__":
  main()
