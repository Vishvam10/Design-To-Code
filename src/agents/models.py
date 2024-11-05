from typing import TypedDict

class ComponentData(TypedDict):
    definition: str
    styles: str

class ComponentDataWithImports(ComponentData):
    imports: str
