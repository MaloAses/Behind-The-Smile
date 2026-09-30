##### Definiciones #####
define ela = Character("[nombre_prota]", color="#FF69B4", what_color="#991f4d", what_size=38)
define clae = Character("Claire", color="#8B5CF6", what_color="#401399", what_size=38)
define a = Character("Aria")
define ama = Character("Amaris")
define sera = Character("Seraphine")
define aka = Character("Akari")
define hi = Character("Hina")
define ju = Character ("nombre del jugador")
define ela_pensando = Character(None, what_italic=True, what_color="#ffb6c1", what_size=38)
define p = Character(None, what_italic=True, what_color="#aaaaaa", what_size=40, what_prefix="(", what_suffix=")")

##### Sprites #####
image claire_loca = "images/Sprites/claire/clae_loca.png"
image elara_UniAbrazando = "images/Sprites/Elara/ela_UniAbrazando.png"


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
