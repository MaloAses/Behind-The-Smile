label splashscreen:
    scene black
    with dissolve

    "ADVERTENCIA: Este juego contiene temas maduros, lenguaje fuerte y contenido no apto para menores de edad."
    "Todos los personajes que aparecen en esta obra son ficticios y mayores de 18 años."
    
    menu:
        ""
        "Sí.":
            hide cartel_advertencia with dissolve
            return # <-- Clave: Apaga el splashscreen y abre el Menú Principal
            
        "No, vete a jugar Minecraft.":
            $ renpy.quit()
label start:


    python:
        nombre_ingresado = renpy.input("{b}{color=#1c0A23}¿Cómo te llamas?{/color}, {color=#c30010}(por defecto Elara){/color}{/b} ", default="Elara", length=15)
        nombre_ingresado = nombre_ingresado.strip()

    if nombre_ingresado:
        $ nombre_prota = nombre_ingresado

        play music "audio/musica/Rainy Morning.mp3"
    "La mañana apenas comenzaba. Los primeros rayos del sol entraban por la ventana, anunciando el inicio de un nuevo día\npara [nombre_prota]."

    scene habitacion manana
    show ela happy2
    ela "Haa... qué bonito amaneció hoy."
    ela "Y lo mejor de todo es que no tengo nada que hacer..."
    hide ela happy2

    "[nombre_prota],se encontraba completamente tranquila, disfrutando de la mañana sin ninguna preocupación."
    "Lo que ella no recordaba era un pequeño detalle..."
    "Hoy era su primer día de clases."
    stop music fadeout 0.5

transform carrera_panico:

 yalign 1.0
 linear 0.5 xpos 0
 linear 0.5 xpos 1920
 linear 0.5 xpos 0
 linear 0.5 xpos 1920
 linear 0.5 xpos 750

show ela suprised1 at carrera_panico
with dissolve
    
ela "¡¡AAAAAAAAAA!!" with hpunch
hide ela suprised1

show ela uniforme_happy
with fade
ela "¡Por fin encontré mi uniforme!"

scene sala2 
with fade
show clae_loca2
with dissolve
clae "jojojjojo"
clae "Mira quien se ha levantado"
clae "y yo pensando que no te ivas a lenvantar"
p "que fastidio"
hide clae_loca2


show ela uniforme_happy
with fade
ela_pensando "oh, que esta claire aqui"
hide ela uniforme_happy

show clae_fastidio31 at right
show ela uniforme_abrazando1 at left
clae "aaaaaa"
clae "NOOOOO,{w=1.0} NI SE TE OCURRA"
clae "NO , YA DIJE QUE NO"
hide clae_fastidio31
    

show ela uniforme_abrazando1 at center
with fade
ela "SEÑORITA CLAE, DEME UN ABRAZO"
menu:
    "Abrazar a claire":
        $ RutaA = "Porfin"
    
    "No abrazar a claire":
        $ RutaA = "que mal"


if RutaA == "Porfin":
    ela "por fin la abraze señorita claire"

else:
    hide ela uniforme_abrazando1
    clae "que fastidio es estar contigo"

return               