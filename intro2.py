from manim import *

class intro2(Scene):
    def construct(self):
        integral = MathTex(r"\int_{0.5}^{4} (0.2 x^2 + 0.5) \, dx")
        integral.to_edge(RIGHT, buff=1.0) #pegada a la derecha con espacio de 1

        self.play(Write(integral)) #crea la integral
        self.wait(3) #espera 3 segundos

        
        ejess = Axes(
            x_range=[0, 5, 1], #va del 0 al 5 de a uno
            y_range=[0, 4, 1], # lo mismoooo pero en y
            x_length=6, #ancho de x
            y_length=5, #alto de y
            axis_config={"include_numbers": True}, #para q muestren los numeros del eje
        )

        curva = ejess.plot(lambda x: 0.2 * x**2 + 0.5, color=WHITE, x_range=[0, 4.5]) #crea la funcion matematica
        #lo pinra te blanco en el intervalo de 0 a 4.5

        area_curva = ejess.get_area(curva, #genera el area asi de color bajo la curva
            x_range=[0.5, 4], #con el mismo intervalo de 0.5 a 4
            color=ORANGE, #el color es naranjo
            opacity=0.6 #con opacidad para q quede mejor
        )


        grafico = VGroup(ejess, curva, area_curva) #los agrupo para poder moverlos
        grafico.to_edge(LEFT, buff=0.8) #los muevo a la izq con 0.8 de espacio

        self.play(Create(ejess), Create(curva)) #crea los ejes y la curva
        self.wait(6)
        self.play(DrawBorderThenFill(area_curva), run_time=2)
        self.wait(10)