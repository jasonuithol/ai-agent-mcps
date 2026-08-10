# Pawn Rams (Bitboards)

Source: https://www.chessprogramming.org/Pawn_Rams_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Rams**

[![](/images/thumb/c/ca/SamuelBakLocked.jpg/240px-SamuelBakLocked.jpg)](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb3)

[Samuel Bak](/Category:Samuel_Bak "Category:Samuel Bak") - Locked [[1]](#cite_note-1)

**Pawn Rams**,  
all [pawns](/Pawn "Pawn") that are blocked by the opponent's pawns. A ram is a mutual mechanical obstruction. If the rammed pawn is no [lever pawn](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)"), it becomes member of the [immobile pawns](/index.php?title=Immobile_Pawns&action=edit&redlink=1 "Immobile Pawns (page does not exist)"). Specially if other properties match, e.g. there is no or no mutual lever-possibility against the opponent counterpart, rams are a **symptom** of **congealment**. The term Ram or [Widder](https://de.wikipedia.org/wiki/Widder) in German ([Ovis](https://en.wikipedia.org/wiki/Ovis), [Aries](https://en.wikipedia.org/wiki/Aries_%28constellation%29)) was coined by [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") [[2]](#cite_note-2) [[3]](#cite_note-3). Rammed none lever pawns in the [center](/Center "Center") or [extended center](/Center#ExtendedCenter "Center") are most important to decide about [bad bishops](/Bad_Bishop "Bad Bishop").

# Blocked Positions

Three or four [isolated](/Isolated_Pawn "Isolated Pawn") rams are a perfect barrier - no path for either king to enter to opposite area.

```
. . . . . . . .
. . . . . . . .
. . . . . . . .
. b . . b . . b
. w . . w . . w
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

# Code

*Working in the bitboard centric world to determine [pawn](/Pawn "Pawn") related pattern set-wise.*
*The code snippets rely on [shifting bitboards](/General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), specially by [one step only](/General_Setwise_Operations#OneStepOnly "General Setwise Operations").*

```
U64 wRam(U64 wpawns, U64 bpawns) {return soutOne(bpawns) & wpawns;}
U64 bRam(U64 wpawns, U64 bpawns) {return nortOne(wpawns) & bpawns;}
```

Obviously the number of white rammed pawns is equal to the number of black rammed pawns.

# Mutual Mechanical Obstruction

[![Widder.jpg](/images/9/9d/Widder.jpg)](http://flickr.com/photos/olaf_k/2079888707/)

Mutual Mechanical Obstruction [[4]](#cite_note-4)

# See also

- [Backward Pawn](/Backward_Pawn "Backward Pawn")
- [Blockade](/Blockade "Blockade")
- [Blockage Detection](/Blockage_Detection "Blockage Detection")

# Forum Posts

- [Pawn ram code in gnuchess](http://groups.google.com/group/gnu.chess/browse_frm/thread/37bbd87f491aa673) by [Chua Kong Sian](/Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](/GNU_Chess#NewsGroup "GNU Chess"), June 18, 1994 » [GNU Chess](/GNU_Chess "GNU Chess")
- [Two ideas for pawn patches](https://groups.google.com/d/msg/fishcooking/rwakDGcuf5E/YUyeJX9rBQAJ) by [Stephane Nicolet](/Stephane_Nicolet "Stephane Nicolet"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), July 28, 2016 » [Stockfish](/Stockfish "Stockfish")

# External Links

- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
- [Monsoon/Typhoon Homepage](https://wannabe.guru.org/scott/hobbies/chess/) by [Scott Gasch](/Scott_Gasch "Scott Gasch")

# References

1. [↑](#cite_ref-1) 
   [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb3), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](/University_of_Minnesota "University of Minnesota")
2. [↑](#cite_ref-2) [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6
3. [↑](#cite_ref-3) [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
4. [↑](#cite_ref-4) [Kämpfende Steinböcke ... fighting ibex](http://www.flickr.com/photos/olaf_k/2079888707/) from [Flickr - Fotosharing!](http://www.flickr.com/), [kleinwegen.net](http://www.kleinwegen.net/)

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**