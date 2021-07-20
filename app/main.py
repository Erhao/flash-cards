import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db.mongo_util import connect_to_mongo, close_mongo_connection
from app.core.config import API_PREFIX_V1
from app.router.card import router as card_router
from app.router.user import router as user_router


app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(card_router, prefix=API_PREFIX_V1)
app.include_router(user_router, prefix=API_PREFIX_V1)
