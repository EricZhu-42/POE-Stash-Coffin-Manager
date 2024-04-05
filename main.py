import json

from stash_parser import StashParser
from coffin_parser import CoffinParser
from price_parser import PriceParser

VERBOSE = False

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
            if data[cat][mod]["count"] > 0:

                if not should_print:
                    should_print = True
                    lines.append(f"============= {cat:^14} =============")

                name = data[cat][mod]['name']
                stock = data[cat][mod]['count']
                price = round(price_parser.get_price(mod))
                
                lines.append(
                    f"{name:<18} | {price:<3} c/ea | Stock: {stock:<2}"
                )
    
    lines = "\n".join(lines)

    print(lines)

if __name__ == "__main__":
    main()
                               