"""Database Mixins"""
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean, String, func
from sqlalchemy.orm import declarative_mixin
from uuid import uuid4


@declarative_mixin
class TimestampMixin:
    """Mixin for created_at and updated_at timestamps (UTC)"""
    
    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
        comment="Creation timestamp (UTC)"
    )
    
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="Last update timestamp (UTC)"
    )


@declarative_mixin
class SoftDeleteMixin:
    """Mixin for soft delete support"""
    
    deleted_at = Column(
        DateTime,
        nullable=True,
        comment="Soft delete timestamp (UTC)"
    )
    
    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
        comment="Soft delete flag"
    )
    
    def soft_delete(self) -> None:
        """Mark record as deleted"""
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()
    
    def restore(self) -> None:
        """Restore soft-deleted record"""
        self.is_deleted = False
        self.deleted_at = None


@declarative_mixin
class UUIDMixin:
    """Mixin for UUID-based public identifiers"""
    
    public_id = Column(
        String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid4()),
        index=True,
        comment="Public UUID (for API and callbacks)"
    )
