import os

import strawberry
import environ

from .types import HouseFeaturesInput

from apps.machine_learning.modeling.build import build_model
from apps.machine_learning.engine.inference import inference
from apps.machine_learning.data.build import create_inferenced_dataset

from apps.houses.data.factory import Factory
from apps.houses.data.reader import Reader
from apps.houses.data.file_readers import YAMLReader


env = environ.Env()


@strawberry.type
class HouseMutation:
    @strawberry.mutation
    def predict_house_price(self, input: HouseFeaturesInput) -> str:
        """Predict user house price using input"""

        # Instantiate factory (view factory pattern)
        factory = Factory()
        # Register file Reader
        factory.register("yaml", YAMLReader)
        # Read file
        file_reader = Reader()
        model_cfg = file_reader.read_file(factory, "yaml", env("model_cfg_pth"))
        data_cfg = file_reader.read_file(factory, "yaml", env("data_cfg_pth"))

        # Load model
        model = build_model(model_cfg, input)

        # Create dataset which will be used for inference
        processed_data = create_inferenced_dataset(data_cfg, input)

        # Make prediction
        res = inference(model, processed_data)
        return f"Price: {res.item(): .2f} $"


@strawberry.type
class Query:
    @strawberry.field
    def house_price(self, info) -> str:
        return "Want to predict your house price?"
