from sqlalchemy import Column, String, Boolean, JSON, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base_class import Base

class PaymentGateway(Base):
    """
    Configuration for different payment providers (Stripe, PayPal, etc.)
    """
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True) # e.g., 'stripe', 'paypal'
    display_name = Column(String)
    is_active = Column(Boolean, default=True)
    config = Column(JSON) # Store API keys, webhook secrets etc.
    logo_url = Column(String, nullable=True)

class Transaction(Base):
    """
    Record of successful/failed payments
    """
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    gateway_id = Column(UUID(as_uuid=True), ForeignKey("paymentgateway.id"))
    amount = Column(Float)
    currency = Column(String)
    status = Column(String) # 'pending', 'completed', 'failed'
    provider_transaction_id = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    metadata_json = Column(JSON, nullable=True)
