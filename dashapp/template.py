from dash import dcc, html, dash_table

def layout(data):
    """Put all HTML here
    """

    frontend = html.Div(
        children=[
            html.H1("Hello World"),
            html.Div(children=[
                dash_table.DataTable(
                    data.to_dict("records"),
                    [{"name": col, "id": col} for col in data.columns]
                )
                ])
        ]
    )
    return frontend