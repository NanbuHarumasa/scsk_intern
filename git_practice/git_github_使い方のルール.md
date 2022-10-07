# git・githubの使い方の手順・ルール
  - 前提: gitにgithubを接続し、一人でinit, add, commit, push, pull, cloneができるようにしておく
  0. `git clone`等で公開されているコード等をクローン
  - 以下繰り返し
  1. `git checkout main`等でローカルリポジトリ内のmainブランチに移動
  2. `git pull`等でリモートリポジトリの最新情報を反映
  3. `git checkout -b future` `git checkout future`等でローカルリポジトリ内の開発用ブランチ(futureブランチ等)に移動
  4. 開発
  5. `git add .`等で変更をステージし、`git commit`等でローカルリポジトリ内の開発用ブランチ(futureブランチ等)へコミット
  6. `git push origin future`等でローカルでの変更内容をリモートリポジトリの開発用ブランチ(futureブランチ等)へプッシュ<br>__※絶対に`git puch origin main`等で、ローカルでの変更内容を直接リモートリポジトリのmainブランチにpushしてはいけない！！__
  7. githubにサインインし、pushしたfutureブランチを開いてpull requestを出す
  8. pull requestを出した当人以外がコードのレビューを行い、問題なければマージ、コンフリクトが起こったら解消する
