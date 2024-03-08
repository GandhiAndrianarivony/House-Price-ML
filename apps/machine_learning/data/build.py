import joblib

import pandas as pd

from apps.houses.schema.types import HouseFeaturesInput


def create_inferenced_dataset(data_cfg, input: HouseFeaturesInput) -> pd.DataFrame:
    """Create inference dataset. Apply created transformation pipeline, etc"""

    model_name = input.to_dict()["model_name"].value
    categorical_encoder_pth = data_cfg["DATA_ENCODER"][model_name][
        "CATEGORICAL_ENCODER"
    ]
    encoder = joblib.load(categorical_encoder_pth)

    output = dict()
    data = input.to_dict()
    for k, v in input.to_dict().items():
        if k != "model_name":
            try:
                output[k] = v.value
            except:
                output[k] = v

    output = pd.DataFrame(output, index=[0])
    output = encoder.fit_transform(output)

    return output
