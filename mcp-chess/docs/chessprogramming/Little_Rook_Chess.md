# Little Rook Chess

Source: https://www.chessprogramming.org/Little_Rook_Chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Little Rook Chess**

[![](/images/thumb/e/ef/Dogm128_shield_chess.jpg/300px-Dogm128_shield_chess.jpg)](https://github.com/olikraus/u8glib/wiki/little_rook_chess)

Little Rook Chess [[1]](#cite_note-1) with DOGM128 (128x64 dots) [[2]](#cite_note-2)

**Little Rook Chess**,  
a small [dedicated](/Dedicated_Chess_Computers "Dedicated Chess Computers") [open source chess program](/Category:Open_Source "Category:Open Source") by [Oliver Kraus](/Oliver_Kraus "Oliver Kraus"),
written in [C](/C "C"), developed to run on an [Arduino Uno](/Arduino#UNO "Arduino") with 32 KiB of [Flash memory](https://en.wikipedia.org/wiki/Flash_memory)
and only 2 KiB of [RAM](/Memory#RAM "Memory"). As a demonstration project how to use Oliver's *u8glib*,
the universal graphics library (monochrom [OLEDs](https://en.wikipedia.org/wiki/OLED) and [GLCDs](https://en.wikipedia.org/wiki/Liquid-crystal_display)) for [embedded systems](https://en.wikipedia.org/wiki/Embedded_system)
[[3]](#cite_note-3),
the focus is on implementing the dedicated [user interface](/User_Interface "User Interface") realized with an *Electronic Assembly DOG [LCD module](https://en.wikipedia.org/wiki/Liquid-crystal_display)*
[[4]](#cite_note-4)
and button shield. Little Rook Chess is part of *u8glib* under the terms of the [new bsd license](https://en.wikipedia.org/wiki/BSD_licenses)
[[5]](#cite_note-5).

# Chess AI

The "chess AI" of Little Rook Chess is rather rudimentary so far, with pure [minimax](/Minimax "Minimax") rather than [alpha-beta](/Alpha-Beta "Alpha-Beta").
The [evaluation](/Evaluation "Evaluation") is based on [material](/Material "Material") with [point values](/Point_Value "Point Value") of {1, 3, 3, 5, 9} and has a few positional terms.
The program keeps an [8x8 board](/8x8_Board "8x8 Board") [array](/Array "Array"), but uses [0x88](/0x88 "0x88") coordinates to validate square indices,
and always [transforms](/0x88#Transformation "0x88") those coordinates at each board access [[6]](#cite_note-6). Little Rook Chess lacks [minor promotions](/Promotions#MinorPromotion "Promotions") and is unaware of [repetitions](/Repetitions "Repetitions") and the [50-move rule](/Fifty-move_Rule "Fifty-move Rule"), but otherwise plays legal chess with [castling](/Castling "Castling") and [en passant](/En_passant "En passant") implemented [[7]](#cite_note-7).

# See also

- [Arduino](/Arduino "Arduino")
- [Micro-Max](/Micro-Max "Micro-Max")

# External Links

- [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)
- [u8glib/chessengine.c at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/csrc/chessengine.c)

# References

1. [↑](#cite_ref-1) Image from [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)
2. [↑](#cite_ref-2) [dogm128e.pdf](http://www.lcd-module.com/eng/pdf/grafik/dogm128e.pdf) by *Electronic Assembly*
3. [↑](#cite_ref-3) [olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki)
4. [↑](#cite_ref-4) [Chip-On-Glass DOG Displays from Electronic Assembly, Display Visions](https://www.lcd-module.com/produkte/dog.html)
5. [↑](#cite_ref-5) [u8glib/license.txt at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/license.txt)
6. [↑](#cite_ref-6) [u8glib/chessengine.c at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/csrc/chessengine.c)
7. [↑](#cite_ref-7) [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)

**[Up one Level](/Engines "Engines")**