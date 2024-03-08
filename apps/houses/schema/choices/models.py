import strawberry
from enum import Enum


@strawberry.enum
class RegressorModel(Enum):
    RF = "RandomForestRegressor"
