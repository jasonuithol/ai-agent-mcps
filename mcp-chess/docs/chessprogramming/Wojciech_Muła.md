# Wojciech Muła

Source: https://www.chessprogramming.org/Wojciech_Muła

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Wojciech Muła**

[![](/images/b/be/WojciechMu%C5%82a.jpg)](https://www.facebook.com/wojciech.mula)

Wojciech Muła [[1]](#cite_note-1)

**Wojciech Muła**,  
a Polish computer scientist and software developer educated from [Rzeszów University of Technology](https://en.wikipedia.org/wiki/Rzesz%C3%B3w_University_of_Technology) in [electrical engineering](https://en.wikipedia.org/wiki/Electrical_engineering) and [computer engineering](https://en.wikipedia.org/wiki/Computer_engineering) [[2]](#cite_note-2), with expertise in low level [programming](/Programming "Programming"), [bit-twiddling](/Bit-Twiddling "Bit-Twiddling") and [performance optimization](/Optimization "Optimization"), in particular [SIMD and SWAR techniques](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") applied to [string search](https://en.wikipedia.org/wiki/String_searching_algorithm), [population count](/Population_Count "Population Count"), [Base64](https://en.wikipedia.org/wiki/Base64) and various algorithms.
In 2008, Wojciech Muła introduced a [SSSE3 population count](/SSSE3#PopCount "SSSE3") based on a pair of [PSHUFB](/SSSE3#PSHUFB "SSSE3") 16 parallel [nibble](/Nibble "Nibble") in-xmm register lookups [[3]](#cite_note-3), in the meantime due to [AVX2](/AVX2 "AVX2") or [AVX-512](/AVX-512 "AVX-512") even possible with doubled or fourfold register widths, competing the native [x86-64](/X86-64 "X86-64") [popcount instruction](/X86-64#gpinstructions "X86-64") [[4]](#cite_note-4).
He is further contributor on the [Polish Wikipedia](https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna) [[5]](#cite_note-5).

# Selected Publications

[[6]](#cite_note-6)

- Wojciech Muła, [Nathan Kurz](https://dblp.uni-trier.de/pers/hd/k/Kurz:Nathan), [Daniel Lemire](https://github.com/lemire) (**2016**). *Faster Population Counts Using AVX2 Instructions*. [arXiv:1611.07612](https://arxiv.org/abs/1611.07612) [[7]](#cite_note-7)
- Wojciech Muła, [Daniel Lemire](https://github.com/lemire) (**2017**). *Faster Base64 Encoding and Decoding Using AVX2 Instructions*. [arXiv:1704.00605](https://arxiv.org/abs/1704.00605)

# Articles

[[8]](#cite_note-8)

- [SSSE3: fast popcount](http://0x80.pl/articles/sse-popcount.html) by Wojciech Muła, May 24, 2008 » [SSSE3 Population Count](/SSSE3#PopCount "SSSE3")
- [Speeding up bit-parallel population count](http://0x80.pl/articles/faster-popcount-for-large-data.html) by Wojciech Muła, April 13, 2015
- [AVX512: ternary functions evaluation](http://0x80.pl/articles/avx512-ternary-functions.html) by Wojciech Muła, March 03, 2015 » [AVX-512 VPTERNLOG](/AVX-512#VPTERNLOG "AVX-512")
- [GNU std::string::find is very slow](http://0x80.pl/notesen/2016-10-08-slow-std-string-find.html) by Wojciech Muła, October 08, 2016
- [Detecting bit patterns with series of zeros followed by ones](http://0x80.pl/notesen/2016-10-16-detecting-bit-pattern.html) by Wojciech Muła, October 16, 2016
- [SIMD-friendly algorithms for substring searching](http://0x80.pl/articles/simd-strfind.html) by Wojciech Muła, November 28, 2016
- [Population count using XOP instructions](http://0x80.pl/articles/xop-popcnt.html) by Wojciech Muła, December 16, 2016

# External Links

- [Wojciech Muła — strona domowa](http://0x80.pl/)
- [User:Wojciech mula](https://commons.wikimedia.org/wiki/User:Wojciech_mula) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
- [Wojciech Muła | Facebook](https://www.facebook.com/wojciech.mula)
- [Wojciech Muła | LinkedIn](https://www.linkedin.com/in/wojciech-mu%C5%82a-534856ab/)
- [Wojciech Muła (WojciechMula) - Libraries.io](https://libraries.io/github/WojciechMula)
- [WojciechMula (Wojciech Muła) · GitHub](https://github.com/WojciechMula)

:   [GitHub - WojciechMula/sse-popcount: SIMD (SSE) population count](https://github.com/WojciechMula/sse-popcount)

# References

1. [↑](#cite_ref-1) [Wojciech Muła | Facebook](https://www.facebook.com/wojciech.mula)
2. [↑](#cite_ref-2) [Wojciech Muła | LinkedIn](https://www.linkedin.com/in/wojciech-mu%C5%82a-534856ab/)
3. [↑](#cite_ref-3) [SSSE3: fast popcount](http://0x80.pl/articles/sse-popcount.html) by Wojciech Muła, May 24, 2008
4. [↑](#cite_ref-4) Wojciech Muła, [Nathan Kurz](https://dblp.uni-trier.de/pers/hd/k/Kurz:Nathan), [Daniel Lemire](https://github.com/lemire) (**2016**). *Faster Population Counts Using AVX2 Instructions*. [arXiv:1611.07612](https://arxiv.org/abs/1611.07612)
5. [↑](#cite_ref-5) [User:Wojciech mula](https://commons.wikimedia.org/wiki/User:Wojciech_mula) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
6. [↑](#cite_ref-6) [dblp: Wojciech Muła](https://dblp.uni-trier.de/pers/hd/m/Mula:Wojciech)
7. [↑](#cite_ref-7) see also [libpopcnt](/Kim_Walisch#PopCount "Kim Walisch") by [Kim Walisch](/Kim_Walisch "Kim Walisch")
8. [↑](#cite_ref-8) [Programming](http://0x80.pl/articles/) by Wojciech Muła

**[Up one Level](/People "People")**