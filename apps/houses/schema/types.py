import typing
import datetime

import strawberry

from .choices.models import RegressorModel

from .choices.fields import (
    NeighborHood,
    MSZoning,
    LotShape,
    Condition,
    HouseStyle,
    Exterior,
    MasVnrType,
    Exter,
    Foundation,
    BsmtQual,
    BsmtCond,
    BsmtExposure,
    BsmtFinType,
    HeatingQC,
    CentralAir,
    Electrical,
    KitchenQual,
    GarageType,
    GarageFinish,
    Garage,
    PavedDrive,
    SaleType,
    SaleCondition,
)


@strawberry.input
class HouseFeaturesInput:
    model_name: RegressorModel
    MSZoning: MSZoning
    LotShape: LotShape
    Neighborhood: NeighborHood
    Condition1: Condition
    HouseStyle: HouseStyle
    Exterior1st: Exterior
    Exterior2nd: Exterior
    MasVnrType: MasVnrType
    ExterQual: Exter
    Foundation: Foundation
    BsmtQual: BsmtQual
    BsmtCond: BsmtCond
    BsmtExposure: BsmtExposure
    BsmtFinType1: BsmtFinType
    HeatingQC: HeatingQC
    CentralAir: CentralAir
    Electrical: Electrical
    KitchenQual: KitchenQual
    GarageType: GarageType
    GarageFinish: GarageFinish
    GarageQual: Garage
    GarageCond: Garage
    PavedDrive: PavedDrive
    SaleType: SaleType
    SaleCondition: SaleCondition
    LotFrontage: float
    LotArea: float
    OverallQual: float
    YearBuilt: int
    YearRemodAdd: int
    MasVnrArea: float
    BsmtFinSF1: float
    BsmtUnfSF: float
    TotalBsmtSF: float
    GrLivArea: float
    BsmtFullBath: float
    HalfBath: float
    FullBath: float
    BedroomAbvGr: float
    TotRmsAbvGrd: float
    Fireplaces: float
    GarageYrBlt: int
    GarageCars: float
    GarageArea: float
    WoodDeckSF: float
    OpenPorchSF: float
    EnclosedPorch: float
    second_flr_SF: float
    first_flr_SF: float

    def to_dict(self) -> dict:
        # Initialize an empty dictionary to store the user input
        user_dict = {}

        # Iterate over the fields in the class
        for field_name in self.__annotations__:
            # Get the value of the field using getattr
            field_value = getattr(self, field_name)

            # Add the field and its value to the dictionary
            if field_value is not None:
                user_dict[field_name] = field_value

        return user_dict
