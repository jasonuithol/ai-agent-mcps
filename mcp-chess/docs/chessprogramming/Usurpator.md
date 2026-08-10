# Usurpator

Source: https://www.chessprogramming.org/Usurpator

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Usurpator**

[![](/images/3/38/Usurbook.jpg)](http://home.hccnet.nl/h.g.muller/chess.html)

Usurpator [[1]](#cite_note-1)

**Usurpator**,  
a series of microcomputer chess programs by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") (HGM), written in [assembly](/Assembly "Assembly") for [6800](/6800 "6800") (Usurpator I) and [6502](/6502 "6502") (Usurpator II), published with listings as a regular book [[2]](#cite_note-2), also adapted for the [Acorn Atom](/Acorn_Atom "Acorn Atom") [[3]](#cite_note-3) [[4]](#cite_note-4) . Usurpator participated at eight [Dutch Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), with some gaps seven times in the period from [1981](/DOCCC_1981 "DOCCC 1981") until the [10th DOCCC](/DOCCC_1990 "DOCCC 1990"), where Usurpator competed as matchbox computer [[5]](#cite_note-5) .

In 2005, 15 years later, Harm Geert Muller was invited by the [CSVN](/CSVN "CSVN") to play the [25th DOCCC](/DOCCC_2005 "DOCCC 2005"), and he rewrote Usurpator in [C](/C "C") (Usurpator V), to run on a laptop, which was 10,000 times faster and had 100,000 times as much memory as the matchbox computer. Since the program was not designed to play that fast, it was thinking much too far ahead at the expense of immediate threats.

# Matchbox

HGM's matchbox computer with a [65SC816](http://www.baltissen.org/newhtm/65sc816.htm) CPU for the purpose of running Usurpator. The matchbox competed three times at [Dutch Computer Chess Championships](/Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), [1986](/DOCCC_1986 "DOCCC 1986") [[6]](#cite_note-6) , [1987](/DOCCC_1987 "DOCCC 1987") [[7]](#cite_note-7) , and [1990](/DOCCC_1990 "DOCCC 1990"):

|  |  |
| --- | --- |
| [HGMwithMatchbox.jpg](http://tinyurl.com/h7yzxry) | [HGMmatchbox.jpg](http://home.hccnet.nl/h.g.muller/chess.html) |
| [DOCCC 1990](/DOCCC_1990 "DOCCC 1990") - Firepower for a full board [[8]](#cite_note-8) | Matchbox Design [[9]](#cite_note-9) |

# Re-Discovering Alpha-Beta

In that early times end of the 70s and early 80s when Harm Geert Muller developed his first programs, he had [Alpha-Beta](/Alpha-Beta "Alpha-Beta") initially wrong in Usurpator I, since it omitted the [deep cutoffs](/Beta-Cutoff#deep "Beta-Cutoff") and was not passing [alpha](/Alpha "Alpha") through the [recursive](/Recursion "Recursion") call. After tracing the [search tree](/Search_Tree "Search Tree") HGM got aware and found out how to do the deep cutoffs, re-discovering Alpha-Beta by himself for Usurpator II [[10]](#cite_note-10) .

# Photos & Games

[![MulArts42a.JPG](/images/c/c0/MulArts42a.JPG)](http://old.csvn.nl/gallery23.html)

[DOCCC 2005](/DOCCC_2005 "DOCCC 2005"): [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") and [Stan Arts](/Stan_Arts "Stan Arts"), Usurpator V - [Neurosis](/Neurosis "Neurosis") [[11]](#cite_note-11) [[12]](#cite_note-12)  
Usurpator V caused some thermic problems in the therefor upright standing Laptop

```
[Event "DOCCC 2005"]
[Site "Leiden NED"]
[Date "2005.11.11"]
[Round "02"]
[White "Usurpator V"]
[Black "Neurosis"]
[Result "0-1"]

1.e4 e5 2.Qh5 Nc6 3.Bc4 g6 4.Qe2 Nd4 5.Qd3 Nf6 6.c3 Nc6 7.Nf3 Bg7
8.b4 d5 9.Bxd5 Nxd5 10.exd5 Be6 11.h3 Bxd5 12.Qc2 e4 13.Ng1 Qg5
14.g4 e3 15.Rh2 Qf4 16.Rg2 Bxg2 17.dxe3 Qh2 18.Ne2 Qh1+ 19.Kd2 O-O-O+
20.Nd4 Ne5 21.Qa4 Nc4+ 22.Kc2 Be4+ 23.Kb3 Qd1+ 24.Kxc4 Bd3+
25.Kc5 Bf8# 0-1
```

# See also

- [KingSlayer](/index.php?title=KingSlayer&action=edit&redlink=1 "KingSlayer (page does not exist)")
- [Micro-Max](/Micro-Max "Micro-Max")
- [Spartacus](/Spartacus "Spartacus")

# Publications

- [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") (**1981**). *Usurpator 6502 6800 computerschaak*. Wolfkamp
- [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") (**1990**). *A Matchbox Chess Computer*. [ICCA Journal, Vol. 13, No. 4](/ICGA_Journal#13_4 "ICGA Journal"), [pdf](http://tinyurl.com/h7yzxry) hosted by [Hein Veldhuis](/Hein_Veldhuis "Hein Veldhuis")

# Forum Posts

- [UsurpatorII emu questions](http://www.talkchess.com/forum/viewtopic.php?t=64747) by [Günther Simon](/G%C3%BCnther_Simon "Günther Simon"), [CCC](/CCC "CCC"), July 28, 2017

# External Links

## Chess Program

- [HGM's Chess Pages](http://home.hccnet.nl/h.g.muller/chess.html)
- [HGM and The Matchbox Chess Computer](http://adamsccpages.blogspot.com/2012/06/hgm-and-matchbox-chess-computer.html) from [Adam's Computer Chess Pages](http://adamsccpages.blogspot.com/) by [Adam Hair](/Adam_Hair "Adam Hair"), June 1, 2012

## Misc

- [Usurper from Wikipedia](https://en.wikipedia.org/wiki/Usurper)
- [Roman usurper from Wikipedia](https://en.wikipedia.org/wiki/Roman_usurper)
- [List of usurpers from Wikipedia](https://en.wikipedia.org/wiki/List_of_usurpers)
- [List of Roman usurpers from Wikipedia](https://en.wikipedia.org/wiki/List_of_Roman_usurpers)
- [Usurper (video game) from Wikipedia](https://en.wikipedia.org/wiki/Usurper_%28game%29)

# References

1. [↑](#cite_ref-1) [HGM's Chess Pages](http://home.hccnet.nl/h.g.muller/chess.html)
2. [↑](#cite_ref-2) [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") (**1981**). *Usurpator 6502 6800 computerschaak*. Wolfkamp
3. [↑](#cite_ref-3) [Re: Atom Software Archive](http://stardot.org.uk/forums/viewtopic.php?t=6544&start=900#p124794) by Multiwizard, [stardot.org.uk](http://stardot.org.uk/forums/index.php), November 13, 2015
4. [↑](#cite_ref-4) [Acorn Nieuws 1982 nummer 4](http://www.acornatom.nl/atom_nieuws/1982/nr4/19824015.htm)
5. [↑](#cite_ref-5) [Re: Retrocomputing with the 6502](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=126155&t=14610) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/Computer_Chess_Forums "Computer Chess Forums"), June 22, 2007
6. [↑](#cite_ref-6) [Jaap van Oosterwijk Bruyn](/Jaap_van_Oosterwijk_Bruyn "Jaap van Oosterwijk Bruyn") (**1986**). *Nona retains her Title*. [ICCA Journal, Vol. 9, No. 3](/ICGA_Journal#9_3 "ICGA Journal")
7. [↑](#cite_ref-7) [Peter Kouwenhoven](/Peter_Kouwenhoven "Peter Kouwenhoven") (**1987**). *The 7th Dutch National Computer-Chess Championship*. [ICCA Journal, Vol. 10, No. 4](/ICGA_Journal#10_4 "ICGA Journal")
8. [↑](#cite_ref-8) Image by [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk"), from [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") (**1990**). *A Matchbox Chess Computer*. [ICCA Journal, Vol. 13, No. 4](/ICGA_Journal#13_4 "ICGA Journal"), [pdf](http://tinyurl.com/h7yzxry) hosted by [Hein Veldhuis](/Hein_Veldhuis "Hein Veldhuis")
9. [↑](#cite_ref-9) [HGM's Chess Pages](http://home.hccnet.nl/h.g.muller/chess.html)
10. [↑](#cite_ref-10) [Re: What the computer chess community needs to decide](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=394125&t=38007) by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), [CCC](/Computer_Chess_Forums "Computer Chess Forums"), February 11, 2011
11. [↑](#cite_ref-11) [25th Dutch Open Computer Chess Championship 2005 - Photo Gallery](http://old.csvn.nl/gallery23.html)
12. [↑](#cite_ref-12) [Downloads | Open Dutch Computer Chess Championships | Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=37&Itemid=26&lang=en&limitstart=5)

**[Up one Level](/Engines "Engines")**