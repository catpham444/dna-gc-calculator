from flask import Flask, request, render_template_string
from gc_calculator import gc_content

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open("index.html") as f:
        return f.read()

@app.route("/gc", methods=["POST"])
def gc():
    seq = request.form["sequence"]
    result = gc_content(seq)
    return f"<h1>GC Content: {result}%</h1><br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
