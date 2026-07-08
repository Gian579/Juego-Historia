from menu import mostrar_menu
import configuracion
from configuracion import musica_batalla
from batalla import batalla, pantalla_victoria, pantalla_derrota, pantalla_final
from menu_preguntas import mostrar_editor

while True:
    opcion = mostrar_menu()

    # ── Modo normal (con dificultad seleccionada) ─────────────────
    if opcion == "modo":
        musica_batalla()
        niveles = configuracion.DIFICULTAD_NIVELES
        errores_por_nivel = {}

        for i, nivel in enumerate(niveles):
            ganado, errores, total = batalla(nivel)
            errores_por_nivel[nivel] = (errores, total)

            if ganado:
                if i < len(niveles) - 1:
                    pantalla_victoria(nivel, errores, total)
                else:
                    pantalla_final(errores_por_nivel)
            else:
                pantalla_derrota(nivel, errores, total)
                break

    # ── Editor de preguntas personalizadas ────────────────────────
    elif opcion == "preguntas":
        resultado = mostrar_editor()

        if resultado == "empezar":
            musica_batalla()
            niveles = configuracion.DIFICULTAD_NIVELES
            preguntas_custom = configuracion.PREGUNTAS_CUSTOM
            errores_por_nivel = {}

            for i, nivel in enumerate(niveles):
                pregs = preguntas_custom.get(nivel, None)
                ganado, errores, total = batalla(nivel, preguntas_custom=pregs)
                errores_por_nivel[nivel] = (errores, total)

                if ganado:
                    if i < len(niveles) - 1:
                        pantalla_victoria(nivel, errores, total)
                    else:
                        pantalla_final(errores_por_nivel)
                else:
                    pantalla_derrota(nivel, errores, total)
                    break
