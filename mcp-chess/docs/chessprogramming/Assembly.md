# Assembly

Source: https://www.chessprogramming.org/Assembly

**[Home](/Main_Page "Main Page") \* [Programming](/Programming "Programming") \* [Languages](/Languages "Languages") \* Assembly**

**Assembly** is a family of [low-level languages](https://en.wikipedia.org/wiki/Low-level_language) for programming computers. They implement a symbolic representation of the [machine instructions](https://en.wikipedia.org/wiki/Machine_code) and data needed to program a particular CPU architecture with its particular [instruction](https://en.wikipedia.org/wiki/Instruction_set)- and register set. An [assembler](https://en.wikipedia.org/wiki/Assembly_language#Assembler) is used to translate the assembly source code into executable machine instructions in [object code](https://en.wikipedia.org/wiki/Object_code). Almost each architecture and its extensions have their own proprietary assembly language with different [syntax](https://en.wikipedia.org/wiki/Syntax) and [mnemonics](https://en.wikipedia.org/wiki/Mnemonic) for operations, data declarations etc..

# Assembler

## CDC 6600/Cyber

[Mobility](/Mobility "Mobility") in [Chess 4.6](/Chess_(Program) "Chess (Program)") based on [47 CXi Xk](https://en.wikipedia.org/wiki/Talk%3ACDC_6600#.27Population_Count.27_.28.22Count_Ones.22.29_Instruction) [Population Count](/Population_Count "Population Count"), written in [COMPASS](https://en.wikipedia.org/wiki/COMPASS), the CDC Macro Assembler for the [CDC 6600](/CDC_6600 "CDC 6600") and [CDC Cyber](/CDC_Cyber "CDC Cyber") [[1]](#cite_note-1). The square list aka [bitboard](/Bitboards "Bitboards") was loaded into two 60-bit registers, with both populations added and stored.

```
** COUNTS - COUNT MEMBERS OF A SQUARE LIST

COUNTS MACRO Y
.STST
LOADS Y
.CHK2
CX'.S1' X'.S1'
CX'.S2' X'.S2'
IX'.SS' X'.S2'+X'.S1'
.STND
COUNTS ENDM 
...
SETQ MOBIL,(PLUS,(COUNTS,(INDEXS,ATKFR,(LSHIFT,SQLN,1))),MOB
```

## Cray

Cray Assembly Language (CAL) [[2]](#cite_note-2), some snippet from [Cray Blitz](/Cray_Blitz "Cray Blitz") [Bitboard](/Bitboards "Bitboards") code for the [Cray-1](/Cray-1 "Cray-1") or [Cray X-MP](/Cray_X-MP "Cray X-MP") [[3]](#cite_note-3):

```
l1020    =         *              
         s3        msave3-1,a2    
         s4        msave4-1,a2    
         a4        pcount-1,a1    
         a6        pcount-1,a5    
         pfirst-1,a1 s1           
         plast-1,a1 s2            
         pfirst-1,a5 s3           
         plast-1,a5 s4            
         a4        a4-1           
         a6        a6+1           
         pcount-1,a1 a4           
         pcount-1,a5 a6
```

## Intel/AMD

### Architectures

| CPU | Assemblers |
| --- | --- |
| [8080](/8080 "8080") / [Z80](/Z80 "Z80") | ASM80 |
| [8086](/8086 "8086") | [MASM](https://en.wikipedia.org/wiki/MASM), [TASM](https://en.wikipedia.org/wiki/TASM), [NASM](https://en.wikipedia.org/wiki/Netwide_Assembler), [GNU Assembler](https://en.wikipedia.org/wiki/GNU_Assembler) |
| [x86](/X86 "X86") | [FASM](https://en.wikipedia.org/wiki/FASM), [MASM](https://en.wikipedia.org/wiki/MASM), [NASM](https://en.wikipedia.org/wiki/Netwide_Assembler), [TASM](https://en.wikipedia.org/wiki/TASM), [GNU Assembler](https://en.wikipedia.org/wiki/GNU_Assembler) |
| [x86-64](/X86-64 "X86-64") | [MASM64](https://en.wikipedia.org/wiki/MASM), [NASM](https://en.wikipedia.org/wiki/Netwide_Assembler), [GNU Assembler](https://en.wikipedia.org/wiki/GNU_Assembler) |

### Syntax

Intel-Syntax: operation target, source

```
  add rax, rdx  ; rax += rdx
```

[AT & T Syntax](https://en.wikipedia.org/wiki/GNU_Assembler) operation<type> source, target

```
  addq %rdx, %rax  /* rax += rdx */
```

## PDP-6

[HAKMEM 169](/Population_Count#HAKMEM169 "Population Count"), to [count the ones](/Population_Count "Population Count") in a [PDP-6](/PDP-6 "PDP-6")/[PDP-10](/PDP-10 "PDP-10") 36-bit word, written in [MIDAS](/index.php?title=MIDAS&action=edit&redlink=1 "MIDAS (page does not exist)") [[4]](#cite_note-4):

```
   LDB B,[014300,,A]      ;or MOVE B,A then LSH B,-1
   AND B,[333333,,333333]
   SUB A,B
   LSH B,-1
   AND B,[333333,,333333]
   SUBB A,B               ;each octal digit is replaced by number of 1's in it
   LSH B,-3
   ADD A,B
   AND A,[070707,,070707]
   IDIVI A,77             ;casting out 63.'s
```

# Inline Assembly

[Inline assembly](https://en.wikipedia.org/wiki/Inline_assembler) is embedded inside various [C](/C "C"), [C++](/Cpp "Cpp"), [D](/D_(Programming_Language) "D (Programming Language)"), [Pascal](/Pascal "Pascal") and [Delphi](/Delphi "Delphi") compiler [[5]](#cite_note-5).

# See also

- [asmFish](/AsmFish "AsmFish") ([x86-64](/X86-64 "X86-64") [port](/Stockfish#ports "Stockfish") of [Stockfish](/Stockfish "Stockfish"))
- [Hardware](/Hardware "Hardware")
- [General Setwise Operations](/General_Setwise_Operations "General Setwise Operations")

# Publications

- [Lance A. Leventhal](http://www.vintage.org/2007/main/bio.php?id=1781) (**1979**). *6502 Assembly Language Programming*. Osborne/[McGraw-Hill](https://en.wikipedia.org/wiki/McGraw-Hill_Education), [pdf](http://www.atarimania.com/documents/6502_Assembly_Language_Programming.pdf)
- [Rodnay Zaks](https://en.wikipedia.org/wiki/Rodnay_Zaks) (**1979**). *[Programming the Z80](https://en.wikipedia.org/wiki/Programming_the_Z80)*. Sybex [[6]](#cite_note-6)
- [Kathe Spracklen](/Kathe_Spracklen "Kathe Spracklen") (**1979**). *Z-80 and 8080 assembly language programming*. [Hayden Books](https://en.wikipedia.org/wiki/Hayden_Books), [amazon.com](http://www.amazon.com/assembly-language-programming-Hayden-computer/dp/0810451670), [Internet Archive](https://archive.org/details/z808080assemblyl00kath) » [8080](/8080 "8080"), [Z80](/Z80 "Z80")
- [Jan Kuipers](/Jan_Kuipers "Jan Kuipers") (**1981**). *Tiny Chess 86 - Een schaakprogramma voor de 8088/8086*. [Databus](http://home.kpn.nl/a.dikker1/museum/databus.html) 06-81, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/06-1981,%20Databus,%20Jan%20Kuipers,%20Tiny%20Chess%2086.pdf) hosted by [Hein Veldhuis](/Hein_Veldhuis "Hein Veldhuis") » [8086](/8086 "8086"), [Tiny Chess 86](/Tiny_Chess_86 "Tiny Chess 86")
- [Zaks, Rodnay](https://en.wikipedia.org/wiki/Rodnay_Zaks) (**1983**). *Programming the 6502 (Fourth Edition)*. Sybex
- [Ward Douglas Maurer](/Ward_Douglas_Maurer "Ward Douglas Maurer") (**1984**). *[APPLE assembly language with Lazerware software](http://www.amazon.com/APPLE-assembly-language-Lazerware-software/dp/091489482X/ref=la_B001HPN2O8_1_2?s=books&ie=UTF8&qid=1410953624&sr=1-2)*. Computer Science Press » [Apple II](/Apple_II "Apple II")
- [Ward Douglas Maurer](/Ward_Douglas_Maurer "Ward Douglas Maurer") (**1985**). *[Commodore 64 assembly language: A course of study based on the DEVELOP-64 assembler/editor/debugger](http://www.amazon.com/Commodore-assembly-language-DEVELOP-64-assembler/dp/0881750409/ref=la_B001HPN2O8_1_3?s=books&ie=UTF8&qid=1410953624&sr=1-3)*. Computer Science Press » [Commodore 64](/Commodore_64 "Commodore 64")
- [Ward Douglas Maurer](/Ward_Douglas_Maurer "Ward Douglas Maurer") (**1990**). *[Assembly language programming on the Mac with MPW](http://www.worldcat.org/title/assembly-language-programming-on-the-mac-with-mpw-second-draft/oclc/22190641)*. [School of Engineering and Applied Science](https://en.wikipedia.org/wiki/George_Washington_University_School_of_Engineering_and_Applied_Science), [George Washington University](https://en.wikipedia.org/wiki/George_Washington_University), GWU-IIST-90-20. » [Macintosh](/Macintosh "Macintosh") [[7]](#cite_note-7)
- [Michael Abrash](https://en.wikipedia.org/wiki/Michael_Abrash) (**1990**). *[Zen of Assembly Language: Knowledge](http://www.amazon.com/exec/obidos/ASIN/0673386023/codihorr-20)*. Scott Foresman Trade, ISBN-13: 978-0673386021 [[8]](#cite_note-8) [[9]](#cite_note-9)
- [Randall Hyde](https://en.wikipedia.org/wiki/Randall_Hyde) (**2003, 2010**). *[The Art of Assembly Language Programming](http://nostarch.com/assembly2.htm)*. No Starch Press, 2nd edition, ISBN-13: 978-1-59327-207-4

# Listings

- [Chess 4.6](/Chess_(Program) "Chess (Program)") [CDC Cyber](/CDC_Cyber "CDC Cyber") [source code](http://www.computerhistory.org/chess/full_record.php?iid=sft-431614f455002), gift of [David Slate](/David_Slate "David Slate"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/3-3.Chess_4.6_Sourcecode.102645430/chess_4-6.sourcecode.102645430.pdf)
- [Sargon](/Sargon "Sargon") [Z80](/Z80 "Z80") [assembly listing](http://www.andreadrian.de/schach/sargon.asm) by [Dan](/Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](/Kathe_Spracklen "Kathe Spracklen"), hosted by [Andre Adrian](/Andre_Adrian "Andre Adrian")
- [Rookie 1.0](/Rookie "Rookie") [68000](/68000 "68000") assembly source, search.s from [Index of /rookie/nostalgia/v1](http://marcelk.net/rookie/nostalgia/v1/)

# Manuals

## [6502](/6502 "6502")

- [6502 Programming Manual](http://archive.6502.org/datasheets/synertek_programming_manual.pdf), August 1976 (pdf)

## [68000](/68000 "68000")

- [MOTOROLA M68000 FAMILY - Programmer’s Reference Manual](http://www.freescale.com/files/archives/doc/ref_manual/M68000PRM.pdf) (pdf)
- [68000 Assembler - User's Manual](http://neo.dmcs.p.lodz.pl/pn/asembler_68000/asm.pdf) (pdf) by Paul McKee

## [Alpha](/DEC_Alpha "DEC Alpha")

- [Alpha Instruction Set (Brief)](https://www.cs.arizona.edu/projects/alto/Doc/local/alpha.instruction.html)
- [Digital UNIX Assembly Language Programmer's Guide](http://www.cs.cmu.edu/afs/cs/academic/class/15213-f98/doc/alpha-asm.pdf), March 1996 (pdf)

## [ARM](/ARM2 "ARM2")

- [ARM Assembler](http://www.heyrick.co.uk/assembler/)
- [ARM Assembly Language Programming](http://www.peter-cockerell.net/aalp/html/frames.html) by [Pete Cockerell](http://www.peter-cockerell.net/)

## [Fairchild F8](/Fairchild_F8 "Fairchild F8")

- [Fairchild F8 Guide To Programming 1977](https://archive.org/details/bitsavers_fairchildfng1977_5888299), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) » [Fairchild F8](/Fairchild_F8 "Fairchild F8")

## HP Saturn

- [Gilbert Fernandes](https://fr.linkedin.com/in/fernandesgilbert), [Eric Rechlin](http://www.hpcalc.org/contact.php) (**2005**). *[Introduction to Saturn Assembly Language](http://www.hpcalc.org/details.php?id=1693)*. Third edition, Part of the [HP Calculator Archive](http://www.hpcalc.org/) » [HP Saturn](https://en.wikipedia.org/wiki/HP_Saturn), [HP 48 series](https://en.wikipedia.org/wiki/HP_48_series)

## [PowerPC](/PowerPC "PowerPC")

- [IBM PowerPC assembly](https://www.ibm.com/developerworks/library/l-ppc/)

## [SPARC](/SPARC "SPARC")

- [SPARC Assembly Language Reference Manual](https://docs.oracle.com/cd/E19457-01/801-6649/801-6649.pdf) (pdf)

## [x86-64](/X86-64 "X86-64")

- [x86-64 Manuals](/X86-64#Manuals "X86-64")

## [Z80](/Z80 "Z80")

- Neil J. Colvin (**1977**). *TDL Z80 Relocating/Linking Assembler User's Manual*. [pdf](http://retrotechnology.com/herbs_stuff/zasm.pdf)

# Forum Posts

- [Assembler handtuning benefit](https://www.stmintz.com/ccc/index.php?id=11909) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), November 11, 1997
- [Assembly language for PC (Off topic)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41366) by [Josué Forte](/Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 21, 2003
- [C vs ASM](http://www.talkchess.com/forum/viewtopic.php?t=47414) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), March 05, 2013 » [C](/C "C")
- [[for fun] rewrite of stockfish into asm and question on source](https://groups.google.com/d/msg/fishcooking/HKIYwO6pF-s/-DOONSK5F-IJ) by [Mohammed Li](/index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), January 09, 2015 » [asmFish](/AsmFish "AsmFish")
- [Some x64 assembler for the curious](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70283) by [Michael Sherwin](/Michael_Sherwin "Michael Sherwin"), [CCC](/CCC "CCC"), March 22, 2019 » [x86-64](/X86-64 "X86-64")

# External Links

- [Assembly language from Wikipedia](https://en.wikipedia.org/wiki/Assembly_language)
- [Comparison of assemblers from Wikipedia](https://en.wikipedia.org/wiki/List_of_assemblers)
- [High-level assembler from Wikipedia](https://en.wikipedia.org/wiki/High-level_assembler)
- [High Level Assembly](http://webster.cs.ucr.edu/AsmTools/HLA/)
- [The Art of Assembly Language Programming and HLA](http://www.plantation-productions.com/Webster/www.artofasm.com/index.html) by [Randall Hyde](https://en.wikipedia.org/wiki/Randall_Hyde)
- [The Assembly Gems page](http://www.df.lth.se/~john_e/) by [John Eckerdal](http://www.df.lth.se/~john_e/about.html)

## DEC

- [PDP-10 Machine Language](http://home.pipeline.com/~hbaker1/pdp-10/pdp-10.html) » [PDP-10](/PDP-10 "PDP-10") [[10]](#cite_note-10)
- [PDP-11 Assembly Language](https://programmer209.wordpress.com/2011/08/03/the-pdp-11-assembly-language/)
- [MACRO-11 from Wikipedia](https://en.wikipedia.org/wiki/MACRO-11)

## IBM

- [IBM Basic assembly language and successors - Wikipedia](https://en.wikipedia.org/wiki/IBM_Basic_assembly_language_and_successors)» [IBM 360](/IBM_360 "IBM 360"), [IBM 370](/IBM_370 "IBM 370"), [ICL 4/70](/ICL_4-70 "ICL 4-70")

## Intel

- [Assembly Language Lab](http://www.azillionmonkeys.com/qed/asmexample.html) by [Paul Hsieh](/Paul_Hsieh "Paul Hsieh")
- [Assembly language page](http://olivier.poudade.free.fr/) by [Olivier Poudade](/Olivier_Poudade "Olivier Poudade")
- [x86 assembly language from Wikipedia](https://en.wikipedia.org/wiki/X86_assembly_language)
- [X86 Assembly/X86 Architecture from Wikibooks](http://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture)
- [x86 Assembly Guide](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
- [Introduction to x64 Assembly](http://software.intel.com/en-us/articles/introduction-to-x64-assembly) by [Chris Lomont](http://www.lomont.org/), March 2012
- [alt.lang.asm](http://groups.google.com/group/alt.lang.asm/topics), [Google Group](http://groups.google.com/)
- [comp.lang.asm.x86](http://groups.google.com/group/comp.lang.asm.x86/topics), [Google Group](http://groups.google.com/)
- [x86 32-bit Assembly for Atheists](http://siyobik.info/index.php?document=x86_32bit_asm)
- [the dasm macro assembler](http://dasm-dillon.sourceforge.net/)
- [asmx multi-CPU assembler](http://xi6.com/projects/asmx/)

# References

1. [↑](#cite_ref-1) [Chess 4.6 source code](http://www.computerhistory.org/chess/full_record.php?iid=sft-431614f455002), gift of [David Slate](/David_Slate "David Slate"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/3-3.Chess_4.6_Sourcecode.102645430/chess_4-6.sourcecode.102645430.pdf)
2. [↑](#cite_ref-2) [Cray Assembly Language Reference - iPaper](http://www.scribd.com/doc/2161814/Cray-Assembly-Language-Reference)
3. [↑](#cite_ref-3) [Robert Hyatt's](/Robert_Hyatt "Robert Hyatt") [Cray Blitz](/Cray_Blitz "Cray Blitz") [crayblitz.tar.gz Source Code](http://www.craftychess.com/downloads/crayblitz/) see folder CAL, unmake.s
4. [↑](#cite_ref-4) [HAKMEM 169](/Population_Count#HAKMEM169 "Population Count") by [Gosper](/Bill_Gosper "Bill Gosper"), Mann, Lenard, [Root and Mann], [HAKMEM](http://home.pipeline.com/~hbaker1/hakmem/hakmem.html)
5. [↑](#cite_ref-5) [Inline assembly for x86 in Linux](http://www.ibm.com/developerworks/library/l-ia.html) by [IBM](/index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)")
6. [↑](#cite_ref-6) [pdf download link by Rodnay Zaks](http://www.z80.info/zaks.html)
7. [↑](#cite_ref-7) [Macintosh Programmer's Workshop from Wikipedia](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop)
8. [↑](#cite_ref-8) [Coding Horror: There Ain't No Such Thing as the Fastest Code](http://www.codinghorror.com/blog/2008/02/there-aint-no-such-thing-as-the-fastest-code.html) by [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood), February 19, 2008
9. [↑](#cite_ref-9) [Re: Developments of the last two years](http://www.talkchess.com/forum/viewtopic.php?t=47384&start=45) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC"), March 03, 2013
10. [↑](#cite_ref-10) MIT PDP-10 'Info' file converted to Hypertext 'html' format by [Henry Baker](http://home.pipeline.com/~hbaker1/home.html)

**[Up one Level](/Languages "Languages")**