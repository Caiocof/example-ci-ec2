from fastapi import APIRouter


app_router = APIRouter()


@app_router.get('/')
def main():
    """
    A route to say hello from API.
    """
    return {"hello": "Bank API"}