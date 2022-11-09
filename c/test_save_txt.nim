# fopen not defined for non-c targets, staticRead didn't work.
let fileContents: seq[string] = readLines("init_write.txt", 2)
echo fileContents

proc fileContent*(): string =
    cast[string](fileContents)

# C run output: @["Text sent from init.c, sort of...", "After running `gcc init.c` and `./a.out`"]

# import dom

# proc onLoad(event: Event) =
#   let p = document.createElement("p")
#   p.innerHTML = cstring(fileContent())
#   p.style.fontFamily = "Helvetica"
#   p.style.color = "red"

#   p.addEventListener("click",
#     proc (event: Event) =
#       window.alert("Hello World!")
#   )

#   document.body.appendChild(p)

# window.onload = onLoad