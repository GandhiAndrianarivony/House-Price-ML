from api import routers
import uvicorn

app = routers.app

if __name__ == "__main__":
    uvicorn.run(routers.app, host="localhost", port=9000)
