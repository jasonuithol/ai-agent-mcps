# Files

Source: https://www.chessprogramming.org/Files

**[Home](/Main_Page "Main Page") \* [Chess](/Chess "Chess") \* Files**

*For disambiguation see also [Computer file](https://en.wikipedia.org/wiki/Computer_file)*

**Files** are the eight vertical lines or columns of a [Chessboard](/Chessboard "Chessboard"), labeled from 'A' to 'H', or 'a' to 'h'. Each file contains eight vertically arranged [Squares](/Squares "Squares") of alternating white and black, or light and dark [Color](/Color "Color").

# File Names

In a descriptive notation, files are also nominated by the [Pieces](/Pieces "Pieces") from their [initial position](/Initial_Position "Initial Position") (similar to [Pawns](/Pawn "Pawn")), like Rook-Files (a- and h-File, see diagram), Knight-Files (b- and g-File), Bishop-Files (c- and f-File), and Queen-File (d-File) and King-File (e-File), also called Center Files.

|  |  |  |
| --- | --- | --- |
|  | abcdefgh |  |
| 8 7 6 5 4 3 2 1 |                                          •      • •      • •      • •      • •      • •      • •      • •      • | 8 7 6 5 4 3 2 1 |
|  | abcdefgh |  |

# Square Mapping Notes

Whether the square difference of neighbored squares on a [rank](/Ranks "Ranks") or file is either 1 or 8, depends on the square mapping. We further rely on [little-endian rank-file mapping](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations"), which keeps consecutive [squares](/Squares "Squares") of a rank as neighbored elements in Memory (or register).

# Square Difference

Within a 0..63 square index range and the mentioned [square mapping](/Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") (a1 = 0), the difference of two neighbored squares on a File is **eight**.

# Enumeration

As mentioned, on a [Chessboard](/Chessboard "Chessboard") the eight files are labeled from 'A' to 'H'. To make them zero based indices as appropriate for [C](/C "C") like programming languages, we enumerate files from 0 to 7. [Little-endian](/Little-endian "Little-endian") file-mapping (as used here) assigns the A-File to index zero. Three bits are required to enumerate from 0 to 7.

A [little-endian](/Little-endian "Little-endian") file-mapping enumeration in [C++](/Cpp "Cpp") might look like this:

```
enum enumFile {
  efAFile = 0,
  efBFile = 1,
  efCFile = 2,
  efDFile = 3,
  efEFile = 4,
  efFFile = 5,
  efGFile = 6,
  efHFile = 7,
};
```

# File from Square

Rank-File mapping of squares keeps the file as the three lower bits of a Square index.

```
file = square & 7; // modulo 8
```

# File-Distance

The file-distance is the [absolute](/Avoiding_Branches#Abs "Avoiding Branches") difference between two files (their 0-7 indices). The maximum file-distance is 7.

```
fileDistance = abs (file1 - file2);
fileDistance = abs (file2 - file1);
```

# Two Squares on a File

Two [Squares](/Squares "Squares") are on the same File, if their file distance is zero. The masking of the file bits can be done after the subtraction.

```
bool squaresOnSameFile(int sq1, int sq2) {
 return ((sq2 - sq1) & 7) == 0;
}
```

The [Symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) aka xor is sufficent for the test as well [[1]](#cite_note-1)

```
bool squaresOnSameFile(int sq1, int sq2) {
 return ((sq1 ^ sq2) & 7) == 0;
}
```

- [Two Squares on a Rank](/Ranks#TwoSquares "Ranks")
- [Two Squares on a Diagonal](/Diagonals#TwoSquares "Diagonals")
- [Two Squares on a Anti-Diagonal](/Anti-Diagonals#TwoSquares "Anti-Diagonals")

# Pawns and Files

- [Half-open File](/Half-open_File "Half-open File")
- [Open File](/Open_File "Open File")
- [Pawns and Files (Bitboards)](/Pawns_and_Files_(Bitboards) "Pawns and Files (Bitboards)")

# See also

- [Ranks](/Ranks "Ranks")
- [Diagonals](/Diagonals "Diagonals")
- [Anti-Diagonals](/Anti-Diagonals "Anti-Diagonals")
- [Squares](/Squares "Squares")
- [Intersection Squares](/Intersection_Squares "Intersection Squares")

# References

1. [↑](#cite_ref-1) [An undetected bug for 10 years](http://talkchess.com/forum3/viewtopic.php?f=7&t=74821) by [Oliver Brausch](/Oliver_Brausch "Oliver Brausch"), [CCC](/CCC "CCC"), August 18, 2020

**[Up one Level](/Chess "Chess")**