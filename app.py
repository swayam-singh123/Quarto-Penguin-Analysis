# Import the FastAPI library
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a route at the root '/'
@app.get("/")
def read_root():
    return {'Hello Swayam!'}
