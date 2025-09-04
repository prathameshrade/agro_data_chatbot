from backend.graph.rag_nodes import RAGPipeline

class AgentGraph:
    def __init__(self):
        self.rag_pipeline = RAGPipeline()

    async def handle_query(self, query: str):
        return await self.rag_pipeline.run(query)
