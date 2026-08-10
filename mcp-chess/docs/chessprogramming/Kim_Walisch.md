# Kim Walisch

Source: https://www.chessprogramming.org/Kim_Walisch

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Kim Walisch**

**Kim Walisch**,  
a software engineer from Luxembourg, and avocational expert in [prime number](https://en.wikipedia.org/wiki/Prime_number) generation [[1]](#cite_note-1) [[2]](#cite_note-2), applying the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) [[3]](#cite_note-3). He is knowledgeable about processor architectures, [software optimization](/Optimization "Optimization") and [bit-twiddling](/Bit-Twiddling "Bit-Twiddling").

# Bitscan

In October 2012, Kim Walisch proposed an improved [bitscan routine](/BitScan#KimWalisch "BitScan"), multiplying the [De Bruijn Sequence](/De_Bruijn_Sequence "De Bruijn Sequence") with a 0-1 mask [separated](/General_Setwise_Operations#LS1BSeparation "General Setwise Operations") by the [least significant one bit](/General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") of a scanned integer or [bitboard](/Bitboards "Bitboards"). The mask separation is cheaper than the [bit isolation](/General_Setwise_Operations#LS1BIsolation "General Setwise Operations") due to the [x86](/X86 "X86") lea instruction, performing the decrement of a source register into another target register, not affecting processor flags. This is a 32-bit bitscan forward routine:

```
const int index32[32] = {
    0,  9,  1, 10, 13, 21,  2, 29, 
   11, 14, 16, 18, 22, 25,  3, 30,
    8, 12, 20, 28, 15, 17, 24,  7,
   19, 27, 23,  6, 26,  5,  4, 31
};

/**
 * bitScanForward
 * @author Kim Walisch (2012)
 * @param v 32-bit set
 * @precondition v != 0
 * @return index (0..31) of least significant one bit
 */
int bitScanForward(unsigned int v) {
   return index32[((v ^ (v - 1)) * 0x07C4ACDDU) >> 27];
}
```

# Population Count

Kim Walisch provides a header-only [C](/C "C")/[C++](/Cpp "Cpp") library for [counting the number of 1 bits](/Population_Count "Population Count") using specialized instructions of various processor architectures [[4]](#cite_note-4), performing algorithms as described by [Wojciech Muła](/Wojciech_Mu%C5%82a "Wojciech Muła") et al. [[5]](#cite_note-5).

# External Links

- [Referent Kim Walisch www.primzahlen.de](http://www.primzahlen.de/referenten/Kim_Walisch/index2.htm) (German)
- [kimwalisch (Kim Walisch) · GitHub](https://github.com/kimwalisch)

:   [GitHub - kimwalisch/libpopcnt: Fast C/C++ bit population count library](https://github.com/kimwalisch/libpopcnt) by Kim Walisch

# References

1. [↑](#cite_ref-1) [Referent Kim Walisch www.primzahlen.de](http://www.primzahlen.de/referenten/Kim_Walisch/index2.htm) (German)
2. [↑](#cite_ref-2) [Formula for primes from Wikipedia](https://en.wikipedia.org/wiki/Formula_for_primes)
3. [↑](#cite_ref-3) [GitHub - kimwalisch/primesieve: Fast C/C++ prime number generator](https://github.com/kimwalisch/primesieve)
4. [↑](#cite_ref-4) [GitHub - kimwalisch/libpopcnt: Fast C/C++ bit population count library](https://github.com/kimwalisch/libpopcnt)
5. [↑](#cite_ref-5) [Wojciech Muła](/Wojciech_Mu%C5%82a "Wojciech Muła"), [Nathan Kurz](https://dblp.uni-trier.de/pers/hd/k/Kurz:Nathan), [Daniel Lemire](https://github.com/lemire) (**2016**). *Faster Population Counts Using AVX2 Instructions*. [arXiv:1611.07612](https://arxiv.org/abs/1611.07612)

**[Up one level](/People "People")**