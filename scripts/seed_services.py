# scripts/seed_services.py
import sys
import os

# Add the project root to Python path so we can import 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.models.service import Service

# Initialize DB (Just in case)
Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()

    # Real data extracted from your design PDF
    services_list = [
        # 1. Travel Services [cite: 872-884]
        Service(
            name="Passport Renewal",
            category="Travel",
            description="Official application to renew an existing adult passport.",
            fee=130.00,
            fee_currency="USD",
            processing_time="6-8 Weeks",
            icon_url="https://img.icons8.com/color/48/passport.png"
        ),
        
        # 2. Transport Services [cite: 301-310]
        Service(
            name="Vehicle Registration Renewal",
            category="Transport",
            description="Renew your vehicle registration online before expiration.",
            fee=50.00,  # Starting fee
            fee_currency="USD",
            processing_time="1-2 Weeks",
            icon_url="https://img.icons8.com/color/48/fiat-500.png"
        ),
        
        # 3. Business Services [cite: 2-9]
        Service(
            name="Small Business Grant",
            category="Business",
            description="Apply for grants to start or expand your small business.",
            fee=0.00,
            fee_currency="USD",
            processing_time="6-8 Weeks",
            icon_url="https://img.icons8.com/color/48/small-business.png"
        ),
        
        # 4. Housing Services [cite: 1632-1641]
        Service(
            name="Property Tax Payment",
            category="Housing",
            description="Pay your annual property taxes online or view payment history.",
            fee=0.00, # Varies by property, base is 0
            fee_currency="USD",
            processing_time="Instant",
            icon_url="https://img.icons8.com/color/48/home.png"
        ),

        # 5. Legal Services [cite: 680-687]
        Service(
            name="Birth Certificate Request",
            category="Legal",
            description="Request certified copy of birth certificate.",
            fee=25.00,
            fee_currency="USD",
            processing_time="2-4 Weeks",
            icon_url="https://img.icons8.com/color/48/birth-date.png"
        )
    ]

    print("🌱 Seeding Services...")
    for service in services_list:
        # Check if it exists first to avoid duplicates
        exists = db.query(Service).filter(Service.name == service.name).first()
        if not exists:
            db.add(service)
            print(f"   Added: {service.name}")
        else:
            print(f"   Skipped (Already exists): {service.name}")

    db.commit()
    db.close()
    print("✅ Database seeding complete!")

if __name__ == "__main__":
    seed_data()