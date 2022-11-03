# Infrastructure

## Getting Started

### Prerequisites

- aws cli
- terraform

AWS にて以下の資材は事前に作成されている

- IAM for the terraform operation
- S3 bucket for the tfstate management

### Installing

AWS terraform user の認証情報を開発環境にセットする。

```shell
# pwd -> packages/Infrastructure
# profile 名は loggy-dev で設定
aws configure list-profiles

# 認証情報を利用
aws configure --profile loggy-dev

# terraform で利用する profile を指定
export AWS_PROFILE=loggy-dev

# envs 配下の操作したい dir に移動
cd envs/dev
# terraform initialize
terraform init
```

### Deployment

```shell
# 差分をチェック
terraform plan

# 反映させる
terraform apply
```

## File Structure

```
- envs
|- dev # 開発環境
|- dev_iam # 開発環境の IAM 周り
```
