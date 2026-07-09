"""Formatting utilities"""
from datetime import datetime
from typing import Optional
import pytz


def format_price(price: int, currency: str = "تومان") -> str:
    """
    Format price with thousand separators
    
    Args:
        price: Price in toman
        currency: Currency label
    
    Returns:
        Formatted price string
    """
    return f"{price:,} {currency}"


def format_date(
    dt: datetime,
    format_str: str = "%Y-%m-%d %H:%M",
    timezone: str = "Asia/Tehran"
) -> str:
    """
    Format datetime in specified timezone
    
    Args:
        dt: Datetime object
        format_str: Format string
        timezone: Timezone name
    
    Returns:
        Formatted date string
    """
    tz = pytz.timezone(timezone)
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    return dt.astimezone(tz).strftime(format_str)


def format_duration_display(months: int) -> str:
    """
    Format duration for display
    
    Args:
        months: Number of months
    
    Returns:
        Formatted duration string
    """
    if months == 1:
        return "یک ماهه"
    elif months == 3:
        return "سه ماهه"
    elif months == 6:
        return "شش ماهه"
    elif months == 12:
        return "سالانه"
    else:
        return f"{months} ماهه"


def format_volume_display(gb: Optional[int]) -> str:
    """
    Format storage volume for display
    
    Args:
        gb: Gigabytes (None for unlimited)
    
    Returns:
        Formatted volume string
    """
    if gb is None or gb == 0:
        return "نامحدود"
    elif gb >= 1024:
        return f"{gb // 1024} ترابایت"
    else:
        return f"{gb} گیگابایت"
