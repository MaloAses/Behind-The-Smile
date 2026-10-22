label splashscreen:
    scene black
    with dissolve

    "ADVERTENCIA: Este juego contiene temas maduros, lenguaje fuerte y contenido no apto para menores de edad."
    "Todos los personajes que aparecen en esta obra son ficticios y mayores de 18 años."

    menu:
        "¿Eres mayor de 18 años y deseas continuar?"

        "Sí.":
            return # Apaga el splashscreen y abre el Menú Principal

        "No, vete a jugar Minecraft.":
            $ renpy.quit()


label start:

    python:
        nombre_ingresado = renpy.input("{b}{color=#1c0A23}¿Cómo te llamas?{/color}, {color=#c30010}(por defecto Elara){/color}{/b} ", default="Elara", length=15)
        nombre_ingresado = nombre_ingresado.strip()

    # Si lo deja vacío, se usa el nombre por defecto
    if not nombre_ingresado:
        $ nombre_ingresado = "Elara"

    $ nombre_prota = nombre_ingresado

    play music "audio/musica/Rainy Morning.mp3"
    "La mañana apenas comenzaba. Los primeros rayos del sol entraban por la ventana, anunciando el inicio de un nuevo día\npara [nombre_prota]."

    scene habitacion manana
    show ela happy2
    ela "Haa... qué bonito amaneció hoy."
    ela "Y lo mejor de todo es que no tengo nada que hacer..."
    hide ela happy2

    "[nombre_prota], se encontraba completamente tranquila, disfrutando de la mañana sin ninguna preocupación."
    "Lo que ella no recordaba era un pequeño detalle..."
    "Hoy era su primer día de clases."
    stop music fadeout 0.5

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
    clae "y yo pensando que no te ibas a levantar"
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
        "Abrazar a Claire":
            $ RutaA = "Porfin"
            $ cambiar_afecto(1)
            $ es_ruta_romantica = True
            $ es_ruta_mala = False

        "No abrazar a Claire":
            $ RutaA = "QueMal"
            $ decisiones_malas += 1
            $ cambiar_afecto(-1)
            $ es_ruta_romantica = False
            $ es_ruta_mala = True

    if RutaA == "Porfin":

        ela "Por fin la abracé, señorita Claire."

        clae "..."

        jump ruta_romantica

    else:

        hide ela uniforme_abrazando1
        show clae_fastidio31
        with fade

        clae "Qué fastidio es estar contigo."

        jump ruta_mala


label ruta_romantica:

    clae "Tal vez... no estuvo tan mal."

    menu:
        "Decirle a Claire que la amas":
            $ cambiar_afecto(1)
            clae "¿En serio me amas?"
            ela "Sí, Claire. Te amo."
            clae "Yo también te amo, [nombre_prota]."

        "Alejarse de Claire":
            $ cambiar_afecto(-1)
            clae "Como quieras..."

    return


label ruta_mala:

    clae "Cada vez me caes peor."
    $ decisiones_malas += 1

    menu:
        "Intentar disculparse":
            # Disculparse NO suma decisiones malas
            clae "No me interesa lo que tengas que decir."
            ela "Lo siento, Claire. No quise molestarte."
            clae "Bueno, supongo que puedo perdonarte esta vez."

        "Ignorar a Claire":
            $ decisiones_malas += 1
            $ cambiar_afecto(-1)
            clae "No me interesa lo que tengas que decir."
            ela "..."
            clae "Bueno, supongo que puedo perdonarte esta vez."

    if decisiones_malas >= 3:

        jump ruta_mala_profunda

    else:

        return


label ruta_mala_profunda:

    clae "Ya no sé qué quieres de mí."

    return
