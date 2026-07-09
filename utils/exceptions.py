"""Custom exceptions for the application"""


class VPNBotException(Exception):
    """Base exception for all bot exceptions"""
    pass


# === DATABASE EXCEPTIONS ===
class DatabaseException(VPNBotException):
    """Database operation error"""
    pass


class RecordNotFound(DatabaseException):
    """Record not found in database"""
    pass


class DuplicateRecordError(DatabaseException):
    """Duplicate record already exists"""
    pass


class TransactionError(DatabaseException):
    """Transaction operation failed"""
    pass


# === VALIDATION EXCEPTIONS ===
class ValidationException(VPNBotException):
    """Validation error"""
    pass


class InvalidCardNumber(ValidationException):
    """Invalid card number format or Luhn check failed"""
    pass


class InvalidPhoneNumber(ValidationException):
    """Invalid phone number format"""
    pass


class InvalidShaba(ValidationException):
    """Invalid SHABA/IBAN format"""
    pass


class InvalidCallbackData(ValidationException):
    """Callback data is invalid or tampered"""
    pass


# === BUSINESS LOGIC EXCEPTIONS ===
class BusinessLogicException(VPNBotException):
    """Business logic error"""
    pass


class InsufficientBalance(BusinessLogicException):
    """User has insufficient balance"""
    pass


class InvalidDiscountCode(BusinessLogicException):
    """Discount code is invalid, expired or used up"""
    pass


class OrderNotFound(BusinessLogicException):
    """Order not found"""
    pass


class PaymentAlreadyVerified(BusinessLogicException):
    """Payment already verified"""
    pass


class ConfigNotAvailable(BusinessLogicException):
    """VPN config is not available"""
    pass


# === PERMISSION EXCEPTIONS ===
class PermissionException(VPNBotException):
    """Permission denied"""
    pass


class AdminOnly(PermissionException):
    """Admin access required"""
    pass


class InsufficientPermissions(PermissionException):
    """Admin lacks required permissions"""
    pass


# === STORAGE EXCEPTIONS ===
class StorageException(VPNBotException):
    """Storage operation error"""
    pass


class FileNotFound(StorageException):
    """File not found in storage"""
    pass


class StorageUploadError(StorageException):
    """Failed to upload file"""
    pass


class StorageDownloadError(StorageException):
    """Failed to download file"""
    pass


# === BOT EXCEPTIONS ===
class BotException(VPNBotException):
    """Bot operation error"""
    pass


class UserBlocked(BotException):
    """User is blocked from using the bot"""
    pass


class MessageSendError(BotException):
    """Failed to send message to user"""
    pass
