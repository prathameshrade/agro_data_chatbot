from fastapi import FastAPI
from backend.graph.agent_graph import AgentGraph

app = FastAPI()
agent_graph = AgentGraph()

@app.get('/')
async def root():
    return {"message": "ARGO AI Conversational System API"}

@app.post('/query')
async def query_agent(query: str):
    response = await agent_graph.handle_query(query)
    return {"response": response}
