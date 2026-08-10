# Michael Levin

Source: https://www.chessprogramming.org/Michael_Levin

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Michael Levin**

**Michael Levin**,  
an American computer scientist, in the 60s affiliated with [Massachusetts Institute of Technology](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), and involved in the initial development of [Lisp](/index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)") within the group of [John McCarthy](/John_McCarthy "John McCarthy"). The 1961 memo on [Alpha-Beta](/Alpha-Beta "Alpha-Beta") by [Daniel Edwards](/Daniel_Edwards "Daniel Edwards") and [Timothy Hart](/Timothy_Hart "Timothy Hart") [[1]](#cite_note-1), contains a Theorem by Michael Levin, the well known formula of the number of [leaf nodes](/Leaf_Node "Leaf Node") that need to be examined in Alpha-Beta.

# Theorem

Levin:  
Let ***n*** be the number of plies in a tree, and let ***b*** be the number of branches a every branch point. Then the number of terminal points on the tree is

```
T = bn
```

However, if the best possible advantage is take of the alpha-beta heuristic then the number of terminal points that need to be examined is for odd *n*,

```
T = b(n+1)/2 + b(n-1)/2 - 1
```

and for even *n*,

```
T = 2bn/2 - 1
```

which can be reformulated for both cases using [ceil and floor](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) functions:

```
T = b⌈n/2⌉ + b⌊n/2⌋ - 1
```

# Quotes

## Alpha-Beta

[Quote](/Template:Quote_McCarthy_on_Alpha-Beta "Template:Quote McCarthy on Alpha-Beta") by [John McCarthy](/John_McCarthy "John McCarthy") from *Human-Level AI is harder than it seemed in [1955](/Timeline#1955 "Timeline")* on the [Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop):

```
Chess programs catch some of the human chess playing abilities but rely on the limited effective branching of the chess move tree. The ideas that work for chess are inadequate for go. Alpha-beta pruning characterizes human play, but it wasn't noticed by early chess programmers - Turing, Shannon, Pasta and Ulam, and Bernstein. We humans are not very good at identifying the heuristics we ourselves use. Approximations to alpha-beta used by Samuel, Newell and Simon, McCarthy. Proved equivalent to minimax by Hart and Levin, independently by Brudno. Knuth gives details.
```

## LISP

[Quote](/Template:Quote_McCarthy_on_LISP "Template:Quote McCarthy on LISP") by [John McCarthy](/John_McCarthy "John McCarthy") in *History of Lisp* [[2]](#cite_note-2):

```
Many people participated in the initial development of LISP, and I haven't been able to remember all their contributions and must settle, at this writing, for a list of names. I can remember Paul W. Abrahams, Robert Brayton, Daniel Edwards, Patrick Fischer, Phyllis Fox, Saul Goldberg, Timothy Hart, Louis Hodes, Michael Levin, David Luckham, Klim Maling, Marvin Minsky, David Park, Nathaniel Rochester of IBM, and Steve Russell.
```

# See also

- [History of Alpha-Beta](/Alpha-Beta#HistoryAlphaBeta "Alpha-Beta")
- [Leaves from Node Types](/Node_Types#LeafNodes "Node Types")
- [LISP](/index.php?title=LISP&action=edit&redlink=1 "LISP (page does not exist)")
- [Odd-Even Effect](/Odd-Even_Effect "Odd-Even Effect")

# Selected Publications

- [John McCarthy](/John_McCarthy "John McCarthy"), [Paul W. Abrahams](/Paul_W._Abrahams "Paul W. Abrahams"), [Daniel Edwards](/Daniel_Edwards "Daniel Edwards"), [Timothy Hart](/Timothy_Hart "Timothy Hart"), Michael Levin (**1962**). *LISP 1.5 Programmer's Manual.* The M.I.T. Press, second edition (1985) available as [pdf reprint](http://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf) [[3]](#cite_note-3)
- Michael Levin (**1963**). *Primitive Recursion*, AIM-055, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/6109) at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- [Timothy Hart](/Timothy_Hart "Timothy Hart"), Michael Levin (**1964**). *LISP Exercises*, AIM-064, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/5924) at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- Michael Levin (**1964**). *Syntax of the New Language*, AIM-068, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/5919) at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- Michael Levin (**1964**). *New Language Storage Conventions*, AIM-069, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/5918) at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")

# References

1. [↑](#cite_ref-1) [Daniel Edwards](/Daniel_Edwards "Daniel Edwards"), [Timothy Hart](/Timothy_Hart "Timothy Hart") (**1961**). *The Alpha-Beta Heuristic*, AIM-030, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/6098) at [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
2. [↑](#cite_ref-2) [John McCarthy](/John_McCarthy "John McCarthy") (**1979**). *[History of Lisp](http://jmc.stanford.edu/articles/lisp.html)*. Chapter 4, From LISP 1 to LISP 1.5
3. [↑](#cite_ref-3) [McCarthy et al. LISP 1.5 Programmer's Manual.](http://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf/view) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum") Software Preservation Group

**[Up one level](/People "People")**