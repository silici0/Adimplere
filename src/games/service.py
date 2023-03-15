from src import config
import json
from src.games.domain.model import Games
import requests


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def gameDecoder(obj):
    if 'game-name' in obj:
        return Games(obj['game-name'], obj['description'], obj['long-term-description'])
    if 'name' in obj:
        return Games(obj['name'], obj['short-game-description'], obj['longgest-game-description'])
    if 'title' in obj:
        return Games(obj['title'], obj['shortDescription'], obj['longDescription'])
    return obj

def short_description():
    list = []
    links=[config.get_microsoft_url(), config.get_nintendo_url(), config.get_steam_url()]
    for url in links:
        data = requests.get(url)
        if validateJSON(data.text):
            list.append(gameDecoder(data.json()).__dict__)

    return list


def long_description(name: str):
    diclist = short_description()
    filterdList = list(filter(lambda x: name in x['title'], diclist))
    return filterdList
