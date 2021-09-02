import genshinstats as gs
from genshinstats import wishes, daily, hoyolab
from pprint import pprint

# gs.set_cookie(ltuid=119480035, ltoken="cnF7TiZqHAAvYqgCBoSPx5EjwezOh1ZHoqSHf7dT")
gs.set_cookies_auto('chrome')

uid = wishes.get_uid_from_authkey()
data = gs.get_user_stats(uid)
total_characters = len(data['characters'])
pyro = 0
hydro = 0
cryo = 0
electro = 0
geo = 0
anemo = 0
print('user "SovsemNeNao" has a total of', total_characters, 'characters')
characters = gs.get_characters(uid)
# for char in characters:
#     print(f"{char['rarity']}* {char['name']:10} | lvl {char['level']:2} C{char['constellation']}")
# pprint(data)
# for character in data['characters']:
#     if character['element'] == 'Pyro':
#         pyro += 1
#     elif character['element'] == 'Hydro':
#         hydro += 1
#     elif character['element'] == 'Cryo':
#         cryo += 1
#     elif character['element'] == 'Electro':
#         electro += 1
#     elif character['element'] == 'Anemo':
#         anemo += 1
#     elif character['element'] == 'Geo':
#         geo += 1
# print(f"Anemo: {anemo},\nPyro: {pyro},\nCryo: {cryo},\nHydro: {hydro},\nElectro: {electro},\nGeo: {geo}\n")
# for i in gs.get_wish_history(size=10, banner_type=301):
#     print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
# pprint(wishes.get_gacha_items())
фцdaily.claim_daily_reward()
print(uid)
chars = gs.get_characters(uid=uid)
pprint(chars)