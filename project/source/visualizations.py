"""
Visualization Module
====================================================

"""
import pandas as pd
import plotly.express as px
from typing import Dict


def bar_chart(data: pd.DataFrame, x: str, y: str, title: str,
              labels: Dict[str, str], top_n: int = 10) -> None:
    """Bar chart for the top-N records."""
    data = data.sort_values(by=y, ascending=False).head(top_n)

    # Prepare text labels: if the series is float, format to 2 decimal places
    if pd.api.types.is_float_dtype(data[y]):
        text_vals = data[y].round(2).map(lambda v: f"{v:.2f}")
    else:
        text_vals = data[y].astype(str)

    fig = px.bar(
        data, x=x, y=y, title=title, labels=labels,
        color=y, 
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False)

    fig.show()
