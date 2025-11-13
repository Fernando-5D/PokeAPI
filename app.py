import requests
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

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
                        "types": resp["types"]
                    }
                    
                    return render_template("pokemon.html", pokemon = pokemon)
                else:
                    flash(f"No se encontro el Pokemon: {nombrePok}")
                    return render_template("form.html")
            except requests.exceptions.RequestException as err:
                flash(f"Ocurrio un error al buscar al Pokemon: {nombrePok}")
                return render_template("form.html")
        else:
            return redirect(url_for("form"))

if __name__ == "__main__":
    app.run(debug=True)
