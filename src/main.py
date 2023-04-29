from fastapi import FastAPI

from src.routes.router import handle_requests

app = FastAPI()
handle_requests(app)
