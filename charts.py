import plotly.express as px

def create_chart(df):

    if len(df.columns) >= 2:

        x = df.columns[0]
        y = df.columns[1]

        fig = px.bar(df,x=x,y=y,title="AI Generated Chart")

        return fig

    return None