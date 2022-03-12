# btctry-deta


[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sadikkuzu/btctry-deta/main.svg)](https://results.pre-commit.ci/latest/github/sadikkuzu/btctry-deta/main)


### Deployment

[Deta](https://deta.sh)

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/sadikkuzu/btctry-deta)

![image](https://user-images.githubusercontent.com/23168063/157983832-4eb5b136-1de7-44cb-8442-a9176e2405b2.png)


#### [Environment Variables](https://docs.deta.sh/docs/micros/env_vars)

```shell
deta update -e .env
```

#### [Cron](https://docs.deta.sh/docs/micros/cron)

```shell
deta cron set "0 10 * * ? *"
```


### Development

```shell
pip install -Ur requirements-dev.txt
pre-commit install
pre-commit run --all-files
pytest --cov=btctry --cov-report term-missing tests/
```

```shell
uvicorn main:app --reload
```
