import strawberry
from enum import Enum


@strawberry.enum
class NeighborHood(Enum):
    Blmngtn = "Bloomington Heights"
    Blueste = "Bluestem"
    BrDale = "Briardale"
    BrkSide = "Brookside"
    ClearCr = "Clear Creek"
    CollgCr = "College Creek"
    Crawfor = "Crawford"
    Edwards = "Edwards"
    Gilbert = "Gilbert"
    IDOTRR = "Iowa DOT and Rail Road"
    MeadowV = "Meadow Village"
    Mitchel = "Mitchell"
    Names = "North Ames"
    NoRidge = "Northridge"
    NPkVill = "Northpark Villa"
    NridgHt = "Northridge Heights"
    NWAmes = "Northwest Ames"
    OldTown = "Old Town"
    SWISU = "South & West of Iowa State University"
    Sawyer = "Sawyer"
    SawyerW = "Sawyer West"
    Somerst = "Somerset"
    StoneBr = "Stone Brook"
    Timber = "Timberland"
    Veenker = "Veenker"


@strawberry.enum
class MSZoning(Enum):
    """Identifies the general zoning classification of the sale."""

    A = "Agriculture"
    C = "Commercial"
    FV = "Floating Village Residential"
    I = "Industrial"
    RH = "Residential High Density"
    RL = "Residential Low Density"
    RP = "Residential Low Density Park "
    RM = "Residential Medium Density"


@strawberry.enum
class Street(Enum):
    """Type of road access to property"""

    Pave = "Paved"
    Grvl = "Gravel"


@strawberry.enum
class LotShape(Enum):
    """General shape of property"""

    Reg = "Regular"
    IR1 = "Slightly irregular"
    IR2 = "Moderately Irregular"
    IR3 = "Irregular"


@strawberry.enum
class LandContour(Enum):
    """Flatness of the property"""

    Lvl = "Near Flat/Level"
    Bnk = "Banked - Quick and significant rise from street grade to building"
    HLS = "Hillside - Significant slope from side to side"
    Low = "Depression"


@strawberry.enum
class Utility(Enum):
    """Type of utilities available"""

    AllPub = "All public Utilities (E,G,W,& S)"
    NoSewr = "Electricity, Gas, and Water (Septic Tank)"
    NoSeWa = "Electricity and Gas Only"
    ELO = "Electricity only"


@strawberry.enum
class LotConfig(Enum):
    """Lot configuration"""

    Inside = "Inside lot"
    Corner = "Corner lot"
    CulDSac = "Cul-de-sac"
    FR2 = "Frontage on 2 sides of property"
    FR3 = "Frontage on 3 sides of property"


@strawberry.enum
class LandSlope(Enum):
    """Slope of property"""

    Gtl = "Gentle slope"
    Mod = "Moderate Slope"
    Sev = "Severe Slope"


@strawberry.enum
class Condition(Enum):
    """Proximity to various conditions"""

    Artery = "Adjacent to arterial street"
    Feedr = "Adjacent to feeder street"
    Norm = "Normal"
    RRNn = "Within 200' of North-South Railroad"
    RRAn = "Adjacent to North-South Railroad"
    PosN = "Near positive off-site feature--park, greenbelt, etc."
    PosA = "Adjacent to postive off-site feature"
    RRNe = "Within 200' of East-West Railroad"
    RRAe = "Adjacent to East-West Railroad"


@strawberry.enum
class BldgType(Enum):
    """Type of dwelling"""

    Fam1 = "Single-family Detached"
    FmCon2 = "Two-family Conversion; originally built as one-family dwelling"
    Duplx = "Duplex"
    TwnhsE = "Townhouse End Unit"
    TwnhsI = "Townhouse Inside Unit"


@strawberry.enum
class HouseStyle(Enum):
    """Style of dwelling"""

    Story1 = "One story"
    Fin1_5 = "One and one-half story: 2nd level finished"
    Unf1_5 = "One and one-half story: 2nd level unfinished"
    Story2 = "Two story"
    Fin2_5 = "Two and one-half story: 2nd level finished"
    Unf2_5 = "Two and one-half story: 2nd level unfinished"
    SFoyer = "Split Foyer"
    SLvl = "Split Level"


@strawberry.enum
class RoofStyle(Enum):
    """Type of roof"""

    Flat = "Flat"
    Gable = "Gable"
    Gambrel = "Gabrel (Barn)"
    Hip = "Hip"
    Mansard = "Mansard"
    Shed = "Shed"


@strawberry.enum
class RoofMatl(Enum):
    """Roof Material"""

    ClyTile = "Clay or Tile"
    CompShg = "Standard (Composite) Shingle"
    Membran = "Membrane"
    Metal = "Metal"
    Roll = "Roll"
    TarAndGrv = "Gravel & Tar"
    WdShake = "Wood Shakes"
    WdShngl = "Wood Shingles"


@strawberry.enum
class Exterior(Enum):
    """Exterior covering on house"""

    AsbShng = "Asbestos Shingles"
    AsphShn = "Asphalt Shingles"
    BrkComm = "Brick Common"
    BrkFace = "Brick Face"
    CBlock = "Cinder Block"
    CemntBd = "Cement Board"
    HdBoard = "Hard Board"
    ImStucc = "Imitation Stucco"
    MetalSd = "Metal Siding"
    Other = "Other"
    Plywood = "Plywood"
    PreCast = "PreCast"
    Stone = "Stone"
    Stucco = "Stucco"
    VinylSd = "Vinyl Siding"
    Wd_Sdng = "Wood Siding"
    WdShing = "Wood Shingles"


