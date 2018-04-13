# S3CaaTest
Test repository of AWS S3 cross account access.
外部アカウントのS3バケットからデータを取ってくる。

## 準備
対象のS3バケットとオブジェクトキーを控えておく。以下のenv-debug.ymlを作成する。

``` yml
BUCKET_NAME: 'your-backet-name'
KEY__NAME: 'data.json'
```

## Lambdaのデプロイ
事前に Shared Credentials を控えておく。

``` sh
$ sls deploy --aws-profile={YOUR_PROFILE} --function=runner --stage=debug
```

## Lambda実行

``` sh
# デプロイしたLambdaを実行
$ sls invoke --aws-profile={YOUR_PROFILE} --function=runner --stage=debug

# ローカル実行 (CredentialはLambdaに付与したIAMロールを使う)
$ sls invoke local --aws-profile={YOUR_PROFILE} --function=runner --stage=debug

# 実行ログ表示
$ sls logs --aws-profile={YOUR_PROFILE} --function=runner --stage=debug
```

## Lambda削除

``` sh
$ sls remove --aws-profile={YOUR_PROFILE} --stage=debug
```

