import requests
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

app.config["SECRET_KEY"] = "pokeapi"
badges = {
    "normal": ["rgb(212, 159, 169)"],
    "fighting": ["rgb(250, 102, 54)"],
    "flying": ["rgb(155, 185, 210)"],
    "poison": ["rgb(161, 106, 225)"],
    "ground": ["rgb(175, 117, 44)"],
    "rock": ["rgb(144, 63, 33)"],
    "bug": ["rgb(60, 161, 83)"],
    "ghost": ["rgb(148, 105, 151)"],
    "steel": ["rgb(65, 199, 154)"],
    "fire": ["rgb(255, 75, 92)"],
    "water": ["rgb(16, 85, 232)"],
    "grass": ["rgb(35, 215, 80)"],
    "electric": ["rgb(250, 255, 111)", "text-dark"],
    "psychic": ["rgb(251, 27, 149)"],
    "ice": ["rgb(133, 219, 251)", "text-dark"],
    "dragon": ["rgb(100, 215, 231)"],
    "dark": ["rgb(91, 89, 126)"],
    "fairy": ["rgb(248, 17, 105)"]
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
