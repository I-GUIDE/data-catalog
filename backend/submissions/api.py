import motor
from beanie import init_beanie
from fastapi import FastAPI
from submissions.routers import authentication

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
#app.add_middleware(SessionMiddleware, secret_key=get_settings().session_secret_key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router, prefix="/api")


@app.on_event("startup")
async def startup_db_client():
    #app.db = motor.motor_asyncio.AsyncIOMotorClient(get_settings().mongo_url)
    #await init_beanie(
    #    database=app.db[get_settings().mongo_database], document_models=[User, Submission, RepositoryToken]
    #)
    pass


@app.on_event("shutdown")
async def shutdown_db_client():
    pass
    #app.db.close()

