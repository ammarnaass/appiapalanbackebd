from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/gateways", response_model=List[schemas.payment.PaymentGateway])
def read_gateways(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve active payment gateways.
    """
    return crud.payment.get_active_gateways(db)

@router.get("/gateways/manage", response_model=List[schemas.payment.PaymentGateway])
def manage_gateways(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all payment gateways for internal management. (Superuser only)
    """
    return db.query(models.payment.PaymentGateway).all()

@router.post("/gateways", response_model=schemas.payment.PaymentGateway)
def create_gateway(
    *,
    db: Session = Depends(deps.get_db),
    gateway_in: schemas.payment.PaymentGatewayCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new payment gateway. (Superuser only)
    """
    gateway = crud.payment.get_gateway_by_name(db, name=gateway_in.name)
    if gateway:
        raise HTTPException(status_code=400, detail="Gateway already exists")
    return crud.payment.create_gateway(db, obj_in=gateway_in)

@router.put("/gateways/{gateway_id}", response_model=schemas.payment.PaymentGateway)
def update_gateway(
    *,
    db: Session = Depends(deps.get_db),
    gateway_id: str,
    gateway_in: schemas.payment.PaymentGatewayUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a payment gateway. (Superuser only)
    """
    gateway = crud.payment.get_gateway(db, id=gateway_id)
    if not gateway:
        raise HTTPException(status_code=404, detail="Gateway not found")
    return crud.payment.update_gateway(db, db_obj=gateway, obj_in=gateway_in)

@router.post("/currency", response_model=schemas.user.User)
def set_preferred_currency(
    *,
    db: Session = Depends(deps.get_db),
    currency: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Set preferred currency for the current user.
    """
    current_user.preferred_currency = currency
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
