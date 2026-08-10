# Java-Bitscan

Source: https://www.chessprogramming.org/Java-Bitscan

**[Home](/Main_Page "Main Page") \* [Board Representation](/Board_Representation "Board Representation") \* [Bitboards](/Bitboards "Bitboards") \* [BitScan](/BitScan "BitScan") \* Java-Bitscan**

[Java 1.5](/Java "Java") has [Long.numberOfTrailingZeros](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html#numberOfTrailingZeros(long)) which might be the preferred one for bitScanForward. [Long.numberOfLeadingZeros](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html#numberOfLeadingZeros(long)) is suited to replace bitScanReverse xor 63.

# Source Samples

Some ports from C-source:

```
    /**
     * @author Gerd Isenberg
     * @return index 0..63 of LS1B -1023 if passing zero
     * @param b a 64-bit word to bitscan
     */
    static public int bitScanForwardDbl(long b)
    {
        double x = (double)(b & - b);
        int exp = (int) (Double.doubleToLongBits(x) >>> 52);
        return (exp & 2047) - 1023;
    }
```

```
    /**
     * @author Matt Taylor
     * @return index 0..63
     * @param bb a 64-bit word to bitscan, should not be zero
     */
    static private final int[] foldedTable = {
     63,30, 3,32,59,14,11,33,
     60,24,50, 9,55,19,21,34,
     61,29, 2,53,51,23,41,18,
     56,28, 1,43,46,27, 0,35,
     62,31,58, 4, 5,49,54, 6,
     15,52,12,40, 7,42,45,16,
     25,57,48,13,10,39, 8,44,
     20,47,38,22,17,37,36,26,
    };

    static public int bitScanForwardMatt(long b) {
       b ^= (b - 1);
       int folded = ((int)b) ^ ((int)(b >>> 32));
       return foldedTable[(folded * 0x78291ACF) >>> 26];
    }
```

```
    /**
     * @author Charles E. Leiserson
     *         Harald Prokop
     *         Keith H. Randall
     * "Using de Bruijn Sequences to Index a 1 in a Computer Word"
     * @return index 0..63
     * @param bb a 64-bit word to bitscan, should not be zero
     */

    static private final long deBruijn = 0x03f79d71b4cb0a89L;
    static private final int[] magicTable = {
      0, 1,48, 2,57,49,28, 3,
     61,58,50,42,38,29,17, 4,
     62,55,59,36,53,51,43,22,
     45,39,33,30,24,18,12, 5,
     63,47,56,27,60,41,37,16,
     54,35,52,21,44,32,23,11,
     46,26,40,15,34,20,31,10,
     25,14,19, 9,13, 8, 7, 6,
    };

    static public int bitScanForwardDeBruijn64 (long b) {
       int idx = (int)(((b & -b) * deBruijn) >>> 58);
       return magicTable[idx];
    }
```

```
    /**
     * @author Gerd Isenberg
     * @return index 0..63 of MS1B -1023 if passing zero
     * @param bb a 64-bit word to bitscan
     */
    static public int bitScanReverse(long bb)
    {
        double x = (double)(bb & ~(bb >>> 32));
        int exp = (int) (Double.doubleToLongBits(x) >> 52);
        int sign = (exp >> 11) & 63; // 63 if < 0 else 0
        exp = (exp & 2047)-1023;
        return exp | sign;
    }
```

**[Up one Level](/BitScan "BitScan")**