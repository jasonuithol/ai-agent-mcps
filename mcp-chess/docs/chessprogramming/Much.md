# Much

Source: https://www.chessprogramming.org/Much

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Much**

**Much**, (MUCH)  
the [Maastricht University](/Maastricht_University "Maastricht University") Chess Program by primary authors [Roger Hünen](/Roger_H%C3%BCnen "Roger Hünen"), [Harry Nefkens](/Harry_Nefkens "Harry Nefkens"), [Tom Pronk](/Tom_Pronk "Tom Pronk") and [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") [[1]](#cite_note-1), represented and operated at the [WCCC 1989](/WCCC_1989 "WCCC 1989") by [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") and [Harm Bakker](/index.php?title=Harm_Bakker&action=edit&redlink=1 "Harm Bakker (page does not exist)").
Much was written in [C](/C "C"), and run on a [Sun-4](/Sun#4 "Sun") [workstation](https://en.wikipedia.org/wiki/Workstation).

# Authors

- [Roger Hünen](/Roger_H%C3%BCnen "Roger Hünen")
- [Harry Nefkens](/Harry_Nefkens "Harry Nefkens")
- [Tom Pronk](/Tom_Pronk "Tom Pronk")
- [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik")

# Description

based on [WCCC 1989](/WCCC_1989 "WCCC 1989") booklet [[2]](#cite_note-2):

```
Much consists of several programs. The user-interface program accepts a move from the operator and subsequently generates evaluation tables for the search program.  The user-interface program also handles time control, the opening library, and the endgame library. The search program receives the board position and evaluation tables from the user-interface program. The evaluation tables are tuned with the opening played. Before each move they are incrementally updated according to the board position (strategical evaluation of squares), but also bonus points are provided to undeveloped pieces, the pair of Bishops in open positions (middlegame/endgame), the Color of the Pawns and Bishop on the board (endgame). Moreover, several plans are encouraged. The configuration belonging to the execution of a plan is supplied with bonus points such that every piece and pawn involved tries to reach the plan-ideal square. The plan as a whole, once started to be carried out, increases the bonus points for every piece/pawn to be played at each move. Much then searches until it is interrupted by the user-interface program. The search program, based on the alpha-beta algorithm and its refinements, uses PVS-search, killer and transposition tables. Move generation is done incrementally. Much uses specialized sub-programs to handle the KBBK, KBNK, KBPK and KNPK endgames. These programs use a goal-directed search.
```

# See also

- [Dutch](/Dutch "Dutch")

# External Links

- [Much's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=355)

# References

1. [↑](#cite_ref-1) [Much's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=355)
2. [↑](#cite_ref-2) [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](https://www.computerhistory.org/chess/doc-434fea055cbb3/) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](/Peter_Jennings "Peter Jennings"), hosted by[The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")

**[Up one level](/Engines "Engines")**