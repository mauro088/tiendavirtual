
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from ..config.config import DB_NAME, DB_PASS, DB_USER, DB_HOST

engine = create_engine("mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" % (DB_USER, DB_PASS, DB_HOST, DB_NAME))

Base = declarative_base()

