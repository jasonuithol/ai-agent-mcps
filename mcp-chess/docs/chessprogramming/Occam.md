# Occam

Source: https://www.chessprogramming.org/Occam

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Occam**

**Occam**,  
a private chess program and later also [Arimaa](/Arimaa "Arimaa") bot by [Don Dailey](/Don_Dailey "Don Dailey") [[1]](#cite_note-1) and [Larry Kaufman](/Larry_Kaufman "Larry Kaufman") [[2]](#cite_note-2), which evolved from [Cilkchess](/Cilkchess "Cilkchess") as experimental development version of Don and Larry's later commercial programs. In it's early state, short after the [WCCC 1999](/WCCC_1999 "WCCC 1999"), Don explicitly mentioned the [Copy-Make](/Copy-Make "Copy-Make") approach in Occam [[3]](#cite_note-3) which he later also preferred in [Doch](/Doch#Copy "Doch") [[4]](#cite_note-4) and presumably in [Komodo](/Komodo "Komodo").

# Position

Don gave following [board representation](/Board_Representation "Board Representation") and [position](/Chess_Position "Chess Position") structure [[5]](#cite_note-5):

```
typedef struct ptag
{
  SQUARES       bd[65];          /* the board                        */
  base_int      king_loc[2];     /* location of kings                */
  u64           hashkey;         /* position key for hash table      */
  int32         mat_sig;         /* signature of material situation  */
  struct ptag   *his[2];         /* pointer to last 2 positions      */
  ev_type       inc_score;       /* incremental component of score   */
  base_int      ply_of_game;     /* even = white to move             */
  base_int      ply_of_search;   /* start at 0                       */
  base_int      pv[PV_LEN];      /* best move from position          */
  base_int      last_move;       /* move that got us here            */
  base_int      null_count;      /* how many recursive null moves?   */
  base_int      in_check;        /* is ctm king in check?            */
} position;
```

# Quotes

## MTD

Reply by [Don Dailey](/Don_Dailey "Don Dailey") to [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), July 20, 1999 [[6]](#cite_note-6):

```
I have a primitive program  called "Occam" playing on the chess server now. I don't have any kind  of aspiration search in it, just pure alpha/beta, no PVS, no MTD or anything. I will implement PVS first so that I  can do comparisions.
```

## Arimaa Bot

Occam was further test-bed for an [Arimaa](/Arimaa "Arimaa") bot which played the first computer-computer challenge in 2004 [[7]](#cite_note-7). Quote by [Omar Syed](/Omar_Syed "Omar Syed") [[8]](#cite_note-8):

```
Soon after the challenge was announced, several members of the game AI-research community attempted to tackle the challenge. The late Don Dailey (developer of the Komodo chess engine) was the first to create an Arimaa engine. Within a couple months Don had a surprisingly strong program offering games in the Arimaa gameroom. In designing Arimaa, I had used the Zillions-of-Games general game-playing engine, which allows specifying the rules of the game in a Lisp like language, and then immediately being able to play the game against the Zillions engine. Using only look ahead and no game-specific knowledge, this engine was able to play at a strong level in most games one could dream of. However, it was incredibly lousy at Arimaa due to the high branching factor. This helped build my confidence that Arimaa would be a difficult game for computers if only a brute-force search was used. However, Don’s program, called OCCAM, surprised me in how well it played when the search engine was much faster and included some game knowledge. When Don realized that there was very little expert knowledge available for Arimaa, he felt that he could not make much progress on his program and went back to developing his chess engine which now has gone on to become the highest rated in the world.
```

# See also

- [Arimaa](/Arimaa "Arimaa")
- [Cilkchess](/Cilkchess "Cilkchess")
- [Doch](/Doch "Doch")
- [Komodo](/Komodo "Komodo")
- [Razoring](/Razoring "Razoring")

# Forum Posts

- [MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61058) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 19, 1999

:   [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61151) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 20, 1999
:   [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61157) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 20, 1999
:   [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61218) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 20, 1999
:   [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61243) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 21, 1999

# External Links

## Chess Engine

- [Finger Occam](http://www6.chessclub.com/finger/occam) at [Internet Chess Club](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")

## Misc

- [William of Ockham from Wikipedia](https://en.wikipedia.org/wiki/William_of_Ockham)
- [Occam's razor from Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)
- [occam (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Occam_%28programming_language%29)

# References

1. [↑](#cite_ref-1) [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61157) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 20, 1999
2. [↑](#cite_ref-2) [Finger Occam](http://www6.chessclub.com/finger/occam) at [Internet Chess Club](/index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")
3. [↑](#cite_ref-3) [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61218) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 20, 1999
4. [↑](#cite_ref-4) [Re: undo move vs. Position Cloning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=291570&t=29770) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), September 16, 2009
5. [↑](#cite_ref-5) [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61243) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 21, 1999
6. [↑](#cite_ref-6) [Re: MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61151) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), July 20, 1999
7. [↑](#cite_ref-7) [Arimaa Challenge 2004](http://arimaa.com/arimaa/challenge/2004/icgaNews2.html)
8. [↑](#cite_ref-8) [Omar Syed](/Omar_Syed "Omar Syed") (**2015**). *The Arimaa Challenge: From Inception to Completion*. [ICGA Journal, Vol. 38, No. 1](/ICGA_Journal#38_1 "ICGA Journal")

**[Up one Level](/Engines "Engines")**