from dotenv import load_dotenv

from settings import Settings


def test_settings_load_expected_test_values() -> None:
    load_dotenv("config/.env.test", override=True)

    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "Lab1 MLOps Intro Test"
    assert settings.API_KEY == "fake-test-api-key"
