import asyncio
from app.db.session import SessionLocal
from app import crud, schemas

async def seed_system_data():
    db = SessionLocal()
    
    print("Seeding system and monetization data...")
    
    # 1. Monetization System
    monetization_key = "monetization_settings"
    m_type = crud.content_type.get_by_key(db, key=monetization_key)
    if not m_type:
        print(f"Creating content type: {monetization_key}...")
        m_type = crud.content_type.create(db, obj_in=schemas.content.ContentTypeCreate(
            key=monetization_key,
            schema={
                "type": "object",
                "properties": {
                    "free_scans_per_day": {"type": "number"},
                    "premium_price_monthly": {"type": "number"},
                    "currency": {"type": "string"},
                    "features": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                }
            }
        ))
    
    # Add Monetization Content
    m_content = crud.content.get_multi_by_type(db, type_key=monetization_key, limit=1)
    if not m_content:
        print("Adding monetization settings content...")
        crud.content.create(db, obj_in=schemas.content.ContentCreate(
            title="Monetization Configuration",
            type_key=monetization_key,
            data={
                "free_scans_per_day": 3,
                "premium_price_monthly": 4.99,
                "currency": "USD",
                "features": ["Unlimited Scans", "AI Expert Support", "Offline Access"]
            },
            is_published=True
        ))

    # 2. System General Config
    sys_key = "system_config"
    s_type = crud.content_type.get_by_key(db, key=sys_key)
    if not s_type:
        print(f"Creating content type: {sys_key}...")
        s_type = crud.content_type.create(db, obj_in=schemas.content.ContentTypeCreate(
            key=sys_key,
            schema={
                "type": "object",
                "properties": {
                    "app_version": {"type": "string"},
                    "maintenance_mode": {"type": "boolean"},
                    "contact_email": {"type": "string"}
                }
            }
        ))
    
    # Add System Config Content
    s_content = crud.content.get_multi_by_type(db, type_key=sys_key, limit=1)
    if not s_content:
        print("Adding system configuration content...")
        crud.content.create(db, obj_in=schemas.content.ContentCreate(
            title="Global System Config",
            type_key=sys_key,
            data={
                "app_version": "0.1.0",
                "maintenance_mode": False,
                "contact_email": "support@appiapalan.com"
            },
            is_published=True
        ))

    print("System data seeding completed successfully.")
    db.close()

if __name__ == "__main__":
    asyncio.run(seed_system_data())
