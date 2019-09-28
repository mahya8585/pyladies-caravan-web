from flask import Flask
# from flask import request
import flask
app = Flask(__name__)


@app.route('/')
def show_index():
    return flask.render_template(
        'index.html'
    )

# ★課題1★ work-details.htmlを表示させるコントローラを作成してください


if __name__ == "__main__":
    app.run(debug=True)
