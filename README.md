# Private ISU 用 CDK

```shell
npm install -g aws-cdk
```

```shell
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

```
pip3 install poetry
poetry install
poetry shell
```

`~/.aws/config`

```
[default]
aws_access_key_id = hoge
aws_secret_access_key = hoge
```

`~/.aws/credentials`

```
[default]
region = ap-northeast-1
output = json
```

```shell
aws config
```

```
cdk ls
cdk synth
cdk deploy
cdk destroy PrivateIsuStack
```

## License

This repository is licensed under the MIT license.
Froked from https://github.com/hoto17296/churadata-isucon
