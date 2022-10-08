# scsk_intern
## How to use
1. `https://www.curict.com/item/60/60bfe0e.html`などを参考にPCにGitをインストール、python3.10等をインストール
2. PowerShell等で任意のディレクトリに移動し`git clone https://github.com/taiseifujisawa/scsk_intern.git`を実行してリポジトリをクローン
3. `cd scsk_intern`でディレクトリを移動
4. flaskの環境変数として`FLASK_APP=supu_app`、`FLASK_ENV=development`を設定(Powershellの場合は`./set_envconst`を実行すれば自動で設定される。PowerShellのスクリプトを実行できない場合は、管理者権限でPowerShellを起動し、`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`を先に実行する。)
5. 必要に応じて仮想環境を立ち上げ(先に`pip install venv`が必要かもしれない)、`python -m pip install -r requirements.txt`を実行
6. `flask run`でサーバーを起動
7. `localhost:5000`にアクセス

## To do
- flaskではDBのバリデーションチェックが外部モジュール依存で、現状inputタグの空文字入力はinputタグ内のrequiredで禁止しているので、外部モジュール適用or他フレームワーク使用を検討
  - そもそもSQLiteではDatetime型がサポート外で、現状正規表現でYYYY-MM-DD以外の入力を禁止している
- ログイン機能を追加
  - パスワードのハッシュ化
- CSSで装飾

- AWSのDBの使い方の勉強、AWSへのデプロイ方法の勉強
