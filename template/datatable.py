import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.pkg_ui import *

from dash import dash_table as dt
from dash import Dash, Input, Output, callback

#df = pd.read_csv('https://git.io/Juf1t')
import random
n = random.random()
print(n)



from collections import OrderedDict
df = pd.DataFrame(OrderedDict(
    [
        [
            'Column {}'.format(i + 1), [(random.randint(1,100)) for i in range(30)]
        ] for i in range(15)
    ]
))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(children=[
    dbc.Label('Click a cell in the table'),
    dt.DataTable(id='tbl',
        columns=[{"id":i, "name":i} for i in df.columns],
        data=df.to_dict('records'),
        editable=False,
        #page_size =10,
        fixed_rows={'headers': True},
        style_cell={
            #'overflow': 'hidden',
            #'textOverflow': 'ellipsis',
            'minWidth': 95, 'maxWidth': 95, 'width': 95 
        },
    },
        
    ),
    dbc.Alert(id='tbl_out')
])

@callback(
    Output('tbl_out', 'children'),
    Input('tbl', 'active_cell')
) 
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

if __name__ == '__main__':
    app.run_server(debug=True)