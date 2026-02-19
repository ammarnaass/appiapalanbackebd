from typing import Optional, Any, List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

# Payment Gateway Schemas
class PaymentGatewayBase(BaseModel):
    name: str
    display_name: str
    is_active: bool = True
    config: dict = {}
    logo_url: Optional[str] = None

class PaymentGatewayCreate(PaymentGatewayBase):
    pass

class PaymentGatewayUpdate(BaseModel):
    display_name: Optional[str] = None
    is_active: Optional[bool] = None
    config: Optional[dict] = None
    logo_url: Optional[str] = None

class PaymentGateway(PaymentGatewayBase):
    id: UUID

    class Config:
        from_attributes = True

# Transaction Schemas
class TransactionBase(BaseModel):
    amount: float
    currency: str
    status: str
    provider_transaction_id: str
    metadata_json: Optional[dict] = None

class TransactionCreate(TransactionBase):
    gateway_id: UUID
    user_id: UUID

class Transaction(TransactionBase):
    id: UUID
    gateway_id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
