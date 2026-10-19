# EID de Cálculo Intermedio - Grupo 14

**Curso:** MATE1134 (2026)

**Tema:** La integral más allá del área

**Pregunta central:** ¿Qué representa una integral cuando la función describe una tasa y no una altura geométrica?

## Integrantes

| Integrante | GitHub |
| --- | --- |
| Benjamin Varela | [BenjaVarela](https://github.com/BenjaVarela) |
| Benjamin Pedraza | [bpedrazav](https://github.com/bpedrazav) |

## Idea matemática

La primera visualización muestra una integral definida como área bajo una curva positiva. En el ejemplo principal, el eje horizontal representa tiempo en minutos y la función `r(t) = 5t + 20` representa una **tasa de entrada de agua** en litros por minuto. Por eso, la integral acumula agua ingresada:

```text
∫₀⁴ (5t + 20) dt = [5t²/2 + 20t]₀⁴ = 120 L
```

Los cinco rectángulos de la escena ilustran aportes en tramos de `0,8 min`: ancho (min) por altura (L/min) da litros. La integral entrega la acumulación exacta entre los minutos 0 y 4. Si la piscina parte vacía y no hay pérdidas ni otras entradas en ese intervalo, al minuto 4 contiene 120 L.

## Archivos

| Archivo | Escena | Contenido |
| --- | --- | --- |
| `introduccion.py` | `introduccion` | Integrantes, tema y pregunta central. |
| `intro2.py` | `intro2` | Interpretación geométrica de una integral. |
| `planteamiento.py` | `Planteamiento` | Tasa de entrada, gráfico, rectángulos, piscina y cálculo. |
| `creditos.py` | `creditos` | Integrantes, fuentes, Manim y declaración de IA. |
| `requirements.txt` | - | Dependencia de Python. |
| `referencias.md` | - | Fuentes completas, recursos y uso de IA. |

El MP4 final combina estas escenas con las voces y se entrega por separado en Blackboard. Los archivos generados por Manim (`media/`) no son necesarios en el repositorio: se reconstruyen con los comandos siguientes.

## Requisitos y ejecución

Se probó con **Python 3.13.15** y **Manim Community 0.22.0**. Manim requiere FFmpeg y una distribución de LaTeX para las expresiones `MathTex`; véase la [guía oficial de instalación](https://docs.manim.community/en/stable/installation.html).

Desde la carpeta del repositorio:

```bash
python -m pip install -r requirements.txt
python -m manim -pqh introduccion.py introduccion
python -m manim -pqh intro2.py intro2
python -m manim -pqh planteamiento.py Planteamiento
python -m manim -pqh creditos.py creditos
```

`-qh` renderiza a 1920 x 1080 y 60 fps; `-p` abre el resultado al terminar. Los MP4 se guardan en `media/videos/`. Para pruebas rápidas, puede cambiarse `-pqh` por `-pql`.

## Fuentes y uso de IA

Las referencias matemáticas, la documentación de Manim y la declaración de uso de IA están en [referencias.md](referencias.md). Las fuentes también se identifican en los créditos del video.
