import requests
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

app.config["SECRET_KEY"] = "pokeapi"
badges = {
    "normal": ["rgb(127, 127, 127)"],
    "fighting": ["rgb(255, 136, 57)"],
    "flying": ["rgb(182, 194, 207)"],
    "poison": ["rgb(76, 145, 59)"],
    "ground": ["rgb(177, 122, 72)"],
    "rock": ["rgb(206, 191, 176)"],
    "bug": ["rgba(20, 170, 0, 1)"],
    "ghost": ["rgb(235, 235, 235)", "text-dark"],
    "steel": ["rgb(80, 88, 97)"],
    "fire": ["rgb(255, 88, 46)"],
    "water": ["rgb(104, 164, 255)"],
    "grass": ["rgb(150, 211, 81)"],
    "electric": ["rgb(231, 214, 62)"],
    "psychic": ["rgb(151, 119, 182)"],
    "ice": ["rgb(108, 197, 219)"],
    "dragon": ["rgb(170, 36, 36)"],
    "dark": ["rgb(57, 38, 75)"],
    "fairy": ["rgb(228, 150, 198)"]
}

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/buscarPok", methods = ("GET", "POST"))
def buscarPoke():
    if request.method == "POST":
        nombrePok = request.form.get("nombrePok").strip().lower()
        if nombrePok:
            try:
                resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombrePok}")
                if resp.status_code == 200:
                    resp = resp.json()
                    
                    pokemon = {
                        "sprites": {
                            "spriteDef": resp["sprites"]["front_default"],
                            "spriteShiny": resp["sprites"]["front_shiny"],
                        },
                        "id": resp["id"],
                        "name": resp["name"],
                        "types": resp["types"],
                        "stats": resp["stats"]
                    }
                    
                    return render_template("pokemon.html", pokemon = pokemon, badges = badges)
                else:
                    flash(f"No se encontro el Pokemon: {str(nombrePok).title()}")
                    return render_template("form.html")
            except requests.exceptions.RequestException as err:
                flash(f"Ocurrio un error al buscar al Pokemon: {str(nombrePok).title()}")
                return render_template("form.html")
        else:
            return redirect(url_for("form"))

if __name__ == "__main__":
    app.run(debug=True)