@strawberry.enum
class MasVnrType(Enum):
    """Masonry veneer type"""

    BrkCmn = "Brick Common"
    BrkFace = "Brick Face"
    CBlock = "Cinder Block"
    none = "None"
    Stone = "Stone"


@strawberry.enum
class Exter(Enum):
    """Evaluates the quality of the material on the exterior"""

    Ex = "Excellent"
    Gd = "Good"
    TA = "Average/Typical"
    Fa = "Fair"
    Po = "Poor"


@strawberry.enum
class Foundation(Enum):
    """Type of foundation"""

    BrkTil = "Brick & Tile"
    CBlock = "Cinder Block"
    PConc = "Poured Contrete"
    Slab = "Slab"
    Stone = "Stone"
    Wood = "Wood"


@strawberry.enum
class Bsmt(Enum):
    """Evaluates the height of the basement"""

    Ex = "Excellent (100+ inches)"
    Gd = "Good (90-99 inches)"
    TA = "Typical (80-89 inches)"
    Fa = "Fair (70-79 inches)"
    Po = "Poor (<70 inches"
    NA = "No Basement"


@strawberry.enum
class BsmtExposure(Enum):
    """Refers to walkout or garden level walls"""

    Gd = "Good Exposure"
    Av = "Average Exposure (split levels or foyers typically score average or above)"
    Mn = "Mimimum Exposure"
    No = "No Exposure"
    NA = "No Basement"


@strawberry.enum
class BsmtFinType(Enum):
    """Rating of basement finished area"""

    GLQ = "Good Living Quarters"
    ALQ = "Average Living Quarters"
    BLQ = "Below Average Living Quarters"
    Rec = "Average Rec Room"
    LwQ = "Low Quality"
    Unf = "Unfinshed"
    NA = "No Basement"


@strawberry.enum
class Heating(Enum):
    """Type of Heating"""

    Floor = "Floor Furnace"
    GasA = "Gas forced warm air furnace"
    GasW = "Gas hot water or steam heat"
    Grav = "Gravity furnace"
    OthW = "Hot water or steam heat other than gas"
    Wall = "Wall furnace"


@strawberry.enum
class HeatingQC(Enum):
    """Heating quality and condition"""

    Ex = "Excellent"
    Gd = "Good"
    TA = "Average/Typical"
    Fa = "Fair"
    Po = "Poor"


@strawberry.enum
class CentralAir(Enum):
    """Central air conditioning"""

    N = "No"
    Y = "Yes"


@strawberry.enum
class Electrical(Enum):
    """Electrical system"""

    SBrkr = "Standard Circuit Breakers & Romex"
    FuseA = "Fuse Box over 60 AMP and all Romex wiring (Average)"
    FuseF = "60 AMP Fuse Box and mostly Romex wiring (Fair)"
    FuseP = "60 AMP Fuse Box and mostly knob & tube wiring (poor)"
    Mix = "Mixed"


@strawberry.enum
class KitchenQual(Enum):
    """Kitchen quality"""

    Ex = "Excellent"
    Gd = "Good"
    TA = "Typical/Average"
    Fa = "Fair"
    Po = "Poor"


@strawberry.enum
class Functional(Enum):
    """Home functionality (Assume typical unless deductions are warranted)"""

    Typ = "Typical Functionality"
    Min1 = "Minor Deductions 1"
    Min2 = "Minor Deductions 2"
    Mod = "Moderate Deductions"
    Maj1 = "Major Deductions 1"
    Maj2 = "Major Deductions 2"
    Sev = "Severely Damaged"
    Sal = "Salvage only"


@strawberry.enum
class GarageType(Enum):
    """Garage location"""

    Types2 = "More than one type of garage"
    Attchd = "Attached to home"
    Basment = "Basement Garage"
    BuiltIn = "Built-In (Garage part of house - typically has room above garage)"
    CarPort = "Car Port"
    Detchd = "Detached from home"
    NA = "No Garage"


@strawberry.enum
class GarageFinish(Enum):
    """Interior finish of the garage"""

    Fin = "Finished"
    RFn = "Rough Finished"
    Unf = "Unfinished"
    NA = "No Garage"


@strawberry.enum
class Garage(Enum):
    Ex = "Excellent"
    Gd = "Good"
    TA = "Typical/Average"
    Fa = "Fair"
    Po = "Poor"
    NA = "No Garage"


@strawberry.enum
class PavedDrive(Enum):
    """Paved driveway"""

    Y = "Paved "
    P = "Partial Pavement"
    N = "Dirt/Gravel"


@strawberry.enum
class SaleType(Enum):
    """Type of sale"""

    WD = "Warranty Deed - Conventional"
    CWD = "Warranty Deed - Cash"
    VWD = "Warranty Deed - VA Loan"
    New = "Home just constructed and sold"
    COD = "Court Officer Deed/Estate"
    Con = "Contract 15% Down payment regular terms"
    ConLw = "Contract Low Down payment and low interest"
    ConLI = "Contract Low Interest"
    ConLD = "Contract Low Down"
    Oth = "Other"


@strawberry.enum
class SaleCondition(Enum):
    Normal = "Normal Sale"
    Abnorml = "Abnormal Sale -  trade, foreclosure, short sale"
    AdjLand = "Adjoining Land Purchase"
    Alloca = "Allocation - two linked properties with separate deeds, typically condo with a garage unit"
    Family = "Sale between family members"
    Partial = "Home was not completed when last assessed (associated with New Homes)"

@strawberry.enum
class MonthNumber(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
