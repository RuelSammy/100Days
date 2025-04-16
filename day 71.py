import pandas as pd

# Plotly imports
import plotly.graph_objects as go
import plotly.express as px

# Bokeh imports
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file
from bokeh.models import ColumnDataSource, HoverTool

# Set to 'plotly' or 'bokeh' to switch visualization library
VIS_LIBRARY = 'bokeh'  # or 'plotly'

# Sample data
data = {
    'Date': pd.date_range(start='2025-01-01', periods=10),
    'Stock Price': [100, 102, 104, 103, 105, 108, 110, 112, 113, 115]
}
df = pd.DataFrame(data)

# ---------- Plotly Chart ----------
def plot_with_plotly(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Stock Price'],
        mode='lines+markers',
        name='Stock Price'
    ))
    fig.update_layout(
        title='Interactive Stock Price Chart (Plotly)',
        xaxis_title='Date',
        yaxis_title='Price ($)',
        hovermode='x unified'
    )
    fig.show()

# ---------- Bokeh Chart ----------
def plot_with_bokeh(df):
    output_file("bokeh_chart.html")  # Saves and opens in browser
    df['Date_str'] = df['Date'].dt.strftime('%Y-%m-%d')
    source = ColumnDataSource(df)

    p = figure(x_axis_type='datetime', title="Interactive Stock Price Chart (Bokeh)", 
               width=800, height=400)
    p.line('Date', 'Stock Price', source=source, line_width=2)
    p.circle('Date', 'Stock Price', source=source, size=8, fill_color='white')

    hover = HoverTool(
        tooltips=[
            ('Date', '@Date_str'),
            ('Price', '@{Stock Price}')
        ],
        mode='vline'
    )
    p.add_tools(hover)

    show(p)

# ---------- Run Based on Choice ----------
if __name__ == '__main__':
    if VIS_LIBRARY.lower() == 'plotly':
        plot_with_plotly(df)
    elif VIS_LIBRARY.lower() == 'bokeh':
        plot_with_bokeh(df)
    else:
        print("Invalid VIS_LIBRARY value. Use 'plotly' or 'bokeh'.")
