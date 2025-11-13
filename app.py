import requests
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

app.config["SECRET_KEY"] = "pokeapi"
badges = {
    "normal": "rgb(255, 255, 255)",
    "fighting": "rgb(255, 255, 255)",
    "flying": "rgb(255, 255, 255)",
    "poison": "rgb(255, 255, 255)",
    "ground": "rgb(255, 255, 255)",
    "rock": "rgb(255, 255, 255)",
    "bug": "rgb(255, 255, 255)",
    "ghost": "rgb(255, 255, 255)",
    "steel": "rgb(255, 255, 255)",
    "fire": "rgb(255, 255, 255)",
    "water": "rgb(255, 255, 255)",
    "grass": "rgb(255, 255, 255)",
    "electric": "rgb(255, 255, 255)",
    "psychic": "rgb(255, 255, 255)",
    "ice": "rgb(255, 255, 255)",
    "dragon": "rgb(255, 255, 255)",
    "dark": "rgb(255, 255, 255)",
    "fairy": "rgb(255, 255, 255)",
    "stellar": "rgb(255, 255, 255)",
    "unknown": "rgb(255, 255, 255)"
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
                        "spriteDef": resp["sprites"]["front_default"],
                        "spriteShiny": resp["sprites"]["front_shiny"],
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
