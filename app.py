import pandas as pd
import gradio as gr
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("project datsets.csv")

# Prepare data
X = df[["Confirmed"]]
y = df["Deaths"]

model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_deaths(confirmed_cases):
    prediction = model.predict([[confirmed_cases]])
    return int(prediction[0])

# Gradio UI
interface = gr.Interface(
    fn=predict_deaths,
    inputs=gr.Number(label="Enter Confirmed COVID Cases"),
    outputs=gr.Number(label="Predicted Deaths"),
    title="COVID-19 Death Prediction",
    description="ML model to predict deaths based on confirmed cases"
)

interface.launch()
