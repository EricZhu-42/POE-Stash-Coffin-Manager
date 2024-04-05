import requests

class PriceParser:
    def __init__(self):
        self.load_price()

    def load_price(self):
        URL = "https://poe.ninja/api/data/itemoverview?league=Necropolis&type=Coffin"

        r = requests.get(URL, proxies=None)
        data = r.json()

        lvl_80_data = [item for item in data["lines"] if item["levelRequired"] == 80]

        mapping = {item["baseType"]: item["chaosValue"] for item in lvl_80_data}

        for family in ["Phrecia", "Grattus", "Veruso", "Perandus", "Nevalius"]:
            mapping[f"Haunted by * {family}"] = sum(item["chaosValue"] for item in lvl_80_data if item["baseType"].endswith(family)) / 4

        self.mapping = mapping
    
    def get_price(self, item):
        return self.mapping.get(item, None)

if __name__ == "__main__":
    print(PriceParser().mapping)