# XOP

Source: https://www.chessprogramming.org/XOP

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* [x86](/X86 "X86") \* XOP**

**XOP**, (eXtended Operations)  
a [x86-64](/X86-64 "X86-64") [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction set extension by [AMD](/AMD "AMD") released with the [Bulldozer microarchitecture](https://en.wikipedia.org/wiki/Bulldozer_%28microarchitecture%29) which have the same functionality as the [SSE5](/SSE5 "SSE5") instruction set formerly proposed by AMD in August 2007, but with a revision of encoding in order to improve compatibility with [Intel's](/Intel "Intel") [AVX](/AVX "AVX") and the [VEX coding scheme](https://en.wikipedia.org/wiki/VEX_prefix).

The XOP instructions utilize a new three-byte XOP prefix preceding the opcode byte. This prefix replaces the use of the 0F, 66, F2 and F3 prefix bytes and the REX prefix and encodes additional information as well [[1]](#cite_note-1). XOP requires bit 11 in EXC set as returned by CPUID function EAX 80000001H.

# Instructions

## Integer Multiply, Add and Accumulate

XOP has a variety of [multiply, add and accumulate](https://en.wikipedia.org/wiki/Multiply-accumulate) instructions operate on and produce packed signed integer values. These instructions are certainly worthwhile for [evaluation](/Evaluation "Evaluation") purpose, for instance VPMACSSWW:

[![VPMACSWW.JPG](/images/3/30/VPMACSWW.JPG)](/File:VPMACSWW.JPG)

VPMACSSWW — Packed Multiply Accumulate Signed Word to Signed Word with Saturation

Since these instructions have the same performance as typical multiply instructions like PMULLW and PMADDWD and require the same execution resources, they effectively make the add step "free". The primary catch to using these instructions is latency; for example, the following sequence to sum a series of multiplies is extremely slow and will take 16 cycles:

| Instruction | Starting Cycle | Ending Cycle |
| --- | --- | --- |
| vpmacssww xmm0, xmm1, xmm2, xmm0 | 0 | 3 |
| vpmacssww xmm0, xmm3, xmm4, xmm0 | 4 | 7 |
| vpmacssww xmm0, xmm5, xmm6, xmm0 | 8 | 11 |
| vpmacssww xmm0, xmm7, xmm8, xmm0 | 12 | 15 |

Whereas the simple version, without XOP, will take just 8 cycles, albeit with more uops:

| Instruction | Starting Cycle | Ending Cycle |
| --- | --- | --- |
| pmullw xmm1, xmm2 | 0 | 3 |
| pmullw xmm3, xmm4 | 1 | 4 |
| pmullw xmm5, xmm6 | 2 | 5 |
| pmullw xmm7, xmm8 | 3 | 6 |
| paddsw xmm0, xmm1 | 1 | 2 |
| paddsw xmm0, xmm3 | 2 | 3 |
| paddsw xmm0, xmm5 | 3 | 4 |
| paddsw xmm0, xmm7 | 4 | 5 |

Multiple accumulators can help avoid this problem, as well as finding other ways to hide the latency.

## Horizontal Add and Subtract

XOP packed horizontal add and subtract signed integer instructions successively add adjacent pairs from the source XMM register and pack the (sign extended) integer result in the destination. For instance, VPHADDWQ can be used to continue the [dot product](https://en.wikipedia.org/wiki/Dot_product) from a previous Multiply, Add and Accumulate:

[![VPHADDWQ.JPG](/images/c/cc/VPHADDWQ.JPG)](/File:VPHADDWQ.JPG)

VPHADDWQ - Packed Horizontal Add Signed Word to Signed Quadword

While some of these instructions may at first appear to be less powerful than the existing [SSSE3](/SSSE3 "SSSE3") phaddw and psubhw, the latter tend to be rather slow in most implementations, while the XOP variants are all fast, single-uop instructions.

## Vector Conditional Moves

The Vector Conditional Moves (**VPCMOV**) instruction implements the [C](/C "C")/[C++](/Cpp "Cpp") language ternary ‘?’ operator at bit level on 128-bit XMM [[2]](#cite_note-2) or 256-bit YMM registers [[3]](#cite_note-3). VPCMOV has four XMM/YMM register operands:

```
 VPCMOV dest, src1, src2, selector
```

The 256-bit version executes following pseudo code in parallel:

```
for (int i = 0; i < 256; i++)
   dest[i] = selector[i] ? src1[i] : src2[i]
```

## Packed Permute Bytes

The Packed Permute Bytes (**VPPERM**) instruction can shuffle 16 bytes out of 32 bytes of input and perform a variety of operations on each byte [[4]](#cite_note-4). VPPERM has four XMM register operands:

```
 VPPERM dest, src1, src2, selector
```

For each of 16 destination [bytes](/Byte "Byte") the corresponding selector-byte addresses one of 32 input bytes (from src1, src2) and a logical operation including bit-reversal:

```
char src[32];   // src2:src1
char select[16];
char dest[16];
for (int i = 0; i < 16; i++) {
   char opera = select[i] >>> 5; // unsigned shift
   char idx32 = select[i] & 31;

   switch ( opera ) {
      case 0: dest[i] =  src[idx32]; break;
      case 1: dest[i] = ~src[idx32]; break;
      case 2: dest[i] =  bitreverse( src[idx32]); break;
      case 3: dest[i] = ~bitreverse( src[idx32]); break;
      case 4: dest[i] = 0x00; break;
      case 5: dest[i] = 0xFF; break;
      case 6: dest[i] =  src[idx32] >> 7;  break; // signed shift
      case 7: dest[i] = ~src[idx32] >> 7;  break; // signed shift
   }
}
```

The "bit reverse" operation is novel on x86 (some other architectures, like ARM, already have fast bit reverse instructions). This allows extremely fast [reversal](/Flipping_Mirroring_and_Rotating#Rotationby180degrees "Flipping Mirroring and Rotating") of [bitboards](/Bitboards "Bitboards"). Since VPPERM can simultaneously reverse bits and bytes, it can for instance reverse two bitboards in one run, even from different sources, which beside other applications makes [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence") work for all four lines.

## Generalized Shift and Rotate

XOP has general logical (unsigned) and arithmetical (signed) shifts and rotates on 128-bit XMM registers. Unlike the existing SSE shift instructions, the XOP variants allow each element of either a [byte](/Byte "Byte"), [word](/Word "Word"), [dword](/Double_Word "Double Word") and [qword](/Quad_Word "Quad Word") vector to be shifted/rotated by different amounts. If the count value is positive, bits are shifted/rotated to the left, otherwise right. All these new instructions require three operands:

```
 VPROT* dest, src, fixed-count
 VPROT* dest, src, variable-count-src
 VPSHL* dest, src, variable-count-src
 VPSHA* dest, src, variable-count-src
```

*\* either B,W,D, or Q*.

[![VPSHLB.JPG](/images/a/a9/VPSHLB.JPG)](/File:VPSHLB.JPG)

VPSHLB - 16 individual left or right shifts

### Applications

The bytewise shifts [[5]](#cite_note-5) allow horizontal [one step shifts](/General_Setwise_Operations#OneStepOnly "General Setwise Operations") of [bitboards](/Bitboards "Bitboards") without wraps over rank bounderies from A- to H-file or vice versa. While one bitboard (8 bytes) might be shifted left, the other one might be shifted right, for instance for white pawn attacks:

```
__m128i noEa_noWe_Attacks( __m128i wPawns {wp:wp} ) {
   const __m128i shifts(0x0101010101010101, 0xFFFFFFFFFFFFFFFF); /* +1,... , -1,... */
   b = _mm_shl_epi8(wPawns, shifts); /* east:west */
   b = _mm_slli_epi64 (b, 8); /* north */
   return b;
}
```

# See Also

- [AltiVec](/AltiVec "AltiVec")
- [AVX](/AVX "AVX")
- [AVX2](/AVX2 "AVX2")
- [AVX-512](/AVX-512 "AVX-512")
- [SIMD and SWAR Techniques](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [SSE](/SSE "SSE")
- [SSE2](/SSE2 "SSE2")
- [SSE3](/SSE3 "SSE3")
- [SSSE3](/SSSE3 "SSSE3")
- [SSE4](/SSE4 "SSE4")
- [SSE5](/SSE5 "SSE5")

# Manuals

- [Volume 6: 128-Bit and 256-Bit XOP, FMA4 and CVT16 Instructions](https://support.amd.com/techdocs/43479.pdf) (pdf)
- [Software Optimization Guide for AMD Family 15h Processors](https://support.amd.com/TechDocs/47414_15h_sw_opt_guide.pdf) (pdf)

# External Links

- [XOP instruction set from Wikipedia](https://en.wikipedia.org/wiki/XOP_instruction_set)
- [Stop the instruction set war](http://www.agner.org/optimize/blog/read.php?i=25) by [Agner Fog](http://www.agner.org/)
- [Population count using XOP instructions](http://0x80.pl/articles/xop-popcnt.html) by [Wojciech Muła](/Wojciech_Mu%C5%82a "Wojciech Muła"), December 16, 2016
- [XOP Intrinsics Added for Visual Studio 2010 SP1](http://msdn.microsoft.com/en-us/library/gg466493) from [MSDN Library](https://en.wikipedia.org/wiki/MSDN_Library)

# References

1. [↑](#cite_ref-1)  [Volume 6: 128-Bit and 256-Bit XOP, FMA4 and CVT16 Instructions](http://support.amd.com/us/Embedded_TechDocs/43479.pdf) (pdf)
2. [↑](#cite_ref-2) [\_mm\_cmov\_si128](http://msdn.microsoft.com/en-us/library/gg445132)
3. [↑](#cite_ref-3) [\_mm256\_cmov\_si256](http://msdn.microsoft.com/en-us/library/gg445173)
4. [↑](#cite_ref-4) [\_mm\_perm\_epi8](http://msdn.microsoft.com/en-us/library/gg466498)
5. [↑](#cite_ref-5) [\_mm\_shl\_epi8](http://msdn.microsoft.com/en-us/library/gg466458.aspx)

**[Up one Level](/X86 "X86")**