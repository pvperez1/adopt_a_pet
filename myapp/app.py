from flask import Flask
from data import pets

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Adopt a Pet!</h1>
                <p>Browse through the links below to find your new furry friend:</p>
                <ul>
                    <li><a href="/animals/dogs">Dogs</a></li>
                    <li><a href="/animals/cats">Cats</a></li>
                    <li><a href="/animals/rabbits">Rabbits</a></li>
                </ul>
            """

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = "<h1>List of {}</h1>".format(pet_type)
    html += "<ul>"

    for pet in pets[pet_type]:
        html += "<li>{n}</li>".format(n = pet["name"])

    html += "</ul>"


    return html



if __name__ == "__main__":
    app.run(debug=True)