from typing_extensions import TypedDict

class GraphState(TypedDict):
  """Class GraphState."""
  text: str
  characters: list[str]
  dialogues: list[str]
