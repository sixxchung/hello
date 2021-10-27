# uvicorn main:app --reload  
import uvicorn
from fastapi import FastAPI

#from app.common.config import conf
#from app.database.conn import db
from app.routes import index #auth

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
    app.include_router(index.router)
    
    return app

app = create_app()

# uvicorn main:app --reload
if __name__ == "__main__" :
    uvicorn.run("main:app", port=8888, reload=True) # reload=conf().PROJ_RELOAD)
