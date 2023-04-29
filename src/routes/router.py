from fastapi import FastAPI

from src.routes.app_router import app_router
from src.routes.account_router import account_router
from src.routes.customer_router import customer_router


def handle_requests(app_instance: FastAPI):
    app_instance.include_router(app_router)
    app_instance.include_router(account_router)
    app_instance.include_router(customer_router)
