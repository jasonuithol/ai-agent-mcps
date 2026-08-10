# Candidates (Bitboards)

Source: https://www.chessprogramming.org/Candidates_(Bitboards)

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Pawn Pattern and Properties](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Candidates**

[![](/images/thumb/1/19/Designated.jpg/240px-Designated.jpg)](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc1)

[Samuel Bak](/Category:Samuel_Bak "Category:Samuel Bak") - The Designated [[1]](#cite_note-1)

**Candidates**,  
pawns that can force themselves to become [passed pawns](/Passed_Pawn "Passed Pawn") simply with a series of pawn moves. Candidates are half-open pawns with no mechanical but dynamical obstructions. Specifially, the pawn must be on a half-open file, and the number of defender pawns that can help the pawn advance are greater than or equal to the number of pawns which attack the pawn or squares in front of it.

# Candidate and Faker

While the intersection of the [frontspan](/Pawn_Spans "Pawn Spans") with opposing pawns is empty, the intersection of [front attackspans](/Attack_Spans "Attack Spans") with opposing pawns is not (otherwise it would already a passer). The opposing pawns as member of the front attackspan(s), stand sentinel over one or more squares in the [frontfill](/Pawn_Fills "Pawn Fills") of the open pawn, and are about to **capture** the open pawn, if it may advance into - or already is - a [lever](/Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)"). Those opposing pawns are called [sentries](/Sentry "Sentry").

If the open pawn has one or more **helper-pawns** on adjacent files, which are able to **recapture** the **sentry**, the candidate is a real one and is guaranteed to force a passer. Otherwise, without enough support from helpers, the candidate is only a [faker](/Faker "Faker").

The following diagrams shows advanced candidates and fakers, assuming black to move:

```
candidates b6, f4   fakers -
sentries   c7, g2   more sentries
helper     c5, g4   than helpers
. . . . | . . .     . . . . | . . .
. . b . . . . .     b . b . . . . .
. w . . . . . .     . w . . . . . .
. . w . . . . .     . . w . . . . .
. . . . . b b .     . . . . . b b .
. . . . . . . .     . . . . . . . .
. . . . . . w .     . . . . w . w .
. . . | . . . .     . . . | . . . .
```

The white candidate on b6 is already in lever-distance with the sentry c7. The sentry c7 is likely forced to capture - otherwise b6 captures or pushes to become a passer. The white helper immediately recaptures and takes the role of the former candidate and becomes a passer. The black candidate on f4 can also force a passer. The helper on g4 compensates the sentry on g2. Usually, the **candidate** has to push forward, not the **helper**.

In the second diagram both candidates are pseudo-candidates or **fakers**, since there are **more** sentries than helpers - a7xb6 is required - otherwise, after c7xb6, c5-c6 would allow the helper to advance to a passer.

## Advanced Candidates

Advanced candidates, already inside or about to enter the opponent side of the board are the most important to consider in evaluation. Even more if the [interspan](/Pawn_Spans#InterSpans "Pawn Spans") of sentries and helper is already one - and it is only about the control of the stop-square - or if the candidate is already part of a lever, the number of attacks and defenses.

In such cases, due to the forced nature of exchanging candidate, sentry and helper, only two or up to five plies are necessary to establish a passer. In fact those candidates may even be more worth than pawns already a passer - specially if the opponent king is outside the candidates square - or if the outside candidate may deflect the opponent king.

One may argue that a candidate already in lever distance with the sentry should be covered by [quiescence search](/index.php?title=Quiescence_search&action=edit&redlink=1 "Quiescence search (page does not exist)") - since it is a capture/recapture sequence. Therefor more important to evaluate are the candidate-helper-duo/trio against one or two sentries, which is likely a kind of static exchange evaluation of the candidate's stop-square.

```
. . . . . . . .
. . s . . s . s   sentries
. . . . . . . .
. c h . . h c h   candidates with helpers
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

To cover sets of advanced white candidates with attacked but sufficient defended stops already on the on the 5th rank, one may use some code like this. Feel free to introduce branches, e.g. if there are no white pawns on the fifth rank. Anyway, [wSafePawnSquares](/Pawn_Attacks_(Bitboards)#PawnAttackMaps "Pawn Attacks (Bitboards)") might be used elsewhere, e.g. to decide whether helper pawns may advance to defend candidate's stop.

```
U64 wCandidatesOn5th(U64 wpawns, U64 bpawns) {
   const U64 rank5     = C64(0x000000ff00000000);
   U64 bPawnAnyAttacks = bPawnAnyAttacks(bpawns);
   U64 wSafeSquares    = wSafePawnSquares(wpawns, bpawns);
   U64 wSafeAttacked   = bPawnAnyAttacks  &  wSafeSquares;
   U64 blackFrontSpan  = (bpawns >> 8)    | (bpawns >> 16); // only for 5th rank
   return wpawns & rank5 &~blackFrontSpan & (wSafeAttacked >> 8);
}
```

## Less Advanced

If it is about the long-term evaluation of [telestop](/Pawn_Spans#StopandDistantStop "Pawn Spans") -squares - or the need of advancement of helper(s) to defend the stop-square, things become more complicated and one probably better relies on search and some general bonus to advance half-free pawns and advanced duos. Feel free to cover attackspan-related stuff for less advanced candidates respectively helpers and helper's helpers.

```
d4 is candidate     d4 is faker         d4 faker due to     d4 is candidate
                                        helper's sentry     due to helper's helper f2
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . s . s . . .     . . s . s . . .     . . s . s . . .     . . s . s . . .
. . . . . . . .     . . . . . . . .     . . . . . hs. .     . . . . . hs. .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . c . . . .     . . . f . . . .     . . . f . . . .     . . . c . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . h . h . . .     . . h . . . . .     . . h . h . . .     . . h . h hh. .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
```

# The Sneaker

Also known as a [hidden passed pawn](/Hidden_Passed_Pawn "Hidden Passed Pawn"). A kind of candidate in disguise is an [unfree pawn](/Unfree_Pawns_(Bitboards) "Unfree Pawns (Bitboards)") or [faker](#Faker) that may become a passer through a sacrificial combination. In the diagram white may sacrifice the faker with b5-b6 - allowing black to establish a passer on b6 - but the sneaker on c6 becomes a much more advanced passer with a frontspan of only two against five:

```
. . . . . . . .
. . b . . . . .
. . w . . . . .
. w . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
```

A sneaker is likely advanced (opponent side of the board), [rammed](/Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") and defended, but no lever. No other opposing pawn controls it's stop or telestop squares.

# See also

- [Candidate Passed Pawn](/Candidate_Passed_Pawn "Candidate Passed Pawn")
- [Hidden Passed Pawn](/Hidden_Passed_Pawn "Hidden Passed Pawn")
- [Passed Pawn](/Passed_Pawn "Passed Pawn")
- [Passed Pawns (Bitboards)](/Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)")

# Forum Posts

- [Candidate passers](https://groups.google.com/d/msg/fishcooking/sx7QLbtbEOg/f_rJP6bZiCcJ) by [Stefan Geschwentner](/Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), October 14, 2013 » [Stockfish](/Stockfish "Stockfish")

# External Links

- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)") [[2]](#cite_note-2)
- [Candidates Tournament from Wikipedia](https://en.wikipedia.org/wiki/Candidates_Tournament)
- [Jango Edwards](https://en.wikipedia.org/wiki/Jango_Edwards) - Harry Christmas, September 10, 2009, [Zeche Carl](https://en.wikipedia.org/wiki/Zeche_Carl) [[3]](#cite_note-3), [Essen](https://en.wikipedia.org/wiki/Essen), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc1), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](/University_of_Minnesota "University of Minnesota")
2. [↑](#cite_ref-2) [Hans Kmoch](/Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6
3. [↑](#cite_ref-3) [Zeche Carl](https://en.wikipedia.org/wiki/Zeche_Carl) is part of [The Industrial Heritage Trail](/Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail")

**[Up one Level](/Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**