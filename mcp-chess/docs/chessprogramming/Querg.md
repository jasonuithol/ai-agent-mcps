# Querg

Source: https://www.chessprogramming.org/Querg

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Querg**

[![](https://upload.wikimedia.org/wikipedia/commons/e/e9/Singular_dwarf_by_Fr%C3%B8lich.jpg)](/File:Singular_dwarf_by_Fr%C3%B8lich.jpg)

Dwarf [[1]](#cite_note-1)

**Querg**,  
a series of private chess programs written by [John F. White](/John_F._White "John F. White") in [6502](/6502 "6502") [assembly](/Assembly "Assembly") to run on an 64K [Atari 130XE](/Atari_8-bit "Atari 8-bit"), as described in the [ICCA Journal, Vol. 11, Nos. 2/3](/ICGA_Journal#11_23 "ICGA Journal"), 1988 [[2]](#cite_note-2). Versions mentioned in the article were dubbed *NovaQuerg* and *SuperQuerg*. In his second [ICCA Journal](/ICGA_Journal#13_1 "ICGA Journal") article, White describes how to store and retrieve moves of an [opening book](/Opening_Book "Opening Book") [[3]](#cite_note-3).

# Etymology

The name Querg [[4]](#cite_note-4) has no meaning, the *Querg P Quigel* fictional character [[5]](#cite_note-5) from [Star Trek Voyager](https://en.wikipedia.org/wiki/Star_Trek:_Voyager) [Pathfinder](https://en.wikipedia.org/wiki/Pathfinder_%28Star_Trek:_Voyager%29) appeared some years later.

# Description

## Move Generation

Most versions of Querg use a [mailbox](/Mailbox "Mailbox") based offset [move generation](/Move_Generation "Move Generation"), [0x88](/0x88 "0x88") techniques coupled with offset move generation are mentioned in the article, and that this technique has advantages for in [check detection](/Check#Detection "Check") as applied in [Paul Wiereyn's](/Paul_Wiereyn "Paul Wiereyn") mate finding program [[6]](#cite_note-6). The experiments with [incremental updated](/Incremental_Updates "Incremental Updates") [movelists](/Move_List "Move List") were not that successful.

## Check Detection

[Checks](/Check "Check") were first [detected](/Check#Detection "Check") by a variant of the method given by Wiereyn, modified to suit a cylindrical representation of the chess board, and rather slower than the original described - the 12 x 10 board is not well suited to implementation of this procedure. The alternative method to delay check detection until a king has been captured saved time in positions where checks are rare, but was inefficient if kings are vulnerable to checks. Finally, White came up with a technique to determine whether pieces give check during generation time.

## Search

Querg applies [PVS](/Principal_Variation_Search "Principal Variation Search") with [Aspiration windows](/Aspiration_Windows "Aspiration Windows") within an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework, where the [principal variation](/Principal_Variation "Principal Variation") is 'fed over' into the next iteration. Two [killer moves](/Killer_Move "Killer Move") were stored and used to [reject moves](/Killer_Heuristic "Killer Heuristic"). Lazy move generation of [PV-](/PV-Move "PV-Move") and killer moves before constructing a whole move list failed to provide any benefit. Forcing moves, that is [checks](/Check "Check") and replies to check, [promotions](/Promotions "Promotions"), threats of promotions by the side not to move, and [captures](/Captures "Captures"), are [extended](/Extensions "Extensions") by a maximum of three additional plies in the whole path. A special routine *HIPL* (high-ply-[pruning](/Pruning "Pruning")) avoids the unnecessary sequence [make move](/Make_Move "Make Move") -> [evaluate](/Evaluation "Evaluation") -> [unmake move](/Unmake_Move "Unmake Move") at [frontier nodes](/Frontier_Nodes "Frontier Nodes") for none forcing moves.

## Evaluation

The [evaluation](/Evaluation "Evaluation") relies largely on first-order terms [[7]](#cite_note-7), considering [material](/Material "Material"), pieces left [en prise](/En_prise "En prise"), [mobility](/Mobility "Mobility") as number of moves plus information from [piece-square tables](/Piece-Square_Tables "Piece-Square Tables"), and [pawn structure](/Pawn_Structure "Pawn Structure").

# Performance

Performance was determined by [test-positions](/Test-Positions "Test-Positions") and games played versus programs running on the same 8-bit Atari, such as [Cyrus](/Cyrus "Cyrus"), [Colossus 3.0](/Colossus_Chess "Colossus Chess"), the old [Sargon 2.5](/Sargon "Sargon"), and others, where *NovaQuerg* finished with 6.5 points out of 14. However, Querg has not played any official tournaments.

# See also

- [Quark](/Quark "Quark")

# Publications

[[8]](#cite_note-8)

- [John F. White](/John_F._White "John F. White") (**1988**). *Querg Chess*. [ICCA Journal, Vol. 11, Nos. 2/3](/ICGA_Journal#11_23 "ICGA Journal")
- [John F. White](/John_F._White "John F. White") (**1990**). *The Amateur's Book-Opening Routine*. [ICCA Journal, Vol. 13, No. 1](/ICGA_Journal#13_1 "ICGA Journal")

# External Links

- [Querg Draughts for Atari ST (1994) - MobyGames](http://www.mobygames.com/game/querg-draughts)
- [I, Querg P Quigel « Pathfinder's Federation Log](http://pathfinderfl.wordpress.com/2011/02/26/i-querg-p-quigel/)
- [Lt Cmd Querg « Pathfinder's Federation Log](http://pathfinderfl.wordpress.com/stotoons/querg/)

# References

1. [↑](#cite_ref-1) A singular, small depiction of a rather gnarly-looking [dwarf](https://en.wikipedia.org/wiki/Dwarf_(mythology)) appearing with the list of dwarves in the [Poetic Edda](https://en.wikipedia.org/wiki/Poetic_Edda) poem [Völuspá](https://en.wikipedia.org/wiki/V%C3%B6lusp%C3%A1), Painting by [Lorenz Frølich](https://en.wikipedia.org/wiki/Lorenz_Fr%C3%B8lich) in [Karl Gjellerup](https://en.wikipedia.org/wiki/Karl_Adolph_Gjellerup) (**1895**). *[Den ældre Eddas Gudesange](https://archive.org/details/denldreeddasgud00saemgoog)*.
2. [↑](#cite_ref-2) [John F. White](/John_F._White "John F. White") (**1988**). *Querg Chess*. [ICCA Journal, Vol. 11, Nos. 2/3](/ICGA_Journal#11_23 "ICGA Journal")
3. [↑](#cite_ref-3) [John F. White](/John_F._White "John F. White") (**1990**). *The Amateur's Book-Opening Routine*. [ICCA Journal, Vol. 13, No. 1](/ICGA_Journal#13_1 "ICGA Journal")
4. [↑](#cite_ref-4) In the German [Colognian dialect](https://en.wikipedia.org/wiki/Colognian_dialect)] a Querg appeared to be a [dwarf](https://en.wikipedia.org/wiki/Dwarf_(mythology)) or [Heinzelmännchen](https://en.wikipedia.org/wiki/Heinzelm%C3%A4nnchen), [Wörterbuchnetz - Rheinisches Wörterbuch](http://woerterbuchnetz.de/RhWB/call_wbgui_py_from_form?sigle=RhWB&mode=Volltextsuche&hitlist=&patternlist=&lemid=RQ00937) (German)
5. [↑](#cite_ref-5) [I, Querg P Quigel « Pathfinder's Federation Log](http://pathfinderfl.wordpress.com/2011/02/26/i-querg-p-quigel/)
6. [↑](#cite_ref-6) [Paul Wiereyn](/Paul_Wiereyn "Paul Wiereyn") (**1985**). *Inventive Problem Solving*. [ICCA Journal, Vol. 8, No. 4](/ICGA_Journal#8_4 "ICGA Journal")
7. [↑](#cite_ref-7) [Jan Eric Larsson](/Jan_Eric_Larsson "Jan Eric Larsson") (**1987**). *Challenging that Mobility is Fundamental*. [ICCA Journal, Vol. 10, No. 3](/ICGA_Journal#10_3 "ICGA Journal")
8. [↑](#cite_ref-8) [ICGA Reference Database](/ICGA_Journal#RefDB "ICGA Journal")

**[Up one level](/Engines "Engines")**