from api import routers
import uvicorn
import environ


env = environ.Env()

app = routers.app

if __name__ == "__main__":
    uvicorn.run("api.routers:app", host="0.0.0.0", port=int(env("API_PORT")), reload=True)
