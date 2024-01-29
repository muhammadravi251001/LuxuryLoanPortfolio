from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('lpetrocelli-retail-banking-demo-data\LuxuryLoanPortfolio.csv')

app = Dash(__name__)

bar_chart_data = df.groupby('purpose').size().reset_index(name='count')
fig1 = px.bar(bar_chart_data, x='purpose', y='count', title='Loan Purpose Distribution')

line_chart_data = df.groupby('funded_date')['funded_amount'].sum().reset_index()
fig2 = px.line(line_chart_data, x='funded_date', y='funded_amount', title='Funding Over Time')

pie_chart_data = df['duration years'].value_counts().reset_index(name='count')
fig3 = px.pie(pie_chart_data, names='index', values='count', title='Duration Years Distribution')

app.layout = html.Div([
    html.H1('Luxury Loan Portfolio Analysis'),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

if __name__ == '__main__':
    app.run_server(debug=True)