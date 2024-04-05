# POE-Stash-Coffin-Manager
(League 3.24) Use the POE stash API to analyze the quantity and types of [Filled Coffin](https://www.poewiki.net/wiki/Filled_Coffin) items in stashes.

## Usage

1. Edit [config.json](https://github.com/EricZhu-42/POE-Stash-Coffin-Manager/blob/main/config.json), replace `POESESSID`, `accountName` and `tab_names`.
2. Run `python main.py`

## Sample output

```
================================           Effect           ================================
25% effect Column  | 5   c/ea | Stock: 10  => Dem: 2  | Bea: 1  | Und: 2  | Hum: 4  | Con: 1 
25% effect Row     | 10  c/ea | Stock: 11  => Dem: 2  | Bea: 3  | Und: 4  | Hum: 1  | Con: 1 
40% adj Bea$t      | 10  c/ea | Stock: 4   => Dem: 0  | Bea: 3  | Und: 1  | Hum: 0  | Con: 0 
40% adj Construct  | 5   c/ea | Stock: 13  => Dem: 1  | Bea: 2  | Und: 5  | Hum: 3  | Con: 2 
40% adj Demon      | 5   c/ea | Stock: 4   => Dem: 0  | Bea: 2  | Und: 2  | Hum: 0  | Con: 0 
40% adj Humanoid   | 5   c/ea | Stock: 3   => Dem: 0  | Bea: 2  | Und: 0  | Hum: 0  | Con: 1 
40% adj Undead     | 10  c/ea | Stock: 7   => Dem: 1  | Bea: 4  | Und: 1  | Hum: 1  | Con: 0 
================================       Increase 300%        ================================
Attack             | 4   c/ea | Stock: 12  => Dem: 1  | Bea: 4  | Und: 4  | Hum: 1  | Con: 2 
Caster             | 5   c/ea | Stock: 17  => Dem: 1  | Bea: 6  | Und: 6  | Hum: 2  | Con: 2 
Elemental          | 4   c/ea | Stock: 12  => Dem: 1  | Bea: 5  | Und: 4  | Hum: 1  | Con: 1 
Prefix             | 5   c/ea | Stock: 5   => Dem: 2  | Bea: 1  | Und: 0  | Hum: 2  | Con: 0
Suffix             | 4   c/ea | Stock: 6   => Dem: 0  | Bea: 1  | Und: 3  | Hum: 2  | Con: 0
================================       Increase 500%        ================================
Attribute          | 5   c/ea | Stock: 14  => Dem: 1  | Bea: 4  | Und: 4  | Hum: 4  | Con: 1
Chaos              | 5   c/ea | Stock: 8   => Dem: 1  | Bea: 1  | Und: 4  | Hum: 0  | Con: 2
Cold               | 3   c/ea | Stock: 17  => Dem: 1  | Bea: 8  | Und: 2  | Hum: 4  | Con: 2
Critical           | 15  c/ea | Stock: 8   => Dem: 0  | Bea: 2  | Und: 1  | Hum: 4  | Con: 1
Defence            | 4   c/ea | Stock: 17  => Dem: 2  | Bea: 6  | Und: 5  | Hum: 3  | Con: 1
Fire               | 4   c/ea | Stock: 20  => Dem: 2  | Bea: 6  | Und: 6  | Hum: 6  | Con: 0
Gem                | 15  c/ea | Stock: 4   => Dem: 1  | Bea: 2  | Und: 0  | Hum: 1  | Con: 0
Life               | 4   c/ea | Stock: 15  => Dem: 1  | Bea: 6  | Und: 3  | Hum: 3  | Con: 2
Lightning          | 4   c/ea | Stock: 23  => Dem: 4  | Bea: 8  | Und: 4  | Hum: 6  | Con: 1
Mana               | 4   c/ea | Stock: 26  => Dem: 1  | Bea: 7  | Und: 12 | Hum: 2  | Con: 4
Minion             | 5   c/ea | Stock: 4   => Dem: 1  | Bea: 2  | Und: 1  | Hum: 0  | Con: 0
Physical           | 4   c/ea | Stock: 21  => Dem: 2  | Bea: 6  | Und: 8  | Hum: 4  | Con: 1
Resistance         | 5   c/ea | Stock: 8   => Dem: 1  | Bea: 3  | Und: 2  | Hum: 1  | Con: 1
Speed              | 15  c/ea | Stock: 3   => Dem: 0  | Bea: 2  | Und: 0  | Hum: 1  | Con: 0
================================       Meta Crafting        ================================
25% fracture       | 10  c/ea | Stock: 7   => Dem: 2  | Bea: 2  | Und: 2  | Hum: 1  | Con: 0
25% mirrored       | 25  c/ea | Stock: 1   => Dem: 1  | Bea: 0  | Und: 0  | Hum: 0  | Con: 0
================================         Modifiers          ================================
+1 Explicit        | 5   c/ea | Stock: 61  => Dem: 10 | Bea: 19 | Und: 16 | Hum: 8  | Con: 8
+1 Item Level      | 3   c/ea | Stock: 44  => Dem: 6  | Bea: 17 | Und: 12 | Hum: 3  | Con: 6
+5 to Quality      | 4   c/ea | Stock: 29  => Dem: 5  | Bea: 13 | Und: 7  | Hum: 3  | Con: 1
-1 Explicit        | 5   c/ea | Stock: 14  => Dem: 1  | Bea: 6  | Und: 7  | Hum: 0  | Con: 0
Modifier Tier      | 8   c/ea | Stock: 60  => Dem: 10 | Bea: 15 | Und: 18 | Hum: 9  | Con: 8
+1 Link to 5       | 4   c/ea | Stock: 18  => Dem: 4  | Bea: 4  | Und: 3  | Hum: 5  | Con: 2
+1 Link to 6       | 15  c/ea | Stock: 1   => Dem: 0  | Bea: 1  | Und: 0  | Hum: 0  | Con: 0
================================        Not Consume         ================================
5% not cons Bea    | 4   c/ea | Stock: 10  => Dem: 1  | Bea: 2  | Und: 3  | Hum: 3  | Con: 1
5% not cons Con    | 5   c/ea | Stock: 8   => Dem: 1  | Bea: 0  | Und: 5  | Hum: 2  | Con: 0
5% not cons Dem    | 4   c/ea | Stock: 7   => Dem: 1  | Bea: 0  | Und: 3  | Hum: 2  | Con: 1
5% not cons Hum    | 3   c/ea | Stock: 14  => Dem: 1  | Bea: 7  | Und: 4  | Hum: 2  | Con: 0
5% not cons Und    | 5   c/ea | Stock: 7   => Dem: 0  | Bea: 5  | Und: 0  | Hum: 2  | Con: 0
================================        Scarcer 150%        ================================
Attack             | 9   c/ea | Stock: 6   => Dem: 0  | Bea: 2  | Und: 0  | Hum: 0  | Con: 4
Caster             | 4   c/ea | Stock: 11  => Dem: 3  | Bea: 1  | Und: 4  | Hum: 1  | Con: 2
Elemental          | 15  c/ea | Stock: 6   => Dem: 0  | Bea: 4  | Und: 0  | Hum: 1  | Con: 1
================================        Scarcer 300%        ================================
Attribute          | 10  c/ea | Stock: 3   => Dem: 0  | Bea: 1  | Und: 2  | Hum: 0  | Con: 0
Chaos              | 10  c/ea | Stock: 4   => Dem: 1  | Bea: 1  | Und: 2  | Hum: 0  | Con: 0
Cold               | 4   c/ea | Stock: 11  => Dem: 4  | Bea: 3  | Und: 4  | Hum: 0  | Con: 0
Critical           | 5   c/ea | Stock: 5   => Dem: 0  | Bea: 2  | Und: 1  | Hum: 0  | Con: 2
Defence            | 5   c/ea | Stock: 8   => Dem: 0  | Bea: 2  | Und: 3  | Hum: 1  | Con: 2
Fire               | 4   c/ea | Stock: 10  => Dem: 0  | Bea: 2  | Und: 4  | Hum: 2  | Con: 2
Gem                | 70  c/ea | Stock: 1   => Dem: 0  | Bea: 1  | Und: 0  | Hum: 0  | Con: 0
Life               | 5   c/ea | Stock: 7   => Dem: 0  | Bea: 4  | Und: 1  | Hum: 2  | Con: 0
Lightning          | 3   c/ea | Stock: 8   => Dem: 2  | Bea: 3  | Und: 2  | Hum: 0  | Con: 1
Mana               | 10  c/ea | Stock: 8   => Dem: 1  | Bea: 1  | Und: 1  | Hum: 3  | Con: 2
Physical           | 9   c/ea | Stock: 6   => Dem: 1  | Bea: 2  | Und: 2  | Hum: 0  | Con: 1
Resistance         | 30  c/ea | Stock: 9   => Dem: 2  | Bea: 4  | Und: 1  | Hum: 1  | Con: 1
Speed              | 5   c/ea | Stock: 7   => Dem: 0  | Bea: 2  | Und: 3  | Hum: 2  | Con: 0
================================           Unique           ================================
* Phrecia          | 4   c/ea | Stock: 12  => Dem: 1  | Bea: 2  | Und: 4  | Hum: 4  | Con: 1
* Grattus          | 4   c/ea | Stock: 12  => Dem: 2  | Bea: 3  | Und: 4  | Hum: 1  | Con: 2
* Veruso           | 4   c/ea | Stock: 13  => Dem: 2  | Bea: 4  | Und: 5  | Hum: 2  | Con: 0
* Perandus         | 30  c/ea | Stock: 6   => Dem: 0  | Bea: 1  | Und: 4  | Hum: 0  | Con: 1
* Nevalius         | 4   c/ea | Stock: 19  => Dem: 0  | Bea: 10 | Und: 2  | Hum: 7  | Con: 0
```
