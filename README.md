# S3CaaTest
Test repository of AWS S3 cross account access.

外部アカウントのS3バケットからデータを取ってくる。

## 準備
対象のS3バケットとオブジェクトキーを控えておく。以下のenv-debug.ymlを作成する。

``` yml
BUCKET_NAME: 'your-backet-name'
KEY_NAME: 'data.json'
```

Serverless Frameworkをインストールしておく

``` sh
$ npm install serverless -g
```

## Lambdaのデプロイ
事前に Shared Credentials を控えておく。

``` sh
$ sls deploy --aws-profile={YOUR_PROFILE} --function=runner --stage=debug
```

## S3バケットポリシー設定
対象のS3バケットにバケットポリシーを設定する。

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{your_account_id}:role/S3Cross-debug-ap-northeast-1-lambdaRole"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{your-backet-name}/*"
        }
    ]
}
```

## Lambdaを実行

``` sh
# デプロイしたLambdaを実行
$ sls invoke --aws-profile={YOUR_PROFILE} --function=runner --stage=debug

# ローカル実行 ([default]のShared Credentialを使う)
$ sls invoke local --function=runner --stage=debug

# 実行ログ表示
$ sls logs --aws-profile={YOUR_PROFILE} --function=runner --stage=debug
```

## Lambda削除

``` sh
$ sls remove --aws-profile={YOUR_PROFILE} --stage=debug
```

