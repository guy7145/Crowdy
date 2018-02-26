api_key = 'AIzaSyDrB0OL0C7ufCwt_XFJx2JgkXhAqN38XaA'
# region products
clothing = 'clothing'
food = 'food'
drink = 'drink'
coffee = 'coffee'
book = 'book'
wheels = 'wheels'
medicine = 'medicine'
locks = 'locks'
# endregion


class NamedObj:
    def __init__(self, name):
        self.__name = name
        return

    def get_name(self):
        return self.__name


class World(NamedObj):
    def __init__(self, location, services, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__services = services
        self.location = location
        return

    def get_services(self):
        return self.__services


class Service(NamedObj):
    def __init__(self, vicinity, products, location, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__products = products
        self.vicinity = vicinity
        self.location = location
        return

    def get_products(self):
        return self.__products


worlds = [
    World(name='Big Beer Sheva', location={'lat': 31.243290, 'lng': 34.810145}, services=[
        Service(name="Be'er Sheva", vicinity="Be'er Sheva", location={'lat': 31.252973, 'lng': 34.791462}, products=[]),
        Service(name="Avazi", vicinity="Derech Hevron 21, Be'er Sheva", location={'lat': 31.2438256, 'lng': 34.809784}, products=[food, drink]),
        Service(name="Ziv Kitchens", vicinity="דיזיין פלוס, דרך חברון 48, באר שבע", location={'lat': 31.243357, 'lng': 34.809923}, products=[food, drink, coffee]),
        Service(name="סטימצקי", vicinity="Derekh Hebron 21, Be'er Sheva", location={'lat': 31.243857, 'lng': 34.809777}, products=[book]),
        Service(name="Golf Kids", vicinity="מרכז ביג, דרך חברון, באר שבע", location={'lat': 31.2430792, 'lng': 34.8106247}, products=[clothing]),
        Service(name="Castro", vicinity="ביג באר שבע, דרך חברון 21, באר שבע", location={'lat': 31.2433956, 'lng': 34.8106206}, products=[clothing]),
        Service(name="FOX HOME", vicinity="דרך חברון 21, Be'er Sheva", location={'lat': 31.2431322, 'lng': 34.8106028}, products=[clothing]),
        Service(name="Super-Pharm", vicinity='ביג ב"ש, חיל ההנדסה 2, באר שבע', location={'lat': 31.2434531, 'lng': 34.8106207}, products=[medicine]),
        Service(name="Studio posing - Events", vicinity="Derekh Hebron 60, Be'er Sheva", location={'lat': 31.243857, 'lng': 34.809777}, products=[drink]),
        Service(name="GOLF&Co", vicinity="דרך חברון 21, Be'er Sheva", location={'lat': 31.2429509, 'lng': 34.8106633}, products=[clothing, coffee]),
        Service(name="גולף", vicinity="מרכז ביג דרך חברון, Be'er Sheva", location={'lat': 31.243855, 'lng': 34.809778}, products=[clothing, coffee]),
        Service(name="פולגת", vicinity="מרכז ביג, דרך חברון, Be'er Sheva", location={'lat': 31.243855, 'lng': 34.809778}, products=[clothing]),
        Service(name="Max Moretti", vicinity="מרכז ביג דרך חברון, Be'er Sheva", location={'lat': 31.243855, 'lng': 34.809778}, products=[clothing]),
        Service(name="אינטימה", vicinity="דרך חברון מרכז ביג, Be'er Sheva", location={'lat': 31.243855, 'lng': 34.809778}, products=[clothing]),
        Service(name="גולף קו", vicinity="מרכז ביג דרך חברון, Be'er Sheva", location={'lat': 31.243855, 'lng': 34.809778}, products=[clothing]),
        Service(name="Israeli Promotion", vicinity="Derech Hevron 21, Be'er Sheva", location={'lat': 31.243857, 'lng': 34.809777}, products=[clothing]),
        Service(name="שילב", vicinity="מתחם ביג, דרך חברון 21, באר שבע", location={'lat': 31.2438855, 'lng': 34.81055049999999}, products=[clothing, coffee]),
        Service(name="Uri locksmith in Beersheba", vicinity="Derech Hevron 15, Be'er Sheva", location={'lat': 31.2439409, 'lng': 34.8097568}, products=[locks, coffee]),
        Service(name="נאפיס", vicinity="מרכז ביג, דרך חברון 62, באר שבע", location={'lat': 31.2426297, 'lng': 34.8106313}, products=[food, drink, coffee]),
        Service(name="גלגלי הנגב", vicinity="Derekh Hebron 19, Be'er Sheva", location={'lat': 31.2439409, 'lng': 34.8097569}, products=[wheels, coffee])
    ])
]


# import googlemaps
# from datetime import datetime
#
# gmaps = googlemaps.Client(key=api_key)
# query = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}&location={},{}&radius={}'
# query = query.format(api_key, 31.243290, 34.810145, 100)
# res = fetch_url(query, return_bytes=True)
# res = res.decode('utf-8')
# places = json.loads(res, encoding='utf-8')
#
# services = []
#
#
# def print_dict(d, depth=0):
#     if type(d) == dict:
#         for k, v in d.items():
#             # print('{}: '.format(k))
#             print_dict(v, depth + 1)
#         if 'name' in d.keys():
#             services.append('Service(name="{}", vicinity="{}", location={})'.format(d['name'], d['vicinity'], d['geometry']['location']))
#     elif type(d) == list:
#         for v in d:
#             print_dict(v, depth + 1)
#     else:
#         # print(d)
#         return d
#
#
# print_dict(places)
# print(services)
# for x in bla:
#     print(x[0])
#     print(x[1])
#     print(gmaps.geocode(x[1]))
#
