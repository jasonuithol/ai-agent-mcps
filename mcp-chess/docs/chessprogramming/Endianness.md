# Endianness

Source: https://www.chessprogramming.org/Endianness

**[Home](/Main_Page "Main Page") \* [Programming](/Programming "Programming") \* [Data](/Data "Data") \* Endianness**

[![](/images/thumb/1/12/Endianess.jpg/300px-Endianess.jpg)](http://vadmyst.blogspot.com/2009/04/discovering-system-endianess.html)

[Little-](/Little-endian "Little-endian") and [Big-endian](/Big-endian "Big-endian") [[1]](#cite_note-1)

**Endianness** is about the order to concatenate sub-items to composite items with respect to reading and writing, or related, storing or transmitting such items, also referred to as [NUXI problem](http://catb.org/jargon/html/N/NUXI-problem.html). The related term [big-endian](/Big-endian "Big-endian") (as opposed to [little-endian](/Little-endian "Little-endian")) comes from [Jonathan Swift's](https://en.wikipedia.org/wiki/Jonathan_Swift) satirical novel [Gulliver’s Travels](https://en.wikipedia.org/wiki/Gulliver%27s_Travels), where tensions are described in [Lilliput and Blefuscu](https://en.wikipedia.org/wiki/Lilliput_and_Blefuscu): whereas royal edict in Lilliput requires cracking open one's [soft-boiled egg](https://en.wikipedia.org/wiki/Boiled_egg) at the small end, inhabitants of the rival kingdom of Blefuscu crack theirs at the big end [[2]](#cite_note-2) .

# Digits in Numbers

With endianness, we have to consider how we usually write text (letters of a word, word of a sentence) and numbers (left to right LTR, right to left RTL, top to bottom TTB, bottom to top BTT). Assuming [textflow](https://en.wikipedia.org/wiki/Bi-directional_text) is from left-to-right (LTR) and [Hindu-Arabic numeral system](https://en.wikipedia.org/wiki/Hindu-Arabic_numeral_system), we write numbers (decimal, as well as binary, octal and hexadecimal) [big-endian](/Big-endian "Big-endian") wise ("big end first") - that is, we write (or transmit) from most significant to least significant digit from left (first) to right (last).

# Numbers in Dates

That was about the endianness of digits in numbers, e.g. 1234 versus 4321. Assume we have three numbers representing a date, the year (two or four digits, yy or yyyy), the month of that year (1..12, mm) and the day of the month (1..31, dd). How do we concatenate the three sub-items?

With respect to the significance of the sub-items, we would use big-endian as well, the biggest item left (first), thus yyyy-mm-dd. Anyway, [Calendar dates](https://en.wikipedia.org/wiki/Calendar_date) are written quite differently in various countries and cultures, also with various separators.

- [Little-endian](/Little-endian "Little-endian"), dd-mm-yyyy common to the vast majority of the world's countries
- Middle-endian mm-dd-yyyy as used in the [United States](https://en.wikipedia.org/wiki/Calendar_date#mm.2Fdd.2Fyy_or_mm.2Fdd.2Fyyyy_.28month.2C_day.2C_year.29) and a few other [countries](https://en.wikipedia.org/wiki/Calendar_date#mm.2Fdd.2Fyy_or_mm.2Fdd.2Fyyyy_.28month.2C_day.2C_year.29), likely more desciptive with name of the month.
- [Big-endian](/Big-endian "Big-endian") yyyy-mm-dd as defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

One of the advantages of using the ISO 8601 big-endian standard date format is that when dates in this format are ordered by a standard [collation](https://en.wikipedia.org/wiki/Collation) by leading characters first, they are also in date order.

# Bytes in Words

How to store [bytes](/Byte "Byte") of a [word](/Word "Word") (or double- and quadword) in [memory](/Memory "Memory") (also called byte-order or byte-sex), where each byte has a unique address, was an disputed issue in the history of computers and micro-processors, especially [Intel](/Intel "Intel") (little-endian) versus [Motorola](/index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") (big-endian). The byte-order is also the primary meaning of endianness.

Big-endian associates the "first" (lower) address with the most significant byte (as we write the most significant digit first). Little-endian stores the least significant (or lower) byte at the lower byte-address of a word. While there are some advantages and disadvantages, endianness is a matter of convention and customization.

Still other architectures, generically called middle-endian or mixed-endian, may have a more complicated ordering; [PDP-11](/PDP-11 "PDP-11"), for instance, stored some 32-bit words, counting from the most significant, as: 2nd byte first, then 1st, then 4th, and finally 3rd.

As a useful side-effect for computerchess from that war of endianness [[3]](#cite_note-3) - almost every common processor has instructions to reverse the byte order of a word, a doubleword or a quadword inside a register, and there are applications to take advantage of that for a kind of reversed arithmetic, most notable as used inside the [Hyperbola Quintessence](/Hyperbola_Quintessence "Hyperbola Quintessence").

If we like to access the i-th byte of a quadword (e.g. a [Bitboard](/Bitboards "Bitboards")), the following code is not endian-independent:

```
U64 *p64 = ...;
BYTE *pbyte = (BYTE*) p64;
BYTE byte = *(pbyte+i-1); // pbyte[i-1] i = 1..8
```

Endian-independent code would look like this:

```
U64 *p64 = ...;
U64  quadword = *p64; // p64[0]
BYTE byte = (BYTE)(quadword >> (8*(i-1))); // i = 1..8
```

# Chessboard Endianness

The common notation to label [Squares](/Squares "Squares") on the [Chessboard](/Chessboard "Chessboard") is to write the file-coordinate at the big-end (left) and the rank-coordinate at the little-end, e.g. "a3" or "f7". Since both sets of labels use distinct sets of characters, the order doesn't matter that much, so even "3a" or "7f" would be sufficient, but not common. However, that is no longer the case if we enumerate bot items from one to eight, or more commonly for zero-based indices, from zero to seven as two octal-digits. Then we have to define the endianness of the square coordinates.

## Files versus Ranks

While this is still arbitrary and a matter of convention, more common is to have the file-coordinate at the little-end, nominated as Least Significant File (LSF) Mapping with following relations:

```
squareIndex = 8*rankIndex + fileIndex
rankIndex   = squareIndex div 8
fileIndex   = squareIndex mod 8
```

## Rank-Endianness

*Is the first rank the little-end or the big-end of the board?*

It don't cares, but it has to be defined and considered thoroughly the chess program's internal [Board Representation](/Board_Representation "Board Representation"). Likely the first rank is considered as little-end, since one is less eight - despite there is no arithmetical significance in the sense of numbers. But one may also argue Rank-Endianness depends on the White's or Black's point of view, and own base-rank is the perspective big-end.

While one mapping is as good as the other - with the same little-endian argument to order the bytes like their addresses, we define first rank with index 0 as little-endian rank-mapping, as used in in most of our code snippets, specially in [Bitboards](/Bitboards "Bitboards"). Big-endian rank-mapping is defined as index zero maps the eighth rank.

The [Forsyth-Edwards Notation](/Forsyth-Edwards_Notation "Forsyth-Edwards Notation") starts left with the big-end rank8 and may therefor considered big-endian. The advantage of big-endian ranks in LSF (Least Significant File) is, if printing a board rank by rank from top to bottom, the printed board appears in the typical and natural 2D bird's eye perspective of the white player.

## File-Endianness

*Is the A-File or the H-File the little-end of the board?*

Having the big-end left seems more natural, due to White's bird's eye perspective, having the A-File left, as well as the big-end digit in numbers. On the other hand, 'a' is less than 'h' in most character codes, and indeed we most often use little-endian file-mapping with the A-File addressed by index zero and the H-file addressed by index seven.

# See also

- [Big-endian](/Big-endian "Big-endian")
- [Little-endian](/Little-endian "Little-endian")
- [Square Mapping Considerations](/Square_Mapping_Considerations "Square Mapping Considerations")
- [Flipping Mirroring and Rotating](/Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")

# External Links

- [Endianness from Wikipedia](https://en.wikipedia.org/wiki/Endianness)
- [IEN 137 - DAV's Endian FAQ - On Holy Wars and a Plea for Peace](https://www.ietf.org/rfc/ien/ien137.txt) by [Danny Cohen](https://en.wikipedia.org/wiki/Danny_Cohen_(engineer)), [USC/ISI](https://en.wikipedia.org/wiki/Information_Sciences_Institute), April 1, 1980
- [Writing endian-independent code in C](https://developer.ibm.com/articles/au-endianc/) *Don't let endianness "byte" you* by Harsha Adiga, [IBM Developer](https://developer.ibm.com/), April 24, 2007

# References

1. [↑](#cite_ref-1) [Discovering System Endianess](http://vadmyst.blogspot.com/2009/04/discovering-system-endianess.html) from [Software Development Blog](http://vadmyst.blogspot.com/), April 27, 2009
2. [↑](#cite_ref-2) [Gulliver's Travels (Part I, Chapter IV) on Wikisource](http://en.wikisource.org/wiki/Gulliver%27s_Travels/Part_I/Chapter_IV)
3. [↑](#cite_ref-3) [IEN 137 - DAV's Endian FAQ - On Holy Wars and a Plea for Peace](https://www.ietf.org/rfc/ien/ien137.txt) by [Danny Cohen](https://en.wikipedia.org/wiki/Danny_Cohen_(engineer)), [USC/ISI](https://en.wikipedia.org/wiki/Information_Sciences_Institute), April 1, 1980

**[Up one Level](/Data "Data")**