# Star Socrates

Source: https://www.chessprogramming.org/Star_Socrates

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Star Socrates**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Socrates_Pio-Clementino_Inv314.jpg/330px-Socrates_Pio-Clementino_Inv314.jpg)](/File:Socrates_Pio-Clementino_Inv314.jpg)

[Socrates](/Mathematician#Socrates "Mathematician") [[1]](#cite_note-1)

**\*Socrates**,  
a parallel chess program, developed by a team from [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") and [Sandia National Laboratories](https://en.wikipedia.org/wiki/Sandia_National_Laboratories) [[2]](#cite_note-2) headed by [Charles Leiserson](/Charles_Leiserson "Charles Leiserson"). Primary programmers were [Don Dailey](/Don_Dailey "Don Dailey"), co-author of [Socrates](/Socrates "Socrates") and [Titan](/Titan "Titan") aka [Socrates II](https://en.wikipedia.org/wiki/Socrates_II), on which \*Socrates was based on, and [Chris Joerg](/Chris_Joerg "Chris Joerg"). Further contributers were [Robert Blumofe](/Robert_Blumofe "Robert Blumofe"), [Matteo Frigo](/Matteo_Frigo "Matteo Frigo"), [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [Bradley Kuszmaul](/Bradley_Kuszmaul "Bradley Kuszmaul"), [Keith H. Randall](/Keith_H._Randall "Keith H. Randall"), [Eric Brewer](/Eric_Brewer "Eric Brewer"), [Michael Halbherr](/Michael_Halbherr "Michael Halbherr"), [Rolf Riesen](/index.php?title=Rolf_Riesen&action=edit&redlink=1 "Rolf Riesen (page does not exist)") (Sandia) and [Yuli Zhou](/Yuli_Zhou "Yuli Zhou").

# Massively Parallel Chess

Quote by [Chris Joerg](/Chris_Joerg "Chris Joerg") and [Bradley Kuszmaul](/Bradley_Kuszmaul "Bradley Kuszmaul") [[3]](#cite_note-3)

```
Computer chess provides a good testbed for understanding dynamic MIMD-style computations. To investigate the programming issues, we engineered a parallel chess program called *Socrates, which running on NCSA's 512 processor CM-5, tied for third in the 1994 ACM International Computer Chess Championship. *Socrates uses the Jamboree algorithm to search game trees in parallel and uses the Cilk 1.0 language and run-time system to express and to schedule the computation. In order to obtain good performance for chess, we use several mechanisms not directly provided by Cilk, such as aborting computations and directly accessing the active message layer to implement a global transposition table distributed across the processors. We found that we can use the critical path C and the total work W to predict the performance of our chess programs. Empirically *Socrates runs in time
```

```
T ≈ 0.95C + 1.09W/P  

on P processors. For best-ordered uniform trees of height h and degree d the average available parallelism in Jamboree search is

ϴ((d/2)h/2)

*Socrates searching real chess trees under tournament time controls yields average available parallelism of over 1000.
```

# History of \*Socrates

History of \*Socrates by [Chris Joerg](/Chris_Joerg "Chris Joerg") from his Ph. D. thesis [[4]](#cite_note-4)

```
We began work on this program in May of 1994. Don Dailey and Larry Kaufman of Heuristic Software provided us with a version of Socrates, their serial chess program. During May and June we parallelized the program using Cilk, focusing mainly on the search algorithm and the transposition table. During June Dailey visited MIT to help tune the program, but we spent most of June simply getting the parallel version of the program to work correctly. In late June, we entered *Socrates in the 1994 ACM International Computer Chess Championship in Cape May, New Jersey. We ran the program on a 512-node CM-5 at the National Center for Supercomputing Applications (NCSA) at the University of Illinois. Despite the fact that we had begun working on the program less than two months earlier, the program ran reliable and finished in third place.
```

# Acknowledgments

by [Chris Joerg](/Chris_Joerg "Chris Joerg") from his Ph. D. thesis:

```
I am especially grateful to my thesis supervisor, Professor Charles Leiserson, who has led the Cilk project. I still remember the day he came to my office and recruited me. He explained how he realized I had other work to do but he wanted to know if I would like to help out part time" on implementing a chess program using PCM. It sounded like a interesting project, so I agreed, but only after making it clear that I could only work part time because I had my thesis project to work on. Well, part time" became full time", and at times full time" became much more than that. Eventually, the chess program was completed, and the chess tournament came and went, yet I still kept working on the PCM system (which was now turning into Cilk). Ultimately, I realized that I should give up on my other project and make Cilk my thesis instead. Charles is a wonderful supervisor and under his leadership, the Cilk project has achieved more than I ever expected. Charles' influence can also be seen in this write-up itself. He has helped me turn this thesis into a relatively coherent document, and he has also pointed out some of my more malodorous grammatical constructions.
```

```
The Cilk project has been a team effort and I am indebted to all the people who have contributed in some way to the Cilk system: Bobby Blumofe, Feng Ming Dong, Matteo Frigo, Shail Aditya Gupta, Michael Halbherr, Charles Leiserson, Bradley Kuszmaul, Rob Miller, Keith Randall, Rolf Riesen, Andy Shaw, Richard Tauriello, and Yuli Zhou. Their contributions are noted throughout this document.
```

```
I thank, along with the members of the Cilk team, the past and present members of the Computation Structures Group. These friends have made MIT both a challenging and a fun place to be. In particular I should thank Michael Halbherr. He not only began the work that lead to the PCM system, but he tried many times to convince me to switch my thesis to this system. It took a while, but I finally realized he was right.
```

```
I am also indebted to Don Dailey and Larry Kaufman, both formerly of Heuristic Software. They wrote the serial Socrates program on which *Socrates is based. In addition, Don and I spent many long nights debugging, testing, and improving (or at least trying to improve) *Socrates. Most of this time we even had fun.
```

```
Professor Arvind, Dr. Andy Boughton, and Dr. Greg Papadopoulus also deserve many thanks. They provided me the freedom, encouragement, and support to work on a wide range of exciting projects throughout my years at MIT.
```

# Description

Description given in 1995 from the [ICGA](/ICGA "ICGA")-site [[5]](#cite_note-5)

```
The Star Socrates 2.0 chess program developed at the MIT Laboratory for Computer Science, will be running on the 1824 node Intel Paragon parallel supercomputer located at Sandia National Laboratories. The lead programmers are Don Dailey and Christopher F.Joerg and the project team is lead by Prof. Leiserson. Heuristic Software provided the original Socrates program on which StarSocrates was originally based. The Paragon is about 50 feet long and weighs about 30,000 pounds. Each node consists of two 50MHz i860 processors with either 16 or 32MB of memory. The program currently runs on both the Connection Machine CM-5 and the Intel Paragon.
```

# Awards

Awards for Cilk Technology & Research [[6]](#cite_note-6) :

```
1995, Second Place in the 1995 International Computer Chess Association's Eighth Computer Chess World Championship for *Socrates 2.0, a chess-playing program written in Cilk.
```

# See also

- [CilkChess](/CilkChess "CilkChess")
- [Socrates](/Socrates "Socrates")
- [StarTech](/StarTech "StarTech")

# Publications

- [Chris Joerg](/Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](/Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Proceedings of the Third DIMACS Parallel Implementation Challenge, 1994, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
- [Bradley Kuszmaul](/Bradley_Kuszmaul "Bradley Kuszmaul"), [Alan Sherman](/Alan_Sherman "Alan Sherman") (**1995**). *\*Socrates 2.0 Beats Grandmaster Sagalchik*. [ICCA Journal, Vol. 18, No. 2](/ICGA_Journal#18_2 "ICGA Journal")
- [Robert Blumofe](/Robert_Blumofe "Robert Blumofe"), [Chris Joerg](/Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](/Bradley_Kuszmaul "Bradley Kuszmaul"), [Charles Leiserson](/Charles_Leiserson "Charles Leiserson"), [Keith H. Randall](/Keith_H._Randall "Keith H. Randall"), [Yuli Zhou](/Yuli_Zhou "Yuli Zhou") (**1995**). *Cilk: An Efficient Multithreaded Runtime System* Proceedings of the Fifth [ACM SIGPLAN](/ACM#SIG "ACM") Symposium on Principles and Practice of Parallel Programming (PPoPP), [pdf](http://supertech.csail.mit.edu/papers/PPoPP95.pdf)
- [Chris Joerg](/Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing*. Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)

# External Links

## Chess Program

- [Star Socrates' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=181)

## Misc

- [Star from Wikipedia](https://en.wikipedia.org/wiki/Star)
- [Socrates from Wikipedia](https://en.wikipedia.org/wiki/Socrates)
- [Terri Lyne Carrington](/Category:Terri_Lyne_Carrington "Category:Terri Lyne Carrington"): [The Mosaic Project](https://en.wikipedia.org/wiki/The_Mosaic_Project_(album)) - Forest Star, [Tokyo Jazz, September 05, 2010](http://www.tokyo-jazz.com/2010/en/program/halla0905d.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   feat.: [Tineke Postma](/Category:Tineke_Postma "Category:Tineke Postma"), [Esperanza Spalding](/Category:Esperanza_Spalding "Category:Esperanza Spalding"), [Ingrid Jensen](https://en.wikipedia.org/wiki/Ingrid_Jensen) and [Chihiro Yamanaka](https://en.wikipedia.org/wiki/Chihiro_Yamanaka) as guest

# References

1. [↑](#cite_ref-1) Bust of Socrates. [Marble](https://en.wikipedia.org/wiki/Marble), Roman copy after a Greek original from the 4th century BC. From the [Quintili Villa](https://en.wikipedia.org/wiki/Villa_of_the_Quintilii) on the [Via Appia](https://en.wikipedia.org/wiki/Appian_Way), [Socrates from Wikipedia](https://en.wikipedia.org/wiki/Socrates)
2. [↑](#cite_ref-2) [8th World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cd6ed), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1995_WCCC/1995%20WCCC.062303014.sm.pdf), Courtesy of [Monroe Newborn](/Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
3. [↑](#cite_ref-3) [Chris Joerg](/Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](/Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Proceedings of the Third DIMACS Parallel Implementation Challenge, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
4. [↑](#cite_ref-4) [Chris Joerg](/Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing* Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](/Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)
5. [↑](#cite_ref-5) [Star Socrates' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=181)
6. [↑](#cite_ref-6) [Awards for Cilk Technology & Research](http://www.cilk.com/company/awards/)

**[Up one Level](/Engines "Engines")**