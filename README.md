# pyladies-caravan-web
PyLadies Caravan 登壇資料

## 当日にたたいたコード

## アプリ起動方法
> cd [ディレクトリパス]/pyladies-caravan-web    
> python controller.py

### Hello Flask
controller.py を新規作成
```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
    

# 実行処理が見つからない場合、この処理を行ってくださいという指令
if __name__ == "__main__":
    app.run()
```

### Hello WebAPI
- http://localhost:5000/greeting/ユーザ名
```
@app.route('/greeting/<string:user_name>')
def greeting_user(user_name):
    return '{uname}さん、こんばんは！'.format(uname=user_name)
```

- http://localhost:5000/greeting?user=ユーザ名
```
from flask import request

@app.route('/greeting')
def greeting_name():
    user = request.args.get('user')
    return '{uname}さん、おはよう？'.format(uname=user)
```

## Hello 画面表示
- templates ディレクトリの作成
- index.htmlの作成
```
<title>welcome!</title>
<h1>Welcome! {{name}}さん!</h1>
```

- controller.pyへの追記
```
import flask

@app.route('/welcome/<string:user_name>')
def welcome_index(user_name):
    return flask.render_template(
        'index.html',
        name=user_name
    )
```

- http://localhost:5000/welcome/ユーザ名

### additional-post formの作成-
- echo.htmlをtemplatesディレクトリ内に作成
```
<!-- bodyタグ内に下記を追記 -->
<p>あなたの打った文字はこちら</p>
<h1>{{echo}}</h1>
```

- index.htmlのbodyタグ内に下記を追記
```
<form action="/echo" method="POST">
   <input type="text" name="input_word" />
   <button type="submit">GO!</button>
</form>
```

- controller.pyに追記
```
@app.route('/echo', methods=['POST'])
def echo():
   echo_word = request.form['input_word']
   return flask.render_template(
       'echo.html',
       echo=echo_word
   )
```

- http://localhost:5000/welcome/ユーザ名

## hello サイバー攻撃
（このコードがサイバー攻撃なわけではありませんが、この仕組みを悪用すると攻撃できてしまいます。Chromeは賢いので下記コードは実行されません。IEなどでお試しください)    
- controller.pyに追記
```
@app.route('/injection')
def hello_injection():
    name = flask.request.args.get('name')
    hello_b = 'hello' + name
    return flask.render_template_string(hello_b)
```
- http://localhost:5000/injection?name=ユーザ名
  - 普通に「hello ユーザ名」と表示される
- http://localhost:5000/injection?name=maaya<script>alert("hack")</script>
  - ユーザ名表示の前にアラートポップアップが表示されてしまう

### 改善案
escape処理を使って、「送られてきたgetパラメータはすべて文字列として取り扱う」ように処理してから表示させる    
- controller.pyのdef injectionを書き換え
```
@app.route('/injecrtion')
def hello_injection():
    name = flask.request.args.get('name')
    name_esc = flask.escape(name)   # <---- ★
    hello_b = 'hello' + name_esc    # <---- ★
    return flask.render_template_string(hello_b)
```

- http://localhost:5000/injection?name=maaya<script>alert("hack")</script>
  - 「hello maaya<script>alert("hack")</script>」と表示され、ポップアップが表示されない


## 課題
### 課題1
controller.py    
/templates/work-details.htmlを表示させるコントローラを作成してください。    

### 課題2
/template/index.html    
work-details.htmlへのリンクを作成してください。    
html内に2箇所設定しています。（「課題」で検索すると見つけやすいです)

### 課題3
/templates/works-details.html    
/static/images/caravan ディレクトリ内の画像がすべて表示されるように記述してください。    
loop文を使って表示してください。    
