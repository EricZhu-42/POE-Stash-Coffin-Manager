import csv

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
                mod, cat, name = row

                mod = mod.strip()
                cat = cat.strip()
                name = name.strip()

                if not len(cat):
                    continue
                
                if cat not in data:
                    data[cat] = {}
                    
                data[cat][mod] = {"name": name, "count": 0}
    
        return data
    
    def parse_coffin(self, coffins, *, verbose=False):
        data = self.load_metadata()

        coffin_counter = dict()

        for c in coffins:
            imp = c["implicit"]
            if imp in coffin_counter:
                coffin_counter[imp] += 1
            else:
                coffin_counter[imp] = 1

        for mod, count in coffin_counter.items():
            success = False
            for cat, mods in data.items():
                if mod in mods:
                    mods[mod]["count"] = count
                    success = True
    
            if verbose and not success:
                print(f"Unknown mod: {mod}")
        
        return data