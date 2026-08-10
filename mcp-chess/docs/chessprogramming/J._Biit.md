# J. Biit

Source: https://www.chessprogramming.org/J._Biit

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* J. Biit**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Everest_kalapatthar.jpg/250px-Everest_kalapatthar.jpg)](/File:Everest_kalapatthar.jpg)

Just Because it is there [[1]](#cite_note-1)

**J. Biit**,  
[Hans Berliner's](/Hans_Berliner "Hans Berliner") first chess program, written in the late 60s in [PL/I](/index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)") to ran on an [IBM System/360](/IBM_360 "IBM 360") [mainframe computer](https://en.wikipedia.org/wiki/Mainframe_computer) [[2]](#cite_note-2) . It played the [First United States Computer Chess Championship](/ACM_1970 "ACM 1970") 1970 in [New York City](https://en.wikipedia.org/wiki/New_York_City), and won versus [Wita](/Awit "Awit"), lost from [Chess 3.0](/Chess_(Program) "Chess (Program)") and drew [Coko III](/Coko "Coko").

Along with [Daly CP](/Daly_CP "Daly CP"), J. Biit was one of the first chess programs operated through a [Graphical User Interface](/GUI "GUI"). The UI was written at [Columbia University](/Columbia_University "Columbia University") for the [IBM 2250 Display Unit](https://en.wikipedia.org/wiki/IBM_2250), and later evolved along with J. Biit to become the [Columbia Computer Chess Program](/CCCP_(US) "CCCP (US)") dubbed CCCP [[3]](#cite_note-3).

# Etymology

J. Biit is the acronym of "Just Because it is there", probably in dependance of the famous quote [[4]](#cite_note-4) by English mountaineer [George Mallory](https://en.wikipedia.org/wiki/George_Mallory), having replied to the question "Why do you want to climb [Mount Everest](https://en.wikipedia.org/wiki/Mount_Everest)?".

# Description

J. Biit was a selective search ([Shannon type B](/Type_B_Strategy "Type B Strategy")) program [[5]](#cite_note-5) that places considerable emphasis on chess knowledge and restricting the number of positions to be examined, as it scored only 30-100 positions during a search using [alpha-beta](/Alpha-Beta "Alpha-Beta") and [incremental board updating](/Incremental_Updates "Incremental Updates"). The program was developed in [PL/I](https://en.wikipedia.org/wiki/PL/I) on the [IBM 360/65](/IBM_360 "IBM 360") at [CMU](/Carnegie_Mellon_University "Carnegie Mellon University"), but was unable to use that system for the [1970 ACM tournament](/ACM_1970 "ACM 1970"). Since the 360 line was supposedly compatable, Kenneth M. King [[6]](#cite_note-6) offered the services of [Columbia's](/Columbia_University "Columbia University") more powerful IBM 360/91. Unfortunately they discovered that it wasn't as compatable as expected and Berliner and assistants spent two rather frantic weeks making program changes. It used about 200 [Kibibyte](https://en.wikipedia.org/wiki/Kibibyte) of [memory](/Memory "Memory") and was about 3500 PL/I statements. The program searches a very small tree. Berliner claimed that, on average, only 30 nodes were examined for a move that required 65 seconds of computation. It used a "[free form of search which terminated in quiescent positions](/Quiescence_Search "Quiescence Search") ... (with) the only bound being the absolute depth limit of 14 ply." It searched two plies for begining and [middle games](/Middlegame "Middlegame"), and 4 plies for [end games](/Endgame "Endgame") .

# Quotes

[Hans Berliner](/Hans_Berliner "Hans Berliner") in his Oral History, March 2005 [[7]](#cite_note-7) :

```
And I wrote a program which actually played chess. And I did it in the way Greenblatt said it ought to be done [8]. It wasn’t anywhere’s near as good a Greenblatt’s program and I wasn’t really a very good programmer obviously, since that was the first time I had written a program...
```

```
So it played. Let’s see, I’ve got to get the timeline right here. Now this was in 1970. Now in 1970 I had already left IBM. I left IBM in 1969, and went to Carnegie Mellon as a doctoral student.
```

```
And, of course, their attraction with Newell and Simon was they would like to find somebody to push their ideas further forward, and that was me. And so I had this program which, in retrospect, was pretty woesome.
```

# Publications

- [Hans Berliner](/Hans_Berliner "Hans Berliner") (**1970**). *Experiences Gained in Constructing and Testing a Chess Program*. [IEEE](/IEEE "IEEE") Symposium System Science and Cybernetics, reprinted in [David Levy](/David_Levy "David Levy") (ed.) (**1988**). *[Computer Games I](https://link.springer.com/book/10.1007/978-1-4613-8716-9)*.

# External Links

## Chess Program

- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](/Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) [[9]](#cite_note-9)

## Misc

- [Michael Hedges](/Category:Michael_Hedges "Category:Michael Hedges") - Because It's There [[10]](#cite_note-10), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   July 1986 at the [Wolf Trap National Park for the Performing Arts](https://en.wikipedia.org/wiki/Wolf_Trap_National_Park_for_the_Performing_Arts) in [Vienna, Virginia](https://en.wikipedia.org/wiki/Vienna,_Virginia)

# References

1. [↑](#cite_ref-1) Everest from [Kala Patthar](https://en.wikipedia.org/wiki/Kala_Patthar) in [Nepal](https://en.wikipedia.org/wiki/Nepal), [Mount Everest from Wikipedia](https://en.wikipedia.org/wiki/Mount_Everest)
2. [↑](#cite_ref-2) [George Atkinson](/index.php?title=George_Atkinson&action=edit&redlink=1 "George Atkinson (page does not exist)") (**1998**). *[Chess and Machine Intuition](http://books.google.com/books?id=ZuTvVo4zo6oC&printsec=frontcover&dq=Chess+and+machine+intuition#v=onepage&q&f=false)*. (Intellect Ltd.) pp 61
3. [↑](#cite_ref-3) [Recollections of CUCC 1968-70 -The CCCP Chess Program](http://www.columbia.edu/cu/computinghistory/elliott-frank.html#cccp)
4. [↑](#cite_ref-4) [George Mallory - Because it is there - Wikiquote](http://en.wikiquote.org/wiki/George_Mallory)
5. [↑](#cite_ref-5) Description based on [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](/Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)
6. [↑](#cite_ref-6) [The IBM 7090](http://www.columbia.edu/cu/computinghistory/7090.html)
7. [↑](#cite_ref-7) [Oral History of Hans Berliner](http://www.computerhistory.org/chess/related_materials/oral-history/hans_berliner.oral_history.2005.102630824/index.php?iid=orl-43343bb768f00), Interviewed by: [Gardner Hendrie](http://www.computerhistory.org/trustee/gardner-hendrie), Recorded: March 7, 2005, [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/oral-history/hans_berliner.oral_history.2005.102630824/berliner.oral_history_transcript.2005.103630824.pdf), pp. 12-13
8. [↑](#cite_ref-8) [Richard Greenblatt](/Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](/Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](/Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31
9. [↑](#cite_ref-9) [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), July 11, 2015
10. [↑](#cite_ref-10) [Naomi Uemura from Wikipedia](https://en.wikipedia.org/wiki/Naomi_Uemura)

**[Up one Level](/Engines "Engines")**