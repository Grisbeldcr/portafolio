from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {
            "title": "Análisis de datos de ventas",
            "tech": "Python, Pandas, Matplotlib",
            "description": "Exploración y visualización de datos comerciales"
        },
        {
            "title": "Sistema de gestión en Java",
            "tech": "Java, POO",
            "description": "Aplicación CRUD con clases y herencia"
        }
    ]
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)


