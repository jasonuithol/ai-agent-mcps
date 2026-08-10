# Sensor Chess

Source: https://www.chessprogramming.org/Sensor_Chess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Sensor Chess**

[![](/images/thumb/c/c5/SensorChess.JPG/300px-SensorChess.JPG)](/File:SensorChess.JPG)

SciSys Sensor Chess with Strong Play Module [[1]](#cite_note-1)

**Sensor Chess**, (SciSys Sensor Chess)  
a [dedicated chess computer](/Dedicated_Chess_Computers "Dedicated Chess Computers") manufactured by [SciSys](/Saitek "Saitek") with [Sensory Board](/Sensory_Board "Sensory Board") and [6502](/6502 "6502") processor at 2 MHz, released in 1981. The program was [Julio Kaplan's](/Julio_Kaplan "Julio Kaplan") **first** program for SciSys, persistent in a 4 KiB [ROM](/Memory#ROM "Memory"), using only 256 byte of [RAM](/Memory#RAM "Memory"). The computer, expandable by modules such as the *Strong Play Module*, the *Super Classical Modul*, and the *Super Hypermodern Module*, was endorsed by [FIDE](/FIDE "FIDE").

# Move Generation

How to [generate moves](/Move_Generation "Move Generation") with 256 bytes RAM or less? Clearly, generation in chunks with [move lists](/Move_List "Move List") for each [ply](/Ply "Ply") is not possible. One idea is to use the last move generated of each ply (if any), which needs to be saved on the ply [stack](/Stack "Stack") for [unmake](/Unmake_Move "Unmake Move") anyway, as state of the generator, which implies [target square](/Target_Square "Target Square"), [source square](/Origin_Square "Origin Square") and [direction](/Direction "Direction"), and with the help of the [board array](/8x8_Board "8x8 Board") or [piece list](/Piece-Lists "Piece-Lists"), the possible [captured piece](/Captures "Captures"), and the moving piece. One may consider one [killer](/Killer_Move "Killer Move") or [PV-move](/PV-Move "PV-Move") and [MVV-LVA](/MVV-LVA "MVV-LVA") for reasonable [move ordering](/Move_Ordering "Move Ordering"), to otherwise use nested loops over target pieces/squares, directions, and source squares and pieces until the next move is found or no more are available.

# See also

- [President Chess](/President_Chess "President Chess")
- [Superstar](/Superstar "Superstar")

# External Links

- [Sensor Chess](http://www.chesscomputeruk.com/html/sensor_chess.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](/Mike_Watters "Mike Watters")
- [SciSys - Strong Play (Sensor Chess module)](http://www.schaakcomputers.nl/hein_veldhuis/database/files/10-1981%20%5BE-4301%5D%20SciSys%20-%20Strong%20Play%20%28Sensor%20Chess%20module%29.pdf) (pdf) by [Hein Veldhuis](/Hein_Veldhuis "Hein Veldhuis")
- [SciSys Sensor Chess](http://www.schach-computer.info/wiki/index.php/SciSys_Sensor_Chess) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)

# References

1. [↑](#cite_ref-1) Image from [SciSys - Strong Play (Sensor Chess module)](http://www.schaakcomputers.nl/hein_veldhuis/database/files/10-1981%20%5BE-4301%5D%20SciSys%20-%20Strong%20Play%20%28Sensor%20Chess%20module%29.pdf) (pdf) by [Hein Veldhuis](/Hein_Veldhuis "Hein Veldhuis")

**[Up one level](/Engines "Engines")**