import os
from typing import Any
from dotenv import load_dotenv

load_dotenv()

DEFAULT_ENV = "dev"
MICROSOFT_STORE_URL = "https://assets.adimplere.com.br/adimplere_test/" \
    "microsoftstore.json"
NINTENDO_STORE_URL = "https://assets.adimplere.com.br/adimplere_test/" \
    "nintendostore.json"
STEAM_URL = "https://assets.adimplere.com.br/adimplere_test/steam.json"


def get_envar(key: str, default: Any = None) -> str:
    envar = os.getenv(key, default)
    if envar is None:
        raise RuntimeError(f"ENVAR {key} isn't set")
    return envar


def get_environment() -> str:
    return get_envar("ENV", DEFAULT_ENV)


def get_app_name() -> str:
    return "Adimplere Server @ " + get_environment()


def get_microsoft_url() -> str:
    return get_envar("NINTENDO_STORE_URL", NINTENDO_STORE_URL)


def get_nintendo_url() -> str:
    return get_envar("MICROSOFT_STORE_URL", MICROSOFT_STORE_URL)


def get_steam_url() -> str:
    return get_envar("STEAM_URL", STEAM_URL)
