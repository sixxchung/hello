# uvicorn main:app --reload  
import uvicorn
from fastapi import FastAPI

#from app.common.config import conf
#from app.database.conn import db
from app.routes import userAPI #auth

def create_app():
    app=FastAPI()
    app.include_router(userAPI.router)
    
    return app

app = create_app()

from starlette.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# uvicorn main:app --reload
if __name__ == "__main__" :
    uvicorn.run("main:app", port=8888, reload=True) # reload=conf().PROJ_RELOAD)
