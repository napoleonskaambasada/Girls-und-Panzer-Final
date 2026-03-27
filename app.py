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
        "image": "images/Bellwall.jpg"
    },
    {
        "name": "Gregor High School",
        "tank": "Kafka",
        "commander": "Panzer 38(t)",
        "image": "images/Gregor.jpg"
    },
    {
        "name": "Gilbert High School",
        "tank": "M26 Pershing",
        "commander": "Jinko Yoshinaga",
        "image": "images/Gilbert.jpg"
    },
    {
        "name": "Koala Forest Academy",
        "tank": "AC.I Sentinel",
        "commander": "Koala (an actual one)",
        "image": "images/Koala.jpg"
    },
    {
        "name": "Maple High School",
        "tank": "Light Tank Mk VIB",
        "commander": "Trout",
        "image": "images/Maple.jpg"
    },
    {
        "name": "Tategoto High School",
        "tank": "Type 95 Ha-Go",
        "commander": "Aung",
        "image": "images/tategoto.jpg"
    },
    {
        "name": "Tatenashi High School",
        "tank": "Type 97 Te-Ke",
        "commander": "Shizuka Tsuruki",
        "image": "images/Tatenashi.jpg"
    },
    {
        "name": "Viggen High School",
        "tank": "Strv m/40 light tank",
        "commander": "Semla",
        "image": "images/Viggen.jpg"
    },
    {
        "name": "West Kureouji Grona Academy",
        "tank": "Black Prince",
        "commander": "Kiri Shiratori",
        "image": "images/Grona.jpg"
    },
    {
        "name": "Yogurt Academy",
        "tank": "Carro Veloce CV.33 II Series L3/33",
        "commander": "Sofia",
        "image": "images/Yogurt.jpg"
    },
    {
        "name": "Neutral High School",
        "tank": "-No tank-",
        "commander": "Senjyu",
        "image": "images/Natural.jpg"
    }


]

higher_education = [
    {
        "name": "All-Stars University Team",
        "tank": "Centurion Mk.I (A41)",
        "commander": "Alice Shimada",
        "image": "images/Stars.jpg" 
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        main_schools=main_schools,
        minor_schools=minor_schools,
        higher_education=higher_education
    )

if __name__ == "__main__":
    app.run(debug=True)