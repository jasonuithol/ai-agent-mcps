# Breakthrough (Game)

Source: https://www.chessprogramming.org/Breakthrough_(Game)

**[Home](/Main_Page "Main Page") \* [Games](/Games "Games") \* Breakthrough (Game)**

**Breakthrough**,  
an [abstract strategy](https://en.wikipedia.org/wiki/Abstract_strategy) board game invented by [Dan Troyka](/index.php?title=Dan_Troyka&action=edit&redlink=1 "Dan Troyka (page does not exist)") in 2000 [[1]](#cite_note-1) [[2]](#cite_note-2). It can be played on various board sizes, most common on an **8x8** [chessboard](/Chessboard "Chessboard") with initially 16 [pawn](/Pawn "Pawn") like counters on its two back ranks. Counters may [push](/Pawn_Push "Pawn Push") one step straight or diagonally forward if the target square is empty, or [capture](/Captures "Captures") one step diagonally if the target square is occupied by an opponent piece. The first player to reach the opponent's back rank or captures all opponent men wins the game [[3]](#cite_note-3).

# Solving Small Boards

[Abdallah Saffidine](/Abdallah_Saffidine "Abdallah Saffidine"), [Nicolas Jouandeau](/index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)"), and [Tristan Cazenave](/Tristan_Cazenave "Tristan Cazenave") applied race patterns and an extension of [Job-level Proof-number search](/Proof-Number_Search "Proof-Number Search") to solve Breakthrough on up to **6x5** boards [[4]](#cite_note-4).

[![Breakthrough5x5.jpg](/images/d/d0/Breakthrough5x5.jpg)](/File:Breakthrough5x5.jpg)

# Programming

As introduced at the [Computer and Games 2013](/CG_2013 "CG 2013") conference in [Yokohama](https://en.wikipedia.org/wiki/Yokohama), [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") and [Therese Horey](/index.php?title=Therese_Horey&action=edit&redlink=1 "Therese Horey (page does not exist)") used a hybrid version of [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") for Breakthrough [[5]](#cite_note-5). Playouts are not complete games but fragments where a reliable evaluation function can be used at the stopping points [[6]](#cite_note-6).

# [Computer Olympiads](/Computer_Olympiad "Computer Olympiad")

- [20th Computer Olympiad, Leiden 2017](/20th_Computer_Olympiad#Breakthrough "20th Computer Olympiad")

# See also

- [BreakThrough](/BreakThrough "BreakThrough") (Chess Program)
- [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [Pawns Breakthrough](/Pawns_Breakthrough "Pawns Breakthrough")
- [Proof-Number Search](/Proof-Number_Search "Proof-Number Search")

# Selected Publications

- [Abdallah Saffidine](/Abdallah_Saffidine "Abdallah Saffidine"), [Nicolas Jouandeau](/index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)"), [Tristan Cazenave](/Tristan_Cazenave "Tristan Cazenave") (**2011**). *Solving breakthrough with Race Patterns and Job-Level Proof Number Search*. [Advances in Computer Games 13](/Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/solving.pdf)
- [Stephan Schiffel](/Stephan_Schiffel "Stephan Schiffel") (**2011**). *Knowledge-Based General Game Playing*. Ph.D. thesis, [Dresden University of Technology](https://en.wikipedia.org/wiki/Dresden_University_of_Technology), advisor [Michael Thielscher](/Michael_Thielscher "Michael Thielscher") and [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [pdf](http://www.qucosa.de/fileadmin/data/qucosa/documents/8874/Stephan_Schiffel_Diss.pdf) [[7]](#cite_note-7)
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz"), [Therese Horey](/index.php?title=Therese_Horey&action=edit&redlink=1 "Therese Horey (page does not exist)") (**2013**). *Programming Breakthrough*. [CG 2013](/CG_2013 "CG 2013")
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz"), [Andrew Isaac](/index.php?title=Andrew_Isaac&action=edit&redlink=1 "Andrew Isaac (page does not exist)") (**2016**). *Using Partial Tablebases in Breakthrough*. [CG 2016](/CG_2016 "CG 2016")
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") (**2017**). *Machine Learning in the Game of Breakthrough*. [Advances in Computer Games 15](/Advances_in_Computer_Games_15 "Advances in Computer Games 15")
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") (**2017**). *Wanderer wins Breakthrough tournament*. [ICGA Journal, Vol. 39, Nos. 3-4](/ICGA_Journal#39_34 "ICGA Journal") » [20th Computer Olympiad 2017](/20th_Computer_Olympiad#Breakthrough "20th Computer Olympiad")

# External Links

- [Breakthrough (board game) from Wikipedia](https://en.wikipedia.org/wiki/Breakthrough_%28board_game%29)
- [Interesting games - MindSports](http://www.mindsports.nl/index.php/side-dishes/interesting-games?start=11)
- [Breakthrough - Free 8x8 Board Game - By Dan Troyka - about.com](http://boardgames.about.com/od/free8x8games/a/breakthrough.htm)
- [Little Golem - online board games - Breakthrough](http://www.littlegolem.net/jsp/forum/topic2.jsp?forum=120&topic=63)

# References

1. [↑](#cite_ref-1) [William Daniel Troyka - Mancala World](http://mancala.wikia.com/wiki/William_Daniel_Troyka)
2. [↑](#cite_ref-2) [Breakthrough (board game) from Wikipedia](https://en.wikipedia.org/wiki/Breakthrough_%28board_game%29)
3. [↑](#cite_ref-3) Image from [Abdallah Saffidine](/Abdallah_Saffidine "Abdallah Saffidine"), [Nicolas Jouandeau](/index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)"), [Tristan Cazenave](/Tristan_Cazenave "Tristan Cazenave") (**2011**). *Solving breakthrough with Race Patterns and Job-Level Proof Number Search*. [Advances in Computer Games 13](/Advances_in_Computer_Games_13 "Advances in Computer Games 13") - Fig. 1: Rules for the game
4. [↑](#cite_ref-4) [Abdallah Saffidine](/Abdallah_Saffidine "Abdallah Saffidine"), [Nicolas Jouandeau](/index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)"), [Tristan Cazenave](/Tristan_Cazenave "Tristan Cazenave") (**2011**). *Solving breakthrough with Race Patterns and Job-Level Proof Number Search*. [Advances in Computer Games 13](/Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/solving.pdf)
5. [↑](#cite_ref-5) [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz"), [Therese Horey](/index.php?title=Therese_Horey&action=edit&redlink=1 "Therese Horey (page does not exist)") (**2013**). *Programming Breakthrough*. [CG 2013](/CG_2013 "CG 2013")
6. [↑](#cite_ref-6) [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2013**). *The wild Years are gone: Monte Carlo in Smoother Waters*. Conference Report [CG 2013](/CG_2013 "CG 2013"), [ICGA Journal, Vol. 36, No. 3](/ICGA_Journal#36_3 "ICGA Journal")
7. [↑](#cite_ref-7) Appandix A. The Rules of Breakthrough - in [Game Description Language](/General_Game_Playing#GDL "General Game Playing")

**[Up one Level](/Games "Games")**