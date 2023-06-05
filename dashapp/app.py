import dash
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Diamonds, Base
from callbacks import register_callbacks
from template import layout

app = dash.Dash(
	__name__,
	url_base_pathname="/",
	suppress_callback_exceptions=True,
)
server = app.server

user = "root"
with open("/run/secrets/db-password") as fp:
    passwd = fp.read()
host = "database"
dbname = "example"
engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{dbname}?charset=utf8mb4")
Session = sessionmaker(engine)

data = pd.read_sql("SELECT * FROM diamonds", engine)

app.layout = layout(Session, data)
register_callbacks(app, engine)

if __name__ == "__main__":
	app.run_server(debug=True, host="0.0.0.0", port=8080)
