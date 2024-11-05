from enum import Enum


class Patterns(Enum):
    
    REACT_COMPONENT_DEFINITION_PATTERN = r"const\s+([A-Za-z_][A-Za-z0-9_]*)\s*="
    REACT_COMPONENT_NAME_EXTRACT_PATTERN = r"<([A-Z]\w*)\s*"
