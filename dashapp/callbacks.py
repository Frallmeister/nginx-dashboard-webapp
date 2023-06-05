from dash import Input, Output, html, dash_table
import pandas as pd
from sqlalchemy import select


def register_callbacks(app, engine) -> None:
    """
    Put all callbacks here
    """
    
    @app.callback(
        Output("table-div", "children"),
        Input("cut-dropdown", "value")
    )
    def create_table(cut):
        if cut == "":
            return html.P("Select a diamond cut")
        else:
            data = pd.read_sql(
                f"SELECT * FROM diamonds where cut = '{cut}'",
                engine,
            )
            data.drop("id_", axis=1, inplace=True)
            return dash_table.DataTable(
                data.to_dict("records"),
                [{"name": col.capitalize(), "id": col} for col in data.columns],
            )
