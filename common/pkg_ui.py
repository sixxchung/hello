# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import dash
from dash import html # dash_html_components 
# https://docs-dash-admin-components.herokuapp.com/
import dash_admin_components as dac

from dash import dcc  # dash_core_components
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from dash.exceptions   import PreventUpdate

### Required libraries ------------------------------------------
import numpy as np
import os

import pandas as pd
from pandas import Series
# column 다 보이기
pd.set_option('display.max_columns', None)
#(참고) warning 제거를 위한 코드
#np.seterr(divide='ignore', invalid='ignore')

### Visualization libraries -------------------------------------
import plotly.express as px
import plotly.graph_objs as obj