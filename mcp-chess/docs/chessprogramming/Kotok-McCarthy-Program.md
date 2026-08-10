# Kotok-McCarthy-Program

Source: https://www.chessprogramming.org/Kotok-McCarthy-Program

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Kotok-McCarthy-Program**

[![](/images/thumb/4/44/JohnMcCarthy.jpg/300px-JohnMcCarthy.jpg)](/File:JohnMcCarthy.jpg)

[John McCarthy](/John_McCarthy "John McCarthy") operating Kotok-McCarthy [[1]](#cite_note-1) [[2]](#cite_note-2)

The **Kotok-McCarthy-Program**,   
also known as "A Chess Playing Program for the [IBM 7090](/IBM_7090 "IBM 7090") Computer" was the first computer program to play chess convincingly. Between 1959 and [1962](/Timeline#1962 "Timeline"), while student of [John McCarthy](/John_McCarthy "John McCarthy") at the [Massachusetts Institute of Technology](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [Alan Kotok](/Alan_Kotok "Alan Kotok") and his fellows [Elwyn Berlekamp](/Elwyn_Berlekamp "Elwyn Berlekamp"), [Michael A. Lieberman](/Michael_A._Lieberman "Michael A. Lieberman"), [Charles Niessen](/Charles_Niessen "Charles Niessen") and [Robert A. Wagner](/Robert_A._Wagner "Robert A. Wagner") wrote a chess program for the IBM 7090. Based on [Alex Bernstein's 1957 program](/The_Bernstein_Chess_Program "The Bernstein Chess Program") and routines by [McCarthy](/John_McCarthy "John McCarthy") and [Paul W. Abrahams](/Paul_W._Abrahams "Paul W. Abrahams"), they added [alpha-beta pruning](/Alpha-Beta "Alpha-Beta") to [minmax](/Minimax "Minimax"), at McCarthy's suggestion. The Kotok-McCarthy-Program was written in [Fortran](/Fortran "Fortran") and [FAP](https://en.wikipedia.org/wiki/IBM_704/9/90_FORTRAN_Assembly_Program#FORTRAN_Assembly_Program), the IBM 7090 macro assembler.

# Type B

Kotok-McCarthy was a selective [Shannon Type B](/Type_B_Strategy "Type B Strategy") kind of program. It considered only a few plausible moves as function of increasing [ply](/Ply "Ply")

{4, 3, 2, 2, 1, 1, 1, 1, 0, 0}

and therefor had some tactical flaws. [Quote](/Template:Quote_Greenblatt_on_Kotok-McCarthy "Template:Quote Greenblatt on Kotok-McCarthy") by [Richard Greenblatt](/Richard_Greenblatt "Richard Greenblatt") concerning [Mac Hack VI](/Mac_Hack "Mac Hack") from his *Oral History* [[3]](#cite_note-3):

Most of this printout was analysis from the Kotok program. And I also saw some kind of a textual thing, which I don’t believe was [Kotok’s](/Alan_Kotok "Alan Kotok") thesis, but which had some of the same information as Kotok’s thesis. It was probably some kind of a technical report, or something, that was anticipatory to Kotok’s thesis [[4]](#cite_note-4). Anyway, one of the things I remembered, and which I just talked with Kotok, as a matter of fact, a few days ago, was the detail that they had is [Alpha Beta](/Alpha-Beta "Alpha-Beta"), and so forth, and they had these whips, and the whips were set at 4, 4, 3, 3, 2, 2, 1, 1. In other words, that was how many. It would first look at the top ply. It would look at the four best moves. The next plys, it would look at the three best. Next ply, two best, next ply, one best. Well, I just recognized immediately that that was incredibly wrong.

You see, basically looking at only one wide, you just have no signals or noise function. In other words, you look at one move, which you think is the best, but there’s a tremendous amount of noise. Well, you look at some more moves, and if you find that one of those are better, you’ve effectively rejected some noise. Well, essentially the thing that I knew that they did, they were very weak chess players, both [McCarthy](/John_McCarthy "John McCarthy") and Kotok. And basically they had a very romanticized view of chess. And so I knew, however, that chess is a very, very precise game. And you really- the name of the game is take the other guy’s pieces, and you don’t just go along. In any kind of a strong game, you don’t just lose pieces, win pieces, lose pieces, win pieces. I mean, if you lose even a single pawn without compensation, then you may have drawing chances, if you’re lucky. Otherwise, the game is lost. Losing more than one pawn almost invariably results in loss of the game, period.

# Stanford-ITEP Match

*see main article [Stanford-ITEP Match](/Stanford-ITEP_Match "Stanford-ITEP Match")*

After graduated from [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), Kotok lost interest in computer chess but his program remained alive. When McCarthy left MIT to take charge of the Artificial Intelligence Laboratory at [Stanford](/Stanford_University "Stanford University"), he took Kotok's program with him and improved it's searching. At the end of 1966 a [four game match](/Stanford-ITEP_Match "Stanford-ITEP Match") began between the Kotok-McCarthy program, running on a [IBM 7090](/IBM_7090 "IBM 7090") computer, and a program developed at the [Institute of Theoretical and Experimental Physics](/Institute_of_Theoretical_and_Experimental_Physics "Institute of Theoretical and Experimental Physics") (ITEP) in Moscow which used a Soviet [M-20](/M-20 "M-20") computer. The match played over nine months was won 3-1 by the The ITEP program, despite playing on slower hardware.

# Quotes

[Quote](/Template:Quote_Alan_Kotok "Template:Quote Alan Kotok") from [Alan Kotok's Oral History](/Alan_Kotok#Oral_History "Alan Kotok") concering the development of a chess program under [John McCarthy](/John_McCarthy "John McCarthy") at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"):

```
So there were a total of five people. There was the initial four were, besides me, Charles Niessen, Chuck Niessen, whose these days is some sort of director over at Lincoln Lab. And Mike Lieberman, who is on the faculty at Berkeley. And Elwyn Berlekamp, who is also Berkeley faculty, and fairly famous computer game theory person. Elwyn dropped out of this project at some point, and Bob Wagner, another so these were all sort of East Campus Model Railroad Club friends - and Bob Wagner is at, I think, University of North Carolina - what’s in Raleigh-Durham?
```

# See also

- [The Bernstein Chess Program](/The_Bernstein_Chess_Program "The Bernstein Chess Program")
- [History of Computer Chess](/History "History")
- [Stanford-ITEP Match](/Stanford-ITEP_Match "Stanford-ITEP Match")
- [Type B Search in Mac Hack VI](/Mac_Hack#TypeB "Mac Hack")

# Publications

- [Alan Kotok](/Alan_Kotok "Alan Kotok") (**1962**). *[Artificial Intelligence Project - MIT Computation Center: Memo 41 - A Chess Playing Program](http://www.kotok.org/AI_Memo_41.html)*. [pdf](ftp://publications.ai.mit.edu/ai-publications/pdf/AIM-041.pdf)
- [Alan Kotok](/Alan_Kotok "Alan Kotok") (**1962**). *A Chess Playing Program for the IBM 7090*. B.S. Thesis, [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), AI Project Memo 41, Computation Center, Cambridge MA. [pdf](http://www.kotok.org/AK-Thesis-1962.pdf)
- [Michael Brudno](http://www.cs.toronto.edu/~brudno/) (**2000**). *Competitions, Controversies, and Computer Chess*, [pdf](http://www.cs.toronto.edu/%7Ebrudno/essays/cchess.pdf)

# External Links

- [Kotok-McCarthy-Program from Wikipedia](https://en.wikipedia.org/wiki/Kotok-McCarthy)
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](/Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) [[5]](#cite_note-5)
- [Opening Moves: Origins of Computer Chess](http://www.computerhistory.org/chess/main.php?sec=thm-42b86c2029762&sel=thm-42b86c7bdbaf1) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")

# References

1. [↑](#cite_ref-1) [John McCarthy, artificial intelligence pioneer, playing chess at Stanford's IBM 7090](http://www.computerhistory.org/chess/stl-431e1a07ca980/) | [Mastering the Game](http://www.computerhistory.org/chess/) | [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum") 1967 ca., Courtesy [Stanford University](/Stanford_University "Stanford University"), [John McCarthy](/John_McCarthy "John McCarthy") used an improved version of the Kotok program to play correspondence chess against a [Soviet program](/ITEP_Chess_Program "ITEP Chess Program") developed at the Moscow [Institute of Theoretical and Experimental Physics](/Institute_of_Theoretical_and_Experimental_Physics "Institute of Theoretical and Experimental Physics") (ITEP) by [George Adelson-Velsky](/Georgy_Adelson-Velsky "Georgy Adelson-Velsky") and others. In 1967, a [four-game match](/Stanford-ITEP_Match "Stanford-ITEP Match") played over nine months was won 3-1 by the Soviet program.
2. [↑](#cite_ref-2) [CSD founding faculty](http://infolab.stanford.edu/pub/voy/museum/pictures/display/1-1.htm) from [Computer History Exhibits Photo Tour](http://infolab.stanford.edu/pub/voy/museum/phototour.html) created January 2000 by [Gio Wiederhold](http://infolab.stanford.edu/~gio/)
3. [↑](#cite_ref-3) [Oral History of Richard Greenblatt](http://archive.computerhistory.org/resources/text/Oral_History/Greenblatt_Richard/greenblatt.oral_history_transcript.2005.102657935.pdf) (pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
4. [↑](#cite_ref-4) [Alan Kotok](/Alan_Kotok "Alan Kotok") (**1962**). *[Artificial Intelligence Project - MIT Computation Center: Memo 41 - A Chess Playing Program](http://www.kotok.org/AI_Memo_41.html)*. [pdf](ftp://publications.ai.mit.edu/ai-publications/pdf/AIM-041.pdf)
5. [↑](#cite_ref-5) [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), July 11, 2015

**[Up one Level](/Engines "Engines")**