# Doch

Source: https://www.chessprogramming.org/Doch

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Doch**

**Doch**,  
an [UCI](/UCI "UCI") compliant chess engine by primary author [Don Dailey](/Don_Dailey "Don Dailey"), supported by chess advisor and evaluation expert and Don's long time collaborator [Larry Kaufman](/Larry_Kaufman "Larry Kaufman").
The development started in 2007 [[1]](#cite_note-1), and it was first released to the public as free engine in fall 2009 [[2]](#cite_note-2).

# Komodo

In January 2010, Doch evolved to [Komodo](/Komodo "Komodo") [[3]](#cite_note-3) to become one of the strongest programs ever.

# Etymology

Doch is [acronym](/Category:Acronym "Category:Acronym") of Don's Chess. Quote from a [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky") interview, December 2009 [[4]](#cite_note-4):

```
Doch was never intended to be the name that would stick. When I first decided to write this program I needed a name and did not want to spend days obsessing over it. I did not want to call it "chess" but it needed a name to give it some personality. Doch stands for DOn's CHess. I never got around to giving it a proper name and I feel a bit immodest calling it after my own name!
```

# Copy-Make

Doch was a 64-bit aka [bitboard](/Bitboards "Bitboards") program, applying a [Copy-Make](/Copy-Make "Copy-Make") approach with a [position](/Chess_Position "Chess Position") state of 192 byte allocated on the [stack](/Stack "Stack") [[5]](#cite_note-5) [[6]](#cite_note-6)

```
position search( position_state *prev,  ...  )
{
   position_state  new_position;
   ... other stuff
   foreach move in movelist do {
       make( prev, &new_position, move );
   }
}
```

# See also

- [Komodo](/Komodo "Komodo")
- [Occam](/Occam "Occam")

# Forum Posts

- [Doch 09.980 (uci) by Don Dailey available](http://www.talkchess.com/forum/viewtopic.php?t=30598) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [CCC](/CCC "CCC"), November 13, 2009
- [Doch (64-bit Version)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=30830) by [Ted Summers](/Ted_Summers "Ted Summers"), [CCC](/CCC "CCC"), November 28, 2009
- [Doch 1.2 update (uci) by Don Dailey available](http://www.talkchess.com/forum/viewtopic.php?t=31082) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [CCC](/CCC "CCC"), December 15, 2009
- [Doch 1.3.1](http://www.talkchess.com/forum/viewtopic.php?t=31493) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), January 05, 2010
- [A New Name for Doch....](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316228&t=31534) by [Fernando Villegas](/Fernando_Villegas "Fernando Villegas"), [CCC](/CCC "CCC"), January 07, 2010

# External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/DOCH](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/DOCH/) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](/Kirill_Kryukov "Kirill Kryukov")
- [Computerschach, Interview with Don Dailey](http://www.schach-welt.de/schach/computerschach/interviews/don-dailey) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Schachwelt.de](http://www.schach-welt.de/), December 18-20, 2009

## Misc

- [doch - Wiktionary](http://en.wiktionary.org/wiki/doch)

# References

1. [↑](#cite_ref-1) [About Komodo](https://komodochess.com/store/pages.php?cmsid=13) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman")
2. [↑](#cite_ref-2) [Doch 09.980 (uci) by Don Dailey available](http://www.talkchess.com/forum/viewtopic.php?t=30598) by [Jim Ablett](/Jim_Ablett "Jim Ablett"), [CCC](/CCC "CCC"), November 13, 2009
3. [↑](#cite_ref-3) [Komodo credit](http://www.talkchess.com/forum/viewtopic.php?t=31920) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), January 22, 2010
4. [↑](#cite_ref-4) [Computerschach, Interview with Don Dailey](http://www.schach-welt.de/schach/computerschach/interviews/don-dailey) by [Frank Quisinsky](/Frank_Quisinsky "Frank Quisinsky"), [Schachwelt.de](http://www.schach-welt.de/), December 18-20, 2009
5. [↑](#cite_ref-5) [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291570&t=29770) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), September 16, 2009
6. [↑](#cite_ref-6) [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291586&t=29770) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), September 16, 2009

**[Up one Level](/Engines "Engines")**