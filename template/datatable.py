import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.pkg_ui import *
from common.config import dt_style

from dash import dash_table as dt
from dash import Dash, Input, Output, callback


#df = pd.read_csv('https://git.io/Juf1t')
import random


from collections import OrderedDict
data ='https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv' 
df = pd.read_csv(data)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(children=[
    dbc.Label('gapminder: 국가별 경제/의료 수준 DataSet (rm year)'),
    html.Div(id='datatable-interactivity-container'),
    dt.DataTable(id='tbl',
        columns=[{"id":i, "name":i} for i in df.columns],
        data=df.to_dict('records'),
        # editable=False,
        filter_action="native",

        sort_action="native",
        sort_mode="multi",

        column_selectable="single",
        selected_columns=[],

        row_selectable="multi",
        selected_rows=[],

        page_action="native",
        page_size=10,
        **dt_style   
    ),

])

@app.callback(
    Output('tbl', 'style_data_conditional'),
    Input('tbl', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


@app.callback(
    Output('datatable-interactivity-container', "children"),
    Input('tbl', "derived_virtual_data"),
    Input('tbl', "derived_virtual_selected_rows"))
def update_graphs(rows, derived_virtual_selected_rows):
    dff = df if rows is None else pd.DataFrame(rows)
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    colors = ['lightskyblue' if i in derived_virtual_selected_rows else 'royalblue'
              for i in range(len(dff))]
    return [
        dcc.Graph(id=column,
            figure={
                "data": [
                    {
                        "x": dff["country"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
        for column in ["pop", "lifeExp", "gdpPercap"] if column in dff
    ]



if __name__ == '__main__':
    app.run_server(debug=True)