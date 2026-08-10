# N.N.

Source: https://www.chessprogramming.org/N.N.

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* N.N.**

|  |  |
| --- | --- |
| **N.N.**, an experimental chess system to select reasonable moves in quiet [middlegame](/Middlegame "Middlegame") positions, developed by [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe") and [Kai von Luck](/Kai_von_Luck "Kai von Luck") at [University of Hamburg](/University_of_Hamburg "University of Hamburg"), written in [LISP](/index.php?title=LISP&action=edit&redlink=1 "LISP (page does not exist)") as subject of their Ph.D. theses [[1]](#cite_note-1), further introduced 1984 at the [Advances in Computer Chess 4](/Advances_in_Computer_Chess_4 "Advances in Computer Chess 4") conference [[2]](#cite_note-2). N.N. is based on hierarchically structured [chess knowledge](/Knowledge "Knowledge"), conceptional divided into three main components, the [knowledge bases](https://en.wikipedia.org/wiki/Knowledge_base), the [planning system](/Planning "Planning"), and various dynamic data structures. The knowledge bases represent positional knowledge and associate classes of [pawn structure](/Pawn_Structure "Pawn Structure") with plans and actions. The planning system directs the evaluation of plans. Each plan is associated with some specific formation and has to be verified dynamically in a concept tree in order to overcome problems resulting from erroneous assumptions about the character of the position. At the conference, two distinct areas of planning were demonstrated, [minority attack](/Minority_Attack "Minority Attack") and the elementary endgame [KPK](/KPK "KPK") [[3]](#cite_note-3). Three typical areas of possible errors were mentioned - each with its own cause and each with a different level of solvability [[4]](#cite_note-4), errors in a particular knowledge base, errors from design decisions, typically about the interaction of distinct instances in the concept tree, and errors in the semantic of planning. | N.N. |

# Dynamic Behavior

A sketch of N.N.'s dynamic behavior, considerably simplified [[5]](#cite_note-5):

```
  Knowledge Bases           Processes           Knowledge Bases
 ┌────────────────┐     ╓────────────────╖     ┌────────────────┐
 │  Prototype     │     ║  Net           ║     │ Discrimination │
 │  Frames        │  ┌─►║  Interpreter   ║◄────│ Net            │
 └────────────────┘  │  ╙────────────────╜     └────────────────┘
     model           │      classes of           classification
     knowledge       │       a given             knowledge
         .           │      position
         .           │          ║
         ▼           │          ▼
 ┌────────────────┐  │  ╓────────────────╖     ┌────────────────┐
 │  Instance      │──┘  ║  Task          ║◄────│ Action         │
 │  Frames        │◄─┐  ║  Scheduler     ║  ┌──│ Scripts        │
 └────────────────┘  │  ╙────────────────╜  │  └────────────────┘
     position        │     trigger of       │     plan
     knowledge       │     appropriate      │     knowledge
                     │     scripts          │
                     │          ║           │
                     │          ▼           │
                     │  ╓────────────────╖  │  ┌────────────────┐
                     └─►║  Task          ║◄─┘  │ Concept        │
                        ║  Scheduler     ║────►│ Tree           │
                        ╙────────────────╜     └────────────────┘
                          concretization          concrete plan
                          of scripts
```

:   ──► [information flow](https://en.wikipedia.org/wiki/Information_flow_(information_theory))
:   ══► [control flow](https://en.wikipedia.org/wiki/Control_flow)
:   ··► [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))

# Etymology

"N. N." is commonly used in the [notation](/Game_Notation "Game Notation") of [chess games](/Chess_Game "Chess Game") [[6]](#cite_note-6), not only when one participant's name is genuinely unknown but when an untitled player faces a master, as in a [simultaneous exhibition](https://en.wikipedia.org/wiki/Simultaneous_exhibition). Another reason is to protect a known player from the insult of a painful defeat [[7]](#cite_note-7) .

# See also

- [Planning](/Planning "Planning")

# Publications

- [Kai von Luck](/Kai_von_Luck "Kai von Luck"), [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe") (**1981**). *[Structures for Knowledge-Based Chess Programs](https://link.springer.com/chapter/10.1007/978-3-662-02328-0_27)*. in [Siekmann](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/s/Siekmann:J=ouml=rg_H=.html) (Ed.), Proc. of [GWAI-81](http://www.informatik.uni-trier.de/%7Eley/db/conf/ki/gwai1981.html)
- [Kai von Luck](/Kai_von_Luck "Kai von Luck"), [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe") (**1982**). *[N.N.: A View of Planning in Chess](https://link.springer.com/chapter/10.1007%2F978-3-642-68826-3_8)*. in [Wahlster](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/w/Wahlster:Wolfgang.html) (Ed.), Proc. of [GWAI-82](http://www.informatik.uni-trier.de/%7Eley/db/conf/ki/gwai1982.html)
- [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe") (**1985**). *Repräsentation von positionellem Schachwissen mit Techniken der künstlichen Intelligenz*. Ph.D. thesis, [University of Hamburg](/University_of_Hamburg "University of Hamburg") (German)
- [Kai von Luck](/Kai_von_Luck "Kai von Luck") (**1985**). *Aspekte wissensgestützter Planung*. Ph.D. thesis, [University of Hamburg](/University_of_Hamburg "University of Hamburg") (German)
- [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe"), [Kai von Luck](/Kai_von_Luck "Kai von Luck") (**1986**). *N.N.: A Case Study in Chess Knowledge Representation*. [Advances in Computer Chess 4](/Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")

# External Links

- [Nomen nescio from Wikipedia](https://en.wikipedia.org/wiki/Nomen_nescio)
- [nomen nescio - Wiktionary](https://en.wiktionary.org/wiki/nomen_nescio)
- [No Name from Wikipedia](https://en.wikipedia.org/wiki/No_Name)
- [America](/Category:America "Category:America") - [A Horse with No Name](https://en.wikipedia.org/wiki/A_Horse_with_No_Name) (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Alexander Reinefeld](/Alexander_Reinefeld "Alexander Reinefeld") (**1985**). [Kai von Luck](/Kai_von_Luck "Kai von Luck"): *Aspekte wissensgestützter Planung*. [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe"): *Repräsentation von positionellem Schachwissen mit Techniken der künstlichen Intelligenz*. [ICCA Journal, Vol. 8, No. 4](/ICGA_Journal#8_4 "ICGA Journal")
2. [↑](#cite_ref-2) [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe"), [Kai von Luck](/Kai_von_Luck "Kai von Luck") (**1986**). *N.N.: A Case Study in Chess Knowledge Representation*. [Advances in Computer Chess 4](/Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
3. [↑](#cite_ref-3) [Jaap van Oosterwijk Bruyn](/Jaap_van_Oosterwijk_Bruyn "Jaap van Oosterwijk Bruyn") (**1984**). *The Fourth Conference on Advances in Computer Chess*. [ICCA Journal, Vol. 7, No. 2](/ICGA_Journal#7_2 "ICGA Journal")
4. [↑](#cite_ref-4) [Dap Hartmann](/Dap_Hartmann "Dap Hartmann") (**1987**). [Book review: Advances in Computer Chess 4](http://portal.acm.org/citation.cfm?id=1057627) from [ACM Portal](http://portal.acm.org/portal.cfm)
5. [↑](#cite_ref-5) Diagram edited from [Kai von Luck](/Kai_von_Luck "Kai von Luck"), [Bernd Owsnicki](/Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe") (**1982**). *[N.N.: A View of Planning in Chess](https://link.springer.com/chapter/10.1007%2F978-3-642-68826-3_8)*. in [Wahlster](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/w/Wahlster:Wolfgang.html) (Ed.), Proc. of [GWAI-82](http://www.informatik.uni-trier.de/%7Eley/db/conf/ki/gwai1982.html), Fig. 1, pp. 93
6. [↑](#cite_ref-6) [David Hooper](https://en.wikipedia.org/wiki/David_Vincent_Hooper), [Kenneth Whyld](https://en.wikipedia.org/wiki/Ken_Whyld) (**1992**). *[The Oxford Companion to Chess](https://en.wikipedia.org/wiki/The_Oxford_Companion_to_Chess)*. 2nd ed., [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), p. 274
7. [↑](#cite_ref-7) [Nomen nescio from Wikipedia](https://en.wikipedia.org/wiki/Nomen_nescio)

**[Up one Level](/Engines "Engines")**