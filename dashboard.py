import plotly.express as px
import pandas as pd

def generate_charts(text):
    data = {
        "Metric": ["Hemoglobin", "Glucose", "Cholesterol"],
        "Value": [13.5, 140, 210]
    }

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Metric",
        y="Value",
        title="Key Health Metrics"
    )
    return fig
