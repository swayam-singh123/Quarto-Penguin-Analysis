from vetiver import VetiverModel
import vetiver
from shiny import app, render, ui, reactive
import uvicorn
import requests

v = VetiverModel(model, model_name='penguin_model', prototype_data=X)
model_board = board_folder("/data/model", allow_pickle_read=True)
vetiver_pin_write(model_board, v)
app = VetiverAPI(v, check_prototype = True)
shinyApp(v, model_board)
