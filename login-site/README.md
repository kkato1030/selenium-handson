# login-site

Selenium の使い方を学ぶためのサンプル用サイトです。

## セットアップ

以下コマンドで環境をセットアップします。

```
$ npm install
$ amplify init
$ amplify push
```

表示される URL にアクセスし、ログイン画面が表示されるか確認しましょう。

## ユーザー作成

ユーザーを簡単に作成できるよう、scripts/create_users.sh を作成しています。
スクリプトを実行することで以下のユーザーを作成できます。

- ユーザー名: TestUser-1 〜 TestUser10
- パスワード: Passw0rd!(共通)

### 設定

利用する際はファイルを開き、ご自身の環境の **Cognito ユーザープールID** および **クライアントID** を入力してください。
(※アプリクライアントは 2 つ作成されていると思いますが、シークレットキーが無い方の ID をご利用ください)

```
# Variables
USER_POOL_ID="ap-northeast-1_XXXXXXXXXX"  # Modify
CLIENT_ID="XXXXXXXXXXXXXXXXXXXXXXXXXX"  # Modify
```

なお以下の値を変更することも可能です。

```
REGION="ap-northeast-1"  # Can Modify
USERNAME_PREFIX="TestUser" # Can Modify
PASSWORD="Passw0rd!" # Can Modify
```

| 値 | 説明 |
| -- | -- |
| REGION | Cognito が存在するリージョン |
| USERNAME_PREFIX | ユーザー作成時の名前が変わる |
| PASSWORD | ユーザー作成時のパスワードが変わる |

## 実行

設定が終わったらスクリプトを実行します。

```
$ ./scripts/create_users.sh
```



