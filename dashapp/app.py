import dash
from callbacks import register_callbacks
from template import layout

app = dash.Dash(
	__name__,
	url_base_pathname="/",
	suppress_callback_exceptions=True,
)
server = app.server

app.layout = layout()

if __name__ == "__main__":
	app.run_server(debug=True, host="0.0.0.0", port=8080)
