# CDC Cyber

Source: https://www.chessprogramming.org/CDC_Cyber

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* CDC Cyber**

[![](/images/thumb/b/b1/Cdc_cyber_176.jpg/300px-Cdc_cyber_176.jpg)](http://www.computerhistory.org/collections/accession/102627699)

Cyber 176 [[1]](#cite_note-1)

**CDC Cyber**,  
a family of [mainframe](https://en.wikipedia.org/wiki/Mainframe_computer) [supercomputers](https://en.wikipedia.org/wiki/Supercomputer) by [Control Data Corporation](https://en.wikipedia.org/wiki/Control_Data_Corporation) during the 1970s and 1980s, included five very different models, 60-bit Cyber 70/170, 64-bit Cyber 180 and 200, Cyberplus and Cyber-18.

# Cyber 70/170

The 70 and 170 series was based on the 60-bit architecture of the [CDC 6600](/CDC_6600 "CDC 6600") and CDC 7600. The Cyber-170 series represented CDCs move from discrete [electronic components](https://en.wikipedia.org/wiki/Electronic_component) and [core memory](https://en.wikipedia.org/wiki/Magnetic-core_memory) to [integrated circuits](https://en.wikipedia.org/wiki/Integrated_circuit) and [semiconductor memory](https://en.wikipedia.org/wiki/Semiconductor_memory).

## Architecture

The 170 had eight 18-bit address registers (A0 through A7), eight 18-bit index registers (B0 through B7), and eight 60-bit operand registers (X0 through X7). Seven of the A registers were tied to their corresponding X register. Setting A1 through A5 read that address and fetched it into the corresponding X1 through X5 register. Likewise, setting register A6 or A7 wrote the corresponding X6 or X7 register to central memory at the address written to the A register.

[![CDC Cyber 170 CPU architecture.png](https://upload.wikimedia.org/wikipedia/commons/3/36/CDC_Cyber_170_CPU_architecture.png)](/File:CDC_Cyber_170_CPU_architecture.png)

Hardware architecture of the CDC Cyber 170 [[2]](#cite_note-2)

## Chess Programs

[![](/images/b/b4/Chess_4.6_electronic_board_ACM1978.jpg)](http://archive.computerhistory.org/projects/chess/related_materials/physical-object/3-1%20and%203-3.Chess_4.6_electronic_board_ACM_9_NACCC_Washington_1978_10264526.NEWBORN.jpg)

[Chess 4.6](/Chess_(Program) "Chess (Program)") [Chesstor](/Chess_(Program)#Chesstor "Chess (Program)"), [ACM 1978](/ACM_1978 "ACM 1978") [[3]](#cite_note-3)

Most prominent chess program running on CDC Cyber 70/170 was [Northwestern University's](/Northwestern_University "Northwestern University") [Chess 4.x](/Chess_(Program) "Chess (Program)"), supported by CDC Cyber hardware consultant [David Cahlander](/David_Cahlander "David Cahlander"). Already at the [WCCC 1974](/WCCC_1974 "WCCC 1974"), with Chess still running on a [CDC 6600](/CDC_6600 "CDC 6600"), [Nils Barricelli's](/Nils_Barricelli "Nils Barricelli") [Freedom](/Freedom "Freedom") ran on a Cyber 74. At [ACM 1975](/ACM_1975 "ACM 1975"), with [Iron Fish](/Iron_Fish "Iron Fish") on a Cyber 74, Chess 4.4 already ran on a Cyber 175 [[4]](#cite_note-4), Chess 4.5 at [ACM 1976](/ACM_1976 "ACM 1976"), Chess 4.6 at [ACM 1977](/ACM_1977 "ACM 1977"), Chess 4.7 at [ACM 1978](/ACM_1978 "ACM 1978"), also playing the [Levy match](/Levy_versus_Chess_1978 "Levy versus Chess 1978"), and Chess 4.9 at [ACM 1979](/ACM_1979 "ACM 1979") all ran on a 60-bit Cyber 176 [[5]](#cite_note-5). [Martin Bryant's](/Martin_Bryant "Martin Bryant") first chess program, [White Knight](/White_Knight "White Knight"), written in [Pascal](/Pascal "Pascal"), was compiled to ran on a Cyber 72 [[6]](#cite_note-6). [Nuchess](/Nuchess "Nuchess") played the [WCCC 1980](/WCCC_1980 "WCCC 1980") on Cyber 176, so did the Austrian [Merlin](/Merlin "Merlin") at the [International Computer Chess Tournament 1984](/International_Computer_Chess_Tournament_1984 "International Computer Chess Tournament 1984"). [Chat](/Chat "Chat") played the [WCCC 1986](/WCCC_1986 "WCCC 1986") on a Cyber 175.

- [Chat](/Chat "Chat")
- [Chess 4.x](/Chess_(Program) "Chess (Program)")
- [Freedom](/Freedom "Freedom")
- [Iron Fish](/Iron_Fish "Iron Fish")
- [Merlin](/Merlin "Merlin")
- [Nuchess](/Nuchess "Nuchess")
- [White Knight](/White_Knight "White Knight")

## Population Count

[Axel H. Horns](http://de.linkedin.com/in/horns) in a reply to [Steven M. Bellovin](/Steven_M._Bellovin "Steven M. Bellovin") in a discussion on CDC [Population Count](/Population_Count "Population Count") [[7]](#cite_note-7):

```
From this lecture I own a copy of "CONTROL DATA CYBER 70 SERIES - 6000 SERIES - 7600 COMPUTER SERIES" pocket manual "COMPASS VERSION 3" printed in 1973. This document clearly states that in the CYBER 70 Models 74 and 6600 Computers, the opcode "47" for "population count" was executed by the DIVIDE UNIT. Contrary, the CYBER 70 Models 76 and 7600 Computers had a separate POPULATION COUNT UNIT. If I understood the opcode table correctly  the respective opcode was executed in one or two clock cycles (very fast; the same as shift opcodes).
```

## Mobility in Chess 4.6

[Mobility](/Mobility "Mobility") in [Chess 4.6](/Chess_(Program) "Chess (Program)") based on [47 CXi Xk](https://en.wikipedia.org/wiki/Talk%3ACDC_6600#.27Population_Count.27_.28.22Count_Ones.22.29_Instruction) [Population Count](/Population_Count "Population Count"), written in [COMPASS](https://en.wikipedia.org/wiki/COMPASS), the CDC Macro [Assembler](/Assembly "Assembly") [[8]](#cite_note-8). The square list aka [bitboard](/Bitboards "Bitboards") was loaded into two 60-bit registers, with both populations added and stored.

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

# Cyber 180

The Cyber 180 series systems were full 64-bit machines. Memory was 64-bit word and 8-bit byte addressable. Integers were 64 bits long, though 32-bit integers were used for addresses in instructions. [Floating point numbers](/Float "Float") were 64 bits for single precision, and 128 bits for [double precision](/Double "Double").

# See also

- [CDC 6600](/CDC_6600 "CDC 6600")
- [Cray-1](/Cray-1 "Cray-1")

# Publications

- Editor (**1978**). *Cyber 176 tops Toronto Chess Tournament*. [Personal Computing, Vol. 2, No. 7](/Personal_Computing#2_7 "Personal Computing"), pp. 79 » [Chess 4.6](/Chess_(Program) "Chess (Program)"), [WCCC 1977](/WCCC_1977 "WCCC 1977")

# External Links

- [CDC Cyber from Wikipedia](https://en.wikipedia.org/wiki/CDC_Cyber)
- [Cyber documentation](http://bitsavers.trailing-edge.com/pdf/cdc/cyber/) from [bitsavers.org](http://bitsavers.informatik.uni-stuttgart.de/)
- [Desktop CYBER Emulator](http://members.iinet.net.au/~tom-hunter/index.html)

:   [CDC CYBER Photos and CDC Advertising Material](http://members.iinet.net.au/~tom-hunter/photos.html)

- [Museum Waalsdorp: Computer history - The Control Data CYBER 74 system](http://www.museumwaalsdorp.nl/computer/en/comp781E.html)
- [Museum Waalsdorp: Computer history - CDC's 180 State Architecture](http://www.museumwaalsdorp.nl/computer/en/180state.html)
- [Starring the Computer - CDC Cyber 180](http://starringthecomputer.com/computer.html?c=24)

# References

1. [↑](#cite_ref-1) [Cyber 176](http://www.computerhistory.org/collections/accession/102627699) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
2. [↑](#cite_ref-2) Scanned from a manual, [CDC Cyber from Wikipedia](https://en.wikipedia.org/wiki/CDC_Cyber)
3. [↑](#cite_ref-3) [Chess 4.6 electronic board](http://archive.computerhistory.org/projects/chess/related_materials/physical-object/) at [ACM 1978](/ACM_1978 "ACM 1978"), Courtesy of [Monroe Newborn](/Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
4. [↑](#cite_ref-4) [Monty Newborn](/Monroe_Newborn "Monroe Newborn") (**1977**). *[Summary of the ACM Sixth U.S. Computer Chess Championship](http://www.atariarchives.org/bcc2/showpage.php?page=22)*. [The Best of Creative Computing Volume 2](/Creative_Computing#Best2 "Creative Computing"), edited by [David Ahl](https://en.wikipedia.org/wiki/David_H._Ahl), hosted by [AtariArchives.org](http://www.atariarchives.org/)
5. [↑](#cite_ref-5) [Ben Mittman](/Ben_Mittman "Ben Mittman"), [Monroe Newborn](/Monroe_Newborn "Monroe Newborn") (**1980**). *[Computer chess at ACM 79: the tournament and the man vs. man and machine match](http://dl.acm.org/citation.cfm?id=358817&dl=ACM&coll=DL&CFID=78577980&CFTOKEN=10389697)*. [Communications of the ACM](/ACM#Communications "ACM"), Vol. 23, Issue 1, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.Computer_chess_at_ACM_79/3-1%20and%203-2%20and%203-3.Computer_chess_at_ACM_79.062303018.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
6. [↑](#cite_ref-6) [Tony Harrington](/Tony_Harrington "Tony Harrington") (**1983**). *University Challenge - Martin Bryant and White Knight*. [Personal Computer World](https://en.wikipedia.org/wiki/Personal_Computer_World), [August 1983](http://www.chesscomputeruk.com/html/publication_archive_1983.html), [pdf](http://www.chesscomputeruk.com/PCW_August_1983.pdf) hosted by [Mike Watters](/Mike_Watters "Mike Watters")
7. [↑](#cite_ref-7) [Sideways Add / Population Count](http://cryptome.org/jya/sadd.htm) by [Jitze Couperus](http://www.couperus.org/), [Steve Bellovin](/Steven_M._Bellovin "Steven M. Bellovin") and [Axel H. Horns](http://de.linkedin.com/in/horns), [cryptography@c2.net](https://en.wikipedia.org/wiki/C2Net), January 28, 1999
8. [↑](#cite_ref-8) [Chess 4.6 source code](http://www.computerhistory.org/chess/full_record.php?iid=sft-431614f455002), gift of [David Slate](/David_Slate "David Slate"), from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/software/3-3.Chess_4.6_Sourcecode.102645430/chess_4-6.sourcecode.102645430.pdf)

**[Up one Level](/Hardware "Hardware")**