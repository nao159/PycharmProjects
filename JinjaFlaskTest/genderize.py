import requests


def get_gender_and_name_and_age(name):
    """It return a list contents of random name with its probably gender"""
    link = f"https://api.genderize.io?name={name}"

    genderize_request = requests.get(url=link)
    data = genderize_request.json()

    data_name = data['name'].capitalize()
    data_gender = data['gender']

    data_age = get_age(name=name)

    new_list = {
        "name": data_name,
        "gender": data_gender,
        "age": data_age
    }
    return new_list


def get_age(name):
    """It returns a single Int element"""
    link = f"https://api.agify.io/?name={name}&country_id=RU"

    random_age_request = requests.get(url=link)
    data = random_age_request.json()

    age = data['age']
    return age

