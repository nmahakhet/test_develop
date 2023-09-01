from fastapi import FastAPI
from app.core.config import settings
from app.routes.route import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routers
app.include_router(api_router, prefix=settings.API_PATH_STR)