#include <stdio.h>

#define SIZE 4

// Matriz de int: filas = productos, columnas = dias

void inicializarTabla(int tabla[SIZE][SIZE]) {
    for (int p = 0; p < SIZE; p++) {
        for (int d = 0; d < SIZE; d++) {
            tabla[p][d] = 0;
        }
    }
}

void pedirVentas(int tabla[SIZE][SIZE]) {
    for (int p = 0; p < SIZE; p++) {
        for (int d = 0; d < SIZE; d++) {
            printf("Ventas del producto %d en el dia %d: ", p + 1, d + 1);
            scanf("%d", &tabla[p][d]);
        }
    }
}

void mostrarTabla(int tabla[SIZE][SIZE]) {
    printf("\n            ");
    for (int d = 0; d < SIZE; d++) {
        printf("Dia %d  ", d + 1);
    }
    printf("\n");
    for (int p = 0; p < SIZE; p++) {
        printf("Producto %d  ", p + 1);
        for (int d = 0; d < SIZE; d++) {
            printf("%5d  ", tabla[p][d]);
        }
        printf("\n");
    }
}

int main() {
    int tabla[SIZE][SIZE];
    int totalGeneral = 0;

    printf("===== Tienda: registro de ventas =====\n");

    inicializarTabla(tabla);
    pedirVentas(tabla);
    mostrarTabla(tabla);

    printf("\n--- Total por producto ---\n");
    for (int p = 0; p < SIZE; p++) {
        int totalProducto = 0;
        for (int d = 0; d < SIZE; d++) {
            totalProducto += tabla[p][d];
        }
        printf("Producto %d: %d\n", p + 1, totalProducto);
        totalGeneral += totalProducto;
    }

    printf("\nTotal de ventas de todos los productos: %d\n", totalGeneral);

    return 0;
}



I'm sorry, but an uncaught exception occurred.

While processing the color property of anonymous style:
  File "game/script.rpy", line 86, in script
    ela "SEÑORITA CLAE, DEME UN ABRAZO"
  File "tmp/gen3-static/styleclass.pxi", line 621, in renpy.styledata.styleclass.Style.slow_abortable.__get__
  File "renpy/style.pyx", line 493, in renpy.style.StyleCore._get
  File "renpy/style.pyx", line 717, in renpy.style.build_style
  File "renpy/style.pyx", line 714, in renpy.style.build_style
  File "tmp/gen3-static/style_functions.pyx", line 336, in style_functions.color_property
Exception: Color string '#FF69B4 ' must be 3, 4, 6, or 8 hex digits long.

-- Full Traceback ------------------------------------------------------------

Traceback (most recent call last):
  File "game/script.rpy", line 86, in script
    ela "SEÑORITA CLAE, DEME UN ABRAZO"
  File "renpy/ast.py", line 2935, in execute
    Say.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "renpy/ast.py", line 994, in execute
    renpy.exports.say(who, what, *args, **kwargs)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/exports/sayexports.py", line 129, in say
    who(what, *args, **kwargs)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/character.py", line 1565, in __call__
    self.do_display(who, what, cb_args=self.cb_args, dtt=dtt, **display_args)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/character.py", line 1220, in do_display
    display_say(who, what, self.do_show, **display_args)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/character.py", line 902, in display_say
    rv = renpy.ui.interact(mouse="say", type=type, roll_forward=roll_forward)
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/ui.py", line 306, in interact
    rv = renpy.game.interface.interact(roll_forward=roll_forward, **kwargs)
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/display/core.py", line 2163, in interact
    repeat, rv = self.interact_core(
                 ~~~~~~~~~~~~~~~~~~^
        preloads=preloads,
        ^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "renpy/display/core.py", line 2709, in interact_core
    root_widget.visit_all(lambda d: d.per_interact())
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "renpy/display/displayable.py", line 460, in visit_all
    d.visit_all(callback, seen)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "renpy/display/displayable.py", line 460, in visit_all
    d.visit_all(callback, seen)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "renpy/display/displayable.py", line 460, in visit_all
    d.visit_all(callback, seen)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "renpy/display/screen.py", line 508, in visit_all
    self.child.visit_all(callback, seen=None)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "renpy/display/displayable.py", line 460, in visit_all
    d.visit_all(callback, seen)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "renpy/display/displayable.py", line 460, in visit_all
    d.visit_all(callback, seen)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "renpy/display/displayable.py", line 460, in visit_all
    d.visit_all(callback, seen)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
[Previous line repeated 1 more time]
  File "renpy/display/displayable.py", line 462, in visit_all
    callback(self)
    ~~~~~~~~^^^^^^
  File "renpy/display/core.py", line 2709, in <lambda>
    root_widget.visit_all(lambda d: d.per_interact())
                                    ~~~~~~~~~~~~~~^^ 
  File "renpy/text/text.py", line 2392, in per_interact
    if self.style.slow_abortable:
       ^^^^^^^^^^^^^^^^^^^^^^^^^ 
  File "tmp/gen3-static/styleclass.pxi", line 621, in renpy.styledata.styleclass.Style.slow_abortable.__get__
  File "renpy/style.pyx", line 493, in renpy.style.StyleCore._get
  File "renpy/style.pyx", line 717, in renpy.style.build_style
  File "renpy/style.pyx", line 714, in renpy.style.build_style
  File "tmp/gen3-static/style_functions.pyx", line 336, in style_functions.color_property
  File "renpy/color.py", line 204, in __new__
    raise Exception(f"Color string {color!r} must be 3, 4, 6, or 8 hex digits long.")
Exception: Color string '#FF69B4 ' must be 3, 4, 6, or 8 hex digits long.

Windows-11-10.0.26300-SP0 AMD64
Ren'Py 8.5.3.26051504
Behind the Smile 1.0
Wed Nov 18 10:31:46 2026
