from sqlalchemy.orm import DeclarativeBase

from ticketless_transport.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
