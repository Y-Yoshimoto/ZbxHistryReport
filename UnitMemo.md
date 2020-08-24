# Unitのセットアップについて

## アプリケーションの起動について
    Unitは、アプリケーションの起動するために、API経由でアプリケーションの設定を記載したjsonを投る必要があるため、コンテナ内でデーモンの実行、curlコマンドでアプリケーションを実行、その後コンテナを動かし続ける為のtailコマンドを実行する``docker-entrypoint.sh``をエントリーポイントとする。

## アプリケーションの実装について
    ``route_func.py``に呼び出す関数、``route_pass.py``にルーティング用のタプルを宣言する。
    ``wsgi.py``が各関数を、パスに基いて実行する。


## DBテストデータについて

### 郵便番号表のインポート
    日本郵便が公開している郵便番号データをダウンロードし、展開してcsvファイルを取り出す。
    [郵便番号データダウンロード] (https://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html)
    csvファイル(全国版:x-ken-all.csv)を``testdata``ディレクトリに入れ、
    ``nkf -w``で文字コードをUTF-8へ変換し、``convert.hs``をコンパイル及び実行する。容量が大きい場合は、csvファイルに対してgrepしておく。
    mariaDBに``--local-infile``オプションを付けた状態で接続し、``testdata``ディレクトリにあるSQLを使用して、データベース,テーブルの作成と権限付与、CSVファイルのインポートを行う。LOADで指定するcsvファイルのパスは、ローカル環境のフルパスを指定する。

## ダンプファイルの取得
以下のコマンでダンプファイルを生成し、次起動時に読み込めるようにしておく
``docker ps -a | grep unit_mariadb``
上記コマンドでポート番号を特定し、以下のコマンドでダンプファイルを取得する
``mysqldump -u root -p -h 127.0.0.1 -P {port} unit --hex-blob > mariadb_custom/unit_startup.sql``
