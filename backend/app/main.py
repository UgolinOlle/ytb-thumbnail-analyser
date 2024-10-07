from fastapi import FastAPI
from app.api.v1.thumbnail import endpoints as thumbnail_routes
from app.core.configs.database import db

# --- Create FastAPI app
app = FastAPI()


@app.on_event("startup")
def startup():
    """
    Handler for the 'startup' event.
    This function is executed when the FastAPI application starts.
    It connects to the database and creates all database tables defined by the models.
    """
    db.connect()
    db.Base.metadata.create_all(bind=db.engine)


@app.on_event("shutdown")
def shutdown():
    """
    Handler for the 'shutdown' event.
    This function is executed when the FastAPI application shuts down.
    It disconnects from the database.
    """
    db.disconnect()


# --- Routers
app.include_router(
    thumbnail_routes.router, prefix="/api/v1/thumbnail", tags=["Thumbnail"]
)
