from google.adk.agents import LlmAgent
from google.genai import types
from google.adk.tools import VertexAiSearchTool

DATASTORE_PATH = "DATASTORE_PATH_HERE"

vertex_search_tool = VertexAiSearchTool(data_store_id=DATASTORE_PATH)

doc_qa_agent = LlmAgent(
    name=AGENT_NAME_VSEARCH,
    model=GEMINI_2_FLASH, # Requires Gemini model
    tools=[vertex_search_tool],
    instruction=f"""You are a helpful assistant that answers questions based on information found in the document store: {DATASTORE_PATH}.
    Use the search tool to find relevant information before answering.
    If the answer isn't in the documents, say that you couldn't find the information.
    """,
    description="Answers questions using a specific Vertex AI Search datastore.",
)
root_agent = doc_qa_agent