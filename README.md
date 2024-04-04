# POE-Stash-Coffin-Manager
(League 3.24) Use the POE stash API to analyze the quantity and types of [Filled Coffin](https://www.poewiki.net/wiki/Filled_Coffin) items in stashes.

## Usage

1. Edit [config.json](https://github.com/EricZhu-42/POE-Stash-Coffin-Manager/blob/main/config.json), replace `POESESSID`, `accountName` and `tab_names`.
2. Run `python main.py`

## Sample output

> Prices are not implemented yet.

```
========= Increase 300%  =========
Caster             | 1C  | 3  left
Elemental          | 1C  | 3  left
Suffix             | 1C  | 1  left
========= Increase 500%  =========
Attribute          | 1C  | 4  left
Chaos              | 1C  | 2  left
Cold               | 1C  | 3  left
Defence            | 1C  | 1  left
Fire               | 1C  | 1  left
Gem                | 1C  | 1  left
Lightning          | 1C  | 1  left
Mana               | 1C  | 3  left
Physical           | 1C  | 4  left
=========  Scarcer 150%  =========
Caster             | 1C  | 2  left
=========  Scarcer 300%  =========
Chaos              | 1C  | 1  left
Defence            | 1C  | 1  left
Fire               | 1C  | 1  left
Lightning          | 1C  | 1  left
Mana               | 1C  | 2  left
Speed              | 1C  | 1  left
========= Meta Crafting  =========
+1 Explicit        | 1C  | 4  left
+1 Item Level      | 1C  | 7  left
-1 Explicit        | 1C  | 1  left
25% effect Column  | 1C  | 2  left
Modifier Tier      | 1C  | 7  left
```
