"""Validation utilities"""
import re
from typing import Tuple


def validate_card_luhn(card_number: str) -> bool:
    """
    Validate card number using Luhn algorithm
    
    Args:
        card_number: 16-digit card number (with or without spaces/dashes)
    
    Returns:
        True if valid, False otherwise
    """
    # Remove spaces and dashes
    card_clean = card_number.replace(' ', '').replace('-', '')
    
    # Check if it's 16 digits
    if not card_clean.isdigit() or len(card_clean) != 16:
        return False
    
    # Luhn algorithm
    digits = [int(d) for d in card_clean]
    checksum = 0
    
    # Process from right to left
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:  # Double every second digit from right
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    
    return checksum % 10 == 0


def format_card_number(card: str) -> str:
    """
    Format card number to readable format
    
    Args:
        card: Unformatted card number
    
    Returns:
        Formatted card number (6274-1211-9826-2321)
    """
    card_clean = card.replace(' ', '').replace('-', '')
    return '-'.join([card_clean[i:i+4] for i in range(0, len(card_clean), 4)])


def validate_phone_number(phone: str) -> bool:
    """
    Validate Iranian phone number
    
    Args:
        phone: Phone number to validate
    
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^(\+98|0)?9\d{9}$'
    return bool(re.match(pattern, phone))


def validate_shaba(shaba: str) -> bool:
    """
    Validate Iranian SHABA number (IBAN)
    
    Args:
        shaba: SHABA number to validate
    
    Returns:
        True if valid, False otherwise
    """
    # IR + 24 alphanumeric characters
    pattern = r'^IR\d{24}$'
    return bool(re.match(pattern, shaba))
