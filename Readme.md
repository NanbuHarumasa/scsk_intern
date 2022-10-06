# scsk_intern_supuapp_sample
## How to use
1. `https://www.curict.com/item/60/60bfe0e.html`などを参考にPCにGitをインストール
2. PowerShell等で任意のディレクトリに移動し`git clone https://github.com/taiseifujisawa/scsk_intern_supuapp_sample.git`を実行してリポジトリをクローン
3. `cd scsk_intern_supuapp_sample`でディレクトリを移動
4. flaskの環境変数として`FLASK_APP=test`、`FLASK_ENV=development`を設定(Powershellの場合は`./set_envconst`を実行すれば自動で設定される。PowerShellのスクリプトを実行できない場合は、管理者権限でPowerShellを起動し、`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`を先に実行する。)
5. `flask run`でサーバーを起動
6. `localhost:5000`にアクセス


