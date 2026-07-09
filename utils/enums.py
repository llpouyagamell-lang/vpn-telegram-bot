"""Helper functions for working with enums"""
from enum import Enum
from typing import Dict, List, Type, TypeVar

T = TypeVar('T', bound=Enum)


def enum_to_dict(enum_class: Type[T]) -> Dict[str, str]:
    """
    Convert enum to dictionary
    
    Args:
        enum_class: Enum class
    
    Returns:
        Dictionary of {value: name}
    """
    return {member.value: member.name for member in enum_class}


def get_enum_values(enum_class: Type[T]) -> List[str]:
    """
    Get all values of an enum
    
    Args:
        enum_class: Enum class
    
    Returns:
        List of enum values
    """
    return [member.value for member in enum_class]
