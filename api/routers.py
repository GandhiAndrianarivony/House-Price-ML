from fastapi import FastAPI

from apps.ml_models import urls

app = FastAPI()


app.include_router(urls.router)