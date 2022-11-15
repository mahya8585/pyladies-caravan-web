# pyladies-caravan-web
PyLadies Caravan 登壇資料

## 当日にたたいたコード

## アプリ起動方法
> cd [ディレクトリパス]/pyladies-caravan-web    
> python app.py

### Hello Flask
app.py を新規作成
```
import flask
app = flask.Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
    

# 実行処理が見つからない場合、この処理を行ってくださいという指令
if __name__ == "__main__":
    app.run()
```

### Hello WebAPI
- http://localhost:5000/hello/ユーザ名
```
@app.route('/hello/<string:user_name>')
def hello_user(user_name):
    return '{uname}さん、こんちわ！'.format(uname=user_name)
```

- http://localhost:5000/greeting?user=ユーザ名
```
@app.route('/greeting')
def greeting():
    user = flask.request.args.get('user')
    display = 'やぁやぁ! ' + user
    return flask.render_template_string(display)
```



## hello サイバー攻撃
http://localhost:5000/greeting?user=<script>alert("hack")</script>

### 改善案
escape処理を使って、「送られてきたgetパラメータはすべて文字列として取り扱う」ように処理してから表示させる    
- controller.pyのdef injectionを書き換え
```
display = 'こんにちは! ' + flask.escape(user)
```

- http://localhost:5000/injection?name=maaya<script>alert("hack")</script>
  - 「hello maaya<script>alert("hack")</script>」と表示され、ポップアップが表示されない

   
