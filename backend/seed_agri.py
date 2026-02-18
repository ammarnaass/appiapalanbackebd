import asyncio
from app.db.session import SessionLocal
from app import crud, schemas

async def seed_data():
    db = SessionLocal()
    
    print("Seeding initial data...")
    
    # Check if admin already exists
    admin_email = "admin@appiapalan.com"
    user = crud.user.get_by_email(db, email=admin_email)
    
    if not user:
        print(f"Creating default admin user: {admin_email}...")
        crud.user.create(db, obj_in=schemas.user.UserCreate(
            email=admin_email,
            password="adminpassword123",
            full_name="System Administrator",
            role="super_admin",
            is_active=True,
            is_superuser=True
        ))
    
    # Check if plants already exist
    if crud.plant.get_multi(db, limit=1):
        print("Plants already seeded.")
        db.close()
        return

    print("Seeding plants and diseases...")
    
    # 1. Tomato
    tomato = crud.plant.create(db, obj_in=schemas.plant_disease.PlantCreate(
        name_ar="طماطم",
        name_en="Tomato",
        scientific_name="Solanum lycopersicum"
    ))
    
    crud.disease.create(db, obj_in=schemas.plant_disease.DiseaseCreate(
        plant_id=tomato.id,
        name_ar="اللفحة المتأخرة",
        name_en="Tomato___Late_blight",
        description_ar="مرض فطرى يصيب الأوراق والسيقان وينتقل بسرعة في الرطوبة العالية.",
        symptoms_ar="بقع مائية داكنة على الأوراق تتحول للون البني.",
        treatment_ar="استخدام مبيدات فطرية نحاسية والتخلص من الأوراق المصابة.",
        is_common=True
    ))

    # 2. Potato
    potato = crud.plant.create(db, obj_in=schemas.plant_disease.PlantCreate(
        name_ar="بطاطس",
        name_en="Potato",
        scientific_name="Solanum tuberosum"
    ))

    crud.disease.create(db, obj_in=schemas.plant_disease.DiseaseCreate(
        plant_id=potato.id,
        name_ar="اللفحة المبكرة",
        name_en="Potato___Early_blight",
        description_ar="مرض فطري يظهر في صورة دوائر متداخلة على الأوراق السفلى.",
        symptoms_ar="بقع بنية جافة دائرية تشبه لوحة التصويب.",
        treatment_ar="التهوية الجيدة بمسافات الزراعة واستخدام مبيدات فطرية وقائية.",
        is_common=True
    ))

    # 3. Pepper
    pepper = crud.plant.create(db, obj_in=schemas.plant_disease.PlantCreate(
        name_ar="فلفل",
        name_en="Pepper",
        scientific_name="Capsicum annuum"
    ))

    print("Seeding completed successfully.")
    db.close()

if __name__ == "__main__":
    asyncio.run(seed_data())
