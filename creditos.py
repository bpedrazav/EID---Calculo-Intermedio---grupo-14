from manim import *


class creditos(Scene):
    def construct(self):
        # Primera pantalla: quiénes hicieron el video.
        titulo = Text("Créditos", font_size=48)
        integrantes = Text(
            "MATE1134 · Grupo 14\n"
            "Benjamin Varela\n"
            "Benjamin Pedraza\n",
            font_size=30,
            line_spacing=1.3,
        )
        primera = VGroup(titulo, integrantes).arrange(DOWN, buff=0.7)
        self.play(FadeIn(primera), run_time=1)
        self.wait(5)
        self.play(FadeOut(primera), run_time=1)

        # Segunda pantalla: fuentes matemáticas citadas en el proyecto.
        fuentes_titulo = Text("Fuentes matemáticas", font_size=42)
        fuentes = Text(
            "MATE1134 · Introducción a la integral (2026)\n"
            "Strang y Herman · Calculus Volume 1 (OpenStax, 2016)\n"
            "Paul Dawkins · Calculus I (Paul's Online Math Notes)",
            font_size=25,
            line_spacing=1.3,
        )
        segunda = VGroup(fuentes_titulo, fuentes).arrange(DOWN, buff=0.7)
        segunda.scale_to_fit_width(config.frame_width - 1)
        self.play(FadeIn(segunda), run_time=1)
        self.wait(8)
        self.play(FadeOut(segunda), run_time=1)

        # Tercera pantalla: animación, IA y ubicación de las referencias.
        recursos_titulo = Text("Herramientas y referencias", font_size=42)
        recursos = Text(
            "Animación: Manim Community\n"
            "Apoyo de IA: OpenAI Codex (código, guion y documentación)\n"
            "Cálculo revisado mediante antiderivada y unidades\n"
            "Enlaces completos: referencias.md del repositorio",
            font_size=24,
            line_spacing=1.3,
        )
        tercera = VGroup(recursos_titulo, recursos).arrange(DOWN, buff=0.7)
        tercera.scale_to_fit_width(config.frame_width - 1)
        self.play(FadeIn(tercera), run_time=1)
        self.wait(8)
        self.play(FadeOut(tercera), run_time=1)
