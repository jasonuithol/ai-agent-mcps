# Reverse Bitboards

Source: https://www.chessprogramming.org/Reverse_Bitboards

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [Sliding Piece Attacks](/Sliding_Piece_Attacks "Sliding Piece Attacks") \* Reverse Bitboards**

The idea of **Reverse Bitboards** was proposed by [Ryan Mack](/Ryan_Mack "Ryan Mack") in [2000](/Timeline#2000 "Timeline") while introducing his *Hyperbola Project*. It was based on the [x XOR (x - 2)](/Subtracting_a_Rook_from_a_Blocking_Piece#oxoro2r "Subtracting a Rook from a Blocking Piece") [bit-twiddling](/Bit-Twiddling "Bit-Twiddling") trick to generate attacks in [positive](/On_an_empty_Board#PositiveRays "On an empty Board") [ray-directions](/Rays#RayDirections "Rays") - and beside the usual [occupancy](/Occupancy "Occupancy") bitboard, to maintain a [reversed or 180 degree rotated](/Flipping_Mirroring_and_Rotating#Rotationby180degrees "Flipping Mirroring and Rotating") occupied bitboard to apply the trick for [negative](/On_an_empty_Board#NegativeRays "On an empty Board") ray-directions as well. It was intended to [traverse](/Bitboard_Serialization "Bitboard Serialization") reversed sets for move-generation, while re-reversion took place in the scalar, square centric world by [xor](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") 63 after [bitscan](/BitScan "BitScan"). Alternatively, for other purposes a [MMX](/MMX "MMX")-bitreversal routine was mentioned.

Ryan made an interesting and thought-provoking contribution. He introduced the predecessor of the [o^(o-2r)-trick](/Subtracting_a_Rook_from_a_Blocking_Piece#oxoro2r "Subtracting a Rook from a Blocking Piece"). With hindsight, the idea of keeping two reversed sets seemed not that successful as the author initially thought. However, [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence"), where fast vertical byteswap flipping is used on the fly to reverse diagonals and files, is somehow the resurrection of Ryan's ideas, vastly improved by [Aleks Peshkov's](/Aleks_Peshkov "Aleks Peshkov") [xor](/General_Setwise_Operations#ExclusiveOr "General Setwise Operations") wizardry. Aleks' [SSSE3 approach](/SSSE3#Peshkov "SSSE3") even relies on keeping reverse occupancies to further use only nine SIMD operations to generate bishop attacks.

---

# The Hyperbola Project - New Technologies

[[1]](#cite_note-1)
What follows here is merely a glimpse at the new advances in computer chess that the **Hyperbola Project** will include. The revolutionary design will generate enormous speed improvements, optimized specifically for the Pentium III processor's SIMD and [MMX](/MMX "MMX") enhancements. The downside is that the initial releases of **Hyperbola** will require a P-III system to operate. As the core engine is being written in [assembly](/Assembly "Assembly") code, it is very difficult to optimize for more than one chip at a time.

The past two years have yielded a serious look at the way computer chess programs operate today. The most significant problem with PC-oriented (non 64-bit) programs is the lack of speed associated with doing 64-bit arithmetic in a 32-bit environment.

MMX technology introduced some 64-bit operations to the Pentium family of microprocessors, which do increase performance noticeably, but not optimally. When using MMX, many operations still have to be completed in the old 32-bit system, which degrades the performance gain when the data has to be exchanged back and forth between the regular registers and the MMX registers.

The improvements shown below also address another significant bottleneck in chess programming: memory speeds. Despite the fact that **Hyperbola** is designed for systems with extremely fast memory (RDRAM), memory is still a bottleneck for some calculations, which require a very tight dependency chain. Since a memory read from the fastest (L1) cache has a latency of three clock cycles, the processor remains stalled in a tight dependency chain such as this, where no other calculations can be completed while the processor waits for the memory read to complete.

## Bitboard Design and Sliding Piece Attack Generation

Generating the attacks for [sliding pieces](/Sliding_Pieces "Sliding Pieces") proved to be a significant bottleneck in the early trials. For example, before generating legal moves for a position, the program must determine whether the king is in check. To do this, the program has to find the attacks of every type of piece from the king's square and check if an appropriate enemy piece resides there. Since this cannot be done while analyzing other moves, this is a huge slowdown under the current technology, which uses four sets of bitboards (three rotated) and several memory lookups to determine the correct attacks.

**Hyperbola's** design is quite different in this respect from other programs. **Hyperbola** introduces the concept of a reversed bitboard in place of three rotated bitboards, and TOTALLY eliminates the lookup tables in favor of simple calculations, all of which can be done in the 64-bit [MMX](/MMX "MMX") registers.

With the research still in progress on this topic, it is not clear as to exactly how much performance can be enhanced by this new technique, but it is clear that performance will be improved very significantly, especially with MMX hardware. Processors that are completely 64-bit, such as the [Intel](/Intel "Intel") [Itanium](/Itanium "Itanium"), will also be very much helped by this technique.

### Now, how do reverse bitboards help generate sliding piece attacks?

First, let's cover what has to be maintained by the program. There is the normal set of bitboards, all generated in the normal direction. And there is a single **reverse bitboard**, which roughly takes the place of the three rotated bitboards in most programs today. The **reverse bitboard** contains the same information as the forward bitboard which denotes all occupied squares, but it is in reverse, that is, bit x in the forward bitboard corresponds to bit 63-x in the **reverse bitboard**.

## What benefit comes from having a reversed bitboard in place of rotated bitboards?

- **Maintenance**

:   A single reversed bitboard is easier to maintain than one rotated bitboard, let alone three. This is because a table lookup is required to convert a bit from the forward format to most rotated formats. With the **reverse bitboard**, simply subtract the bit number from 63. Considering that only one of these bitboards has to be maintained instead of three, this issue is important.

- **The Calculations**

:   When taking account of memory latencies, calculating the piece attacks using the forward and **reverse bitboards** can be done significantly faster due to total independence on lookup tables and complex calculations. There are a few slight snags with the diagonal calculations, but they are minor.
:   The benefit of having the forward and **reverse bitboards** really shines in light of a very important bit manipulation trick: x XOR (x - 2) contains bits set to one, starting from the second bit, and stopping at the first bit of x that is one, but including it.
:   Now, if x is the bitboard of all occupied squares, and it is shifted to the right so that the square for which attacks are being calculated becomes bit zero, then XORing **x with (x - 2)** gives a mask of all squares attacked by the piece on the desired square, once the result is shifted back to the left. It does not include the piece that is making the attack, but it does include the first occupied square. This is exactly the result the lookup tables return!
:   The snags come from wraparound - that is, when the mask goes to the end of the file, rank, or diagonal... and keeps going where it shouldn't. This can be easily fixed in rank/file attacks by masking only the rank or file in question, but it is more complicated on diagonals.

### Where do the reverse bitboards come in?

The regular bitboard is fine for calculating any attacks that go in the positive direction from the starting square (by masking the rank, file, or diagonal), but the bit-manipulating trick won't work in the opposite direction. The solution is simple: calculate attacks in the opposite direction using a **reverse bitboard**, so that on that bitboard they extend in the positive direction and can be calculated as above.

The real problem comes in trying to combine the forward and **reverse bitboards** - there is just no simple way to un-reverse the bitboard. The technique to do the switch is not terribly cumbersome, but it certainly cannot be used in cases where only one set of attacks is being generated... the delay far outweighs the gain.

However, in **Hyperbola**, this delay can be managed for an overall gain. Though it is unclear whether these types of calculations will even be used in generating legal moves, due to an incremental move generator, the two bitboards can be scanned separately, converting the returns from the bitscans from reverse to forward (by subtracting from 63) instead of converting the entire bitboard.

A more pertinent issue arises with determining whether the king is in check, which is done before generating any legal moves. Possible ways to go about this include converting the **reverse bitboard**, which is probably not optimal, maintaining **reverse bitboards** for the sliding pieces of both colors, which is possible, and testing the individual squares on the bitboards both in forward and in reverse, which is nearly out of the question. In the newer chip architectures any unpredictable branches severely degrade performance, and the technique to avoid that is also slow because it can only be used on 32-bit registers.

The most viable option is to maintain four **reverse bitboards**, one for the bishops/queens and rooks/queens of each color. Updating them does not degrade performance because only one of the four must be updated for any move, or none at all, in addition to the regular updates.

With the extra **reverse bitboards**, it is now very easy to determine if the king is in check without any memory tables. First, calculate the attacks from the king's square for both types of sliding pieces, and simply AND them with the appropriate bitboards of enemy pieces. After that, OR all the results of the comparisons together, and take a single branch.

A possible shortcut exists here still. If the king is not in check, which is almost always the case, and all of the possible sliding piece lines are closed or empty, which is usually true, then the king cannot be checked by a sliding piece. The merit of this idea is questionable, but a more concrete idea is much more helpful. If the previously used sliding piece attack bitboards are saved and it is determined that none of the squares on those bitboards have changed in the bitboard of occupied pieces, then the bitboards can be used again and the calculations skipped. If this shortcut is used, then it might be more economical to reverse the bitboard(s) after calculating them and ignoring the additional **reverse bitboards**. That depends on the hit rate.

### How can the reverse bitboards be converted back to normal?

The fastest way to do this isn't a huge deal, but it cannot be run in parallel with other operations and does degrade performance if it is run too often. Suppose we have the lower 16 bits of a bitboard, x: FEDCBA9876543210.

1. Load the constant, k = 5555555555555555h
2. x = [(x shl 1) and k] or [(x and k) shr 1] EFCDAB8967452301
3. Load the constant, k = 3333333333333333h
4. x = [(x shl 2) and k] or [(x and k) shr 2] CDEF89AB45670123
5. Load the constant, k = 0F0F0F0F0F0F0F0Fh
6. x = [(x shl 4) and k] or [(x and k) shr 4] 89ABCDEF01234567
7. Now, due to the availability of a MMX shift instruction that operates on 16-bit words, the bytes can now be switched more easily
8. x = (x shlw 8) or (x shrw 8) 0123456789ABCDEF
9. And finally, the pshufw on the P-III reorganizes the words in a single instruction
10. x = x pshufw 00011011b

Since all of this arithmetic can be done in the MMX registers, it runs very much in parallel and can complete in a reasonable time frame on the P-III. If this algorithm were to be redesigned for P-II or PMMX architectures (without the pshufw) it would be a little slower since two more steps need to be completed. Trying to do this without 64-bit support would be extremely slow due to the extended-precision operands, despite that most of it could be done in parallel. (This algorithm is also in parallel, so it would probably take over twice as long.)

*Copyright © 2000 Ryan Mack*

---

# See also

- [Flipping Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
- [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence")
- [Move Generation in Thor's Hammer](/Thor%27s_Hammer#MoveGeneration "Thor's Hammer")
- [Praetorian](/Praetorian "Praetorian")
- [Subtracting a Rook from a Blocking Piece](/Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece")

# Forum Discussions

- [what do think about n xor (n-2) and 'reverse bitboards'?!](https://www.stmintz.com/ccc/index.php?id=177693) by Stefan, [CCC](/CCC "CCC"), July 01, 2001
- [Reversed vs. Rotated Bitboards](https://www.stmintz.com/ccc/index.php?id=210339) by [Sune Fischer](/Sune_Fischer "Sune Fischer"), [CCC](/CCC "CCC"), January 28, 2002
- [Reverse Bitboards](https://www.stmintz.com/ccc/index.php?id=276884) by [Sander de Zoete](/Sander_de_Zoete "Sander de Zoete"), [CCC](/CCC "CCC"), January 13, 2003

# References

1. [↑](#cite_ref-1) Copy of the no longer available site: *The Hyperbola Project - New Technologies*, Copyright © 2000 [Ryan Mack](/Ryan_Mack "Ryan Mack")

**[Up one Level](/Sliding_Piece_Attacks "Sliding Piece Attacks")**