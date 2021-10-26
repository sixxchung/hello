# uvicorn main:app --reload  
import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel

#from app.common.config import conf
#from app.database.conn import db
from app.routes import index #auth

from dataclasses import asdict
from typing import Optional
# app=FastAPI()
import requests
from starlette.requests import Request
from starlette.responses import JSONResponse

db = []

class City(BaseModel):
    name:str
    timezone:str


def create_app():
    app=FastAPI()
    # c=conf()
    # conf_dict = asdict(c)
    # db.init_app(app, **conf_dict)

    ###### Initialize Database 
    ###### Initialize Redis
    ###### define Middleware
    ###### define Router  (/routes/xxx.py)
    #app.include_router(index.router)
    #app.include_router(auth.router, tags=["Authentication"], prefix="/auth")

    @app.get("/")
    async def root():
        return {"hello":"world"}  
    
    
    @app.post("/cities")
    async def create_city(city: City):
        """
        `Create City`
        :return last record:
        """
        db.append(city.dict())
        print(city.dict())
        return db[-1]
    
    @app.get("/cities")
    def get_cities():
        results = []
        for city in db:
            print(city)
            strs = "http://worldtimeapi.org/api/timezone/Asia/Seoul"
            r = Request.get(strs)
            cur_time = r.json()['datetime']
            results.append
        return results

    # @app.get("/cities/{city_id}")
    # async def get_city(city_id:int):
    #     return result 



    # @app.get("/cities/{city_id}")
    # async def delete_city(city_id:int):
    #     return {"hello":"world"} 

  

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
