# app/main.py
from fastapi import FastAPI
from app.core.database import engine, Base
# 1. Add 'eligibility' here so the DB always creates the tables
from app.models import user, service, eligibility,application
from app.routers import auth
from app.routers import services
from app.routers import eligibility
from app.routers import applications
# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CIVIQ API",
    description="Backend for Government Services Portal",
    version="1.0.0"
)

# 2. Include all routers
app.include_router(auth.router)
app.include_router(services.router)
app.include_router(eligibility.router, tags=["Eligibility"])
app.include_router(applications.router, tags=["Applications"])

@app.get("/")
def read_root():
    return {"message": "Welcome to CIVIQ API", "status": "Running"}