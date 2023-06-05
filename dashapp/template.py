from dash import dcc, html

def layout(data):
    """Put all HTML here
    """

    frontend = html.Div(
        children=[
            html.H1("Hello World"),
            html.P(data.to_string())
        ]
    )
    return frontend