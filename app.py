from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

bloques = {
    "profesionales": {
        "titulo": "Proyectos profesionales",
        "descripcion": "Desarrollo de soluciones tecnológicas en telecomunicaciones, análisis de datos y software, enfocadas en resolver problemas reales con criterio técnico y visión estratégica.",
        "proyectos": [
            {"nombre": "Desarrollo Web y Backend", "slug": "portafolio-flask", "tagline": "Diseño y desarrollo de aplicaciones web orientadas a mostrar procesos, lógica y soluciones técnicas reales." },
            {"nombre": "Análisis de Datos Aplicado", "slug": "analisis-datos", "tagline": "Transformación de datos técnicos y operativos en información clara para la toma de decisiones."}, 
            {"nombre": "Automatización de Procesos y Reportes", "slug": "automatizacion-reportes", "tagline": "Reducción de tareas manuales mediante scripts y flujos automatizados que mejoran la eficiencia."}
        ]
    },
    "personales": {
        "titulo": "Proyectos personales y comunicación",
        "descripcion": "Iniciativas donde la tecnología, la experiencia personal y la comunicación se integran para crear impacto, reflexión y aprendizaje compartido.",
        "proyectos": [
            {"nombre": "Flor de Loto (Medium)", "slug": "flor-de-loto", "tagline": "Escritura reflexiva que convierte experiencias personales en acompañamiento y aprendizaje compartido."},
            {"nombre": "Grisarito", "slug": "None", "tagline": "Proyecto creativo en construcción que explora comunicación visual, adaptación y proceso."} 
        ]
    },
    "aprendizaje": {
        "titulo": "Aprendizaje Continuo en Tecnología",
        "descripcion": "Formación constante en tecnologías, idiomas y herramientas como parte de un compromiso profesional con la mejora continua y la adaptabilidad.",
        "proyectos": [
            {"nombre": "Python y Flask", "slug": "python-flask", "tagline": "Desarrollo backend y aplicaciones web como base de soluciones escalables."},
            {"nombre": "SQL y análisis de datos", "slug": "sql-datos", "tagline": "Consulta, limpieza y análisis de datos para comprender sistemas y procesos."},
            {"nombre": "Inglés técnico", "slug": "ingles-tecnico", "tagline": "Comunicación profesional en entornos tecnológicos y documentación especializada." }
        ]
    }
}

proyectos_detalle = {
    "portafolio-flask": {
        "titulo": "Desarrollo Web y Backend",
        "contexto": "Necesidad de centralizar mi experiencia técnica, proyectos y narrativa profesional en un solo espacio propio.",
        "problema": "Los CV tradicionales no permiten mostrar procesos, decisiones técnicas ni evolución profesional.",
        "solucion": "Diseñé y desarrollé un portafolio web utilizando Flask, HTML y CSS.",
        "impacto": "Obtuve un espacio escalable, personal y técnico que crece junto a mis habilidades.",
        "tecnologias": ["Python", "Flask", "HTML", "CSS"],
        "links": {
            "Repositorio en GitHub": "https://github.com/Grisbeldcr/portafolio",
         }  
    },
    "analisis-datos" : {
        "titulo": "Análisis de Datos Aplicado",
        "categoria": "Proyectos profesionales",
        "contexto": "Trabajo con datos técnicos y operativos provenientes de sistemas, procesos y redes.",
        "problema": "La información existe, pero suele estar desordenada o sin análisis, lo que impide detectar patrones y oportunidades.",
        "solucion": "Análisis exploratorio, limpieza y visualización de datos.",
        "impacto": "Mejor toma de decisiones técnicas y estratégicas a partir de datos confiables.",
        "tecnologias": [],
        "links": {},    
    },
   "automatizacion-reportes": {
        "titulo": "Automatización de Procesos y Reportes",
        "categoria": "Proyectos profesionales",
        "contexto": "Procesos técnicos y administrativos con tareas repetitivas.",
        "problema": "Las tareas manuales consumen tiempo, generan errores y reducen la eficiencia operativa.",
        "solucion": "Automatización mediante scripts y generación de reportes.",
        "impacto": "Ahorro de tiempo, reducción de errores y mejora en la consistencia de la información.",
        "tecnologias": [],
        "links": {},
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
    },
     #"Aprendizaje Continuo en Tecnología" : {
     #   "titulo": 
     #   "categoria":
     #   "contexto": "El sector tecnológico exige actualización constante y adaptación a nuevas herramientas.",
     #   "problema": "Depender solo de la experiencia pasada limita el crecimiento profesional.",
     #   "solucion": "Plan de aprendizaje continuo en programación, análisis de datos, desarrollo web e inglés técnico.",
     #   "impacto": "Mayor autonomía, adaptabilidad y evolución constante del perfil profesional.",
     #   "tecnologias": []
    #    }
     #}
     #"Grisarito — En desarrollo : {
     #   "titulo": 
     #   "categoria":
     #   "contexto": "Proyecto creativo que integra diseño manual, comunicación visual y adaptación a distintas circunstancias.",
     #   "problema":
     #   "solucion":
     #   "impacto":
     #   "tecnologias": []
     #   "links":
    #}
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



