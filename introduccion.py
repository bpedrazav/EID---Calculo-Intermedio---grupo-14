from manim import *

class introduccion(Scene):
    def construct(self):
        titulooo = Text("Grupo 14: La integral más allá del área",
                        font_size=19)
        integrantes_pregun = Text("¿Qué representa una integral cuando la función describe una tasa y no una altura geométrica?" "\nIntegrantes: Benjamin Varela, Benjamin Pedraza y Benjamin Riquelme",
                         font_size=16)
        

        titulooo.scale_to_fit_width(config.frame_width - 1.5) #se ajusta para q caiga bien y no se aprete
        
        grupo = VGroup(titulooo, integrantes_pregun).arrange(DOWN, buff=0.8) #los agrupo y los acomodo entre ellos en vertical
        grupo.move_to(ORIGIN)

        #para q se escriba asi el texto
        self.play(Write(titulooo), run_time=2)
        self.play(Write(integrantes_pregun), run_time=2)
        self.wait(15) # es para q la escena se demore
        