# Ferranti Mark 1

Source: https://www.chessprogramming.org/Ferranti_Mark_1

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* Ferranti Mark 1**

**Ferranti Mark 1**,  
the world's first commercially available general-purpose electronic computer, produced by [Ferranti](https://en.wikipedia.org/wiki/Ferranti) [[1]](#cite_note-1). The first machine was delivered to the [University of Manchester](/University_of_Manchester "University of Manchester") in February 1951 [[2]](#cite_note-2). Ferranti Mark 1 was a tidied up and commercialized version of the [Manchester Mark 1](https://en.wikipedia.org/wiki/Manchester_Mark_1) developed in 1948-1949 at the University of Manchester, which was a further development of the [Manchester Small-Scale Experimental Machine](https://en.wikipedia.org/wiki/Manchester_Small-Scale_Experimental_Machine) (SSEM, nicked Baby) by [Frederic C. Williams](https://en.wikipedia.org/wiki/Frederic_Calland_Williams), [Tom Kilburn](https://en.wikipedia.org/wiki/Tom_Kilburn) and Geoff Tootill [[3]](#cite_note-3). During the 1940s, [Alan Turing](/Alan_Turing "Alan Turing") and others such as [Konrad Zuse](/Konrad_Zuse "Konrad Zuse") developed the idea of using the computer's own [memory](/Memory "Memory") to hold both the [program](/index.php?title=Program&action=edit&redlink=1 "Program (page does not exist)") and [data](/Data "Data"). It was [John von Neumann](/John_von_Neumann "John von Neumann") who became widely credited with defining that [stored-program computer](https://en.wikipedia.org/wiki/Stored-program_computer) architecture, on which the Mark 1 was based [[4]](#cite_note-4) [[5]](#cite_note-5).

# Memory

The Mark 1 used a 20-[bit](/Bit "Bit") word stored as a single line of dots on a [Williams-Kilburn tube](https://en.wikipedia.org/wiki/Williams_tube), each tube storing 64 lines. Instructions were stored in a single word, while numbers were stored in two words (40 bits). The [main memory](/Memory "Memory") had eight tubes, each storing one page of 64 words. Other tubes stored the single 80-bit accumulator (A), the 40-bit multiplicand/quotient register (MQ) and eight B-lines, or index registers, used to modify instructions. An extra 20-bit word per tube stored an offset value into the secondary storage, a 512-page [magnetic drum](https://en.wikipedia.org/wiki/Magnetic_drum).

[![Williams-tube.jpg](https://upload.wikimedia.org/wikipedia/commons/0/0e/Williams-tube.jpg)](/File:Williams-tube.jpg)

[Williams-Kilburn tube](https://en.wikipedia.org/wiki/Williams_tube) [[6]](#cite_note-6)

# Instructions

The 20 bit instructions had an address and an operator part. The coding of instructions was: bits 0-8 the [CRT](https://en.wikipedia.org/wiki/Cathode_ray_tube) address, bits 10-12 the B-line address and bits 13-19 the function code. Writing of programs was based on a numerical system to the [base 32](https://en.wikipedia.org/wiki/Base32) [[7]](#cite_note-7). Integer numbers were usually treated as 40 bit double words, negative numbers already represented as [Two's complement](/General_Setwise_Operations#TheTwosComplement "General Setwise Operations"). The Mark 1 had an instruction to find the position of the most significant digit [[8]](#cite_note-8) aka [Bitscan reverse](/index.php?title=Bitscan&action=edit&redlink=1 "Bitscan (page does not exist)") or [Leading Zero Count](/index.php?title=Bitscan&action=edit&redlink=1 "Bitscan (page does not exist)") for the purpose to convert integers to normalized [floating point numbers](/Float "Float"), as well as a [Population Count](/Population_Count "Population Count") instruction for [Cryptography](https://en.wikipedia.org/wiki/Cryptography) purposes [[9]](#cite_note-9). Arithmetical and logical instructions other than multiplication took 1.2 milliseconds (5 x 240 microseconds beats ), 40\*40=80 bit multiplication 2.16 milliseconds (9 beats) [[10]](#cite_note-10) [[11]](#cite_note-11).

# Console

[![Mark1controls.gif](/images/thumb/7/79/Mark1controls.gif/640px-Mark1controls.gif)](http://curation.cs.manchester.ac.uk/computer50/www.computer50.org/mark1/ip-fm1.controls.html)

The two larger CRT displays could be switched to show the current contents of any of the 8 pages. The four smaller displays (presumably) permanently showed the current contents of the four auxiliary tubes, A (80-bit Accumulator), B (8 20-bit B-lines), C (Control Address and Present Instruction) and D (current multiplicand value). See the next picture and comment for the Input/Output equipment. [[12]](#cite_note-12)

# Checkers

The first successful [AI](/Artificial_Intelligence "Artificial Intelligence") program was written in 1950/1951 by [Christopher Strachey](/Christopher_Strachey "Christopher Strachey"), initially for the [Pilot ACE](https://en.wikipedia.org/wiki/Pilot_ACE) at [National Physical Laboratory](https://en.wikipedia.org/wiki/National_Physical_Laboratory,_UK), exhaustings its memory [[13]](#cite_note-13). Strachey’s [checkers](/Checkers "Checkers") (draughts) program was soon ported and ran on the Mark I computer at the [University of Manchester](/University_of_Manchester "University of Manchester"), and by the summer of 1952 the program could play a complete game of checkers at a reasonable speed [[14]](#cite_note-14) [[15]](#cite_note-15), and already featured [Bitboards](/Bitboards "Bitboards") for White, Black and Kings to [represent the board](/Board_Representation "Board Representation") [[16]](#cite_note-16).

# Chess

[Alan Turing](/Alan_Turing "Alan Turing"), while affiliated with the [University of Manchester](/University_of_Manchester "University of Manchester") began "porting" his pen and paper program [Turochamp](/Turochamp "Turochamp") to run on a Mark 1, as well started with [Michie's](/Donald_Michie "Donald Michie") and [Wylie's](/Shaun_Wylie "Shaun Wylie") program [Machiavelli](/Machiavelli "Machiavelli"), but could not complete them [[17]](#cite_note-17). Influenced by Turing's ideas, [Dietrich Prinz](/Dietrich_Prinz "Dietrich Prinz") developed the first limited chess program for the Ferranti Mark 1 in 1951, dubbed [Mate-in-two](/Mate-in-two "Mate-in-two") [[18]](#cite_note-18) [[19]](#cite_note-19).

# Quotes

by [Jack Good](/Jack_Good "Jack Good"), 1998 [[20]](#cite_note-20):

```
In a letter to F C Williams in July 1951 I said "A facetious question is whether it is intended to display chess positions on the monitoring tubes". Of course today it is no longer at all facetious.
```

# See also

- [Alan Turing](/Alan_Turing "Alan Turing")
- [Christopher Strachey](/Christopher_Strachey "Christopher Strachey")
- [Dietrich Prinz](/Dietrich_Prinz "Dietrich Prinz")
- [Mate-in-two](/Mate-in-two "Mate-in-two")
- [University of Manchester](/University_of_Manchester "University of Manchester")

# Selected Publications

[[21]](#cite_note-21)

- [Alan Turing](/Alan_Turing "Alan Turing") (**1949**). *[Alan Turing's Manual for the Ferranti Mk. I](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f45472f)*. transcribed in 2000 by [Robert Thau](http://www.panix.com/%7Erst/), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-1.Ferranti_Mark_1_manual.Turing-Alan/2-1.Ferranti_Mark_1_manual.Turing-Alan.1951.UNIVERSITY_OF_MANCHESTER.062303005.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
- [Dietrich Prinz](/Dietrich_Prinz "Dietrich Prinz") (**1951**). *Introduction to Programming on the Manchester Electronic Digital Computer*. [[22]](#cite_note-22) [[23]](#cite_note-23)
- [Alan Turing](/Alan_Turing "Alan Turing") (**1951**). *[Programmers' Handbook for the Manchester Electronic Computer Mark II](http://www.alanturing.net/turing_archive/archive/m/m01/M01-001.html)*. 1st edition
- [Alan Turing](/Alan_Turing "Alan Turing") (**1952**). *[Programmers' Handbook for the Manchester Electronic Computer Mark II](http://www.computer50.org/kgill/mark1/progman.html)*. 2nd edition, revised by [R.A. Brooker](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/b/Brooker:R=_A=.html)

# External Links

- [Ferranti Mark 1 from Wikipedia](https://en.wikipedia.org/wiki/Ferranti_Mark_1)

:   [Manchester Mark 1 from Wikipedia](https://en.wikipedia.org/wiki/Manchester_Mark_1)

- [The Ferranti Mark 1 (Digital 60)](http://www.digital60.org/birth/manchestercomputers/mark1/ferranti.html)
- [Ferranti Mark 1](http://www.computer50.org/mark1/FM1.html) from [Computer 50 - The University of Manchester Celebrates the Birth of the Modern Computer](http://www.computer50.org/)
- [The Ferranti Mark I computer](http://www.mosi.org.uk/media/34368825/ferranti%20mark%20i%20computer.pdf) pdf from [Museum of Science and Industry in Manchester](https://en.wikipedia.org/wiki/Museum_of_Science_and_Industry_%28Manchester%29)
- [The “Modern” History of Artificial Intelligence and Programs](http://www.macalester.edu/psychology/whathap/ubnrp/intelligence05/MMhistory.html) from [Neuroscience Of Intelligence](http://www.macalester.edu/academics/psychology/whathap/ubnrp/intelligence05/index.html)
- [LoveLetters\_1.0, 2009—...:](http://www.alpha60.de/art/love_letters/) by [David Link](http://www.alpha60.de/) » [Christopher Strachey's](/Christopher_Strachey "Christopher Strachey") love letters

# References

1. [↑](#cite_ref-1) [Ferranti: the Company](http://www.chilton-computing.org.uk/acl/technology/atlas/p001.htm) from [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory")
2. [↑](#cite_ref-2) [Ferranti Mark 1 - History and specifications, from Wikipedia](https://en.wikipedia.org/wiki/Ferranti_Mark_1#History_and_specifications)
3. [↑](#cite_ref-3) [Manchester Small-Scale Experimental Machine from Wikipedia](https://en.wikipedia.org/wiki/Manchester_Small-Scale_Experimental_Machine)
4. [↑](#cite_ref-4) [Manchester Mark 1 - Background](https://en.wikipedia.org/wiki/Manchester_Mark_1#Background)
5. [↑](#cite_ref-5) [Von Neumann architecture from Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)
6. [↑](#cite_ref-6) [Williams tube from Wikipedia](https://en.wikipedia.org/wiki/Williams_tube)
7. [↑](#cite_ref-7) [Programming the Mark 1](http://www.computer50.org/mark1/program.html)
8. [↑](#cite_ref-8) [Alan Turing](/Alan_Turing "Alan Turing") (**1949**). *[Alan Turing's Manual for the Ferranti Mk. I](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f45472f)*. transcribed in 2000 by [Robert Thau](http://www.panix.com/~rst/), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-1.Ferranti_Mark_1_manual.Turing-Alan/2-1.Ferranti_Mark_1_manual.Turing-Alan.1951.UNIVERSITY_OF_MANCHESTER.062303005.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), 9.4 The position of the most significant digit
9. [↑](#cite_ref-9) [Cryptography](https://en.wikipedia.org/wiki/Cryptography) is also a significant application of the /R function symbol, which counts the number of one bits in a word; Turing refers to this as the "sideways adder" in his quick-reference summary. from [Alan Turing](/Alan_Turing "Alan Turing") (**1949**). *[Alan Turing's Manual for the Ferranti Mk. I](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f45472f)*. transcribed in 2000 by [Robert Thau](http://www.panix.com/~rst/), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-1.Ferranti_Mark_1_manual.Turing-Alan/2-1.Ferranti_Mark_1_manual.Turing-Alan.1951.UNIVERSITY_OF_MANCHESTER.062303005.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), 9.4 The position of the most significant digit
10. [↑](#cite_ref-10) [Ferranti Mark 1 - Specification](http://www.computer50.org/mark1/FM1.html#specification) from [Computer 50 - The University of Manchester Celebrates the Birth of the Modern Computer](http://www.computer50.org/)
11. [↑](#cite_ref-11) [11. The time occupied by various operations](http://www.computer50.org/kgill/mark1/progman.html#s11) from [Alan Turing](/Alan_Turing "Alan Turing") (**1951**). *[Programmers' Handbook for the Manchester Electronic Computer Mark II](http://www.alanturing.net/turing_archive/archive/m/m01/M01-001.html)*. 1st edition
12. [↑](#cite_ref-12) [The Ferranti Mark 1](http://curation.cs.manchester.ac.uk/computer50/www.computer50.org/mark1/ip-fm1.controls.html) from [Mark 1 Photo Gallery](http://curation.cs.manchester.ac.uk/computer50/www.computer50.org/mark1/photogallery.html#fm1), The two larger [CRT](https://en.wikipedia.org/wiki/Cathode_ray_tube) displays could be switched to show the current contents of any of the 8 pages. The four smaller displays (presumably) permanently showed the current contents of the four auxiliary tubes, A (80-bit Accumulator), B (8 20-bit B-lines), C (Control Address and Present Instruction) and D (current multiplicand value). Copyright [The University of Manchester](/University_of_Manchester "University of Manchester") 1998, 1999
13. [↑](#cite_ref-13) [Christopher Strachey from Wikipedia](https://en.wikipedia.org/wiki/Christopher_Strachey)
14. [↑](#cite_ref-14) [artificial intelligence (AI) :: Early milestones in AI](http://www.britannica.com/EBchecked/topic/37146/artificial-intelligence-AI/219091/Early-milestones-in-AI?anchor=ref739464) from [Britannica Online Encyclopedia](https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica)
15. [↑](#cite_ref-15) [The “Modern” History of Artificial Intelligence and Programs](http://www.macalester.edu/psychology/whathap/ubnrp/intelligence05/MMhistory.html) from [Neuroscience Of Intelligence](http://www.macalester.edu/academics/psychology/whathap/ubnrp/intelligence05/index.html)
16. [↑](#cite_ref-16) On [Bitboards](/Bitboards "Bitboards") for White, Black and Kings to [represent the checkers board](/Board_Representation "Board Representation"), see [David Link Video](/Ferranti_Mark_1#DavidLinkVideo "Ferranti Mark 1") at 1:04:02
17. [↑](#cite_ref-17) [Chronology of Computing](http://www.fbi.fh-darmstadt.de/fileadmin/vmi/chronologie/index.htm) compiled by [David Singmaster](/Mathematician#DSingmaster "Mathematician")
18. [↑](#cite_ref-18) [Dietrich Prinz](/Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
19. [↑](#cite_ref-19) [First video game - 1947–1958: Chess, from Wikipedia](https://en.wikipedia.org/wiki/First_video_game#1947.E2.80.931958:_Chess)
20. [↑](#cite_ref-20) [Excerpts from Acceptance Speech for the 1998 Computer Pioneers Award from the IEEE - Jack Good](http://www.chilton-computing.org.uk/acl/associates/permanent/good.htm) hosted by [Atlas Computer Laboratory](/Atlas_Computer_Laboratory "Atlas Computer Laboratory")
21. [↑](#cite_ref-21) [Mark 1 Documents](http://www.computer50.org/kgill/mark1/mark1book.html) from [Computer 50 - The University of Manchester Celebrates the Birth of the Modern Computer](http://www.computer50.org/)
22. [↑](#cite_ref-22) [Papers of Dr Dietrich G. Prinz - ELGAR: Electronic Gateway to Archives at Rylands](http://archives.li.man.ac.uk/ead/html/gb133nahc-pri-p1.shtml) [The John Rylands University Library](http://www.library.manchester.ac.uk/) [The University of Manchester](/University_of_Manchester "University of Manchester")
23. [↑](#cite_ref-23) [UK National Archive for the History of Computing - Draft Catalogue Version 1.0](http://www.chstm.manchester.ac.uk/downloads/media,38917,en.pdf), August 15, 2005 (pdf)

**[Up one Level](/Hardware "Hardware")**