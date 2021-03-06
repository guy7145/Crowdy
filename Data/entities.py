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
        self.name = name
        return

    def get_name(self):
        return self.name


class World(NamedObj):
    def __init__(self, location, services, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__services = {s.get_name(): s for s in services}
        self.location = location
        return

    def get_services(self):
        return self.__services


class Service(NamedObj):
    def __init__(self, vicinity, categories, location, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories = categories
        self.vicinity = vicinity
        self.lat = location['lat']
        self.lng = location['lng']
        return

    def get_categories(self):
        return self.categories

    def __repr__(self):
        return 'service: {},{},{},{},{}'.format(self.get_name(), self.vicinity, self.lat, self.lng, self.categories)

    def __dict__(self):
        return {'name': self.get_name(), 'status': 0, 'lat': self.lat, 'lng': self.lng, 'categories': self.categories}


worlds = {
    w.get_name(): w for w in [World(name="Big_BS", location={"lat": 31.243290, "lng": 34.810145}, services=[
        Service(name="Beer Sheva", vicinity="Beer Sheva", location={"lat": 31.252973, "lng": 34.791462}, categories=[]),
        Service(name="Avazi", vicinity="Derech Hevron 21, Be'er Sheva", location={"lat": 31.2438256, "lng": 34.809784}, categories=[food, drink]),
        Service(name="Ziv Kitchens", vicinity="דיזיין פלוס, דרך חברון 48, באר שבע", location={"lat": 31.243357, "lng": 34.809923}, categories=[food, drink, coffee]),
        Service(name="סטימצקי", vicinity="Derekh Hebron 21, Be'er Sheva", location={"lat": 31.243857, "lng": 34.809777}, categories=[book]),
        Service(name="Golf Kids", vicinity="מרכז ביג, דרך חברון, באר שבע", location={"lat": 31.2430792, "lng": 34.8106247}, categories=[clothing]),
        Service(name="Castro", vicinity="ביג באר שבע, דרך חברון 21, באר שבע", location={"lat": 31.2433956, "lng": 34.8106206}, categories=[clothing]),
        Service(name="FOX HOME", vicinity="דרך חברון 21, Be'er Sheva", location={"lat": 31.2431322, "lng": 34.8106028}, categories=[clothing]),
        Service(name="Super-Pharm", vicinity='ביג ב"ש, חיל ההנדסה 2, באר שבע', location={"lat": 31.2434531, "lng": 34.8106207}, categories=[medicine]),
        Service(name="Studio posing - Events", vicinity="Derekh Hebron 60, Be'er Sheva", location={"lat": 31.243857, "lng": 34.809777}, categories=[drink]),
        Service(name="GOLF&Co", vicinity="דרך חברון 21, Be'er Sheva", location={"lat": 31.2429509, "lng": 34.8106633}, categories=[clothing, coffee]),
        Service(name="גולף", vicinity="מרכז ביג דרך חברון, Be'er Sheva", location={"lat": 31.243855, "lng": 34.809778}, categories=[clothing, coffee]),
        Service(name="פולגת", vicinity="מרכז ביג, דרך חברון, Be'er Sheva", location={"lat": 31.243855, "lng": 34.809778}, categories=[clothing]),
        Service(name="Max Moretti", vicinity="מרכז ביג דרך חברון, Be'er Sheva", location={"lat": 31.243855, "lng": 34.809778}, categories=[clothing]),
        Service(name="אינטימה", vicinity="דרך חברון מרכז ביג, Be'er Sheva", location={"lat": 31.243855, "lng": 34.809778}, categories=[clothing]),
        Service(name="גולף קו", vicinity="מרכז ביג דרך חברון, Be'er Sheva", location={"lat": 31.243855, "lng": 34.809778}, categories=[clothing]),
        Service(name="Israeli Promotion", vicinity="Derech Hevron 21, Be'er Sheva", location={"lat": 31.243857, "lng": 34.809777}, categories=[clothing]),
        Service(name="שילב", vicinity="מתחם ביג, דרך חברון 21, באר שבע", location={"lat": 31.2438855, "lng": 34.81055049999999}, categories=[clothing, coffee]),
        Service(name="Uri locksmith in Beersheba", vicinity="Derech Hevron 15, Be'er Sheva", location={"lat": 31.2439409, "lng": 34.8097568}, categories=[locks, coffee]),
        Service(name="נאפיס", vicinity="מרכז ביג, דרך חברון 62, באר שבע", location={"lat": 31.2426297, "lng": 34.8106313}, categories=[food, drink, coffee]),
        Service(name="גלגלי הנגב", vicinity="Derekh Hebron 19, Be'er Sheva", location={"lat": 31.2439409, "lng": 34.8097569}, categories=[wheels, coffee])])
                              ]
}


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
