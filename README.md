# POE-Stash-Coffin-Manager
(League 3.24) Use the POE stash API to analyze the quantity and types of [Filled Coffin](https://www.poewiki.net/wiki/Filled_Coffin) items in stashes.

## Usage

1. Edit [config.json](https://github.com/EricZhu-42/POE-Stash-Coffin-Manager/blob/main/config.json), replace `POESESSID`, `accountName` and `tab_names`.
2. Run `python main.py`

## Sample output

```
================================       Increase 300%        ================================
Attack             | 5   c/ea | Stock: 3   => Dem: 1  | Bea: 0  | Und: 2  | Hum: 0  | Con: 0
Caster             | 5   c/ea | Stock: 11  => Dem: 1  | Bea: 2  | Und: 5  | Hum: 1  | Con: 2
Elemental          | 4   c/ea | Stock: 5   => Dem: 0  | Bea: 0  | Und: 4  | Hum: 0  | Con: 1
Prefix             | 5   c/ea | Stock: 3   => Dem: 1  | Bea: 1  | Und: 0  | Hum: 1  | Con: 0
Suffix             | 4   c/ea | Stock: 3   => Dem: 0  | Bea: 1  | Und: 2  | Hum: 0  | Con: 0
================================       Increase 500%        ================================
Attribute          | 5   c/ea | Stock: 8   => Dem: 1  | Bea: 2  | Und: 2  | Hum: 3  | Con: 0
Chaos              | 5   c/ea | Stock: 7   => Dem: 0  | Bea: 1  | Und: 4  | Hum: 0  | Con: 2
Cold               | 5   c/ea | Stock: 6   => Dem: 0  | Bea: 3  | Und: 1  | Hum: 1  | Con: 1
Critical           | 15  c/ea | Stock: 3   => Dem: 0  | Bea: 1  | Und: 1  | Hum: 1  | Con: 0
Defence            | 5   c/ea | Stock: 9   => Dem: 0  | Bea: 2  | Und: 4  | Hum: 2  | Con: 1
Fire               | 5   c/ea | Stock: 7   => Dem: 0  | Bea: 2  | Und: 3  | Hum: 2  | Con: 0
Gem                | 15  c/ea | Stock: 3   => Dem: 1  | Bea: 1  | Und: 0  | Hum: 1  | Con: 0
Life               | 5   c/ea | Stock: 3   => Dem: 0  | Bea: 0  | Und: 0  | Hum: 3  | Con: 0
Lightning          | 5   c/ea | Stock: 10  => Dem: 2  | Bea: 2  | Und: 3  | Hum: 3  | Con: 0
Mana               | 5   c/ea | Stock: 12  => Dem: 0  | Bea: 3  | Und: 6  | Hum: 1  | Con: 2
Minion             | 5   c/ea | Stock: 1   => Dem: 0  | Bea: 1  | Und: 0  | Hum: 0  | Con: 0
Physical           | 4   c/ea | Stock: 9   => Dem: 0  | Bea: 2  | Und: 4  | Hum: 2  | Con: 1
Resistance         | 5   c/ea | Stock: 2   => Dem: 0  | Bea: 1  | Und: 1  | Hum: 0  | Con: 0
================================        Scarcer 150%        ================================
Attack             | 10  c/ea | Stock: 3   => Dem: 0  | Bea: 1  | Und: 0  | Hum: 0  | Con: 2
Caster             | 5   c/ea | Stock: 7   => Dem: 2  | Bea: 1  | Und: 3  | Hum: 0  | Con: 1
Elemental          | 15  c/ea | Stock: 1   => Dem: 0  | Bea: 1  | Und: 0  | Hum: 0  | Con: 0
================================        Scarcer 300%        ================================
Attribute          | 10  c/ea | Stock: 2   => Dem: 0  | Bea: 1  | Und: 1  | Hum: 0  | Con: 0
Chaos              | 10  c/ea | Stock: 1   => Dem: 0  | Bea: 0  | Und: 1  | Hum: 0  | Con: 0
Cold               | 5   c/ea | Stock: 5   => Dem: 2  | Bea: 1  | Und: 2  | Hum: 0  | Con: 0
Critical           | 5   c/ea | Stock: 5   => Dem: 0  | Bea: 2  | Und: 1  | Hum: 0  | Con: 2
Defence            | 5   c/ea | Stock: 4   => Dem: 0  | Bea: 1  | Und: 2  | Hum: 1  | Con: 0
Fire               | 5   c/ea | Stock: 3   => Dem: 0  | Bea: 0  | Und: 0  | Hum: 2  | Con: 1
Life               | 10  c/ea | Stock: 1   => Dem: 0  | Bea: 0  | Und: 1  | Hum: 0  | Con: 0
Lightning          | 5   c/ea | Stock: 4   => Dem: 2  | Bea: 0  | Und: 2  | Hum: 0  | Con: 0
Mana               | 10  c/ea | Stock: 5   => Dem: 1  | Bea: 1  | Und: 1  | Hum: 2  | Con: 0
Physical           | 10  c/ea | Stock: 5   => Dem: 1  | Bea: 1  | Und: 2  | Hum: 0  | Con: 1
Resistance         | 30  c/ea | Stock: 5   => Dem: 0  | Bea: 2  | Und: 1  | Hum: 1  | Con: 1
Speed              | 5   c/ea | Stock: 6   => Dem: 0  | Bea: 2  | Und: 2  | Hum: 2  | Con: 0
================================       Meta Crafting        ================================
+1 Explicit        | 5   c/ea | Stock: 20  => Dem: 5  | Bea: 6  | Und: 4  | Hum: 4  | Con: 1
+1 Item Level      | 5   c/ea | Stock: 22  => Dem: 2  | Bea: 7  | Und: 8  | Hum: 0  | Con: 5
+5 to Quality      | 4   c/ea | Stock: 10  => Dem: 2  | Bea: 3  | Und: 4  | Hum: 0  | Con: 1
-1 Explicit        | 5   c/ea | Stock: 5   => Dem: 1  | Bea: 1  | Und: 3  | Hum: 0  | Con: 0
20% additional     | 209 c/ea | Stock: 2   => Dem: 1  | Bea: 0  | Und: 1  | Hum: 0  | Con: 0
25% effect Column  | 5   c/ea | Stock: 4   => Dem: 1  | Bea: 1  | Und: 1  | Hum: 0  | Con: 1
25% effect Row     | 10  c/ea | Stock: 3   => Dem: 2  | Bea: 1  | Und: 0  | Hum: 0  | Con: 0
25% fracture       | 8   c/ea | Stock: 2   => Dem: 1  | Bea: 0  | Und: 0  | Hum: 1  | Con: 0
Modifier Tier      | 10  c/ea | Stock: 35  => Dem: 8  | Bea: 8  | Und: 10 | Hum: 4  | Con: 5
```
