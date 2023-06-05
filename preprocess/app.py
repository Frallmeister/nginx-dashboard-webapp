import time
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Diamonds, Base

user = "root"
with open("/run/secrets/db-password") as fp:
    passwd = fp.read()
host = "database"
dbname = "example"

engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{dbname}?charset=utf8mb4")

Base.metadata.create_all(engine)

while True:
    raw_data = pd.read_csv("/data/raw_data.csv")
    raw_data.drop("Unnamed: 0", axis=1, inplace=True)
    # records = raw_data.to_dict("records")

    stored = pd.read_sql(
        "SELECT * FROM diamonds",
        engine
    )
    stored.drop("id_", axis=1, inplace=True)

    raw_data = pd.concat([raw_data, stored]).drop_duplicates()
    records = raw_data.to_dict("records")

    # Delete all records
    with Session(engine) as session:
        stmt = select(Diamonds)
        for row in session.scalars(stmt):
            session.delete(row)
        session.commit()

    # Add new records
    with Session(engine) as session:
        for record in records:
            session.add(Diamonds(**record))
        session.commit()
    time.sleep(10)
