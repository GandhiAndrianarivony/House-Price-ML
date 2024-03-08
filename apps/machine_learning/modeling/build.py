import joblib

from apps.houses.schema.types import HouseFeaturesInput


def build_model(model_cfg, input: HouseFeaturesInput):
    """Build model from saved model"""

    model_name = input.to_dict()["model_name"].value
    model_weight = model_cfg.get("MODEL")[model_name]["weight"]
    loaded_model = joblib.load(model_weight)

    return loaded_model
