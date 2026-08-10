# SIMD Techniques

Source: https://www.chessprogramming.org/SIMD_Techniques

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* SIMD techniques**

[x86](/X86 "X86") [MMX](/MMX "MMX")- or [SSE2](/SSE2 "SSE2") [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")-instruction sets provide a **Packed Move Mask Byte**, pmovmskb-instruction [[1]](#cite_note-1), available in [C](/C "C")/[C++](/Cpp "Cpp") as [\_mm\_movemask\_epi](/SSE2#_mm_movemask_epi "SSE2") intrinsic, which moves the most-significant bits of each byte of a MMX- or XMM-register to the lowest 8 or 16 bits of a general purpose register. Thus, this instruction may be used to map [file](/Files "Files")- or [diagonal](/Diagonals "Diagonals") occupancies to consecutive [bits](/Bit "Bit").

# Bishop Attacks

For diagonals one may mask and compare byte-wise to get the occupancy to the sign-bits. With [SSE2](/SSE2 "SSE2") and 128-bit XMM-registers one may process both diagonal- and anti-diagonal-occupancies in one run:

```
u64 fillRightAttacks[8][64]; // [file][occupiedIndex]
__m128i xmmBmask[64]; // antidiagonal::diagonal -  masks

U64 bishopAttacksSSE2(U64 occ, unsigned int sq) {
   __m128 mocc;
   mocc = _mm_cvtsi64x_si128(occ);            // gp to xmm, 0:occ
   mocc = _mm_unpacklo_epi64(mocc, mocc);     // occupancy to both xmm-halfs, occ:occ
   mocc = _mm_and_si128 (mocc, xmmBmask[sq]); // mask diagonal and antidiagonal
   mocc = _mm_cmpeq_epi8(mocc, xmmBmask[sq]); // cmp bytewise equal, FF if set, 00 otherwise
   unsigned int o = _mm_movemask_epi(mocc);   // get the 16 sign bits
   return (xmmBmask[sq].m128i_u64[0] & fillRightAttacks[sq>>3][(o>>1)&63])
        | (xmmBmask[sq].m128i_u64[1] & fillRightAttacks[sq>>3][(o>>9)&63]);
}
```

This sample code uses a shared 4KByte fill right lookup similar to fillUpAttacks of [kindergarten bitboards](/Kindergarten_Bitboards "Kindergarten Bitboards"). Of course one may use distinct lookup tables similar to [rotated bitboards](/Rotated_Bitboards "Rotated Bitboards") indexed by square and occupied-state without the trailing mask ands.

# See also

- [CFish - AVX2 Attacks](/CFish#AVX2_Attacks "CFish")
- [SSSE3 Version](/SSSE3#SSSE3Version "SSSE3") of [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")
- [Fill Right with SSE2-instructions](/SSE2#EastAttacks "SSE2")
- [SSE2-Wrapper in C++](/SSE2#SSE2WrapperinCpp "SSE2")

# Forum Posts

- [Re: Kindergarten bitboards without multiplying](http://www.talkchess.com/forum/viewtopic.php?t=29296&start=4) by [Wylie Garvin](/index.php?title=Wylie_Garvin&action=edit&redlink=1 "Wylie Garvin (page does not exist)"), [CCC](/CCC "CCC"), August 08, 2009

# External Links

- [SIMD from Wikipedia](https://en.wikipedia.org/wiki/SIMD)
- [PMOVMSKB: Move Byte Mask (x86 Instruction Set Reference)](https://x86.puri.sm/html/file_module_x86_id_243.html)

# References

1. [↑](#cite_ref-1) [PMOVMSKB: Move Byte Mask (x86 Instruction Set Reference)](https://x86.puri.sm/html/file_module_x86_id_243.html)

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**