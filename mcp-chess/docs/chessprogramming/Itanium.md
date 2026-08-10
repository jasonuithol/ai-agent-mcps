# Itanium

Source: https://www.chessprogramming.org/Itanium

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* Itanium**

[![](/images/thumb/f/f5/Intel-Itanium-Processor-9500.jpg/300px-Intel-Itanium-Processor-9500.jpg)](http://wccftech.com/intel-itanium-kittson-ia64-processors-32nm/)

Die shot of [Itanium 9500](https://en.wikipedia.org/wiki/List_of_Intel_Itanium_microprocessors#Poulson_.2832_nm.29) [[1]](#cite_note-1)

**Itanium**,  
a family of 64-bit microprocessors by [Intel](/Intel "Intel") that implement the [IA-64](https://en.wikipedia.org/wiki/IA-64) architecture originated by [Hewlett-Packard](https://en.wikipedia.org/wiki/Hewlett-Packard) (HP) and later jointly developed by HP and Intel. While the early development started in 1989 by HP, Intel officially announced the name of the processor, Itanium, on October 4, 1999 [[2]](#cite_note-2). The Itanium [Merced](https://en.wikipedia.org/wiki/List_of_Intel_Itanium_microprocessors#.22Merced.22_.28180_nm.29) was released on June 2001, [Itanium 2](https://en.wikipedia.org/wiki/Itanium#Itanium_2:_2002.E2.80.932010) McKinley and Madison in 2002 and 2003 respectively, the so far most recent [Poulson](https://en.wikipedia.org/wiki/List_of_Intel_Itanium_microprocessors#Poulson_.2832_nm.29) (Itanium 9500) in November 2012, and [Kittson](https://en.wikipedia.org/wiki/Itanium#Kittson) planned for 2015 [[3]](#cite_note-3). Initially intended as Intel's successor for [x86](/X86 "X86") aka IA-32 architecture, [AMD](/AMD "AMD") forced Intel to change priorities with [x86-64](/X86-64 "X86-64").

# Architecture

IA-64 applies [explicitly parallel instruction computing](https://en.wikipedia.org/wiki/Explicitly_parallel_instruction_computing) (EPIC) which allows the processor to execute multiple instructions in each clock cycle. EPIC implements a form of [very long instruction word](https://en.wikipedia.org/wiki/Very_long_instruction_word) (VLIW) architecture, in which a single instruction word contains up to three instructions. With EPIC, the compiler determines in advance which instructions can be executed at the same time, rather than the processor itself. The architecture implements [branch predication](https://en.wikipedia.org/wiki/Branch_predication) and [speculation](https://en.wikipedia.org/wiki/Speculative_execution), has 128 64-bit general purpose registers, 128 82-bit floating point or [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") registers, 64 one-bit predicates, and eight branch registers, and thirty functional execution units in eleven groups, such as various [ALUs](/Combinatorial_Logic#ALU "Combinatorial Logic"), [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") units with parallel shift and multiply, and [population count](/Population_Count "Population Count") unit.

[![Itanium architecture.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Itanium_architecture.svg/960px-Itanium_architecture.svg.png)](/File:Itanium_architecture.svg)

Itanium architecture [[4]](#cite_note-4)

# x86 Support

[x86](/X86 "X86") (IA-32) instructions were supported by hardware [[5]](#cite_note-5) , and since 2006 emulated with the [IA-32 Execution Layer](https://en.wikipedia.org/wiki/IA-32_Execution_Layer).

# Chess Programs

[TSCP](/TSCP "TSCP") [[6]](#cite_note-6) , [Tinker](/Tinker "Tinker") [[7]](#cite_note-7) and [Crafty](/Crafty "Crafty") were mentioned running under Itanium. While the original Merced was disappointing, [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") reported a good performance of Crafty on McKinley in 2003 [[8]](#cite_note-8) , close to the [Opteron](/X86-64 "X86-64") with double frequency. [Eugene Nalimov](/Eugene_Nalimov "Eugene Nalimov"), at that time member of the [Microsoft](/Microsoft "Microsoft") Visual compiler team targeting the Itanium platform, provided a IA-64 optimzed [BitScan](/BitScan "BitScan") aka firstOne and lastOne in [C](/C "C") [[9]](#cite_note-9) , taking advantage of IA-64's [branch predication](https://en.wikipedia.org/wiki/Branch_predication).

# See also

- [i860](/I860 "I860")
- [x86](/X86 "X86")
- [x86-64](/X86-64 "X86-64")

# Forum Posts

- [Re: What are the chances of getting a new 64bit instruction for chess :)](https://www.stmintz.com/ccc/index.php?id=116773) by [Eugene Nalimov](/Eugene_Nalimov "Eugene Nalimov"), [CCC](/CCC "CCC"), June 27, 2000
- [Will the Itanium have a BSF or BSR instruction?](https://www.stmintz.com/ccc/index.php?id=124638) by Larry Griffiths, [CCC](/CCC "CCC"), August 15, 2000 » [BitScan](/BitScan "BitScan")
- [Itanium](https://www.stmintz.com/ccc/index.php?id=150518) by John Dahlem, [CCC](/CCC "CCC"), January 17, 2001
- [Intel Itanium 2 Benchmarks](https://www.stmintz.com/ccc/index.php?id=232633) by [Vincent Lejeune](/index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](/CCC "CCC"), May 29, 2002
- [Itanium2 Testing Crafty & Tinker Informal Results](https://www.stmintz.com/ccc/index.php?id=284689) by [Brian Richardson](/Brian_Richardson "Brian Richardson"), [CCC](/CCC "CCC"), February 16, 2003
- [IA-64 vs OOOE (attn Taylor, Hyatt)](https://www.stmintz.com/ccc/index.php?id=283740) by [Tom Kerrigan](/Tom_Kerrigan "Tom Kerrigan"), [CCC](/CCC "CCC"), February 11, 2003
- [Question: Itanium Info](https://www.stmintz.com/ccc/index.php?id=334345) by Slater Wold, [CCC](/CCC "CCC"), December 08, 2003

# External Links

- [Intel® Itanium® Processors](http://www.intel.com/content/www/us/en/processors/itanium/itanium-processor.html)
- [Itanium from Wikipedia](https://en.wikipedia.org/wiki/Itanium)
- [IA-64 from Wikipedia](https://en.wikipedia.org/wiki/IA-64)
- [List of Intel Itanium microprocessors from Wikipedia](https://en.wikipedia.org/wiki/List_of_Intel_Itanium_microprocessors)
- [How the Itanium Killed the Computer Industry](http://www.pcmag.com/article.aspx/curl/2339629) by [John C. Dvorak](http://www.pcmag.com/author-bio/john-c.-dvorak), [PCMag.com](https://en.wikipedia.org/wiki/PC_Magazine), January 26, 2009
- [Intel's Next Generation Itanium 'Kittson' IA64 Processor Detailed - 32nm Process, 9300/9500 Socket Compatible](http://wccftech.com/intel-itanium-kittson-ia64-processors-32nm/) by [Usman Pirzada](http://wccftech.com/author/usmanpirzada/), April 2015

# References

1. [↑](#cite_ref-1) [Intel's Next Generation Itanium 'Kittson' IA64 Processor Detailed - 32nm Process, 9300/9500 Socket Compatible](http://wccftech.com/intel-itanium-kittson-ia64-processors-32nm/) by [Usman Pirzada](http://wccftech.com/author/usmanpirzada/), April 2015
2. [↑](#cite_ref-2) [Intel names Merced chip Itanium - CNET News](https://archive.is/IUNih) by [Michael Kanellos](https://www.linkedin.com/pub/michael-kanellos/0/803/20b), [CNET News](https://en.wikipedia.org/wiki/CNET), October 4, 1999
3. [↑](#cite_ref-3) [Itanium from Wikipedia](https://en.wikipedia.org/wiki/Itanium)
4. [↑](#cite_ref-4) Diagram of the architecture of the Itanium (IA-64) 64-bit Intel microprocessor, Image by [Fred the Oyster](https://commons.wikimedia.org/wiki/User:Fred_the_Oyster), September 08, 2014, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [IA-64 from Wikipedia](https://en.wikipedia.org/wiki/IA-64), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)
5. [↑](#cite_ref-5) [Re: Deep-Fritz 18 on a 64 cpu itanium (intel not AMD) system](https://www.stmintz.com/ccc/index.php?id=277735) by [Eugene Nalimov](/Eugene_Nalimov "Eugene Nalimov"), [CCC](/CCC "CCC"), January 16, 2003
6. [↑](#cite_ref-6) [Re: Question: Itanium Info](https://www.stmintz.com/ccc/index.php?id=334348) by K. Burcham, [CCC](/CCC "CCC"), December 08, 2003
7. [↑](#cite_ref-7) [Itanium2 Testing Crafty & Tinker Informal Results](https://www.stmintz.com/ccc/index.php?id=284689) by [Brian Richardson](/Brian_Richardson "Brian Richardson"), [CCC](/CCC "CCC"), February 16, 2003
8. [↑](#cite_ref-8) [Re: Question: Itanium Info](https://www.stmintz.com/ccc/index.php?id=334474) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), December 09, 2003
9. [↑](#cite_ref-9) [Re: Will the Itanium have a BSF or BSR instruction?](https://www.stmintz.com/ccc/index.php?id=124712) by [Eugene Nalimov](/Eugene_Nalimov "Eugene Nalimov"), [CCC](/CCC "CCC"), August 16, 2000

**[Up one Level](/Hardware "Hardware")**