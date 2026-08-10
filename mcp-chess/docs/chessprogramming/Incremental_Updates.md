# Incremental Updates

Source: https://www.chessprogramming.org/Incremental_Updates

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* [Position](/Chess_Position "Chess Position") \* Incremental Updates**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Kandinsky_-_Mouvement_I.jpg/330px-Kandinsky_-_Mouvement_I.jpg)](/File:Kandinsky_-_Mouvement_I.jpg)

[Wassily Kandinsky](/Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Mouvement I [[1]](#cite_note-1)

**Incremental updates** keep global or shared structures up to date after [making](/Make_Move "Make Move") and [unmaking](/Unmake_Move "Unmake Move") [moves](/Moves "Moves") on the [internal board](/Board_Representation "Board Representation"), likely inside a [depth-first](/Depth-First "Depth-First"), [alpha-beta](/Alpha-Beta "Alpha-Beta") like [search-algorithm](/Search "Search"). Incremental update on the same global or shared data ever and ever, will likely keep it in fast cache memory, and saves [memory bandwidth](https://en.wikipedia.org/wiki/Memory_bandwidth) compared to a [Copy-Make](/Copy-Make "Copy-Make") approach, which needs a make-update on the copy as well, but no unmake-update rather than decrementing a [ply-index](/Ply "Ply") or fetching a pointer.

# Chess Position

Incremental updates by make/unmake are obligatory for square centric board [arrays](/Array "Array") like [mailbox](/Mailbox "Mailbox") and [0x88](/0x88 "0x88") along with their [piece-lists](/Piece-Lists#IncrementalUpdate "Piece-Lists"), as well for the classical [bitboard board-definition](/Bitboard_Board-Definition "Bitboard Board-Definition"). A move only affects a small fraction of the complete board structure and the update cost is small compared to a copy of the whole board. Also one usually doesn't need an array of boards for random access, but only the current one.

However, there are aspects of a [chess position](/Chess_Position "Chess Position"), which can not generally restored from a child-position by unmaking a move, and which therefor need to be restored by either re-playing the whole game record from the root position, or to be memorized inside an [array](/Array "Array") indexed by [ply](/Ply "Ply") or on a [stack](/Stack "Stack") ([LIFO](https://en.wikipedia.org/wiki/LIFO_(computing))), most notably [ep state](/En_passant "En passant"), [castling rights](/Castling_Rights "Castling Rights") and the [halfmove clock](/Halfmove_Clock "Halfmove Clock") enforcing the [fify-move rule](/Fifty-move_Rule "Fifty-move Rule"). Also, if one doesn't keep a captured piece (if any) inside the move object, one has to memorize those pieces elsewhere as well, to restore the target square of the move about to unmake.

# Material and Hash keys

Subject of incremental updates are further data which only change conditionally on certain move types, like [material](/Material "Material") signature, only affected by [captures](/Captures "Captures") or [promotions](/Promotions "Promotions"), or for instance [zobrist keys](/Zobrist_Hashing "Zobrist Hashing") for a [pawn hash table](/Pawn_Hash_Table "Pawn Hash Table"), only affected by moving/capturing pawns. Standard zobrist keys for [TT purpose](/Transposition_Table "Transposition Table") and dependent on ep state and castling rights, are slightly more complicated to restore. If stored inside a record anyway to detect [repetitions](/Repetitions "Repetitions"), one has the option to restore the key after unmake from that record.

It is a good idea to compare incremental updated stuff like zobrist keys with its from scratch generated counterparts for [debug](/Debugging "Debugging") purposes.

# Evaluation

Other global structures or variables as candidates of an incremental update are related to [Evaluation](/Evaluation "Evaluation"), beside the mentioned [material](/Material "Material") (balance), [lazy evaluation](/Lazy_Evaluation "Lazy Evaluation") terms, like the sum of all [piece-square values](/Piece-Square_Tables "Piece-Square Tables") [[2]](#cite_note-2) [[3]](#cite_note-3) .

# Attack table

Some programs keep [Attack and Defend Maps](/Attack_and_Defend_Maps "Attack and Defend Maps") up to date incrementally, which is runtime dependent on the number of squares whose attacks-to are influenced by the move. Due to its size and utilization, copy-make is no issue, but on the fly generation if actually needed.

# See also

- [Attack and Defend Maps](/Attack_and_Defend_Maps "Attack and Defend Maps")
- [BCH Hashing](/BCH_Hashing "BCH Hashing")
- [Bitboard Update By Move](/General_Setwise_Operations#UpdateByMove "General Setwise Operations")
- [Color Flipping](/Color_Flipping "Color Flipping")
- [Copy-Make](/Copy-Make "Copy-Make")
- [Encoding Moves](/Encoding_Moves "Encoding Moves")
- [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation")
- [Make Move](/Make_Move "Make Move")
- [Material](/Material "Material")
- [NNUE](/NNUE "NNUE")
- [Unmake Move](/Unmake_Move "Unmake Move")
- [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")

# Publications

- [John J. Scott](/John_J._Scott "John J. Scott") (**1969**). *A chess-playing program*. [Machine Intelligence Vol. 4](http://www.doc.ic.ac.uk/~shm/MI/mi4.html)
- [David Slate](/David_Slate "David Slate"), [Larry Atkin](/Larry_Atkin "Larry Atkin") (**1977**). *Chess 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](/Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (1988) in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Peter W. Frey](/Peter_W._Frey "Peter W. Frey") (**1983**). *The Alpha-Beta Algorithm: Incremental Updating, Well-Behaved Evaluation Functions, and Non-Speculative Forward Pruning*. Computer Game-Playing (ed. [Max Bramer](/Max_Bramer "Max Bramer")), pp. 285-289. Ellis Horwood Limited

# Forum Posts

## 2005 ...

- [Incremental updating for positional evaluation](http://www.talkchess.com/forum/viewtopic.php?t=20370) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), March 27, 2008
- [Incremental Zobrist - slow?](http://www.talkchess.com/forum/viewtopic.php?t=28523) by [Vlad Stamate](/Vlad_Stamate "Vlad Stamate"), [CCC](/CCC "CCC"), June 20, 2009 » [Zobrist Hashing](/Zobrist_Hashing "Zobrist Hashing")
- [undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?t=29770) by BoldReceiver, [CCC](/CCC "CCC"), September 16, 2009

:   [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291570&t=29770) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), September 16, 2009 » [Doch](/Doch "Doch")

## 2010 ...

- [Incremental or non-incremental PST evaluation calcs](http://www.talkchess.com/forum/viewtopic.php?t=42167) by [Mark Pearce](/index.php?title=Mark_Pearce&action=edit&redlink=1 "Mark Pearce (page does not exist)"), [CCC](/CCC "CCC"), January 26, 2012 » [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables")
- [copy/make vs make/unmake](http://www.talkchess.com/forum/viewtopic.php?t=50805) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), January 07, 2014
- [Incrementally-updated attack map](http://www.talkchess.com/forum/viewtopic.php?t=52085) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), April 21, 2014 » [Attack and Defend Maps](/Attack_and_Defend_Maps "Attack and Defend Maps")
- [Memory usage in make/unmake vs logic complexity](http://www.talkchess.com/forum/viewtopic.php?t=53502) by [Matthew Lai](/Matthew_Lai "Matthew Lai"), [CCC](/CCC "CCC"), August 30, 2014

## 2015 ...

- [Incremental update](http://www.talkchess.com/forum/viewtopic.php?t=58628) by [Matthew R. Brades](/Matthew_R._Brades "Matthew R. Brades"), [CCC](/CCC "CCC"), December 19, 2015
- [The Inferno thread](http://www.talkchess.com/forum3/viewtopic.php?t=63356) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/CCC "CCC"), March 06, 2017 » [Tenjiku Shogi](/Shogi#Tenjiku "Shogi")
- [How to incrementally update attack tables?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68995) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), November 21, 2018 » [Attack and Defend Maps](/Attack_and_Defend_Maps "Attack and Defend Maps")

# External Links

- [Search Techniques in REBEL (Lazy Eval)](http://www.top-5000.nl/authors/rebel/chess840.htm#LAZY%20EVAL) from [How Rebel Plays Chess](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder") » [Lazy Evaluation](/Lazy_Evaluation "Lazy Evaluation"), [Rebel](/Rebel "Rebel")

# References

1. [↑](#cite_ref-1) [Wassily Kandinsky - Mouvement I](https://commons.wikimedia.org/wiki/File:Kandinsky_-_Mouvement_I.jpg), [Tretyakov Gallery](https://en.wikipedia.org/wiki/Tretyakov_Gallery)
2. [↑](#cite_ref-2) [Search Techniques in REBEL (Lazy Eval)](http://www.top-5000.nl/authors/rebel/chess840.htm#LAZY%20EVAL) from [How Rebel Plays Chess](http://www.top-5000.nl/authors/rebel/chess840.htm) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
3. [↑](#cite_ref-3) [Incremental updating for positional evaluation](http://www.talkchess.com/forum/viewtopic.php?t=20370) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), March 27, 2008

**[Up one Level](/Chess_Position "Chess Position")**