from bs4 import BeautifulSoup
import requests

url = "https://fantasy.espn.com/baseball/players/add?leagueId=2090495493"
result = requests.get(url)
website_code = result.text
doc = BeautifulSoup(website_code, "html.parser")
print(doc.prettify())

player_name = doc.find_all(text="Ohtani")
print(player_name)







