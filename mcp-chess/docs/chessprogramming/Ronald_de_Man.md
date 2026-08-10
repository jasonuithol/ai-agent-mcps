# Ronald de Man

Source: https://www.chessprogramming.org/Ronald_de_Man

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Ronald de Man**

**Ronald de Man**, [alias](https://en.wikipedia.org/wiki/Alias) [Syzygy](https://en.wikipedia.org/wiki/Syzygy),  
a Dutch mathematician, computer scientist and IP lawyer, in the 90s researcher at [Eindhoven University of Technology](https://en.wikipedia.org/wiki/Eindhoven_University_of_Technology), competitor at the [International Mathematical Olympiad](https://en.wikipedia.org/wiki/International_Mathematical_Olympiad) 1990, winning the Silver medal [[1]](#cite_note-1) , and the [ACM International Collegiate Programming Contest](https://en.wikipedia.org/wiki/ACM_International_Collegiate_Programming_Contest) 1995, to win Bronze within the *ARoMA* team from [Delft University of Technology](/Delft_University_of_Technology "Delft University of Technology") [[2]](#cite_note-2) [[3]](#cite_note-3) . He is co-developer of the [Linux](/Linux "Linux") [desktop environment](https://en.wikipedia.org/wiki/Desktop_environment) and [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface) [GNOME](https://en.wikipedia.org/wiki/GNOME) [[4]](#cite_note-4) , and as chess programmer author of the chess and [Antichess](/Losing_Chess "Losing Chess") [[5]](#cite_note-5) playing program [Sjaak](/Sjaak "Sjaak"), which plays at [FICS](/index.php?title=FICS&action=edit&redlink=1 "FICS (page does not exist)") under the handle *TrojanKnight* [[6]](#cite_note-6) [[7]](#cite_note-7) [[8]](#cite_note-8). He ported [Stockfish](/Stockfish "Stockfish") to plain [C](/C "C"), dubbed [CFish](/CFish "CFish"), and to [Rust](/Rust "Rust") as [Rustfish](/Rustfish "Rustfish").

# Scoring Root Moves

Ronald de Man proposed a method to apply [randomness](/Search_with_Random_Leaf_Values "Search with Random Leaf Values") [[9]](#cite_note-9) and/or bonuses, i.e. developing bonus, or penalties suggested by an [oracle](/Oracle "Oracle"), in [scoring](/Score "Score") [moves](/Moves "Moves") at the [root](/Root "Root") without any changes in [alpha-beta search](/Alpha-Beta "Alpha-Beta") or [leaf evaluation](/Evaluation "Evaluation"), and without any problems with the [transposition table](/Transposition_Table "Transposition Table") [[10]](#cite_note-10):

```
First of all, don't worry, it is possible. But you should not try to pass the bonus to the tip nodes. That would indeed give hash problems. The solution is to not change anything in your Search() procedure. That already solves all potential hash problems. You just add the bonus AFTER Search() has returned a value for a particular root move. So that would be done in your SearchRoot(). What you basically do there is change every occurrence of
```

```
value = -Search(-beta, -alpha,...)
in
value = bonus[n] - Search(bonus[n]-beta, bonus[n]-alpha,...)
```

```
where bonus[n] is the development bonus value for the move you are currently searching. It is all very natural when you think about it. You should consider Search() as a black box. You give it some numbers alpha and beta, and Search() gives you a number x, with the properties that, relative to the real value v of this move,
```

```
1. If v <= alpha, then x <= alpha,
2. If v >= beta, then x >= beta,
3. If alpha < v < beta, then x = v.
```

```
If you search a move, you want to know if its real value + bonus[n] is bigger than alpha. So you want to know if its real value is bigger than alpha-bonus[n]. So you give Search() the bounds alpha-bonus[n] and beta-bonus[n], and add bonus[n] to the result. And you do this in SearchRoot().
```

```
So no fudging with hash table scores whatsoever!
```

```
Of course this trick gives all kinds of possibilities. Not only can you stimulate development, or add in some randomization. It is also easy to solve the 'underpromotion' problem: to prevent the program from under-promoting to a rook (in situations where the piece will probably be captured the next move anyway), you give underpromotion moves a penalty. Or in trivially drawn endgames like KRKR you give captures a bonus. Or in not-so-trivially drawn endgames for which tablebases give draw values you give moves that give away a piece (but do not change the outcome) a penalty, hoping that the opponent will make a fatal mistake further on in the game :-)
```

```
Ronald de Man
```

# Bloom Filter

Ronald de Man revealed the trick to speed up [repetition detection](/Repetitions "Repetitions") with a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter), implemented as a small [hash table](/Hash_Table "Hash Table") indexed by some lower bits of the hash-key, to increment a counter while entering and decrement the counter while leaving a node [[11]](#cite_note-11) [[12]](#cite_note-12) .

# Syzygy Bases

In April 2013, Ronald de Man published his [Syzygy Bases](/Syzygy_Bases "Syzygy Bases") [[13]](#cite_note-13) , a compact [endgame tablebase](/Endgame_Tablebases "Endgame Tablebases") of up to six pieces. It consist of two sets of files, **WDL** files storing win/draw/loss information considering the [fifty-move rule](/Fifty-move_Rule "Fifty-move Rule"), for access during search, and **DTZ** files with [distance-to-zero](/Endgame_Tablebases#DTZ "Endgame Tablebases") information for access at the [root](/Root "Root") [[14]](#cite_note-14) [[15]](#cite_note-15) .

# Selected Publications

[[16]](#cite_note-16)

- Ronald de Man (**1995**). *[On Composants of Solenoids](http://www.ams.org/journals/era/1995-01-02/S1079-6762-95-02005-1/home.html)*. [Fundamenta Mathematicae](https://en.wikipedia.org/wiki/Fundamenta_Mathematicae) 147, [pdf](http://matwbn.icm.edu.pl/ksiazki/fm/fm147/fm14726.pdf) [[17]](#cite_note-17)
- Ronald de Man (**1999**). *[The Generating Function for the Number of Roots of a Coxeter Group](http://dl.acm.org/citation.cfm?id=312392)*. [Journal of Symbolic Computation, Vol. 27, No.6](http://www.informatik.uni-trier.de/~ley/db/journals/jsc/jsc27.html#Man99) [[18]](#cite_note-18)
- [Richa Malhotra](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Malhotra:Richa.html), [Ronald van Haalen](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/h/Haalen:Ronald_van.html), Ronald de Man, [Michiel van Everdingen](http://nl.linkedin.com/in/michielvaneverdingen) (**2003**) *[Managing service-level agreements in metro ethernet networks using backpressure](http://onlinelibrary.wiley.com/doi/10.1002/bltj.10065/abstract)*. [Bell Labs Technical Journal, Vol. 8, No. 2](http://www.informatik.uni-trier.de/~ley/db/journals/bell/bell8.html#MalhotraHME03) [[19]](#cite_note-19) .

# Forum Posts

## 1995 ...

- [Re: random play](http://groups.google.com/group/rec.games.chess.computer/msg/a30577d2a7a74a51) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 28, 1996 [[20]](#cite_note-20)
- [Re: Hash functions for use with a transition table](http://groups.google.com/group/rec.games.chess.computer/msg/9b240379394bc968) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 7, 1997 » [BCH Hashing](/BCH_Hashing "BCH Hashing")
- [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/0df39371422a600c) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), April 3, 1997 » [Oracle](/Oracle "Oracle")
- [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
- [Re: triple repetition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c431ac1739de871b/d8f8d6ee1b252b86) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 27, 1997

## 2010 ...

- [New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681) by Ronald de Man, [CCC](/CCC "CCC"), April 01, 2013 » [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")
- [tablebase caching / mmap() / page cache](http://www.talkchess.com/forum/viewtopic.php?t=49702) by Ronald de Man, [CCC](/CCC "CCC"), October 13, 2013 » [Memory](/Memory "Memory"), [Endgame Tablebases](/Endgame_Tablebases "Endgame Tablebases"), [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")
- [Question to syzygy author](http://www.talkchess.com/forum/viewtopic.php?t=59947) by [Marco Costalba](/Marco_Costalba "Marco Costalba"), [CCC](/CCC "CCC"), April 24, 2016
- [tablebase compression / academic integrity](http://www.talkchess.com/forum/viewtopic.php?t=60222) by Ronald de Man, [CCC](/CCC "CCC"), May 19, 2016 [[21]](#cite_note-21)
- [pin-aware see](https://groups.google.com/d/msg/fishcooking/S_4E_Xs5HaE/mS3VTnuEFgAJ) by Ronald de Man, [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), September 14, 2016 » [SEE - The Swap Algorithm](/SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm"), [Pin](/Pin "Pin"), [Stockfish](/Stockfish "Stockfish")
- [DTM50](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67536) by Ronald de Man, [CCC](/CCC "CCC"), May 22, 2018

# External Links

- [syzygy1 · GitHub](https://github.com/syzygy1)
- [GitHub - syzygy1/tb](https://github.com/syzygy1/tb) » [Syzygy Bases](/Syzygy_Bases "Syzygy Bases")
- [GitHub - syzygy1/Cfish: C port of Stockfish](https://github.com/syzygy1/Cfish) » [CFish](/CFish "CFish")
- [Syzygy from Wikipedia](https://en.wikipedia.org/wiki/Syzygy)

:   [Syzygy (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Syzygy_%28mathematics%29)

- [ICGA: Losing Chess](http://icga.leidenuniv.nl/icga/games/losingchess/) by [Guy Haworth](/Guy_Haworth "Guy Haworth")

# References

1. [↑](#cite_ref-1) [International Mathematical Olympiad - Ronald de Man](http://www.imo-official.org/participant_r.aspx?id=2462)
2. [↑](#cite_ref-2) ['Programmeren hoef je niet te kunnen' - TU Delta - Weekblad van de Technische Universiteit Delft](http://www.delta.tudelft.nl/artikel/-programmeren-hoef-je-niet-te-kunnen/10155), March 16, 1995 (Dutch)
3. [↑](#cite_ref-3) [ACM Programming Contest World Finals](http://icpc.baylor.edu/past/)
4. [↑](#cite_ref-4) [gnome-libs-32bit-1.4.2-11.1.x86\_64 RPM](http://rpmfind.net/linux/RPM/opensuse/11.1/x86_64/gnome-libs-32bit-1.4.2-11.1.x86_64.html)
5. [↑](#cite_ref-5) [ICGA: Losing Chess](http://ilk.uvt.nl/icga/games/losingchess/) by [Guy Haworth](/Guy_Haworth "Guy Haworth")
6. [↑](#cite_ref-6) [Statistics for TrojanKnight(C)](http://www.nicklong.net/chess/atomic/mewis/trojanknight.txt)
7. [↑](#cite_ref-7) [Re: AEGON 97/ 1st round: HIARCS lost](http://groups.google.com/group/rec.games.chess.computer/msg/6bb58a0605f7e2f1) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), April 25 1997
8. [↑](#cite_ref-8) [FICS Statistics - April 2004, Best Ratings - Computer List](http://poincare.matf.bg.ac.rs/~andrew/suicide/fics/en0404C.htm)
9. [↑](#cite_ref-9) [Re: random play](https://groups.google.com/d/msg/rec.games.chess.computer/AI3xadkLEIk/UUqnp9J3BaMJ) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), November 28, 1996
10. [↑](#cite_ref-10) [Re: computer chess "oracle" ideas...](https://groups.google.com/d/msg/rec.games.chess.computer/me7GkjsEgds/iC_ZJm5UwswJ) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997, see also [Re: mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=390268) by [Don Beal](/Don_Beal "Don Beal"), [CCC](/CCC "CCC"), October 04, 2004 » [Mate Threat Extensions](/Mate_Threat_Extensions "Mate Threat Extensions"), [Null Move](/Null_Move_Pruning "Null Move Pruning") and [WAC](/Win_at_Chess "Win at Chess") booster
11. [↑](#cite_ref-11) [Re: triple repetition](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c431ac1739de871b/d8f8d6ee1b252b86) by Ronald de Man, [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), October 27, 1997
12. [↑](#cite_ref-12) [Marcel van Kervinck](/Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf)
13. [↑](#cite_ref-13) [Re: New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681&start=45) by Ronald de Man, [CCC](/CCC "CCC"), April 10, 2013
14. [↑](#cite_ref-14) [New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681) by Ronald de Man, [CCC](/CCC "CCC"), April 01, 2013
15. [↑](#cite_ref-15) [syzygy1/tb · GitHub](https://github.com/syzygy1/tb) by Ronald de Man
16. [↑](#cite_ref-16) [DBLP: Ronald de Man](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Man:Ronald_de.html)
17. [↑](#cite_ref-17) [Solenoidal vector field from Wikipedia](https://en.wikipedia.org/wiki/Solenoidal_vector_field)
18. [↑](#cite_ref-18) [Coxeter group from Wikipedia](https://en.wikipedia.org/wiki/Coxeter_group)
19. [↑](#cite_ref-19) [Metro Ethernet from Wikipedia](https://en.wikipedia.org/wiki/Metro_Ethernet)
20. [↑](#cite_ref-20) [Randomness in move selection](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ba5f8759ec0ce454) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), December 01, 1996
21. [↑](#cite_ref-21) [Victor Zakharov](/Victor_Zakharov "Victor Zakharov"), [Michael G. Malkovsky](/Michael_G._Malkovsky "Michael G. Malkovsky"), [Vladislav Y. Shchukin](/Vladislav_Y._Shchukin "Vladislav Y. Shchukin") (**2016**). *[Compression of underdetermined data in a 7-piece chess table](http://link.springer.com/article/10.3103%2FS0278641916010076)*. [Moscow University Computational Mathematics and Cybernetics](http://www.springer.com/mathematics/journal/11968), Vol. 40, No. 1

**[Up one level](/People "People")**