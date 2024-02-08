from fastapi import APIRouter

from . import schemas, repositories

router = APIRouter(
    tags=['AIML']
)

@router.post("/predict/")
def predict(request: schemas.HouseData):
    return repositories.predict(request)