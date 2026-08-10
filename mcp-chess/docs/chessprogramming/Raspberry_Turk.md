# Raspberry Turk

Source: https://www.chessprogramming.org/Raspberry_Turk

**[Home](/Main_Page "Main Page") \* [Dedicated Chess Computers](/Dedicated_Chess_Computers "Dedicated Chess Computers") \* Raspberry Turk**

[![](/images/thumb/e/e5/RaspberryTurkTable.jpg/300px-RaspberryTurkTable.jpg)](http://www.raspberryturk.com/details/table.html)

Raspberry Turk Table [[1]](#cite_note-1)

**Raspberry Turk**,  
a [chess playing robot](/Robots#Turk "Robots") developed and build by [Joey Meyer](/index.php?title=Joey_Meyer&action=edit&redlink=1 "Joey Meyer (page does not exist)") as sophisticated [DIY](https://en.wikipedia.org/wiki/Do_it_yourself) project, inspired by the 18th century chess playing [The Turk](https://en.wikipedia.org/wiki/The_Turk). It is programmed almost entirely in [Python](/Python "Python") to run on a [Raspberry Pi](/Raspberry_Pi "Raspberry Pi") incorporating aspects of [computer vision](https://en.wikipedia.org/wiki/Computer_vision), [data science](https://en.wikipedia.org/wiki/Data_science), [machine learning](/Learning "Learning"), [robotics](https://en.wikipedia.org/wiki/Robotics), and [3D printing](https://en.wikipedia.org/wiki/3D_printing), so far using [Stockfish](/Stockfish "Stockfish") as its chess eingine with a fixed time control of one second per move [[2]](#cite_note-2). Raspberry Turk's [open-source software](https://en.wikipedia.org/wiki/Open-source_software) is available under the [MIT license](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"), first published on [GitHub](https://en.wikipedia.org/wiki/GitHub) in March 2017 [[3]](#cite_note-3).

# Chess Table

The [chessboard](/Chessboard "Chessboard") is placed or painted on a table with the mounted [actuator](https://en.wikipedia.org/wiki/Actuator) and [sensor](https://en.wikipedia.org/wiki/Sensor). Red and Green colored [pieces](/Pieces "Pieces") were used for better [piece and move recognition](/Piece_Recognition "Piece Recognition") using a [camera module](https://en.wikipedia.org/wiki/Camera_module) [[4]](#cite_note-4) placed above the board [[5]](#cite_note-5). The pieces incorporate small [metal](https://en.wikipedia.org/wiki/Metal) [dowels](https://en.wikipedia.org/wiki/Dowel) on top, so that a [electromagnet](https://en.wikipedia.org/wiki/Electromagnet) of a three [servo](https://en.wikipedia.org/wiki/Servo_control) controlled [Selective Compliance Articulated Robot Arm (SCARA)](https://en.wikipedia.org/wiki/SCARA) can lift and move them [[6]](#cite_note-6).

# Game Loop

After initializing the starting position with [side to move](/Side_to_move "Side to move"), the [game loop](/Chess_Game#GameLoop "Chess Game") basically switches between waiting for the opponent [entering](/Entering_Moves "Entering Moves") a move by comparing [480x480px images](https://en.wikipedia.org/wiki/Display_resolution) of the board, and calculating and making the Turk's moves using the robot arm.

# See also

- [Kempelen](/Kempelen "Kempelen")
- [Mr. Turk](/Mr._Turk "Mr. Turk")
- [The Turk](/The_Turk "The Turk") by [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") and [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns")
- [The Turk](/The_Turk_(TR) "The Turk (TR)") by [Yakup İpek](/Yakup_%C4%B0pek "Yakup İpek")

# Forum Posts

- [A modern Turk](http://www.talkchess.com/forum/viewtopic.php?t=63612) by Horacio Montenegro, [CCC](/CCC "CCC"), April 01, 2017

# External Links

- [Raspberry Turk](http://www.raspberryturk.com/)
- [GitHub - joeymeyer/raspberryturk: The Raspberry Turk is a robot that can play chess](https://github.com/joeymeyer/raspberryturk)
- Chess Playing Robot Powered by [Raspberry Pi](/Raspberry_Pi#Turk "Raspberry Pi") - Raspberry Turk by [Joey Meyer](/index.php?title=Joey_Meyer&action=edit&redlink=1 "Joey Meyer (page does not exist)"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Raspberry Turk - Table](http://www.raspberryturk.com/details/table.html)
2. [↑](#cite_ref-2) [Raspberry Turk - Chess Engine](http://www.raspberryturk.com/details/ai.html)
3. [↑](#cite_ref-3) [GitHub - joeymeyer/raspberryturk: The Raspberry Turk is a robot that can play chess](https://github.com/joeymeyer/raspberryturk)
4. [↑](#cite_ref-4) [Camera Module - Raspberry Pi](https://www.raspberrypi.org/products/camera-module/)
5. [↑](#cite_ref-5) [Raspberry Turk - Vision](http://www.raspberryturk.com/details/vision.html)
6. [↑](#cite_ref-6) [Raspberry Turk - The Arm](http://www.raspberryturk.com/details/arm.html)

**[Up one level](/Dedicated_Chess_Computers "Dedicated Chess Computers")**