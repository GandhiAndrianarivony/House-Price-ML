import strawberry
from enum import Enum


@strawberry.enum
class NeighborHood(Enum):
    bloomington_heights = "Blmngtn"
    bluestem = "Blueste"
    briardale = "BrDale"
    brookside = "BrkSide"
    clear_creek = "ClearCr"
    college_creek = "CollgCr"
    crawford = "Crawfor"
    edwards = "Edwards"
    Gilbert = "Gilbert"
    iowa_dot_and_rail_road = "IDOTRR"
    meadow_village = "MeadowV"
    mitchell = "Mitchel"
    north_ames = "NAmes"
    northridge = "NoRidge"
    northpark_villa = "NPkVill"
    northridge_weights = "NridgHt"
    northwest_ames = "NWAmes"
    old_town = "OldTown"
    south_and_west_of_iowa_state_university = "SWISU"
    sawyer = "Sawyer"
    sawyer_est = "SawyerW"
    somerset = "Somerst"
    stone_brook = "StoneBr"
    Timberland = "Timber"
    Veenker = "Veenker"


@strawberry.enum
class MSZoning(Enum):
    """Identifies the general zoning classification of the sale."""

    commercial = "C (all)"
    floating_village_residential = "FV"
    residential_high_density = "RH"
    residential_low_density = "RL"
    residential_medium_density = "RM"


@strawberry.enum
class LotShape(Enum):
    """General shape of property"""

    regular = "Reg"
    slightly_irregular = "IR1"
    moderately_irregular = "IR2"
    irregular = "IR3"


@strawberry.enum
class Condition(Enum):
    """Proximity to various conditions"""

    adjacent_to_arterial_street = "Artery"
    adjacent_to_feeder_street = "Feedr"
    normal = "Norm"
    within_200_of_north_south_railroad = "RRNn"
    Adjacent_to_North_South_Railroad = "RRAn"
    Near_positive_off_site_feature_park_greenbelt = "PosN"
    Adjacent_to_postive_off_site_feature = "PosA"
    Within_200_of_East_West_Railroad = "RRNe"
    Adjacent_to_East_West_Railroad = "RRAe"


@strawberry.enum
class HouseStyle(Enum):
    """Style of dwelling"""

    One_story = "1Story"
    One_and_one_half_story__2nd_level_finished = "1.5Fin"
    One_and_one_half_story__2nd_level_unfinished = "1.5Unf"
    Two_story = "2Story"
    Two_and_one_half_story__2nd_level_finished = "2.5Fin"
    Two_and_one_half_story__2nd_level_unfinished = "2.5Unf"
    Split_Foyer = "SFoyer"
    Split_Level = "SLvl"


@strawberry.enum
class MasVnrType(Enum):
    """Masonry veneer type"""

    Brick_Common = "BrkCmn"
    Brick_Face = "BrkFace"
    Cinder_Block = "None"
    none = "MISSING"
    Stone = "Stone"


@strawberry.enum
class Exter(Enum):
    """Evaluates the quality of the material on the exterior"""

    Excellent = "Ex"
    Good = "Gd"
    Average_or_Typical = "TA"
    Fair = "Fa"
    # Poor = "Po"


@strawberry.enum
class Foundation(Enum):
    """Type of foundation"""

    Brick_and_Tile = "BrkTil"
    Cinder_Block = "CBlock"
    Poured_Contrete = "PConc"
    Slab = "Slab"
    Stone = "Stone"
    Wood = "Wood"


@strawberry.enum
class BsmtCond(Enum):
    """Evaluates the height of the basement"""

    Excellent_100_inches = "Ex"
    Good_90_to_99_inches = "Gd"
    Typical_80_to_89_inches = "TA"
    Fair_70_79_inches = "Fa"
    # Poor_lt_70_inches = "Po"
    No_Basement = "MISSING"


@strawberry.enum
class BsmtQual(Enum):
    """Evaluates the height of the basement"""

    Excellent_100_inches = "Ex"
    Good_90_to_99_inches = "Gd"
    Typical_80_to_89_inches = "TA"
    Fair_70_79_inches = "Fa"
    Poor_lt_70_inches = "Po"
    No_Basement = "MISSING"


@strawberry.enum
class BsmtExposure(Enum):
    """Refers to walkout or garden level walls"""

    Good_Exposure = "Gd"
    Average_Exposure_split_levels_or_foyers_typically_score_average_or_above = "Av"
    Mimimum_Exposure = "Mn"
    No_Exposure = "No"
    No_Basement = "MISSING"


