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
Shared Credentials を控えておく。

``` sh
$ sls deploy --aws-profile={YOUR_PROFILE} --function=runner --stage=debug
```
