# The Bernstein Chess Program

Source: https://www.chessprogramming.org/The_Bernstein_Chess_Program

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* The Bernstein Chess Program**

[![](/images/thumb/1/15/Bernstein-alex.1958.l02645391.ibm-archives.jpg/300px-Bernstein-alex.1958.l02645391.ibm-archives.jpg)](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f6482e6)

[Alex Bernstein](/Alex_Bernstein "Alex Bernstein"), [IBM 704](/IBM_704 "IBM 704") console [[1]](#cite_note-1)

**The Bernstein Chess Program**,  
was the first complete chess program, developed around [1957](/Timeline#1957 "Timeline") at [Service Bureau Corporation](https://en.wikipedia.org/wiki/Service_Bureau_Corporation), [Madison](https://en.wikipedia.org/wiki/Madison_Avenue) & [59th Street](https://en.wikipedia.org/wiki/59th_Street_%28Manhattan%29), [Manhattan](https://en.wikipedia.org/wiki/Manhattan), [New York City](https://en.wikipedia.org/wiki/New_York_City) [[2]](#cite_note-2), by chess player and programmer at [IBM](/index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)"), [Alex Bernstein](/Alex_Bernstein "Alex Bernstein") with his colleagues [Michael de V. Roberts](/Michael_de_V._Roberts "Michael de V. Roberts"), [Timothy Arbuckle](/Timothy_Arbuckle "Timothy Arbuckle") and [Martin Belsky](/Martin_Belsky "Martin Belsky"), supported by chess advisor [Arthur Bisguier](https://en.wikipedia.org/wiki/Arthur_Bisguier) [[3]](#cite_note-3), who became IBM employee at that time and in 1957 [international chess grandmaster](https://en.wikipedia.org/wiki/International_Grandmaster), and supervised by [Nathaniel Rochester](/Nathaniel_Rochester "Nathaniel Rochester") [[4]](#cite_note-4). [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck), who was married to [Joseph F. Traub](/Mathematician#JFTraub "Mathematician"), interviewed Alex Bernstein as published with several details given on the development of the program in her seminal book *[Machines Who Think](/Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")* [[5]](#cite_note-5).

# Quotes

## McCorduck

Quotes by [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) from *[Machines Who Think](/Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")* [[6]](#cite_note-6)

```
Bernstein drew upon not only his own experience with chess, but began to study Modern Chess Openings, which came out then every two years, and spent six months going through some five hundred chess openings. He assigned scores to various positions, scores that depended not only on the pieces retained, but also on area control of the board and mobility. He also developed a fourth measure, what he called a “greens area” around the king, meaning that the more squares outward from the king controlled by his own side the better. But after six months of this he gave it up. He couldn’t make any sense out of it.
```

```
At this time, Bernstein was unaware of Shannon’s seminal papers, and did not know that chess had caught the interests of a group at Los Alamos, including J. Kister, P. Stein, S. Ulam, W. Walden, and M. Wells, who were working on a limited 6x6 board, rather than the regulation 8x8. Nor did he know that Allen Newell, J. C. Shaw, and Herbert Simon together, and John McCarthy independently, were also pondering chess-playing machines. Alex Bernstein only knew that the problem was hot ...
```

```
It was now that Bernstein became aware of Turing’s work and read at least one of Shannon’s papers. When he finally began to see how he might codify some of the principles he felt were essential, he telephoned Claude Shannon at MIT. “I went up to MIT and spent a day or two with him, telling him what I was planning to do, and he said he thought it was intelligent, and a good way of proceeding. Essentially I felt I’d received his blessings, which was pleasant.”
```

```
Bernstein also mentioned that he was working on the problem to Dr. Edward Lasker, a well-known chess writer, who introduced him to Stanislaw Ulam of the Los Alamos group. Bernstein had the advantage that the Los Alamos group didn’t have, of a machine with a large amount of memory, although the four thousand words of memory the IBM 704 had to begin with were insufficient for Bernstein’s program in the end. The 704’s memory was to have doubled by the time Bernstein finished his program, and he still came within two hundred words of overflowing memory.
```

```
So Bernstein’s chess program selected what seemed to be the likeliest fruitful moves, and these it examined in considerable depth, comparing one to another among a number of dimensions. The program contained a large data base, which allowed it to examine any particular piece or square at any time. In descending order of importance, the program asked such questions as, Is the king in check? If the king is in check, there is nothing else to do. Is the king in double check? If he is, merely to capture one piece that threatens the king will be insufficient; the king must be moved. The next question had to do with material: is there any to be gained, or any in danger of capture? And clearly it is more important to rescue or capture a rook than to rescue or capture a pawn, and this was factored into the program.
```

## McCarthy

As mentioned by [John McCarthy](/John_McCarthy "John McCarthy") [[7]](#cite_note-7), the Bernstein Chess Program under construction was presented at the [1956 Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop):

```
Alex Bernstein of IBM presented his chess program under construction. My reaction was to invent and recommend to him alpha-beta pruning. He was unconvinced.
```

# Shannon Type B

The Bernstein Chess Program was the prototype of a selective forward pruning, [Shannon Type B](/Type_B_Strategy "Type B Strategy") program. On an [IBM 704](/IBM_704 "IBM 704"), one of the last vacuum tube computers, it searched four [plies](/Ply "Ply") [minimax](/Minimax "Minimax") in around 8 minutes, considering seven most plausible moves from each position and [evaluated](/Evaluation "Evaluation") [material](/Material "Material"), [mobility](/Mobility "Mobility"), [area control](/Square_Control "Square Control") and [king defense](/King_Safety "King Safety") [[8]](#cite_note-8).

# Publications

[[9]](#cite_note-9)

- [Alex Bernstein](/Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](/Michael_de_V._Roberts "Michael de V. Roberts") (**1958**). *[Computer vs. Chess-Player](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f690f16)*. [Scientific American](/Scientific_American "Scientific American"), Vol. 198, reprinted **1988** in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Alex Bernstein](/Alex_Bernstein "Alex Bernstein")  (**1958**). *[A Chess Playing Program for the IBM 704](http://www.computerhistory.org/chess/full_record.php?iid=doc-4316153963418)*. [Chess Review](https://en.wikipedia.org/wiki/Chess_Review), July 1958
- [Alex Bernstein](/Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](/Michael_de_V._Roberts "Michael de V. Roberts"), [Timothy Arbuckle](/Timothy_Arbuckle "Timothy Arbuckle"), [Martin Belsky](/Martin_Belsky "Martin Belsky") (**1958**). *[A chess playing program for the IBM 704](https://www.computerhistory.org/chess/doc-431e18a41d415/)*. Proceedings of the 1958 Western Joint Computer Conference
- [Fritz Leiber](https://en.wikipedia.org/wiki/Fritz_Leiber) (**1962**). *[The 64-Square Madhouse](https://en.wikipedia.org/wiki/Fritz_Leiber_bibliography#Short_stories)*. [Worlds of If](http://www.unz.org/Pub/WorldsIfSF-1962may-00064) [[10]](#cite_note-10)
- [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) (**1979**). *Machines Who Think*. [W. H. Freeman](https://en.wikipedia.org/wiki/W._H._Freeman_and_Company)
- [David Levy](/David_Levy "David Levy"), [Monroe Newborn](/Monroe_Newborn "Monroe Newborn") (**1982**). *[All About Chess and Computers](http://link.springer.com/book/10.1007/978-3-642-85538-2)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) (**2004**). *[Machines Who Think: A Personal Inquiry into the History and Prospects of Artificial Intelligence](/Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")*. [A. K. Peters](https://en.wikipedia.org/wiki/A_K_Peters) (25th anniversary edition)

# External Links

- [Alex Bernstein](https://www.computerhistory.org/chess/search/?q=Alex+Bernstein) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
- [Photos](https://www.gettyimages.de/fotos/ibm-704?editorialproducts=timelife&family=editorial&phrase=IBM%20704&page=1&recency=anydate&suppressfamilycorrection=true) with [Edward Lasker](https://en.wikipedia.org/wiki/Edward_Lasker) by [Andreas Feininger](https://en.wikipedia.org/wiki/Andreas_Feininger), [Getty Images](https://en.wikipedia.org/wiki/Getty_Images) » [Quote from Machines Who Think](/IBM_704#QuoteMachinesWhoThink "IBM 704")
- [The History of Computer Chess - Part 3 - Alex Bernstein](https://www.chess.com/blog/Ginger_GM/the-history-of-computer-chess-part-3-alex-bernstein) by [Simon Williams](https://en.wikipedia.org/wiki/Simon_Williams_(chess_player)), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), August 31, 2019
- [The History of Computer Chess - Part 4 - Alex Bernstein continued...](https://www.chess.com/blog/Ginger_GM/the-history-of-computer-chess-part-4-alex-bernstein-continued) by [Simon Williams](https://en.wikipedia.org/wiki/Simon_Williams_(chess_player)), [Chess.com](/index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), September 28, 2019
- [Runner-Up - The New Yorker - November 29, 1958](https://www.newyorker.com/magazine/1958/11/29/runner-up-4)
- Alex Bernstein: *juega al ajedrez con un* IBM 704 (Thinking Machines), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [IBM programmer Alex Bernstein](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f6482e6) 1958 Courtesy of [IBM](/index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") Archives from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
2. [↑](#cite_ref-2) [Runner-Up - The New Yorker - November 29, 1958](http://www.newyorker.com/magazine/1958/11/29/runner-up-4)
3. [↑](#cite_ref-3) [Arthur Bisguier from Wikipedia.de](http://de.wikipedia.org/wiki/Arthur_Bisguier) (German)
4. [↑](#cite_ref-4) [Nathaniel Rochester (computer scientist) from Wikipedia](https://en.wikipedia.org/wiki/Nathaniel_Rochester_%28computer_scientist%29)
5. [↑](#cite_ref-5) [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=17) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), June 09, 2019
6. [↑](#cite_ref-6) [Pamela McCorduck](https://en.wikipedia.org/wiki/Pamela_McCorduck) (**2004**). *[Machines Who Think: A Personal Inquiry into the History and Prospects of Artificial Intelligence](/Artificial_Intelligence#MachinesWhoThink "Artificial Intelligence")*. [A. K. Peters](https://en.wikipedia.org/wiki/A_K_Peters) (25th anniversary edition), pp. 182-185
7. [↑](#cite_ref-7) [The Dartmouth Workshop--as planned and as it happened](http://www-formal.stanford.edu/jmc/slides/dartmouth/dartmouth/node1.html)
8. [↑](#cite_ref-8) [Alex Bernstein](/Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](/Michael_de_V._Roberts "Michael de V. Roberts") (**1958**). *[Computer vs. Chess-Player](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f690f16)*. [Scientific American](/Scientific_American "Scientific American"), Vol. 198, reprinted **1988** in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
9. [↑](#cite_ref-9) hosted by [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
10. [↑](#cite_ref-10) [Fritz Leiber's "The 64-Square Madhouse"](http://www.talkchess.com/forum/viewtopic.php?t=49858) by [Ian Osgood](/Ian_Osgood "Ian Osgood"), [CCC](/CCC "CCC"), October 28, 2013

**[Up one Level](/Engines "Engines")**