from typing import List, Optional, Any
from sqlalchemy.orm import Session
from app.models.payment import PaymentGateway, Transaction
from app.schemas.payment import PaymentGatewayCreate, PaymentGatewayUpdate, TransactionCreate

class CRUDPayment:
    def get_gateway(self, db: Session, id: Any) -> Optional[PaymentGateway]:
        return db.query(PaymentGateway).filter(PaymentGateway.id == id).first()

    def get_gateway_by_name(self, db: Session, name: str) -> Optional[PaymentGateway]:
        return db.query(PaymentGateway).filter(PaymentGateway.name == name).first()

    def get_active_gateways(self, db: Session) -> List[PaymentGateway]:
        return db.query(PaymentGateway).filter(PaymentGateway.is_active == True).all()

    def create_gateway(self, db: Session, *, obj_in: PaymentGatewayCreate) -> PaymentGateway:
        db_obj = PaymentGateway(
            name=obj_in.name,
            display_name=obj_in.display_name,
            is_active=obj_in.is_active,
            config=obj_in.config,
            logo_url=obj_in.logo_url
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_gateway(self, db: Session, *, db_obj: PaymentGateway, obj_in: PaymentGatewayUpdate) -> PaymentGateway:
        update_data = obj_in.model_dump(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_transaction(self, db: Session, *, obj_in: TransactionCreate) -> Transaction:
        db_obj = Transaction(
            user_id=obj_in.user_id,
            gateway_id=obj_in.gateway_id,
            amount=obj_in.amount,
            currency=obj_in.currency,
            status=obj_in.status,
            provider_transaction_id=obj_in.provider_transaction_id,
            metadata_json=obj_in.metadata_json
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

payment = CRUDPayment()
