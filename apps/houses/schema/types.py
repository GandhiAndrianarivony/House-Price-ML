import datetime
import strawberry

from .choices import (
    NeighborHood,
    MSZoning,
    LotShape,
    Condition,
    HouseStyle,
    Exterior,
    MasVnrType,
    Exter,
    Foundation,
    Bsmt,
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
    BsmtQual: Bsmt
    BsmtCond: Bsmt
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
    YearBuilt: datetime.date
    YearRemodAdd: datetime.date
    MasVnrArea: float
    BsmtFinSF1: float
    BsmtUnfSF: float
    TotalBsmtSF: float
    FlrSF1: float
    FlrSF2: float
    GrLivArea: float
    BsmtFullBath: float
    BsmtHalfBath: float
    FullBath: float
    BedroomAbvGr: float
    TotRmsAbvGrd: float
    Fireplaces: float
    GarageYrBlt: datetime.date
    GarageCars: float
    GarageArea: float
    WoodDeckSF: float
    OpenPorchSF: float
    EnclosedPorch: float

