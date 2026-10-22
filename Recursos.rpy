##### Definiciones #####
define ela = Character("[nombre_prota]", color="#FF69B4", what_color="#991f4d", what_size=38)
define clae = Character("Claire", color="#8B5CF6", what_color="#401399", what_size=38)
define a = Character("Aria")
define ama = Character("Amaris")
define sera = Character("Seraphine")
define aka = Character("Akari")
define hi = Character("Hina")
define ju = Character("nombre del jugador")
define ela_pensando = Character(None, what_italic=True, what_color="#ffb6c1", what_size=38)
define p = Character(None, what_italic=True, what_color="#aaaaaa", what_size=40, what_prefix="(", what_suffix=")")

##### Sprites #####
## OJO: el script usa los nombres clae_loca2, clae_fastidio31, ela uniforme_abrazando1, etc.
## Verifica que existan como archivos en images/ o defínelos aquí con "image".
image claire_loca = "images/Sprites/claire/clae_loca.png"
image elara_UniAbrazando = "images/Sprites/Elara/ela_UniAbrazando.png"

##### Animaciones #####
transform carrera_panico:
    yalign 1.0
    linear 0.5 xpos 0
    linear 0.5 xpos 1920
    linear 0.5 xpos 0
    linear 0.5 xpos 1920
    linear 0.5 xpos 750

##### Aviso de afecto #####
## Uso en el script: $ cambiar_afecto(1)  o  $ cambiar_afecto(-1)
init python:
    def cambiar_afecto(cantidad):
        store.afecto_claire += cantidad
        renpy.show_screen("afecto_popup", cantidad)

transform afecto_aparece:
    on show:
        alpha 0.0 yoffset -20
        linear 0.3 alpha 1.0 yoffset 0
    on hide:
        linear 0.4 alpha 0.0

screen afecto_popup(cantidad):
    zorder 150

    frame at afecto_aparece:
        xalign 0.98
        yalign 0.04
        padding (24, 12)
        if cantidad > 0:
            background Solid("#2e7d32dd")
            text "Afecto con Claire +[cantidad]" size 30 color "#ffffff"
        else:
            background Solid("#b71c1cdd")
            text "Afecto con Claire [cantidad]" size 30 color "#ffffff"

    timer 2.5 action Hide("afecto_popup")

##### Variables #####
default nombre_prota = "Elara"

##### rutas #####
default RutaA = ""
default afecto_claire = 0
default decisiones_malas = 0
default es_ruta_romantica = False
default es_ruta_mala = False


#label abrazarclaire:
    #$ abrazarclaire = True
    #ela ""
    #jump rutaA

#label noabrazo:
    #ela "Esta bien, no la abrazo señorita claire"
    #jump rutaA


#label rutaA:
    #if abrazarclaire:
        #ela "si, por la abraze"
    #else:
        #clae "es un fastidio estar contigo"
        #clae "sadhsdsf"
