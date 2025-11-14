var def = document.getElementById("def")
var shi = document.getElementById("shi")
var sprite = document.getElementById("sprite")

def.addEventListener("change", () => {
    if (def.checked) sprite.src = "{{ pokemon.sprites.spriteDef }}"
})

shi.addEventListener("change", () => {
    if (shi.checked) sprite.src = "{{ pokemon.sprites.spriteShiny }}"
})
