from app import app
from model.sponsors_model import sponsors_model

obj = sponsors_model()


@app.route("/sponsors")
def sponsors_contoller():
    return obj.sponsors_list_model()
