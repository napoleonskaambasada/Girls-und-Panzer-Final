from flask import Flask, render_template

app = Flask(__name__)

schools = [
    {
        "name": "Ōarai Girls Academy",
        "tank": "Panzer IV",
        "commander": "Miho Nishizumi",
        "image": "images/panzer4.jpg"
    },
    {
        "name": "Kuromorimine Girls Academy",
        "tank": "Tiger I",
        "commander": "Maho Nishizumi",
        "image": "images/tiger1.jpg"
    },
    {
        "name": "St. Gloriana Girls College",
        "tank": "Churchill",
        "commander": "Darjeeling",
        "image": "images/churchill.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html", schools=schools)

if __name__ == "__main__":
    app.run(debug=True)