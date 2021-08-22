import requests
import pandas as pd

response = requests.get("https://valorant-api.com/v1/weapons")

data = response.json()

def additional_stats():
    weapon = data["data"]
    weapon_list = []
    for i in range(0, 17):
        name = weapon[i]["displayName"]
        fireRate = weapon[i]["weaponStats"]["fireRate"]
        magazineSize = weapon[i]["weaponStats"]["magazineSize"]
        seconds_to_spend_bullets = (magazineSize / fireRate)
        reload_time = weapon[i]["weaponStats"]["reloadTimeSeconds"]
        equip_time = weapon[i]["weaponStats"]["equipTimeSeconds"]
        new_item = {"name": name, "fireRate": fireRate, "magazineSize": magazineSize, "time before reload": f"{'{0:.2f}'.format(seconds_to_spend_bullets)} seconds", "reload_time": reload_time}
        weapon_list.append(new_item)
    sorted_weapon_list = sorted(weapon_list, key=lambda key: key['fireRate'])
    for object in sorted_weapon_list:
        print(object)



additional_stats()
