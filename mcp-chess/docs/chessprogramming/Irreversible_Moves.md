# Irreversible Moves

Source: https://www.chessprogramming.org/Irreversible_Moves

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Moves](/Moves "Moves") \* Irreversible Moves**

**Irreversible Moves** can not be reversed. Thus, they are either [captures](/Captures "Captures") or [pawn moves](/Pawn_Push "Pawn Push") [[1]](#cite_note-1). [Making](/Make_Move "Make Move") those irreversible moves, resets the [halfmove clock](/Halfmove_Clock "Halfmove Clock") inside a [position](/Chess_Position "Chess Position") object to zero, concerning the [fifty-move rule](/Fifty-move_Rule "Fifty-move Rule"). [Quiet](/Quiet_Moves "Quiet Moves") and otherwise [reversible moves](/Reversible_Moves "Reversible Moves"), which lose the [castling rights](/Castling_Rights "Castling Rights"), that is [rook](/Rook "Rook")- and [king](/King "King")-moves from their initial [square](/Squares "Squares"), including [castling](/Castling "Castling") itself, are irreversible in the sense to reverse the same rights - since once a castling right is lost, it is lost forever, and reset the position index to determine [repetition of positions](/Repetitions#RepetitionOfPositions "Repetitions"). However, those "irreversible" moves don't reset, but increment the halfmove clock [[2]](#cite_note-2) [[3]](#cite_note-3).

# See also

- [Fifty-move Rule](/Fifty-move_Rule "Fifty-move Rule")
- [Halfmove Clock](/Halfmove_Clock "Halfmove Clock")
- [Reversible Moves](/Reversible_Moves "Reversible Moves")

# External Links

- [Irreversible (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Irreversible)
- [Irreversible process from Wikipedia](https://en.wikipedia.org/wiki/Irreversible_process)
- [Point of no return from Wikipedia](https://en.wikipedia.org/wiki/Point_of_no_return)
- [Computerschach - Eine Wette, die ich gerne verloren habe](http://www.horst-wandersleben.de/Wette.htm) by [Horst Wandersleben](/index.php?title=Horst_Wandersleben&action=edit&redlink=1 "Horst Wandersleben (page does not exist)") (German) [[4]](#cite_note-4)

# References

1. [↑](#cite_ref-1) including [promotions](/Promotions "Promotions")
2. [↑](#cite_ref-2) [Half Move Clock Confusion](http://www.open-chess.org/viewtopic.php?f=3&t=2209) by HumbleProgrammer, [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 10, 2013
3. [↑](#cite_ref-3) [Computerschach - Eine Wette, die ich gerne verloren habe](http://www.horst-wandersleben.de/Wette.htm) by [Horst Wandersleben](/index.php?title=Horst_Wandersleben&action=edit&redlink=1 "Horst Wandersleben (page does not exist)")
4. [↑](#cite_ref-4) [Dieter Bürßner](/Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") found a game finished in a [fifty-move rule](/Fifty-move_Rule "Fifty-move Rule") draw, where [castling](/Castling "Castling") occurred during the last fifty moves

**[Up one Level](/Moves "Moves")**