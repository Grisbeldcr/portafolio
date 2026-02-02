from flask import Flask, render_template

app = Flask(__name__)

bloques = {
    "profesionales": {
        "titulo": "Proyectos profesionales",
        "descripcion": "Desarrollo de soluciones tecnológicas en telecomunicaciones, análisis de datos y software, enfocadas en resolver problemas reales con criterio técnico y visión estratégica.",
        "proyectos": [
            {"nombre": "Portafolio Web con Flask", "slug": "portafolio-flask"},
            {"nombre": "Análisis de datos de redes", "slug": "analisis-redes"},
            {"nombre": "Automatización de reportes", "slug": "automatizacion-reportes"}
        ]
    },
    "personales": {
        "titulo": "Proyectos personales y comunicación",
        "descripcion": "Iniciativas donde la tecnología, la experiencia personal y la comunicación se integran para crear impacto, reflexión y aprendizaje compartido.",
        "proyectos": [
            {"nombre": "Flor de Loto (Medium)", "slug": "flor-de-loto"},
            {"nombre": "Grisarito", "slug": "grisarito"} 
        ]
    },
    "aprendizaje": {
        "titulo": "Aprendizaje continuo",
        "descripcion": "Formación constante en tecnologías, idiomas y herramientas como parte de un compromiso profesional con la mejora continua y la adaptabilidad.",
        "proyectos": [
            {"nombre": "Python y Flask", "slug": "python-flask"},
            {"nombre": "SQL y análisis de datos", "slug": "sql-datos"},
            {"nombre": "Inglés técnico", "slug": "ingles-tecnico"}
        ]
    }
}

proyectos_detalle = {
    "portafolio-flask": {
        "titulo": "Portafolio Web con Flask",
        "contexto": "Necesidad de centralizar mi experiencia técnica, proyectos y narrativa profesional en un solo espacio propio.",
        "problema": "Los CV tradicionales no permiten mostrar procesos, decisiones técnicas ni evolución profesional.",
        "solucion": "Diseñé y desarrollé un portafolio web utilizando Flask, HTML y CSS, estructurando los proyectos por categorías y rutas dinámicas.",
        "impacto": "Obtuve un espacio escalable, personal y técnico que crece junto a mis habilidades.",
        "tecnologias": ["Python", "Flask", "HTML", "CSS"],
        "links": {
            "Repositorio en GitHub": "https://github.com/Grisbeldcr/portafolio",
            "Demo local": "http://127.0.0.1:5000"
        } 
        
    },
    "flor-de-loto": {
        "titulo": "Flor de Loto",
        "categoria": "Proyecto personal",
        "contexto": "Flor de Loto nace como un espacio de escritura reflexiva para transformar experiencias personales profundas en aprendizaje compartido.",
        "problema": "Muchas personas atraviesan duelo, migración o enfermedad en silencio, sin espacios seguros donde sentirse acompañadas.",
        "solucion": "A través de textos breves y narrativas honestas, el proyecto ofrece palabras que acompañan, validan y generan conexión.",
        "impacto": "Desarrollé una voz narrativa propia, disciplina creativa y la capacidad de comunicar experiencias complejas con claridad y sensibilidad.",
        "tecnologias": ["Medium", "Narrativa personal", "Comunicación escrita"],
        "links": {
            "Medium": "https://medium.com/@grisbelc",
            "Instagram": "https://instagram.com/flor_de_loto312"
        }
    }
}


@app.route("/")
def index():
    return render_template("index.html", bloques=bloques)

@app.route("/proyecto/<slug>")
def proyecto(slug):
    proyecto = proyectos_detalle.get(slug)
    if not proyecto:
        return "Proyecto no encontrado", 404
    return render_template("proyecto.html", proyecto=proyecto)


if __name__ == "__main__":
    app.run(debug=True)



