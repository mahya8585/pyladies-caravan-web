from flask import Flask
import flask
import glob
import os
app = Flask(__name__)


@app.route('/')
def show_index():
    return flask.render_template(
        'index.html'
    )

# ★課題1★ work-details.htmlを表示させるコントローラを作成してください
@app.route('/about')
def show_about_us():
    image_list = glob.glob(os.path.join('.',  'static', 'images', 'caravan', '*'))
    images = []
    for i in image_list:
        images.append(os.path.basename(i))

    return flask.render_template(
        'works-details.html',
        images=images
    )


if __name__ == "__main__":
    app.run(debug=True)
