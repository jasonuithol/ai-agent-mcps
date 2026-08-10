# Atlas

Source: https://www.chessprogramming.org/Atlas

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Atlas**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Singer_Sargent%2C_John_-_Atlas_and_the_Hesperides_-_1925.jpg/330px-Singer_Sargent%2C_John_-_Atlas_and_the_Hesperides_-_1925.jpg)](/File:Singer_Sargent,_John_-_Atlas_and_the_Hesperides_-_1925.jpg)

[Atlas](https://en.wikipedia.org/wiki/Atlas_%28mythology%29) and the [Hesperides](https://en.wikipedia.org/wiki/Hesperides) [[1]](#cite_note-1)

**Atlas**,  
an early chess program written in 1967 by [Alex Bell](/Alex_Bell "Alex Bell") at [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory"), [Chilton](https://en.wikipedia.org/wiki/Chilton,_Oxfordshire). It was basically a resurrected, cleaned up [Algol](/Algol "Algol") version of Bell's and [Barricelli's](/Nils_Barricelli "Nils Barricelli") old program from the early 60s to test evolutionary theories, which had an [evaluation function](/Evaluation_Function "Evaluation Function") based purely on [mobility](/Mobility "Mobility") - at that time the first fully legal chess program to run in England [[2]](#cite_note-2), and likely also the base of Barricelli's [WCCC 1974](/WCCC_1974 "WCCC 1974") entry [Freedom](/Freedom "Freedom").

Atlas, running on an [ICL](https://en.wikipedia.org/wiki/International_Computers_Limited) [Atlas](https://en.wikipedia.org/wiki/Atlas_%28computer%29) computer [[3]](#cite_note-3), looked three [plies](/Ply "Ply") ahead with [alpha-beta](/Alpha-Beta "Alpha-Beta"), and would accept almost any [captures](/Captures "Captures") in that [depth](/Depth "Depth") with weighting on swaps of the more powerful pieces, i.e. it would always swap a queen for a queen. If no captures were present it prepared to [castle](/Castling "Castling") or [mini-maximised](/Minimax "Minimax") its mobility. A slight modification prevented it from moving its queen in the first 5 moves [[4]](#cite_note-4). Atlas played a few sparring games against [Lancaster](/Lancaster "Lancaster") [[5]](#cite_note-5), [John Scott's](/John_J._Scott "John J. Scott") program, then dubbed "Scott" [[6]](#cite_note-6), and largely suffered from [horizon effect](/Horizon_Effect "Horizon Effect").

# Move Generation

A description of Atlas' [move generation](/Move_Generation "Move Generation") techniques along with a mate-in-two solver is given with Algol source code listing in *Games Playing with Computers*, 3.1 Chess [[7]](#cite_note-7). Atlas uses two distinct [8x8 boards](/8x8_Board "8x8 Board") [1:65] and [piece lists](/Piece-Lists "Piece-Lists") [O:16] for white and black man with identical [piece coding](/Pieces#PieceCoding "Pieces"), passing the boards per reference as 'mymanin' or 'opponents' dependent on [side to move](/Side_to_move "Side to move"). Pre-calculated rook and bishop tables contain one vector of [direction](/Direction "Direction") increments, i.e. east (+1), west (-1), north (+8), and south (-8) for rooks, and further for each square a vector of ray-direction terminal [destination squares](/Target_Square "Target Square"). The embedded routine 'rookorbishopmove' in scope of the outer move generation routine loops over all four directions, gets increment and terminal target square from the rook or bishop table, and iterates the destination along the ray. Inside the ray-loop it tests whether the target is occupied by an own man, to terminate the ray-loop, otherwise it stores the move, and then tests to break after a capture or even an illegal king capture with an extra exit 'cutoff'.

```
procedure rookorbishopmove(rookorbishop);
  integer array rookorbishop;
  begin 
    for j := 0 step 1 until 3 do
    begin 
      k := rookorbishop[j]; k is increment:
      l := rookorbishop[4 * square + j]; l is terminal square
      for i := square + k step k until l do 
      begin 
        if mymanin[i] ≠ 0 then goto newdirection;
        c := c+1;
        moves[c] := i;
        if opponents[i] ≠ 0 then 
        begin
          if opponents[i] = 6 then goto cutoff else goto newdirection
        end
      end;
newdirection:
    end
  end of rookorbishopmove;
```

# Master

In the early 70s, Atlas evolved to [Master](/Master "Master") in collaboration with [Peter Kent](/Peter_Kent "Peter Kent"), and later with [John Birmingham](/John_Birmingham "John Birmingham") and chess expert [John Waldron](/John_Waldron "John Waldron"), while Alex Bell finally left Chilton.

# Namesake

- [Atlas](/Atlas_(ESP) "Atlas (ESP)") by [Andrés Manzanares Campillo](/Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo")

# See also

- [Master](/Master "Master")

# Publications

- [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), [index](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/index.htm)
- [Alex Bell](/Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess?* [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press), [amazon](http://www.amazon.com/Machine-Plays-Chess-Pergamon/dp/0080212220)

# External Links

## Chess Program

- [Games Playing with Computers | Chapter 3: Board Games](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm), in [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin)
- [MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm). Excerpt from [Alex Bell](/Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess?*. [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press), hosted by [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") from [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)

## Misc

- [Atlas (computer) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28computer%29)
- [Atlas (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28disambiguation%29)
- [Atlas from Wikipedia](https://en.wikipedia.org/wiki/Atlas)
- [Atlas Mountains from Wikipedia](https://en.wikipedia.org/wiki/Atlas_Mountains)
- [Atlas (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28mythology%29)

:   [Calypso (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Calypso_%28mythology%29)

- [Farnese Atlas from Wikipedia](https://en.wikipedia.org/wiki/Farnese_Atlas)
- [Atlas (rocket family) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28rocket_family%29)
- [Atlas (star) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28star%29)
- [Atlas (moon) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28moon%29)
- [Colossochelys atlas from Wikipedia](https://en.wikipedia.org/wiki/Colossochelys_atlas)
- [Youn Sun Nah](/Category:Youn_Sun_Nah "Category:Youn Sun Nah") & [Ulf Wakenius](/Category:Ulf_Wakenius "Category:Ulf Wakenius") - Calypso Blues @ [Jazz sous les pommiers](https://fr.wikipedia.org/wiki/Jazz_sous_les_pommiers), May 28, 2011, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Atlas and the Hesperides](https://commons.wikimedia.org/wiki/File:Singer_Sargent,_John_-_Atlas_and_the_Hesperides_-_1925.jpg) by [John Singer Sargent](/index.php?title=Category:John_Singer_Sargent&action=edit&redlink=1 "Category:John Singer Sargent (page does not exist)"), between circa 1922 and circa 1925, current location: [Museum of Fine Arts, Boston](https://en.wikipedia.org/wiki/Museum_of_Fine_Arts,_Boston), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm). Excerpt from [Alex Bell](/Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess?*. [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press), hosted by [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") from [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
3. [↑](#cite_ref-3) [Atlas Computer Laboratory](http://www.chilton-computing.org.uk/acl/literature/acl/p004.htm), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
4. [↑](#cite_ref-4) [MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm). Excerpt from [Alex Bell](/Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess?*. [Pergamon Press](https://en.wikipedia.org/wiki/Pergamon_Press), hosted by [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory") from [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory)
5. [↑](#cite_ref-5) [John J. Scott](/John_J._Scott "John J. Scott") (**1969**). *Lancaster vs. Mac Hack*. [ACM SIGART Bulletin](/ACM#SIG "ACM"), Vol. 16
6. [↑](#cite_ref-6) [Chess programs: Scott](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p005.htm#index22) from [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin)
7. [↑](#cite_ref-7) [Games Playing with Computers | Chapter 3: Board Games](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm), in [Alex Bell](/Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin)

**[Up one Level](/Engines "Engines")**