import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
	html.Div([
		html.Label('Hello, what do you like to do in your free time?')],
		style={
			'display': 'block', 'fontSize': '1.6rem', 'marginBottom': '1rem'
		}
	),
	dcc.Dropdown(
		id="hobby-dropdown",
		options=[
			{'label': 'Choose:', 'value': ''},
			{'label': 'Read books', 'value': 'read'},
			{'label': 'Bake cakes', 'value': 'bake'},
			{'label': 'Solve trigonometrical problems', 'value': 'trigonometry'},
			{'label': "Work in the Granny's garden", 'value': 'garden'},
		],
		value='',
		style={ 'maxWidth': '400px'}
	),
	dcc.Graph(
		id='hobby-plot',
		animate=True
	),
])

@app.callback(
	Output('hobby-plot', 'figure'),
	[Input('hobby-dropdown', 'value')]
)

def update_figure(value):
	if value == 'garden':
		return {
			'data': [
				go.Bar(x=[1], y=[5], name="Read books"),
				go.Bar(x=[1], y=[4], name="Bake cakes"),
				go.Bar(x=[1], y=[7], name="Solve trigonometrical problems"),
				go.Bar(x=[1], y=[4], name="Work in the Granny's garden")
			],
			'layout': {
				'title': 'What other users choose'
			}
		}
	elif value == 'read':
		return {
			'data': [
				go.Bar(x=[1], y=[6], name="Read books"),
				go.Bar(x=[1], y=[4], name="Bake cakes"),
				go.Bar(x=[1], y=[7], name="Solve trigonometrical problems"),
				go.Bar(x=[1], y=[3], name="Work in the Granny's garden")
			],
			'layout': {
				'title': 'What other users choose'
			}
		}
	elif value == 'bake':
		return {
			'data': [
				go.Bar(x=[1], y=[5], name="Read books"),
				go.Bar(x=[1], y=[5], name="Bake cakes"),
				go.Bar(x=[1], y=[7], name="Solve trigonometrical problems"),
				go.Bar(x=[1], y=[3], name="Work in the Granny's garden")
			],
			'layout': {
				'title': 'What other users choose'
			}
		}
	elif value == 'trigonometry':
		return {
			'data': [
				go.Bar(x=[1], y=[5], name="Read books"),
				go.Bar(x=[1], y=[4], name="Bake cakes"),
				go.Bar(x=[1], y=[8], name="Solve trigonometrical problems"),
				go.Bar(x=[1], y=[3], name="Work in the Granny's garden")
			],
			'layout': {
				'title': 'What other users choose'
			}
		}
	else:
		return {
			'data': [
				go.Bar(x=[1], y=[5], name="Read books"),
				go.Bar(x=[1], y=[4], name="Bake cakes"),
				go.Bar(x=[1], y=[7], name="Solve trigonometrical problems"),
				go.Bar(x=[1], y=[3], name="Work in the Granny's garden")
			],
			'layout': {
				'title': 'What other users choose'
			}
		}

if __name__ == '__main__':
	app.run_server(debug=True)
