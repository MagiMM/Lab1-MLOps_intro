import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    allowed_environments = {"dev", "test", "prod"}
    if environment not in allowed_environments:
        raise ValueError(
            "The --environment argument must be one of: dev, test, prod. "
            f"Got: {environment!r}"
        )

    env_path = os.path.join("config", f".env.{environment}")
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Environment file not found: {env_path}")

    load_dotenv(dotenv_path=env_path, override=True)


def export_secret_envs(secrets_file: str = "secrets.decrypted.yaml") -> None:
    if not os.path.exists(secrets_file):
        raise FileNotFoundError(
            f"Secrets file not found: {secrets_file}. "
            "Create it with: sops --decrypt secrets.yaml > secrets.decrypted.yaml"
        )

    with open(secrets_file, "r", encoding="utf-8") as file:
        secrets = yaml.safe_load(file) or {}

    for key, value in secrets.items():
        if key == "sops":
            continue
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secret_envs()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
