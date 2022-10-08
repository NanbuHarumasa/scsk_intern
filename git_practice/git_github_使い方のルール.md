# git・githubの使い方の手順・ルール
  - 前提1: gitにgithubを接続し、一人でinit, add, commit, push, pull, cloneができるようにしておく
  - 前提2: コラボレータとして登録してもらっておく

  0. `git clone`等で公開されているリポジトリをクローン
  - 以下繰り返し
  1. `git checkout main`等でローカルリポジトリ内のmainブランチに移動
  2. `git pull origin main`等でリモートリポジトリの最新情報を反映
  3. `git checkout -b future` `git checkout future`等でローカルリポジトリ内の開発用ブランチ(futureブランチ等)に移動
  4. 開発
  5. `git add .`等で変更をステージし、`git commit -m "メッセージ内容"`等でローカルリポジトリ内の開発用ブランチ(futureブランチ等)へコミット
  6. HTTPSでcommitするときは、自分のgithubアカウントのusernameとpasswordの入力が求められる。passwordにはトークンを入力するので事前に作っておく。また、もし5でメールアドレスやユーザー名が入力されていないというエラーがでたら、表示されるコマンドを実行(``--global``はなくてもよい。またメールアドレスやユーザー名は適当でよい。)
  7. `git push origin future`等でローカルでの変更内容をリモートリポジトリの開発用ブランチ(futureブランチ等)へプッシュ<br>__※絶対に`git push origin main`等で、ローカルでの変更内容を直接リモートリポジトリのmainブランチにpushしてはいけない！！__
  8. githubにサインインし、pushしたfutureブランチを開いてpull requestを出す
  9. pull requestを出した当人以外がコードのレビューを行い、問題なければmainブランチにマージする、コンフリクトが起こったら解消する
