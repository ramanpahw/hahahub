from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from graph_state import GraphState
import os

def dialogue_generator_node(state: GraphState):
  ### Generates dialogue from the text ###
  # Step 1: Get the text
  text = state["text"]
  characters = state["characters"]

  # Step 2: Set up Gemini via LangChain GoogleGenerativeAI
  llm = GoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    temperature=0.1
  )

  # Step 3: Use context as the input variable
  prompt = PromptTemplate(
    input_variables=["text", "characters"],
    template=(
      "You are an expert in funny and humorous dialogue generation from text and characters in a script format.\n"
      "Generate script format dialogues using the following text:\n\n"
      "{text}\n\n"
      "and characters \n\n"
      "{characters}\n\n"
      "Dialogues:"
    )
  )

  # Step 4: Build the chain
  chain = (prompt | llm)

  # Step 5: Run the chain
  result = chain.invoke({"text": text, "characters": characters})

  state["dialogues"] = result
  return state
