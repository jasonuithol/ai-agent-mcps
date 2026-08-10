# Havannah

Source: https://www.chessprogramming.org/Havannah

**[Home](/Main_Page "Main Page") \* [Games](/Games "Games") \* Havannah**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Havannah_winning_structures.svg/330px-Havannah_winning_structures.svg.png)](/File:Havannah_winning_structures.svg)

Base-8 Havannah board sample [[1]](#cite_note-1)

**Havannah**,  
a [two-player](https://en.wikipedia.org/wiki/Two-player_game) [zero-sum](https://en.wikipedia.org/wiki/Zero-sum_%28game_theory%29) and [perfect information](https://en.wikipedia.org/wiki/Perfect_information) [abstract strategy](https://en.wikipedia.org/wiki/Abstract_strategy), [connection](https://en.wikipedia.org/wiki/Connection_game) [board game](https://en.wikipedia.org/wiki/Board_game) played on a base-10 or base-8 [hexagonal board](https://en.wikipedia.org/wiki/Hex_map), invented in 1979 by [Christian Freeling](https://en.wikipedia.org/wiki/Christian_Freeling). The pattern of cells are filled with stones one by one. To win, one has to be the first to connect three sides ("fork") or two corners ("bridge") or to form a ring. Computer Havannah is played at the [Computer Olympiad](/Computer_Olympiad "Computer Olympiad") organized by the [ICGA](/ICGA "ICGA") since 2009 [[2]](#cite_note-2). Most competitive Programs apply variants of [Monte-Carlo Tree Search](/Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") and [UCT](/UCT "UCT").

# [Computer Olympiads](/Computer_Olympiad "Computer Olympiad")

- [14th Computer Olympiad, Pamplona 2009](/14th_Computer_Olympiad#Havannah "14th Computer Olympiad")
- [15th Computer Olympiad, Kanazawa 2010](/15th_Computer_Olympiad#Havannah "15th Computer Olympiad")
- [16th Computer Olympiad, Tilburg 2011](/16th_Computer_Olympiad#Havannah "16th Computer Olympiad")

# Base-10 Board

[![Havannah-10.jpg](/images/4/41/Havannah-10.jpg)](http://www.althofer.de/lange-nacht-jena-2009.html)

Base-10 Board by Ed van Zon, demonstrating bridge, ring and fork [[3]](#cite_note-3)

# The Havannah Challenge

In the Fall/Winter 2002 edition of the "Abstract Games" magazine, [Christian Freeling](https://en.wikipedia.org/wiki/Christian_Freeling) claimed in an open letter that Havannah is too difficult for computers, and that within 10 years no program would be able to achieve a single win against him in a match over ten games - on a base-10 baord, and wagered a €1000 prize money. The challenge match was held October 15–19, 2012 in [Enschede](https://en.wikipedia.org/wiki/Enschede), the [Netherlands](https://en.wikipedia.org/wiki/Netherlands) at the offices of [DGT](/index.php?title=DGT&action=edit&redlink=1 "DGT (page does not exist)") over the internet using the *igGameCenter* [[4]](#cite_note-4) [[5]](#cite_note-5), during which Freeling played ten games against three of the strongest Havannah-playing programs available, [Lajkonik](https://www.game-ai-forum.org/icga-tournaments/program.php?id=697) by [Marcin Ciura](/index.php?title=Marcin_Ciura&action=edit&redlink=1 "Marcin Ciura (page does not exist)") et al., [Castro](https://www.game-ai-forum.org/icga-tournaments/program.php?id=618) by [Timo Ewalds](/index.php?title=Timo_Ewalds&action=edit&redlink=1 "Timo Ewalds (page does not exist)"), and [Wanderer](https://www.game-ai-forum.org/icga-tournaments/program.php?id=605) by [Richard Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") et al., playing (at least) one game as Black and one as White against each opponent. The match ended in a 7-3 score for humanity, but not 10-0, and Freeling already lost the challenge at game 2, when he had to resign a game with white against Lajkonik. In the first game, its parameters selected by [Rémi Coulom's](/R%C3%A9mi_Coulom "Rémi Coulom") [CLOP](/CLOP "CLOP") in quick games versus Castro, Lajkonik played poorly. Marcin used CLOPless values relying on intuition and some test positions for the second game, which Lajkonik won [[6]](#cite_note-6).

# Publications

## 2009

- [Fabien Teytaud](/Fabien_Teytaud "Fabien Teytaud"), [Olivier Teytaud](/Olivier_Teytaud "Olivier Teytaud") (**2009**). *Creating an Upper-Confidence-Tree program for Havannah*. [Advances in Computer Games 12](/Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [inria-00380539 as pdf](http://hal.inria.fr/docs/00/38/05/39/PDF/hav.pdf) » [UCT](/UCT "UCT")

## 2010 ...

- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") (**2010**). *[Improving Monte-Carlo Tree Search in Havannah](http://www.springerlink.com/content/p4x16832317r1214/)*. [CG 2010](/CG_2010 "CG 2010")
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") (**2010**). *Castro wins Havannah Tournament*. [ICGA Journal, Vol. 33, No. 4](/ICGA_Journal#33_4 "ICGA Journal") » [15th Computer Olympiad](/15th_Computer_Olympiad#Havannah "15th Computer Olympiad")
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") (**2011**). *Experiments with Monte-Carlo Tree Search in the Game of Havannah*. [ICGA Journal, Vol. 34, No. 3](/ICGA_Journal#34_3 "ICGA Journal")
- [Jan Stankiewicz](/index.php?title=Jan_Stankiewicz&action=edit&redlink=1 "Jan Stankiewicz (page does not exist)"), [Mark Winands](/Mark_Winands "Mark Winands"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**2011**). *[Monte-Carlo Tree Search Enhancements for Havannah](https://www.conftool.net/acg13/index.php?page=browseSessions&form_session=1)*. [Advances in Computer Games 13](/Advances_in_Computer_Games_13 "Advances in Computer Games 13")
- [Junichi Hashimoto](/Junichi_Hashimoto "Junichi Hashimoto"), [Akihiro Kishimoto](/Akihiro_Kishimoto "Akihiro Kishimoto"), [Kazuki Yoshizoe](/index.php?title=Kazuki_Yoshizoe&action=edit&redlink=1 "Kazuki Yoshizoe (page does not exist)"), [Kokolo Ikeda](/Kokolo_Ikeda "Kokolo Ikeda") (**2011**). *[Accelerated UCT and Its Application to Two-Player Games](https://www.conftool.net/acg13/index.php?page=browseSessions&form_session=3)*. [Advances in Computer Games 13](/Advances_in_Computer_Games_13 "Advances in Computer Games 13")
- [Richard J. Lorentz](/Richard_J._Lorentz "Richard J. Lorentz") (**2012**). *Castro wins Havannah Tournament*. [ICGA Journal, Vol. 35, No. 1](/ICGA_Journal#35_1 "ICGA Journal") » [16th Computer Olympiad](/16th_Computer_Olympiad#Havannah "16th Computer Olympiad")
- [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2012**). *Havannah – The Old Man and the C’s*. [ICGA Journal, Vol. 35, No. 4](/ICGA_Journal#35_4 "ICGA Journal")
- [Jan Krabbenbos](/Jan_Krabbenbos "Jan Krabbenbos"), [Ton van der Valk](/index.php?title=Ton_van_der_Valk&action=edit&redlink=1 "Ton van der Valk (page does not exist)") (**2012**). *The Havannah Challenge*. [ICGA Journal, Vol. 35, No. 4](/ICGA_Journal#35_4 "ICGA Journal")
- [Edouard Bonnet](/index.php?title=Edouard_Bonnet&action=edit&redlink=1 "Edouard Bonnet (page does not exist)"), [Florian Jamain](/index.php?title=Florian_Jamain&action=edit&redlink=1 "Florian Jamain (page does not exist)"), [Abdallah Saffidine](/Abdallah_Saffidine "Abdallah Saffidine") (**2013**). *Havannah and TwixT are PSPACE-complete*. [CG 2013](/CG_2013 "CG 2013") [[7]](#cite_note-7)

## 2015 ...

- [Joris Duguépéroux](/index.php?title=Joris_Dugu%C3%A9p%C3%A9roux&action=edit&redlink=1 "Joris Duguépéroux (page does not exist)"), [Ahmad Mazyad](/index.php?title=Ahmad_Mazyad&action=edit&redlink=1 "Ahmad Mazyad (page does not exist)"), [Fabien Teytaud](/Fabien_Teytaud "Fabien Teytaud"), [Julien Dehos](/index.php?title=Julien_Dehos&action=edit&redlink=1 "Julien Dehos (page does not exist)") (**2016**). *Pruning playouts in Monte-Carlo Tree Search for the game of Havannah*. [CG 2016](/CG_2016 "CG 2016")

# External Links

- [Havannah from Wikipedia](https://en.wikipedia.org/wiki/Havannah)
- [Havannah (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=37)
- [Havannah](http://mindsports.nl/index.php/arena/havannah/) from [MindSports](http://mindsports.nl/index.php)
- [Havannah | Board Game | BoardGameGeek](http://www.boardgamegeek.com/boardgame/2759/havannah)
- [Sensei's Library: Havannah](http://senseis.xmp.net/?Havannah)
- [Lange Nacht der Wissenschaften - Long Night of Sciences, Jena - 2009](http://www.althofer.de/lange-nacht-jena-2009.html), [Ingo Althöfer's](/Ingo_Alth%C3%B6fer "Ingo Althöfer") [Pictorial report](/index.php?title=Ingo_Alth%C3%B6fer_reports_to_include&action=edit&redlink=1 "Ingo Althöfer reports to include (page does not exist)") covers Havannah
- [Havannah Challenge 2012 games](http://mindsports.nl/index.php/arena/havannah/644)
- [Ton van der Valk - YouTube](http://www.youtube.com/user/TonyVanderValk?feature=watch)

# References

1. [↑](#cite_ref-1) Three ways to win in Havannah, Vectorized by [Mysid](https://en.wikipedia.org/wiki/User:Mysid) in [Inkscape](https://en.wikipedia.org/wiki/Inkscape) on a PNG by [Fritzlein](https://en.wikipedia.org/wiki/User:Fritzlein), August 14, 2007, [Havannah from Wikipedia](https://en.wikipedia.org/wiki/Havannah)
2. [↑](#cite_ref-2) [Havannah (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=37)
3. [↑](#cite_ref-3) [Lange Nacht der Wissenschaften - Long Night of Sciences, Jena - 2009](http://www.althofer.de/lange-nacht-jena-2009.html), [Ingo Althöfer's](/Ingo_Alth%C3%B6fer "Ingo Althöfer") [Pictorial report](/index.php?title=Ingo_Alth%C3%B6fer_reports_to_include&action=edit&redlink=1 "Ingo Althöfer reports to include (page does not exist)")
4. [↑](#cite_ref-4) [gGameCenter :: Online games for iGoogle and Facebook](http://www.iggamecenter.com/info/en/main.html)
5. [↑](#cite_ref-5) [Jan Krabbenbos](/Jan_Krabbenbos "Jan Krabbenbos"), [Ton van der Valk](/index.php?title=Ton_van_der_Valk&action=edit&redlink=1 "Ton van der Valk (page does not exist)") (**2012**). *The Havannah Challenge*. [ICGA Journal, Vol. 35, No. 4](/ICGA_Journal#35_4 "ICGA Journal")
6. [↑](#cite_ref-6) [Ingo Althöfer](/Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2012**). *Havannah – The Old Man and the C’s*. [ICGA Journal, Vol. 35, No. 4](/ICGA_Journal#35_4 "ICGA Journal")
7. [↑](#cite_ref-7) [PSPACE-complete from Wikipedia](https://en.wikipedia.org/wiki/PSPACE-complete)

**[Up one Level](/Games "Games")**