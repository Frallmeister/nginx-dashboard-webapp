from dash import dcc, html, dash_table
from sqlalchemy import select, distinct
from sqlalchemy.orm import Session
from models import Diamonds

def get_cut_values(Session):
    with Session() as session:
        stmt = select(distinct(Diamonds.cut))
        cuts = [cut for cut in session.scalars(stmt)]
    return cuts


def layout(Session, data):
    """Put all HTML here
    """

    frontend = html.Div(
        children=[
            html.H1("Hello Diamonds"),
            dcc.Dropdown(
                options=get_cut_values(Session),
                value="",
                id="cut-dropdown",
                ),
            html.Div(id="table-div"),
        ]
    )
    return frontend