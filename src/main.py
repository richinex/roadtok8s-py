# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Declare an instance of the FastAPI class
app = FastAPI()

# use the app instance as a decorator to handle an HTTP route and an HTTP method
@app.get("/")
def read_index():
    """
    Return a Python dictionary that supports JSON serialization.
    """
    return {"Hello": "World"}

@app.get("api/v1/hello-world/")
def read_hello_world():
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}
