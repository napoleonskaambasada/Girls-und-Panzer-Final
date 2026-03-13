from flask import Flask, render_template

app = Flask(__name__)

schools = [
    {
        "name": "Ōarai Girls Academy",
        "tank": "Panzer IV",
        "commander": "Miho Nishizumi",
        "image": "images/Oarai.jpg"
    },
    {
        "name": "Kuromorimine Girls Academy",
        "tank": "Tiger I",
        "commander": "Maho Nishizumi",
        "image": "images/Kuromorimine.jpg"
    },
    {
        "name": "Pravda High School",
        "tank": "T-34/85",
        "commander": "Katyusha",
        "image": "images/Pravda.jpg"
    },
    {
        "name": "St. Gloriana Girls College",
        "tank": "Churchill",
        "commander": "Darjeeling",
        "image": "images/Gloriana.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html", schools=schools)

if __name__ == "__main__":
    app.run(debug=True)