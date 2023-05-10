from flask import Flask, request, url_for, render_template

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="")

"""Homepage"""

@app.route('/home/')
@app.route('/')
def root():
    return render_template(
        'index.html'
    )

"""Page About me"""

@app.route('/about/')
def about():
    return render_template(
        'about.html'
    )


