from manim import *

class PlanteamientoPiscina(Scene):
    def construct(self):
        # 1. Ejes (Tiempo vs Caudal)
        ejes = Axes(
            x_range=[0, 5, 1],    # Tiempo de 0 a 5 min
            y_range=[0, 50, 10],  # Caudal hasta 50 L/min
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True},
        )
        
        # Etiquetas de los ejes
        etiquetas = ejes.get_axis_labels(
            x_label=Text("Tiempo (min)", font_size=16), 
            y_label=Text("Caudal (L/min)", font_size=16)
        )

        # 2. Función f(t) = 5t + 20 (Caudal)
        curva = ejes.plot(lambda t: 5*t + 20, x_range=[0, 4.5], color=BLUE)
        
        # 3. Área bajo la curva (Representa los litros acumulados)
        area = ejes.get_area(curva, x_range=[0, 4], color=BLUE, opacity=0.5)

        # Agrupar la gráfica y moverla a la izquierda para dejar espacio al texto
        grafica_grupo = VGroup(ejes, etiquetas, curva, area).scale(0.8).to_edge(LEFT)

        # 4. Desarrollo matemático paso a paso
        desarrollo = MathTex(
            r"\int_{0}^{4} (5t + 20) \, dt",
            r"= \left[ \frac{5t^2}{2} + 20t \right]_{0}^{4}",
            r"= \frac{5(4)^2}{2} + 20(4)",
            r"= 40 + 80",
            r"= 120 \text{ Litros}"
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(RIGHT, buff=1)

        self.play(Create(ejes), Write(etiquetas))
        self.play(Create(curva))
        
        self.play(Write(desarrollo[0])) 
        self.wait(5)
        
        # Sincroniza esta parte con tu explicación de que el área es la cantidad total
        self.play(DrawBorderThenFill(area), run_time=2)
        
        # Bucle para mostrar el resto de las ecuaciones una por una
        for i in range(1, len(desarrollo)):
            self.play(Write(desarrollo[i]))
            self.wait(5)
            
        self.wait(3)