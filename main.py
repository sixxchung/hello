# uvicorn app.main:app --reload  
import uvicorn
from fastapi import FastAPI

from dataclasses import asdict
from typing import Optional

#from app.common.config import conf
#from app.database.conn import db
from app.routes import index #auth

# app=FastAPI()

def create_app():
    app=FastAPI()
    # c=conf()
    # conf_dict = asdict(c)
    # db.init_app(app, **conf_dict)

    ###### Initialize Database
    ###### Initialize Redis
    ###### define Middleware
    ###### define Router  (/routes/xxx.py)
    app.include_router(index.router)
    #app.include_router(auth.router, tags=["Authentication"], prefix="/auth")
    return app

app = create_app()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id:int, q:Optional[str]=None):
#     return {"item_id": item_id, "q": q}

# uvicorn main:app --reload
if __name__ == "__main__" :
    #uvicorn.run("main:app",host="0.0.0.0", port=6666, reload=True) # reload=conf().PROJ_RELOAD)
    uvicorn.run("main:app", port=8888, reload=True) # reload=conf().PROJ_RELOAD)
