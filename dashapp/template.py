from dash import dcc, html

def layout():
    """Put all HTML here
    """

    frontend = html.Div(
        children=[
            html.H1("Hello World"),
        ]
    )
    return frontend