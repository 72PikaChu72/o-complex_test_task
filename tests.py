import tests
from main import getCoords, getForecast, getSuggestions

def test_getCoords():
    assert getCoords("Москва") == ('55.7540584', '37.62049')

def test_getForecast():
    assert getForecast(55.7558, 37.6173)["current_weather"]["temperature"] != None

def test_getSuggestions():
    assert getSuggestions("Москва")[0]["value"] == "г Москва"

def test_getCoords_nonexistent_city():
    assert getCoords("фывфыв") == (None, None)

def test_getSuggestions_nonexistent_prefix():
    assert getSuggestions("фывфыв") == []
