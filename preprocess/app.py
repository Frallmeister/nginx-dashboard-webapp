import time
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Titanic, Base

user = "root"
with open("/run/secrets/db-password") as fp:
    passwd = fp.read()
host = "database"
dbname = "example"

engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{dbname}?charset=utf8mb4")

Base.metadata.create_all(engine)

while True:
    time.sleep(5)