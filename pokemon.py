from urllib.request import Request, urlopen
import json

class Pokemon:
    def __init__(self, data_url):
        req = Request(
            url=data_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urlopen(req) as url:
            data = json.load(url)

        self.id = data["id"]
        self.name = data["name"]
        self.cost = data["cost"]
        self.category = data["category"]["name"]
        self.attributes = []
        for attribute in data["attributes"]:
            self.attributes.append(attribute["name"])

    def json_convertion(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "category": self.category,
            "attributes": self.attributes
        }

    def __str__(self):
        to_return = f"Pokemon {self.id}\nname: {self.name}\ncosts: {self.cost}, category: {self.category}\nattributes: "
        for attribute in self.attributes:
            to_return += str(attribute) + ", "
        return to_return[:-2]