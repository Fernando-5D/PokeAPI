def = document.getElementById("def")
shi = document.getElementById("shi")
sprite = document.getElementById("sprite")

function changeSprite(check, spriteName) {
    check.addEventListener("change", () => {
        if (check.checked) {
            sprite.setAttribute("src", `{{ pokemon[\"${spriteName}\"] }}`)
        }
    })
}

changeSprite(def, "spriteDef")
changeSprite(shi, "spriteShiny")
