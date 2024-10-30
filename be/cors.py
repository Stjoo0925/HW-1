from fastapi.middleware.cors import CORSMiddleware
import os

allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )