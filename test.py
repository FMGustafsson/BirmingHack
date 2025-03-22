import requests # type: ignore
import json
import toml
url = "https://api.themoviedb.org/3/authentication"
secrets = toml.load("./secrets.toml")
print(secrets)
headers = {
    "accept": "application/json",
    "Authorization": secrets["tmdb"]
}
response = requests.get(url, headers=headers)
print(response.text)
response2 = json.loads(requests.get("https://api.themoviedb.org/3/search/movie?query=To+Live+Die+In+LA", headers=headers).text)
film = response2["results"][0]
print(film)
response3 = json.loads(requests.get(f"https://api.themoviedb.org/3/movie/{film['id']}/credits", headers=headers).text)
print(response3)
castAndCrew = response3
cast = castAndCrew['cast']
crew = castAndCrew['crew']
for i in range(0,10):
    print(f"{cast[i]['name']} as {cast[i]['character']}")
for i in range(0,10):
    print(f"{crew[i]['name']} was {crew[i]['job']}")
