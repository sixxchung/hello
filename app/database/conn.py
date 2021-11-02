from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session 

user_name = 'enduser'
user_pwd  = '1234'
db_host   = 'localhost' #"172.17.0.1" #"127.0.0.1"
db_name   = 'edudb'

DATABASE = "mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" %(
    user_name, 
    user_pwd,
    db_host,
    db_name
)
#DATABASE = "mysql+pymysql://enduser:1234@localhost/edudb?charset=utf8mb4"


ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False, 
        autoflush=False,
        bind = ENGINE
    )
)
# create instance
Base = declarative_base()
Base.query = session.query_property()


