from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from graph_state import GraphState
import os

def character_identifier_node(state: GraphState):
  ### Idenfies the nouns/characters from the given text ###
  # Step 1: Get the text
  text = state["text"]

  # Step 2: Set up Gemini via LangChain GoogleGenerativeAI
  llm = GoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    temperature=0.1
  )

  # Step 3: Use context as the input variable
  prompt = PromptTemplate(
    input_variables=["context"],
    template=(
      "You are an expert in identifying characters / people / nouns from text.\n"
      "Idenfity the characters / people / nouns from the following paragraphs:\n\n"
      "{context}\n\n"
      "Characters:"
    )
  )

  # Step 4: Build the chain
  chain = (prompt | llm)

  # Step 5: Run the chain
  result = chain.invoke({"context": text})

  state["characters"] = result
  return state