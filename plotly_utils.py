from typing import List

import numpy as np
import pandas as pd
import plotly.graph_objects as go


def _description_format(description: str) -> str:
    result = []
    for i, word in enumerate(description[:500].split()):
        if i % 10 == 0:
            result.append("<br>")
        result.append(word)
    return " ".join(result) + " ..."


def _build_hovertext(df: pd.DataFrame) -> List:
    return (
            "Query: <b>" + df["search_query"] + "</b><br>"
            + "Title: <b>" + df["title"] + "</b>"
            # + df["cleaned_description"].apply(_description_format)
    )


def build_2d_figure(df: pd.DataFrame, color_labels: List[int], vectors: np.array):
    fig2d = go.Figure(data=[go.Scatter(
        x=vectors[:, 0],
        y=vectors[:, 1],
        hovertext=_build_hovertext(df),
        mode='markers',
        marker=dict(size=20, color=color_labels, colorscale='Viridis', opacity=0.8)
    )])
    fig2d.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    return fig2d


def build_3d_figure(df: pd.DataFrame, color_labels: List[int], vectors: np.array):
    fig3d = go.Figure(data=[go.Scatter3d(
        x=vectors[:, 0],
        y=vectors[:, 1],
        z=vectors[:, 2],
        hovertext=_build_hovertext(df),
        mode='markers',
        marker=dict(size=20, color=color_labels, colorscale='Viridis', opacity=0.8)
    )])
    fig3d.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    return fig3d
