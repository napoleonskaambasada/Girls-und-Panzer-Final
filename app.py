from flask import Flask, render_template

app = Flask(__name__)

main_schools = [
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
    },
    {
        "name": "Chi-Ha-Tan Academy",
        "tank": "Type 97 Chi-Ha",
        "commander": "Kinuyo Nishi",
        "image": "images/Chihatan.jpg"
    },
    {
        "name": "Anzio High School",
        "tank": "Carro Veloce CV.33",
        "commander": "Chiyomi Anzai",
        "image": "images/Anzio.jpg"
    },
    {
        "name": "Jatkosota High School",
        "tank": "BT-42",
        "commander": "Mika",
        "image": "images/Jaktosota.jpg"
    },
    {
        "name": "Saunders University High School",
        "tank": "M4 Sherman",
        "commander": "Kay",
        "image": "images/Saunders.jpg"
    },
    {
        "name": "BC Freedom Academy",
        "tank": "Renault FT-17",
        "commander": "Azumi",
        "image": "images/BC.jpg"
    }      
]

 
minor_schools = [
    {
        "name": "Maginot Girls Academy",
        "tank": "Char B1",
        "commander": "Éclair",
        "image": "images/maginot.jpg"
    },
    {
        "name": "Bonple High School",
        "tank": "7TP",
        "commander": "Jajka",
        "image": "images/bonple.jpg"
    },
    {
        "name": "Viking Fisheries High School",
        "tank": "Strv m/42",
        "commander": "Nina",
        "image": "images/viking.jpg"
    },
    {
        "name": "Blue Division High School",
        "tank": "Panzer I",
        "commander": "El",
        "image": "images/bluedivision.jpg"
    },
    {
        "name": "Count High School",
        "tank": "KV-2",
        "commander": "Count",
        "image": "images/count.jpg"
    },
    {
        "name": "Waffle Academy",
        "tank": "TKS Tankette",
        "commander": "Unknown",
        "image": "images/waffle.jpg"
    },
    {
        "name": "Kebab High School",
        "tank": "Renault R35",
        "commander": "Bosporus",
        "image": "images/kebak.jpg"
    },
    {
        "name": "Bellwall Academy",
        "tank": "T-44",
        "commander": "Emi Nakasuga",
        "image": "images/Bewall.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },
    {
        "name": "",
        "tank": "",
        "commander": "",
        "image": "images/.jpg"
    },


]

@app.route("/")
def home():
    return render_template(
        "index.html",
        main_schools=main_schools,
        minor_schools=minor_schools
    )

if __name__ == "__main__":
    app.run(debug=True)