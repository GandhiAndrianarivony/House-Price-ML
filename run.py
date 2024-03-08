from api import routers
import uvicorn
import environ

# Prior import
from apps.machine_learning.data.transforms.transforms import (
    Imputer,
    LogTransformer,
    CategoricalMapper   
)

env = environ.Env()

app = routers.app

if __name__ == "__main__":
    uvicorn.run(
        "api.routers:app", host="0.0.0.0", port=int(env("DOCKER_HOST_PORT")), reload=True
    )
