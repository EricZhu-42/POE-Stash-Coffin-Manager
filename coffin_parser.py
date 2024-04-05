import csv

CATEGORIES = ["Beast", "Demon", "Undead", "Humanoid", "Construct"]
METADATA_FILE = "mods.csv"

class CoffinParser:
    def __init__(self):
        pass
    
    def load_metadata(self):
        data = {}

        with open(METADATA_FILE, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)

            for row in reader:
                mod, mod_type, name = row

                mod = mod.strip()
                mod_type = mod_type.strip()
                name = name.strip()

                if not len(mod_type):
                    continue
                
                if mod_type not in data:
                    data[mod_type] = {}
                    
                data[mod_type][mod] = {"name": name, "total_count": 0, "sub_counts": {cat: 0 for cat in CATEGORIES}}

        return data
    
    def parse_coffin(self, coffins, *, verbose=False):
        data = self.load_metadata()
        unparsed_mods = set()

        for c in coffins:
            imp = c["implicit"]
            cat = c["category"]

            success = False
            for mode_type in data.keys():
                if imp in data[mode_type]:
                    data[mode_type][imp]["sub_counts"][cat] += 1
                    data[mode_type][imp]["total_count"] += 1
                    success = True
                    break
            
            if verbose and not success and imp not in unparsed_mods:
                unparsed_mods.add(imp)
                print("Unparsed mod:", imp)

        return data