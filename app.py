# Import the FastAPI library
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a route at the root '/'
@app.get("/")
def read_root():
    return {'Hello Swayam!'}
  
from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app

import requests

req_data = {
  "bill_length_mm": 0,
  "species_Chinstrap": False,
  "species_Gentoo": False,
  "sex_male": False
}
req = requests.post('http://127.0.0.1:8080/predict', json = [req_data])
res = req.json().get('predict')[0]

import logging

from shiny import app, render, ui, reactive
import requests

api_url = 'http://127.0.0.1:8080/predict'

app_ui = ui.page_fluid(
    ui.panel_title("Penguin Mass Predictor"), 
    ui.layout_sidebar(
        ui.panel_sidebar(
            [ui.input_slider("bill_length", "Bill Length (mm)", 30, 60, 45, step = 0.1),
            ui.input_select("sex", "Sex", ["Male", "Female"]),
            ui.input_select("species", "Species", ["Adelie", "Chinstrap", "Gentoo"]),
            ui.input_action_button("predict", "Predict")]
        ),
        ui.panel_main(
            ui.h2("Penguin Parameters"),
            ui.output_text_verbatim("vals_out"),
            ui.h2("Predicted Penguin Mass (g)"), 
            ui.output_text("pred_out")
        )
    )   
)

def server(input, output, session):
    @reactive.Calc
    def vals():
        d = {
            "bill_length_mm" : input.bill_length(),
            "sex_Male" : input.sex() == "Male",
            "species_Gentoo" : input.species() == "Gentoo", 
            "species_Chinstrap" : input.species() == "Chinstrap"

        }
        return d
    
    @reactive.Calc
    @reactive.event(input.predict)
    def pred():
        r = requests.post(api_url, json = vals())
        return r.json().get('predict')[0]

    @output
    @render.text
    def vals_out():
        return f"{vals()}"

    @output
    @render.text
    def pred_out():
        return f"{round(pred())}"

app = App(app_ui, server)
