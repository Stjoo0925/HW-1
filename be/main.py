from fastapi import FastAPI
from cors import setup_cors
from counter import router as counter_router

app = FastAPI()

setup_cors(app)

app.include_router(counter_router)