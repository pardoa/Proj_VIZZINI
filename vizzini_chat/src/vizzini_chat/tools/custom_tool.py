from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput



class CoffeeBlendSearchInput(BaseModel):
    query: str = Field(..., description="Attributes or keywords to search for in coffee blends.")

class CoffeeBlendSearchTool(BaseTool):
    name: str = "Coffee Blend Database Search"
    description: str = (
        "Searches Vizzini_DB.md for coffee blends matching given attributes, flavor, method, etc."
    )
    args_schema: Type[BaseModel] = CoffeeBlendSearchInput

    def _run(self, query: str) -> str:
        with open("src/vizzini_chat/database/Vizzini_DB.md", encoding="utf-8") as f:
            db = f.read()
        # Implement a simple search (improvement: use markdown parser, fuzzy, etc.):
        results = []
        blend_sections = db.split("## ")
        for section in blend_sections:
            if query.lower() in section.lower():
                results.append(section[:500])
        if not results:
            return "No matching blend found."
        return "\n\n".join(results[:3])