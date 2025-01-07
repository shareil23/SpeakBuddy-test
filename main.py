from fastapi import FastAPI
from controller.api import routers

app = FastAPI()

# register route from controllers
for router in routers:
    app.include_router(router)
