import flask
app = flask.Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/hello/<string:user_name>')
def hello_user(user_name):
    return '{uname}さん、こんちわ！'.format(uname=user_name)


@app.route('/greeting')
def greeting():
    user = flask.request.args.get('user')
    user_sec = flask.escape(user)
    display = 'やぁやぁ! ' + user_sec
    return flask.render_template_string(display)
    
    
if __name__ == '_main__':
    app.run()