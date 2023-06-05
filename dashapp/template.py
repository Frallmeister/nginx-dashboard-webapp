from dash import dcc, html
import pandas as pd

def get_cut_values(engine):
    data = pd.read_sql(
        "SELECT DISTINCT(cut) FROM diamonds",
        engine,
        )
    return data["cut"].to_list()


def layout(engine):
    """Put all HTML here
    """

    frontend = html.Div(
        children=[
            html.H1("Hello Diamonds"),
            dcc.Dropdown(
                options=get_cut_values(engine),
                value="",
                id="cut-dropdown",
                ),
            html.Div(id="figure-div"),
            html.Div(id="table-div"),
        ]
    )
    return frontend