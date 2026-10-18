from manim import * 

class Planteamiento(Scene):
    def construct(self):
        integral = MathTex(r"\int_0^4 (5t+20)\,dt") #la crea en formato matematico
        integral.to_edge(UP)  
        self.play(Write(integral))  
        self.wait(45)  #nos da tiempo para explicar cada cosa
        self.play(integral.animate.scale(0.75).to_corner(UR))# la achica y la mueve para que no moleste

        ejes = Axes(#ejes del plano
            x_range=[0, 5, 1],# eje x de 0 a 5 saltando de 1 en 1
            y_range=[0, 50, 10], # lo mismooo
            
            x_length=5.5, #so9n las dimesiones de ancho y alto
            y_length=4, 
            axis_config={"include_numbers": True},#muestra los numeros
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.4) #lo ubica izq abajo
        etiquetas = ejes.get_axis_labels(#pone los nombres de los ejes
            x_label=Text("tiempo (min)", font_size=18),
            y_label=Text("entrada de agua (L/min)", font_size=17),)

        curva = ejes.plot(  
            lambda t: 5*t + 20, #crea la curva de la funcionn
            x_range=[0, 4], 
            color=BLUE)

        rectangulos = ejes.get_riemann_rectangles(  
            curva,  # Usa la curva que acabamos de dibujar.
            x_range=[0, 4],  #los rectángulos van del minuto 0 al 4
            dx=0.8,
            input_sample_type="center",
            color=BLUE_D,
            fill_opacity=0.35)

        area = ejes.get_area(
            curva,
            x_range=[0, 4],  #desde el min 0 al 4
            color=BLUE,
            opacity=0.5,#lo deja asi medio transparenteee
            )

        piscina = Rectangle(width=3.6, height=1.8, color=WHITE)#dibuja los bordes de la piscina
        piscina.to_edge(RIGHT, buff=0.8).align_to(ejes, DOWN)#lo mueve a la derecha
        texto_piscina = Text("Piscina", font_size=24).next_to(piscina, UP) # le pone el textitooo

        agua = Rectangle(
            width=3.5, height=0.01,#empieza casi vacio
            stroke_width=0, #lo hace sin borde
            fill_color=BLUE, fill_opacity=0.7,#azul desteñido asi
        )
        agua.move_to(piscina.get_bottom(), aligned_edge=DOWN)#lo ubica en el fondo

        agua_llena = Rectangle(
            width=3.5, height=1.7,# la altura del agua
            stroke_width=0,#no le mete bordeee
            fill_color=BLUE, fill_opacity=0.7,)
        agua_llena.move_to(piscina.get_bottom(), aligned_edge=DOWN)#lo mueve al fondo

        self.play(Create(ejes), Write(etiquetas))#crea los ejes y sus texto
        self.wait(8)#da tiempo para explicar
        self.play(Create(curva))
        self.wait(8) #da tiempo para explicar la curva

        self.play(DrawBorderThenFill(rectangulos), run_time=2)
        self.wait(18) #da tiempo para los rectangulos

        self.play(Create(piscina), Write(texto_piscina))
        self.add(agua)
        self.wait(5)#da tiempo para sinxronizarlo

        self.play(
            FadeOut(rectangulos), #saca los rectangulos
            FadeIn(area),#pinta el area bajo
            Transform(agua, agua_llena),#hace subir el agua
            run_time=3)# la transformación dura tres segumdos
        self.wait(6) 

        self.play(FadeOut(piscina), FadeOut(texto_piscina), FadeOut(agua)) #saca la piscina y el agua

        paso = MathTex(r"= \left[\frac{5t^2}{2}+20t\right]_0^4")  #escribe la antiderivada
        paso.scale(0.62).next_to(integral, DOWN, buff=0.6).align_to(integral, LEFT)
        sustitucion = MathTex(r"= \frac{5(4)^2}{2}+20(4)-0")
        sustitucion.scale(0.62).next_to(paso, DOWN, buff=0.5).align_to(paso, LEFT)
        suma = MathTex(r"= 40+80")
        suma.scale(0.62).next_to(sustitucion, DOWN, buff=0.5).align_to(paso, LEFT)
        resultado = MathTex(r"= 120\ \mathrm{L}")
        resultado.scale(0.62).next_to(suma, DOWN, buff=0.5).align_to(paso, LEFT)

        self.play(Write(paso))
        self.wait(12) 
        self.play(Write(sustitucion))
        self.wait(12)
        self.play(Write(suma))
        self.wait(10)
        self.play(Write(resultado))
        self.wait(6) 

        unidades = MathTex(r"\mathrm{min}\cdot\frac{\mathrm{L}}{\mathrm{min}}=\mathrm{L}")
        unidades.scale(0.7).next_to(resultado, DOWN, buff=0.6).align_to(paso, LEFT)
        self.play(Write(unidades))
        self.wait(10)

        cierre = Text("Entraron 120 L entre los minutos 0 y 4", font_size=23)
        cierre.to_edge(DOWN)  
        self.play(Write(cierre))
        self.wait(12)
