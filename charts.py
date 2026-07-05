import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Heatmap tương quan
def heatmap(df):
    corr = df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="Viridis",
        aspect="auto"
    )

    fig.update_layout(
        title="Ma trận tương quan",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)


# Histogram
def histogram(df, column):
    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Phân bố {column}"
    )

    st.plotly_chart(fig, use_container_width=True)


# Boxplot
def boxplot(df, column):
    fig = px.box(
        df,
        y=column,
        title=f"Boxplot {column}"
    )

    st.plotly_chart(fig, use_container_width=True)


# Scatter
def scatter(df, x, y, color=None):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title=f"{x} vs {y}"
    )

    st.plotly_chart(fig, use_container_width=True)


# Bar chart
def bar(df, x, y):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=f"{y} theo {x}"
    )

    st.plotly_chart(fig, use_container_width=True)