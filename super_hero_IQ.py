import requests

class SuperHero():
    name = 'some_Name'
    iq = 1

def get_all_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    results = requests.get(url)
    return results.json()

def get_heroes_info(self):
    for id in get_all_heroes():
        if id['name'] == self.name:
            self.name = id['name']
            self.iq = id['powerstats']['intelligence']

def the_smartest():
    if Halk.iq == max(Halk.iq, Captain_America.iq, Thanos.iq):
        print(f'Самый умный: {Halk.name}')
    elif Captain_America.iq == max(Halk.iq, Captain_America.iq, Thanos.iq):
         print(f'Самый умный: {Captain_America.name}')
    else:
        print(f'Самый умный: {Thanos.name}')
        
Halk = SuperHero()
Halk.name = 'Halk'

Captain_America = SuperHero()
Captain_America.name = 'Captain America'

Thanos = SuperHero()
Thanos.name = 'Thanos'

if __name__ == "__main__":

    get_heroes_info(Halk)
    get_heroes_info(Captain_America)
    get_heroes_info(Thanos)

    the_smartest()
