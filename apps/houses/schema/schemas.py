from .types import HouseFeaturesInput

import strawberry


@strawberry.type
class HouseMutation:
    @strawberry.mutation
    def predict_house_price(self, input: HouseFeaturesInput) -> float:
        return 2.5


@strawberry.type
class Query:
    @strawberry.field
    def house_price(self, info) -> str:
        return "Want to predict your house price?"
