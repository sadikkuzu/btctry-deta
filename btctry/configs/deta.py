from os import environ as env


class DetaConfig:
    BASE_NAME = env.get("BASE_NAME", "btctry")
