import json

from stash_parser import StashParser
from coffin_parser import CoffinParser
from price_parser import PriceParser

VERBOSE = True
SHOW_CAT = True

def main():

    with open("config.json", "r") as f:
        config = json.load(f)

    parser = StashParser(config)
    coffins = parser.get_coffins()

    coffin_parser = CoffinParser()
    data = coffin_parser.parse_coffin(coffins, verbose=VERBOSE)

    price_parser = PriceParser()

    lines = []

    for cat in data:
        if not len(cat):
            continue

        should_print = False
        for mod in data[cat]:
            if data[cat][mod]["total_count"] > 0:

                if not should_print:
                    should_print = True

                    if SHOW_CAT:
                        corner = 34
                    else:
                        corner = 9

                    lines.append("="*corner + f" {cat:^22} " + "="*corner)

                name = data[cat][mod]['name']
                stock = data[cat][mod]['total_count']
                price = round(price_parser.get_price(mod))

                line = f"{name:<18} | {price:<3} c/ea | Stock: {stock:<3}"

                if SHOW_CAT:
                    line += f" => Dem: {data[cat][mod]['sub_counts']['Demon']:<2} | Bea: {data[cat][mod]['sub_counts']['Beast']:<2} | Und: {data[cat][mod]['sub_counts']['Undead']:<2} | Hum: {data[cat][mod]['sub_counts']['Humanoid']:<2} | Con: {data[cat][mod]['sub_counts']['Construct']:<2}"
                
                lines.append(line)
    
    lines = "\n".join(lines)

    print(lines)

if __name__ == "__main__":
    main()
                               