from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Siemano we frameworku !!!"

#po wpisaniu adresu w formie /ciag znakow. Ten ciag znakow(name) jest najpierw zamienany argumentem title
#a potem wysweitalny w postaci hello + wpisany string
@app.route("/<string:name>")
def hello(name):
    name = name.title()
    return f"Hello, {name} !"




if __name__ == "__main__":
    app.run()