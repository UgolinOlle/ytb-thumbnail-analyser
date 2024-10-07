from fastapi import FastAPI
from app.api.v1.thumbnail import endpoints as thumbnail_routes
from app.core.configs.database import db

# Create FastAPI app
app = FastAPI()


# Connect to the database when the app starts
@app.on_event("startup")
def startup():
    db.connect()
    db.Base.metadata.create_all(bind=db.engine)


# Disconnect from the database when the app shuts down
@app.on_event("shutdown")
def shutdown():
    db.disconnect()


# Include the routes for CRUD operations related to thumbnails
app.include_router(
    thumbnail_routes.router, prefix="/api/v1/thumbnail", tags=["Thumbnail"]
)
