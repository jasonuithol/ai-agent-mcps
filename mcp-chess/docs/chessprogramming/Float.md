# Float

Source: https://www.chessprogramming.org/Float

**[Home](/Main_Page "Main Page") \* [Programming](/Programming "Programming") \* [Data](/Data "Data") \* Float**

**Float** is a 32-bit data type representing the [single precision floating-point format](https://en.wikipedia.org/wiki/Single_precision_floating-point_format), in [IEEE 754-1985](https://en.wikipedia.org/wiki/IEEE_754-1985) called single, in [IEEE 754-2008](https://en.wikipedia.org/wiki/IEEE_754-2008) the 32-bit base 2 format is officially referred to as binary32. Due to [normalization](https://en.wikipedia.org/wiki/Normal_number_%28computing%29) the true [significand](https://en.wikipedia.org/wiki/Significand) includes an implicit leading one bit unless the exponent is stored with all bits zeros (0x00) or ones (0xff) which are reserved for [Denormal numbers](https://en.wikipedia.org/wiki/Subnormal_numbers). Thus only 23 bits of the significand are stored but the total precision is 24 bits (≈7.225 decimal digits). [Exponent bias](https://en.wikipedia.org/wiki/Exponent_bias) is 0x7f.

# Format

[![Float example.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Float_example.svg/960px-Float_example.svg.png)](/File:Float_example.svg)

[Single precision floating-point format](https://en.wikipedia.org/wiki/Single_precision_floating-point_format)

# x86 Float Instruction Sets

Recent [x86](/X86 "X86") and [x86-64](/X86-64 "X86-64") processors provide [x87](https://en.wikipedia.org/wiki/X87), [SSE](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions) and [3DNow!](https://en.wikipedia.org/wiki/3DNow%21) ([AMD](/AMD "AMD") only, shared with [MMX](/MMX "MMX")/x87) floating point instruction sets. 3DNow! and SSE are [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instructions with vectors of two or four floats. Since SSE is not obligatory for x86-32, 32-bit operating systems rely on x87. x86-64 64-bit operating systems may use the faster SSE instructions, but so far only 64-bit compiler for 64-bit [Windows](/Windows "Windows") emit those instructions implicitly for floating point operations [[1]](#cite_note-1) . SSE instructions can be mixed with x87 or 3DNow! and are explicitly available through (inline) [Assembly](/Assembly "Assembly") or intrinsics of various [C](/C "C")-Compilers.

## Integer to Float Conversion

### X87

To convert a signed or unsigned integer to float, two x87 instructions are needed, FILD and FSTP working on the x87 floating point stack [[2]](#cite_note-2) .

**FILD**
The FILD instruction converts a signed-integer in memory to [double-extended-precision](https://en.wikipedia.org/wiki/Extended_precision) (80-bit) format and pushes the value onto the x87 register stack. The value can be a 16-bit, 32-bit, or 64- bit integer value. Signed values from memory can always be represented exactly in x87 registers without rounding.

**FSTP**
The FSTP instruction pops the x87 stack after copying the value. The instruction FSTP ST(0) is the same as popping the stack with no data transfer. If the specified destination is a single-precision or double-precision memory location, the instruction converts the value to the appropriate precision format. It does this by rounding the significand of the source value as specified by the rounding mode determined by the RC field of the x87 control word and then converting to the format of destination. It also converts the exponent to the width and bias of the destination format.

### SSE

**CVTDQ2PS**
Converts four packed signed doubleword integers in the source operand (second operand) to four packed single-precision floating-point values in the destination operand (first operand).

- Mnemonic: CVTDQ2PS xmm1, xmm2
- Intrinsic: [\_mm\_cvtepi32\_ps](http://msdn.microsoft.com/en-us/library/36bwxcx5.aspx)

**CVTPI2PS**
Converts two packed signed doubleword integers in the source operand (second operand) to two packed single-precision floating-point values in the destination operand (first operand).

- Mnemonic: CVTPI2PS xmm, mm
- Intrinsic: [\_mm\_cvtpd\_ps](http://msdn.microsoft.com/de-de/library/ae2ksssb.aspx)

### 3DNow!

**PI2FD**
Converts packed 32-bit integer values to packed floating-point, single-precision values

- Mnemonic: PI2FD mm1, mm2
- Intrinsic: [\_m\_pi2fd](http://msdn.microsoft.com/en-us/library/72a8t1hy.aspx)

# BitScan Purpose

Integer to Float conversion can be used as base 2 logarithm of a power of two value of a 32-bit signed or unsigned integer, which might even base of a 64-bit [bitscan](/BitScan "BitScan") [[3]](#cite_note-3) . The 23 lower significant bits are always zero, the exponent contains the biased bitindex:

| i | 2^i as hexstring | tofloat as hexstring | exponent - 127 |
| --- | --- | --- | --- |
| 0 | 0x00000001 | 0x3f800000 | 0 |
| 1 | 0x00000002 | 0x40000000 | 1 |
| 2 | 0x00000004 | 0x40800000 | 2 |
| 3 | 0x00000008 | 0x41000000 | 3 |
| 4 | 0x00000010 | 0x41800000 | 4 |
| 5 | 0x00000020 | 0x42000000 | 5 |
| 6 | 0x00000040 | 0x42800000 | 6 |
| 7 | 0x00000080 | 0x43000000 | 7 |
| 8 | 0x00000100 | 0x43800000 | 8 |
| 9 | 0x00000200 | 0x44000000 | 9 |
| 10 | 0x00000400 | 0x44800000 | 10 |
| 11 | 0x00000800 | 0x45000000 | 11 |
| 12 | 0x00001000 | 0x45800000 | 12 |
| 13 | 0x00002000 | 0x46000000 | 13 |
| 14 | 0x00004000 | 0x46800000 | 14 |
| 15 | 0x00008000 | 0x47000000 | 15 |
| 16 | 0x00010000 | 0x47800000 | 16 |
| 17 | 0x00020000 | 0x48000000 | 17 |
| 18 | 0x00040000 | 0x48800000 | 18 |
| 19 | 0x00080000 | 0x49000000 | 19 |
| 20 | 0x00100000 | 0x49800000 | 20 |
| 21 | 0x00200000 | 0x4a000000 | 21 |
| 22 | 0x00400000 | 0x4a800000 | 22 |
| 23 | 0x00800000 | 0x4b000000 | 23 |
| 24 | 0x01000000 | 0x4b800000 | 24 |
| 25 | 0x02000000 | 0x4c000000 | 25 |
| 26 | 0x04000000 | 0x4c800000 | 26 |
| 27 | 0x08000000 | 0x4d000000 | 27 |
| 28 | 0x10000000 | 0x4d800000 | 28 |
| 29 | 0x20000000 | 0x4e000000 | 29 |
| 30 | 0x40000000 | 0x4e800000 | 30 |
| 31 | 0x80000000 | 0x4f000000 | 31 |
| 31 | 0x80000000 | 0xcf000000 | 31 |

# See also

- [Double Word](/Double_Word "Double Word")
- [SSE](/SSE "SSE")
- [SSE2](/SSE2 "SSE2")
- [Double](/Double "Double")

# Publications

- [David Goldberg](/index.php?title=David_Goldberg&action=edit&redlink=1 "David Goldberg (page does not exist)") (**1991**). *What every computer scientist should know about floating-point arithmetic*. [ACM Computing Surveys](/ACM#Surveys "ACM"), [pdf](https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf)
- [Ward Douglas Maurer](/Ward_Douglas_Maurer "Ward Douglas Maurer") (**1996**). *[Relative Precision in the Inductive Assertion Method](http://www.researchgate.net/publication/221014653_Relative_Precision_in_the_Inductive_Assertion_Method)*. [WNAA 1996](http://www.informatik.uni-trier.de/~ley/db/conf/naa/wnaa1996.html) [[4]](#cite_note-4)
- [Jacek Mańdziuk](/Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Daniel Osman](/index.php?title=Daniel_Osman&action=edit&redlink=1 "Daniel Osman (page does not exist)") (**2004**). *Alpha-Beta Search Enhancements with a Real-Value Game-State Evaluation Function*. [ICGA Journal, Vol. 27, No. 1](/ICGA_Journal#27_1 "ICGA Journal"), [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICGA.pdf)
- [William W. Edmonson](http://www.ece.ncsu.edu/people.php/wwedmons), [Maarten H. van Emden](/Maarten_van_Emden "Maarten van Emden") (**2008**). *Interval Semantics for Standard Floating-Point Arithmetic*. [arXiv:0810.4196](https://arxiv.org/abs/0810.4196)

# Forum Posts

- [Re: Which is better, IYHO](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/cbd402de3b07b976/b31333d734e8a6cc) by [Ian Kennedy](/Ian_Kennedy "Ian Kennedy"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), August 20, 1995
- [Re: Floating point VS Integer Math](https://www.stmintz.com/ccc/index.php?id=18674) by [Bruce Moreland](/Bruce_Moreland "Bruce Moreland"), [CCC](/CCC "CCC"), May 14, 1998
- [Evaluation functions. Why integer?](http://www.talkchess.com/forum/viewtopic.php?t=22817) by oysteijo, [CCC](/CCC "CCC"), August 06, 2008 » [Evaluation](/Evaluation "Evaluation"), [Score](/Score "Score")
- [OT: denormals](http://www.talkchess.com/forum/viewtopic.php?t=44841) by [Martin Sedlak](/Martin_Sedlak "Martin Sedlak"), [CCC](/CCC "CCC"), August 19, 2012
- [floating point SSE eval](http://www.talkchess.com/forum/viewtopic.php?t=50472) by [Marco Belli](/Marco_Belli "Marco Belli"), [CCC](/CCC "CCC"), December 13, 2013 » [Evaluation](/Evaluation "Evaluation"), [Score](/Score "Score")
- [Google's bfloat for neural networks](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70504) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), April 16, 2019 » [Neural Networks](/Neural_Networks "Neural Networks")

# External Links

- [Floating point from Wikipedia](https://en.wikipedia.org/wiki/Floating_point)
- [Single precision floating-point format from Wikipedia](https://en.wikipedia.org/wiki/Single_precision_floating-point_format)
- [Half-precision floating-point format from Wikipedia](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
- [bfloat16 floating-point format from Wikipedia](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
- [Survey of Floating-Point Formats](http://www.mrob.com/pub/math/floatformats.html) by [Robert Munafo](http://www.mrob.com/pub/index.html)
- [About Floating Point Arithmetic](http://info.uptrend.ch/uptrend/page/display/numerische-probleme-mit-reals?v=54) from [Johanns Blog](/Johann_Joss#Blog "Johann Joss")

# References

1. [↑](#cite_ref-1) [Calling conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
2. [↑](#cite_ref-2) [AMD64 ArchitectureProgrammer’s Manual Volume 5: 64-Bit Media and x87 Floating-Point Instructions](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/26569.pdf)
3. [↑](#cite_ref-3) [Fast 3DNow! BitScan](https://www.stmintz.com/ccc/index.php?id=268305) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg") from [CCC](/Computer_Chess_Forums "Computer Chess Forums"), December 01, 2002
4. [↑](#cite_ref-4) [Floyd–Hoare logic from Wikipedia](https://en.wikipedia.org/wiki/Hoare_logic)

**[Up one Level](/Data "Data")**