from bs4 import BeautifulSoup
import requests
import openpyxl
with open(r"C:\Users\cherb\PycharmProjects\pythonProject1\Projects\ESPN_Fantasy.html", encoding="utf-8") as f:
    doc = BeautifulSoup(f, "html.parser")


# url = "https://fantasy.espn.com/baseball/players/add?leagueId=2090495493"
# result = requests.get(url)
# website_code = result.text
# doc = BeautifulSoup(website_code, "html.parser")
# print(doc.prettify())
#
# player_name = doc.find_all(text="Ohtani")
# print(player_name)


# Finds player names
tbody_tags = doc.find_all("a", class_="AnchorLink link clr-link pointer")
list_of_tags = []
list_of_players = []




for tag in tbody_tags:
    list_of_tags.append(tag)

for i in list_of_tags:
    player_names = i.next
    list_of_players.append(player_names)

for i in list_of_players:
    if i.startswith(" ("):
        list_of_players.remove(i)


print(list_of_players)








