# Amundsen

Source: https://www.chessprogramming.org/Amundsen

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Amundsen**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Nlc_amundsen.jpg/330px-Nlc_amundsen.jpg)](/File:Nlc_amundsen.jpg)

Victory awaits him, who has everything in order.  
 Luck we call it.  
 Defeat is definitely due for him,  
 who has neglected to take the necessary precautions.  
 Bad luck we call it.  
Roald Amundsen [[1]](#cite_note-1) [[2]](#cite_note-2)

**Amundsen**, (Jonte)  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](/Category:Open_Source "Category:Open Source") by [John Bergbom](/index.php?title=John_Bergbom&action=edit&redlink=1 "John Bergbom (page does not exist)"), written in [C](/C "C") and licensed under the [GPL](/Free_Software_Foundation#GPL "Free Software Foundation").
Started as college course project at the Department of Numerical Analysis and Computing Science, [Royal Institute of Technology](https://en.wikipedia.org/wiki/Royal_Institute_of_Technology), [Stockholm](https://en.wikipedia.org/wiki/Stockholm) [[3]](#cite_note-3), a name change from Jonte to Amundsen took place between version 0.25 and 0.3, since the initial name was already used at [FICS](/index.php?title=Free_Internet_Chess_Server&action=edit&redlink=1 "Free Internet Chess Server (page does not exist)") [[4]](#cite_note-4).
Amundsen was first released in May 2004, as announced by [Dann Corbit](/Dann_Corbit "Dann Corbit") in [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums") [[5]](#cite_note-5).

# Description

## [Board Representation](/Board_Representation "Board Representation")

Amundsen is a [bitboard](/Bitboards "Bitboards") engine and applies [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") using the classical 1/2 MiB lookup tables, indexed by [8-bit line occupancy](/Occupancy_of_any_Line "Occupancy of any Line") to determine [sliding piece attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks"), ignoring the possible fourfold reduction excluding the redundant [outer squares](/First_Rank_Attacks#TheOuterSquares "First Rank Attacks").  [Population count](/Population_Count "Population Count"), [bitscan forward](/BitScan#Bitscanforward "BitScan") and [reverse](/BitScan#Bitscanreverse "BitScan") further use three 16-bit indexed, 64K lookup tables of [double word](/Double_Word "Double Word") integers, which is another 3/4 MiB of memory [[6]](#cite_note-6).

```
int bits_in_16bits[65536];
int first_bit_in_16bits[65536];
int last_bit_in_16bits[65536];

/* This function returns the number of the first set bit in an int64.
   The search is done from LSB to MSB. */
int get_first_bitpos(int64 n) {
  if (first_bit_in_16bits[n & 0xffff] >= 0)
    return first_bit_in_16bits[n & 0xffff];
  if (first_bit_in_16bits[(n >> 16) & 0xffff] >= 0)
    return first_bit_in_16bits[(n >> 16) & 0xffff] + 16;
  if (first_bit_in_16bits[(n >> 32) & 0xffff] >= 0)
    return first_bit_in_16bits[(n >> 32) & 0xffff] + 32;
  if (first_bit_in_16bits[(n >> 48) & 0xffff] >= 0)
    return first_bit_in_16bits[(n >> 48) & 0xffff] + 48;
  return -1;
}
```

## [Search](/Search "Search")

The search is [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with [transposition](/Transposition_Table "Transposition Table") and [refutation table](/Refutation_Table "Refutation Table") inside an [iterative deepening](/Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](/Aspiration_Windows "Aspiration Windows"), further using [AEL-pruning](/AEL-Pruning "AEL-Pruning") à la [Heinz](/Ernst_A._Heinz "Ernst A. Heinz"), as well as [LMR](/Late_Move_Reductions "Late Move Reductions") and [IID](/Internal_Iterative_Deepening "Internal Iterative Deepening") in case of a missing [hash move](/Hash_Move "Hash Move") at [PV-nodes](/Node_Types#PV "Node Types"). [Checks](/Check_Extensions "Check Extensions"), [pawn moves to the 7th rank](/Passed_Pawn_Extensions "Passed Pawn Extensions"), and [mate threatening moves](/Mate_Threat_Extensions "Mate Threat Extensions") are [extended](/Extensions "Extensions"), [killer-](/Killer_Heuristic "Killer Heuristic") and [history heuristic](/History_Heuristic "History Heuristic") help to [order moves](/Move_Ordering "Move Ordering"), and a [SEE swap routine](/SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") is used to determine winning [captures](/Captures "Captures").

## [Evaluation](/Evaluation "Evaluation")

Amundsen's evaluation with a [pawn structure cache](/Pawn_Hash_Table "Pawn Hash Table") features [piece-square tables](/Piece-Square_Tables "Piece-Square Tables"), and further considers [mobility](/Mobility "Mobility"), [passed pawns](/Passed_Pawn "Passed Pawn") and [hidden passed pawns](/Hidden_Passed_Pawn "Hidden Passed Pawn"), [king safety](/King_Safety "King Safety") through [king piece tropism](/King_Safety#KingTropism "King Safety"), and various features and defects such as [outposts](/Outposts "Outposts"), [rook on open file](/Rook_on_Open_File "Rook on Open File"), [seventh rank](/Rook_on_Seventh "Rook on Seventh") and [behind passers](/Tarrasch_Rule "Tarrasch Rule"), and [bad bishop](/Bad_Bishop "Bad Bishop") to name a few, and knows to trade pieces when ahead, but pawns when behind.

# See also

- [PolarChess](/PolarChess "PolarChess")
- [Siberian Chess](/Siberian_Chess "Siberian Chess")

# Publications

- [John Bergbom](/index.php?title=John_Bergbom&action=edit&redlink=1 "John Bergbom (page does not exist)") (**2004**). *Schackprogrammet Amundsen*. (2D1464 Större avancerad individuell kurs i datalogi) [pdf](http://www.nada.kth.se/kurser/kth/2D1464/amundsen/rapport.pdf) (Swedish) [[7]](#cite_note-7)

# Forum Posts

- [A new chess program](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47652) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 22, 2004
- [Amundsen 0.3 and his book : problem ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47667) by Claude Dubois, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 24, 2004
- [Amundsen 0.35 exe](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48692) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 25, 2004
- [Amundsen 05 Windows binaries](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=3481&p=17419#p17419) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 14, 2005
- [Amundsen 0.65 (released on January 11th 2008)](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=7065#p32462) by [Denis P. Mendoza](/Denis_Mendoza "Denis Mendoza"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 15, 2008
- [Amundsen 0.65.1 Windows builds available](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=7158) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 23, 2008
- [Amundsen\_075JA with illegal moves](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=49886) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 18, 2009

# External Links

## Chess Engine

- [Amundsen chess program](http://www.bergbomconsulting.se/chess/)

:   [Amundsen chess program | Testsuites](http://www.bergbomconsulting.se/chess/testsuites.html) » [Test-Positions](/Test-Positions "Test-Positions")

- [Amundsen](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Amundsen&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](/CCRL "CCRL")

## Misc

- [Roald Amundsen from Wikipedia](https://en.wikipedia.org/wiki/Roald_Amundsen)
- [Amundsen (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Amundsen_%28disambiguation%29)

# References

1. [↑](#cite_ref-1) [Roald Amundsen - Wikiquote](https://en.wikiquote.org/wiki/Roald_Amundsen)
2. [↑](#cite_ref-2) Photo by [Ludwik Szacinski](https://no.wikipedia.org/wiki/Ludwik_Szaci%C5%84ski), in [Roald Amundsen](https://en.wikipedia.org/wiki/Roald_Amundsen) (**1908**). *[Roald Amundsen's The North West Passage: Being a Record of a Voyage of Exploration of the ship Gjøa, 1903-1907](https://www.wdl.org/en/item/7316/)*. [Dutton](https://en.wikipedia.org/wiki/E._P._Dutton), New York City; [National Library of Canada](https://en.wikipedia.org/wiki/Library_and_Archives_Canada), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), see also [Roald Amundsen - Northwest Passage (1903–1906) from Wikipedia](https://en.wikipedia.org/wiki/Roald_Amundsen#Northwest_Passage_(1903%E2%80%931906)), [Gjøa from Wikipedia](https://en.wikipedia.org/wiki/Gj%C3%B8a)
3. [↑](#cite_ref-3) [Master of Science - Nada, KTH](http://www.nada.kth.se/kurser/master/index-eng.html)
4. [↑](#cite_ref-4) [Amundsen chess program](http://www.bergbomconsulting.se/chess/)
5. [↑](#cite_ref-5) [A new chess program](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47652) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 22, 2004
6. [↑](#cite_ref-6) [amundsen-0.80.tar.gz](http://www.bergbomconsulting.se/chess/), bitboards.c
7. [↑](#cite_ref-7) [Amundsen chess program](http://www.nada.kth.se/kurser/kth/2D1464/amundsen/index.html) (old page)

**[Up one level](/Engines "Engines")**