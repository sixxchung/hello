import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.pkg_ui import *

from dash import dash_table as dt

#df = pd.read_csv('https://git.io/Juf1t')
import random

from collections import OrderedDict
df = pd.DataFrame(
    OrderedDict(
        [
            ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
            ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
            ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
            ("Humidity", [10, 20, 30, 40, 50, 60]),
            ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
        ]
    )
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(children=[
    dbc.Label('Click a cell in the table'),
    dt.DataTable(id='tbl',
        columns=[{"id":i, "name":i} for i in df.columns],
        data=df.to_dict('records'),
        editable=False,
        #page_size =10,
        virtualization=True,
        #fixed_rows={'headers': True},
        # style_cell={
        #     #'overflow': 'hidden',
        #     #'textOverflow': 'ellipsis',
        #     'minWidth': 95, 'maxWidth': 95, 'width': 95 
        # },        
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

# Name                    Version                   Build  Channel
# dash                      1.19.0             pyhd3eb1b0_0  
# dash-admin-components     0.1.4                    pypi_0    pypi
# dash-bootstrap-components 0.13.0             pyhd8ed1ab_0    conda-forge
# dash-core-components      1.3.1                      py_0  
# dash-html-components      1.0.1                      py_0  
# dash-renderer             1.1.2                      py_0  
# dash-table                4.4.1              pyhd3eb1b0_0