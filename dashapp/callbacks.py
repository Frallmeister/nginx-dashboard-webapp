from dash import dcc, Input, Output, html, dash_table
import pandas as pd
import plotly.express as px
from sqlalchemy import select


def register_callbacks(app, engine) -> None:
    """
    Put all callbacks here
    """

    @app.callback(
        Output("figure-div", "children"),
        Input("cut-dropdown", "value"),
    )
    def plot_carat_and_price(cut):
        if cut == "":
            return html.P("")
        else:
            data = pd.read_sql(
                f"SELECT carat, price FROM diamonds WHERE cut = '{cut}'",
                engine,
            )
            fig = px.scatter(data, x="carat", y="price")
            avg_price = round(data["price"].mean())
            fig.update_layout(
                title_text=f"Average price for {cut} cut diamonds: {avg_price}"
            )
            return dcc.Graph(figure=fig)

    
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