@strawberry.enum
class BsmtFinType(Enum):
    """Rating of basement finished area"""

    Good_Living_Quarters = "GLQ"
    Average_Living_Quarters = "ALQ"
    Below_Average_Living_Quarters = "BLQ"
    Average_Rec_Room = "Rec"
    Low_Quality = "LwQ"
    Unfinshed = "Unf"
    No_Basement = "MISSING"


@strawberry.enum
class HeatingQC(Enum):
    """Heating quality and condition"""

    Excellent = "Ex"
    Good = "Gd"
    Average_or_Typical = "TA"
    Fair = "Fa"
    Poor = "Po"


@strawberry.enum
class CentralAir(Enum):
    """Central air conditioning"""

    No = "N"
    Yes = "Y"


@strawberry.enum
class Electrical(Enum):
    """Electrical system"""

    Standard_Circuit_Breakers_and_Romex = "SBrkr"
    Fuse_Box_over_60_AMP_and_all_Romex_wiring__Average = "FuseA"
    AMP_60_Fuse_Box_and_mostly_Romex_wiring_Fair = "FuseF"
    AMP_60_Fuse_Box_and_mostly_knob_and_tube_wiring_poor = "FuseP"
    Mixed = "Mix"


@strawberry.enum
class KitchenQual(Enum):
    """Kitchen quality"""

    Excellent = "Ex"
    Good = "Gd"
    Typical_or_Average = "TA"
    Fair = "Fa"


@strawberry.enum
class GarageType(Enum):
    """Garage location"""

    More_than_one_type_of_garage = "Types2"
    Attached_to_home = "Attchd"
    Basement_Garage = "Basment"
    Built_In_Garage_part_of_house___typically_has_room_above_garage = "BuiltIn"
    Car_Port = "CarPort"
    Detached_from_home = "Detchd"
    No_Garage = "MISSING"


@strawberry.enum
class GarageFinish(Enum):
    """Interior finish of the garage"""

    Finished = "Fin"
    Rough_Finished = "RFn"
    Unfinished = "Unf"
    No_Garage = "MISSING"


@strawberry.enum
class Garage(Enum):
    Excellent = "Ex"
    Good = "Gd"
    Typical_or_Average = "TA"
    Fair = "Fa"
    Poor = "Po"
    No_Garage = "MISSING"


@strawberry.enum
class PavedDrive(Enum):
    """Paved driveway"""

    Paved = "Y"
    Partial_Pavement = "P"
    Dirt_gravel = "N"


@strawberry.enum
class SaleType(Enum):
    """Type of sale"""

    Warranty_Deed___Conventional = "WD"
    Warranty_Deed_Cash = "CWD"
    Home_just_constructed_and_sold = "New"
    Court_Officer_Deed_or_Estate = "COD"
    Contract_15pct_Down_payment_regular_terms = "Con"
    Contract_Low_Down_payment_and_low_interest = "ConLw"
    Contract_Low_Interest = "ConLI"
    Contract_Low_Down = "ConLD"
    Other = "Oth"


@strawberry.enum
class SaleCondition(Enum):
    Normal_Sale = "Normal"
    Abnormal_Sale__trade_foreclosure_short_sale = "Abnorml"
    Adjoining_Land_Purchase = "AdjLand"
    Allocation_two_linked_properties_with_separate_deeds_typically_condo_with_a_garage_unit = "Alloca"
    Sale_between_family_members = "Family"
    Home_was_not_completed_when_last_assessed_associated_with_New_Homes = "Partial"


@strawberry.enum
class Exterior(Enum):
    """Exterior covering on house"""

    Asbestos_Shingles = "AsbShng"
    Asphalt_Shingles = "AsphShn"
    Brick_Common = "BrkComm"
    Brick_Face = "BrkFace"
    Cinder_Block = "CBlock"
    Cement_Board = "CemntBd"
    Hard_Board = "HdBoard"
    Imitation_Stucco = "ImStucc"
    Metal_Siding = "MetalSd"
    Plywood = "Plywood"
    Stone = "Stone"
    Stucco = "Stucco"
    Vinyl_Siding = "VinylSd"
    Wood_Siding = "Wd_Sdng"
    Wood_Shingles = "WdShing"
