from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from api.routers.Operators import router as operator_router
from api.routers.Weapons import router as weapon_router
from api.routers.Attachments import router as attachment_router
from api.routers.Gadgets import router as gadgets_router
from api.routers.Utilities import router as utility_router
from api.routers.Maps import router as maps_router

all_routers = [operator_router, weapon_router, attachment_router, gadgets_router, utility_router, maps_router]


@asynccontextmanager
async def lifespan(app: FastAPI):
    #This is where populate went in Will's demo
    yield

app = FastAPI(
    title = "Siege API",
    description = "An API for Tom Clancy's Rainbow Six Siege",
    version = "0.1.0",
    lifespan = lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

for router in all_routers:
    app.include_router(router)