# Arduino

Source: https://www.chessprogramming.org/Arduino

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* Arduino**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Arduino_Mega.jpg/330px-Arduino_Mega.jpg)](/File:Arduino_Mega.jpg)

Arduino Mega [[1]](#cite_note-1)

**Arduino**, (due to a legal dispute, since 2015 it is known as **Genuino** outside the [United States](https://en.wikipedia.org/wiki/United_States) [[2]](#cite_note-2))  
a family of [open-source hardware](https://en.wikipedia.org/wiki/Open-source_hardware) [single-board microcontrollers](https://en.wikipedia.org/wiki/Single-board_microcontroller) based on the [Atmel](https://en.wikipedia.org/wiki/Atmel) 8-bit [AVR](https://en.wikipedia.org/wiki/Atmel_AVR) [RISC](https://en.wikipedia.org/wiki/Reduced_instruction_set_computing) chips [[3]](#cite_note-3) . An important aspect of the Arduino is the standard way that connectors are exposed, allowing the CPU board to be connected to a variety of interchangeable add-on modules known as shields [[4]](#cite_note-4) . Some shields communicate with the Arduino board directly over various pins, but many shields are individually addressable via an [I²C](https://en.wikipedia.org/wiki/I%C2%B2C) [serial](https://en.wikipedia.org/wiki/Serial_communication) [bus](https://en.wikipedia.org/wiki/Bus_%28computing%29), allowing many shields to be stacked and used in parallel [[5]](#cite_note-5) .

This page focuses on two boards with concrete computer chess applications.

# Arduino Uno

The **Arduino Uno** is based on the 8-bit [ATmega328](https://en.wikipedia.org/wiki/ATmega328) running at 16 MHz with 32 KiB [ISP](https://en.wikipedia.org/wiki/In-system_programming) [Flash memory](https://en.wikipedia.org/wiki/Flash_memory) with read-while-write capabilities, 1 KiB [EEPROM](/Memory#ROM "Memory"), and 2 KiB [SRAM](/Memory#RAM "Memory"). It has 14 digital input/output pins and six [analog inputs](https://en.wikipedia.org/wiki/Analog-to-digital_converter) and [USB connection](https://en.wikipedia.org/wiki/USB).

# Arduino Mega

The 2009 released **Arduino Mega** uses the 8-bit ATmega1280 [[6]](#cite_note-6) , also running at 16 MHz, but with 128 KiB of Flash memory which 4 KiB used by [bootloader](https://en.wikipedia.org/wiki/Booting), 8 KiB SRAM, and 4 KiB EEPROM. Arduino Mega has 54 digital input/output pins, 16 analog inputs, 4 [UARTs](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver/transmitter), and USB connection. Its 2010 successor, the **Arduino Mega 2560** [[7]](#cite_note-7) features the more advanced ATmega2560 [[8]](#cite_note-8) with 256 KiB Flash memory.

# Development

Arduino provides an [integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment) running on a host computer, supporting the [C](/C "C")/[C++](/Cpp "Cpp") based Arduino language [[9]](#cite_note-9) . Software written using Arduino language are called sketches, and undergoes minor changes like automatic generation of function prototypes during the build process, and then passed directly to a [C/C++ compiler](https://en.wikipedia.org/wiki/GNU_Compiler_Collection). All standard C and C++ constructs supported by AVR-g++ should work in Arduino. Alternatively, one may compile programs for the Arduino using AVR development tools, which requires configuration to link against the appropriate files in the Arduino core libraries [[10]](#cite_note-10) .

# Computer Chess

Arduino controllers are suitable to build a [dedicated chess computer](/Dedicated_Chess_Computers "Dedicated Chess Computers") - to control a self-made [sensory board](/Sensory_Board "Sensory Board") [[11]](#cite_note-11), or even to run small chess programs.

## Chess Programs

[Micro-Max](/Micro-Max "Micro-Max") by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") was aleady ported for the [Atmel](https://en.wikipedia.org/wiki/Atmel)-[ATmega88](https://en.wikipedia.org/wiki/ATmega88) by [Andre Adrian](/Andre_Adrian "Andre Adrian") [[12]](#cite_note-12) , and is also available as *ATM18 mini chess computer* [[13]](#cite_note-13) from the electronics magazine [Elektor](https://en.wikipedia.org/wiki/Elektor). [Óscar Toledo Gutiérrez'](/%C3%93scar_Toledo_Guti%C3%A9rrez "Óscar Toledo Gutiérrez") program [Toledo Nanochess](/Toledo "Toledo") seems appropriate for the Arduino boards as well [[14]](#cite_note-14) . Otherwise, for **Uno** and **Mega**, there are some more chess programs available, dedicated and [emulated](https://en.wikipedia.org/wiki/Emulator).

### Little Rook Chess

[Little Rook Chess](/Little_Rook_Chess "Little Rook Chess") by [Oliver Kraus](/Oliver_Kraus "Oliver Kraus") is a chess game for using the Arduino **Uno** with a dedicated [user interface](/User_Interface "User Interface") realized with an Electronic Assembly DOG [LCD module](https://en.wikipedia.org/wiki/Liquid-crystal_display) [[15]](#cite_note-15) and button shield. Little Rook Chess is part of the *u8glib library* (Universal 8bit Graphics Library) [[16]](#cite_note-16) under the terms of the [new bsd license](https://en.wikipedia.org/wiki/BSD_licenses) [[17]](#cite_note-17).

### MicroChess

*Obsolescence Guaranteed* [[18]](#cite_note-18) has ported the original [6502](/6502 "6502") [MicroChess](/MicroChess "MicroChess"), wrapped in a 6502 emulator, to the Arduino [[19]](#cite_note-19). A further development is the *KIM Uno* [[20]](#cite_note-20), a calculator-sized [KIM-1](/KIM-1 "KIM-1") replica with MicroChess built in. Both projects are open source software/hardware using the MicroChess source code (which is available but not open source) with permission from [Peter Jennings](/Peter_Jennings "Peter Jennings").

### Myopic

[Myopic](/Myopic "Myopic") by [Steven Edwards](/Steven_Edwards "Steven Edwards") is suited for the Arduino **Mega**, written in [C++](/Cpp "Cpp") and released under the [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license) [[21]](#cite_note-21) .

## Chess Robot

The [Arduino Due Chess Robot](/Robots#CRAP "Robots") is a self build [sensory board](/Sensory_Board "Sensory Board") with robot arm by [Chris Quayle](/index.php?title=Chris_Quayle&action=edit&redlink=1 "Chris Quayle (page does not exist)") as a hobby project - powered by an Arduino **Due** and incorporating [Micro-Max](/Micro-Max "Micro-Max") by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") as chess AI.

## Square Off

[Square Off](/index.php?title=Square_Off&action=edit&redlink=1 "Square Off (page does not exist)"), the [dedicated](/Dedicated_Chess_Computers "Dedicated Chess Computers") [robot](/Robots "Robots") [sensory board](/Sensory_Board "Sensory Board") features an [Arduino Mega](#MEGA) with [ATmega 2560](https://en.wikipedia.org/wiki/Atmel_AVR) chip to control the piece moving two axis [robotic arm](https://en.wikipedia.org/wiki/Robotic_arm), to detect piece movement, and to communicate with a [smartphone](https://en.wikipedia.org/wiki/Smartphone) via [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth) [[22]](#cite_note-22).

## ArdEBoard

The [ArdEBoard](/index.php?title=ArdEBoard&action=edit&redlink=1 "ArdEBoard (page does not exist)") by [Dominik Klein](/Dominik_Klein "Dominik Klein") [[23]](#cite_note-23) is a [sensory chess board](/Sensory_Board "Sensory Board") based on [reed switches](https://en.wikipedia.org/wiki/Reed_switch) and [magnets](https://en.wikipedia.org/wiki/Magnet) glued below every [chess piece](/Pieces "Pieces"). Source code for an [ATmega32U4](https://en.wikipedia.org/wiki/AVR_microcontrollers) to control the board is freely available at [GitHub](https://en.wikipedia.org/wiki/GitHub) [[24]](#cite_note-24).

## Analog Evaluation

Reading the 10-bit [analog-to-digital converter](https://en.wikipedia.org/wiki/Analog-to-digital_converter), adequately supplied by a [score](/Score "Score") voltage of a [noisy](https://en.wikipedia.org/wiki/Noise_%28electronics%29) [analog](/Analog_Evaluation "Analog Evaluation") [leaf evaluation](/Evaluation "Evaluation") with some discrete [analog circuits](https://en.wikipedia.org/wiki/Analogue_electronics) and [op-amps](https://en.wikipedia.org/wiki/Operational_amplifier) takes about 100 microseconds and is likely too slow for that interesting application [[25]](#cite_note-25) .

# See also

- [Dedicated Chess Computers](/Dedicated_Chess_Computers "Dedicated Chess Computers")
- [PIC Microcontroller](/PIC_Microcontroller "PIC Microcontroller")
- [Raspberry Pi](/Raspberry_Pi "Raspberry Pi")
- [Sensory Board](/Sensory_Board "Sensory Board")
- [UDOO](/UDOO "UDOO")

# Forum Posts

## 2005 ...

- [Arduino on Linux](http://forum.arduino.cc/index.php/topic,47769.0.html) by erich, [Arduino Forum](http://forum.arduino.cc/), October 11, 2005
- [Chess for the Arduino](http://forum.arduino.cc/index.php?topic=8330.0) by [chessplayer](/Steven_Edwards "Steven Edwards"), [Arduino Forum](http://forum.arduino.cc/), December 06, 2009 » [Myopic](/Myopic "Myopic")

## 2010 ...

- [Myopic, a new Creative Commons chess program](http://www.talkchess.com/forum/viewtopic.php?t=34445) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), May 22, 2010 » [Myopic](/Myopic "Myopic")
- [Nanochess auf avr](http://www.mikrocontroller.net/topic/208206) by Sam, [Mikrocontroller.net GCC Forum](http://www.mikrocontroller.net/forum/gcc), February 11, 2011 (German)
- [Re: Graphic LCD shield with EA DOGS102W display](http://forum.arduino.cc/index.php?PHPSESSID=648umgfcdcm48s18muh43kb731&topic=50524.msg468770#msg468770) by [Oliver Kraus](/Oliver_Kraus "Oliver Kraus"), [Arduino Forum](http://forum.arduino.cc/), June 18, 2011
- [My Arduino-Based 6502 Simulation/Emulation...thing?](http://forum.6502.org/viewtopic.php?f=8&t=2343) by halkun, [6502.org Forum](http://forum.6502.org/), November 26, 2012
- [KIM Uno: a KIM-1 emulator on an Arduino Uno](http://www.vintage-computer.com/vcforum/showthread.php?43229-KIM-Uno-a-KIM-1-emulator-on-an-Arduino-Uno) by Oscar, [Vintage Computer Forum](http://www.vintage-computer.com/vcforum/forum.php?s=95696db15561250b61c9f1ac4b458693), June 21, 2014
- [Poll: Arduino Uno Tournament](http://www.talkchess.com/forum/viewtopic.php?t=53305) by David Eather, [CCC](/CCC "CCC"), August 15, 2014
- [Chess Mate Arduino chess computer via Hackaday](http://www.talkchess.com/forum/viewtopic.php?t=58517) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), December 08, 2015 [[26]](#cite_note-26)
- [My chess robot project using Micromax chess on Arduino](http://www.talkchess.com/forum/viewtopic.php?t=64823) by [Chris Quayle](/index.php?title=Chris_Quayle&action=edit&redlink=1 "Chris Quayle (page does not exist)"), [CCC](/CCC "CCC"), August 06, 2017 » [Arduino Due Chess Robot](/Robots#CRAP "Robots")

## 2020 ...

- [Electronic Chess Board: Arduino Source-Code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76561) by [Dominik Klein](/Dominik_Klein "Dominik Klein"), [CCC](/CCC "CCC"), February 12, 2021 » [ArdEBoard](#ArdEBoard)
- [I built dynamically programmable arduino based computer to run a chess program](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78541) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 30, 2021

# External Links

## Arduino

- [Arduino - HomePage](http://arduino.cc/)

:   [Arduino Board Uno](http://arduino.cc/en/Main/ArduinoBoardUno)
:   [Arduino Board Due](http://arduino.cc/en/Main/ArduinoBoardDue)
:   [Arduino Mega 2560](https://store.arduino.cc/arduino-mega-2560-rev3)

- [Arduino from Wikipedia](https://en.wikipedia.org/wiki/Arduino)
- [List of Arduino boards and compatible systems from Wikipedia](https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems)
- [Arduino / Atmel AVR](http://www.grappendorf.net/arduino) by [Dirk Grappendorf](http://www.grappendorf.net/)
- [Arduino microcontroller projects](http://cosinekitty.com/arduino.html) by [Don Cross](/Don_Cross "Don Cross")

## Computer Chess

- [Arduino & Raspberry PI Chess Computer](http://www.chess.fortherapy.co.uk/) running [Stockfish](/Stockfish "Stockfish") on [Raspberry Pi](/Raspberry_Pi "Raspberry Pi"), by [Max Dobres](/index.php?title=Max_Dobres&action=edit&redlink=1 "Max Dobres (page does not exist)") » [Sensory Board](/Sensory_Board "Sensory Board")
- [Little Rook Chess - Library for the Dogm-Graphics-LCD modules (AVR, Arduino compatible) - Google Project Hosting](http://code.google.com/p/dogm128/wiki/chess), by [Oliver Kraus](/Oliver_Kraus "Oliver Kraus")

:   [chess.c - dogm128 - Library for the Dogm-Graphics-LCD modules (AVR, Arduino compatible) - Google Project Hosting](http://code.google.com/p/dogm128/source/browse/libraries/Dogm/utility/chess.c)

- [Use this Open Source Lib to play Chess with Arduino](http://pcbheaven.com/opendir/index.php?show=193ih3156lxbbd90dc9) by [Giorgos Lazaridis](http://pcbheaven.com/opendir/index.php?author=Giorgos%20Lazaridis), [PCB Heaven](http://www.pcbheaven.com/), October 14, 2014 » [Micro-Max](/Micro-Max "Micro-Max")
- [Chessuino](https://sites.google.com/site/chessuino/) by [Diego Cueva](/index.php?title=Diego_Cueva&action=edit&redlink=1 "Diego Cueva (page does not exist)"), based on [Micro-Max](/Micro-Max "Micro-Max") by [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller"), ported for the [Atmel](https://en.wikipedia.org/wiki/Atmel)-[ATmega88](https://en.wikipedia.org/wiki/ATmega88) by [Andre Adrian](/Andre_Adrian "Andre Adrian")

:   CHESSuino = Chess + Arduino, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- Wireless Arduino Powered Chess, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- [Arduino Due Chess Robot](https://forum.arduino.cc/index.php?topic=490965.0) by [Chris Quayle](/index.php?title=Chris_Quayle&action=edit&redlink=1 "Chris Quayle (page does not exist)") » [Arduino Due Chess Robot](/Robots#CRAP "Robots")
- [Arduino Blog » Square Off is a chess board with a high-tech twist](https://blog.arduino.cc/2016/10/17/square-off-is-a-chess-board-with-a-high-tech-twist/), October 17, 2016  » [Square Off](/index.php?title=Square_Off&action=edit&redlink=1 "Square Off (page does not exist)")
- [GitHub - asdfjkl/ArdEBoard: Arduino Leonardo / Pro-Micro (ATmega32U4) based electronic chess board with Reed switches](https://github.com/asdfjkl/ArdEBoard) by [Dominik Klein](/Dominik_Klein "Dominik Klein") » [ArdEBoard](#ArdEBoard)

## Development

- [Getting Started with Arduino](http://arduino.cc/en/Guide/HomePage)
- [Arduino Development Environment](http://arduino.cc/en/Guide/Environment)

:   [Arduino - BuildProcess](http://arduino.cc/en/Hacking/BuildProcess)
:   [Arduino - FAQ](http://arduino.cc/en/Main/FAQ)
:   [Arduino - Reference](http://arduino.cc/en/Reference/HomePage)
:   [Arduino - Tutorials](http://arduino.cc/en/Tutorial/HomePage)

- [Atmel® Studio 6 - Supporting Two Architectures: AVR and ARM, with One Integrated Studio - Overview](http://www.atmel.com/microsite/atmel_studio6/)
- [AVRDUDE - AVR Downloader/UploaDEr](http://www.nongnu.org/avrdude/)

### [Assembly](/Assembly "Assembly")

- [AVR ASM INTRODUCTION](https://sites.google.com/site/avrasmintro/)
- [AVR-Assembly Tutorial](http://www.avr-asm-tutorial.net/) by [Gerhard Schmidt](http://www.dg4fac.de/)

### [C](/C "C"), [C++](/Cpp "Cpp")

- [AVR Libc Home Page](http://www.nongnu.org/avr-libc/)
- [WinAVR GCC](http://winavr.sourceforge.net/)
- [The AVR Eclipse Plugin - AVR-Eclipse](http://avr-eclipse.sourceforge.net/wiki/index.php/The_AVR_Eclipse_Plugin)
- [Developing Software for the Atmel AVR with AVR-Eclipse, AVR-GCC & AVRDude — Interactive Matter Lab](http://interactive-matter.eu/how-to/developing-software-for-the-atmel-avr-with-avr-eclipse-avr-gcc-avrdude/)
- [grappendorf/arduino-eclipse · GitHub](https://github.com/grappendorf/arduino-eclipse) by [Dirk Grappendorf](http://www.grappendorf.net/)

### [Java](/Java "Java")

- [The NanoVM - Java for the AVR](http://www.harbaum.org/till/nanovm/index.shtml)
- [Netbeans plugin for AVR microcontrollers — Project Kenai](https://java.net/projects/nbplugin-avr)

## Misc

- [Arduino (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Arduino_%28disambiguation%29)
- [Arduinna (goddess) from Wikipedia](https://en.wikipedia.org/wiki/Arduinna)
- [394 Arduina (asteroid) from Wikipedia](https://en.wikipedia.org/wiki/394_Arduina)

# References

1. [↑](#cite_ref-1) Image by [David Mellis](http://www.flickr.com/people/36749491@N00), July 12, 2010, hosted at [Flickr](https://en.wikipedia.org/wiki/Flickr), [Arduino from Wikipedia](https://en.wikipedia.org/wiki/Arduino)
2. [↑](#cite_ref-2) [Arduino from Wikipedia](https://en.wikipedia.org/wiki/Arduino)
3. [↑](#cite_ref-3) [Arduino - Getting Started](http://arduino.cc/en/Guide/HomePage)
4. [↑](#cite_ref-4) [Arduino - Products](http://arduino.cc/en/Main/Products)
5. [↑](#cite_ref-5) [Arduino from Wikipedia](https://en.wikipedia.org/wiki/Arduino)
6. [↑](#cite_ref-6) [Atmel - ATmega1280](http://www.atmel.com/devices/atmega1280.aspx)
7. [↑](#cite_ref-7) [Arduino Mega 2560 Rev3](https://store.arduino.cc/arduino-mega-2560-rev3)
8. [↑](#cite_ref-8) [ATmega2560 - 8-bit AVR Microcontrollers](http://www.microchip.com/wwwproducts/en/atmega2560)
9. [↑](#cite_ref-9) [Arduino - Reference](http://arduino.cc/en/Reference/HomePage)
10. [↑](#cite_ref-10) [Arduino - FAQ](http://arduino.cc/en/Main/FAQ)
11. [↑](#cite_ref-11) [Arduino & Raspberry PI Chess Computer](http://www.chess.fortherapy.co.uk/)  running [Stockfish](/Stockfish "Stockfish") on [Raspberry Pi](/Raspberry_Pi "Raspberry Pi"), by [Max Dobres](/index.php?title=Max_Dobres&action=edit&redlink=1 "Max Dobres (page does not exist)")
12. [↑](#cite_ref-12) [Self-made Chess Computer SHAH](http://www.andreadrian.de/schach/#Selbstbau_Schachcomputer_SHAH) based on an [Atmel](https://en.wikipedia.org/wiki/Atmel)-[ATmega88](https://en.wikipedia.org/wiki/ATmega88) [Microcontroller](https://en.wikipedia.org/wiki/Microcontroller) and Micro-Max-port by [Andre Adrian](/Andre_Adrian "Andre Adrian") (German)
13. [↑](#cite_ref-13) [ATM18 Mini Chess Computer](http://www.elektor.com/magazines/2009/september/atm18-mini-chess-computer.1041342.lynkx) from [ELEKTOR.com – Platform for electronics and microcontrollers](http://www.elektor.com/elektor-uk.35.lynkx)
14. [↑](#cite_ref-14) [Nanochess auf avr](http://www.mikrocontroller.net/topic/208206) by Sam, [Mikrocontroller.net GCC Forum](http://www.mikrocontroller.net/forum/gcc), February 11, 2011 (German)
15. [↑](#cite_ref-15) [ELECTRONIC ASSEMBLY : LCD DOG series, flexibe, flat and colorful](http://www.lcd-module.com/products/dog.html)
16. [↑](#cite_ref-16) [little\_rook\_chess · olikraus/u8glib Wiki · GitHub](https://github.com/olikraus/u8glib/wiki/little_rook_chess)
17. [↑](#cite_ref-17) [u8glib/license.txt at master · olikraus/u8glib · GitHub](https://github.com/olikraus/u8glib/blob/master/license.txt)
18. [↑](#cite_ref-18) [Obsolescence Guaranteed Home](http://obsolescence.wix.com/obsolescence)
19. [↑](#cite_ref-19) [6502 Microchess on an Arduino](http://obsolescenceguaranteed.blogspot.ch/2014/06/6502-microchess-on-arduino.html)
20. [↑](#cite_ref-20) [KIM Uno](http://obsolescence.wix.com/obsolescence#!kim-uno-summary/chcm)
21. [↑](#cite_ref-21) [Myopic, a new Creative Commons chess program](http://www.talkchess.com/forum/viewtopic.php?t=34445) by [Steven Edwards](/Steven_Edwards "Steven Edwards"), [CCC](/CCC "CCC"), May 22, 2010
22. [↑](#cite_ref-22) [Arduino Blog » Square Off is a chess board with a high-tech twist](https://blog.arduino.cc/2016/10/17/square-off-is-a-chess-board-with-a-high-tech-twist/), October 17, 2016
23. [↑](#cite_ref-23) [Electronic Chess Board: Arduino Source-Code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76561) by [Dominik Klein](/Dominik_Klein "Dominik Klein"), [CCC](/CCC "CCC"), February 12, 2021
24. [↑](#cite_ref-24) [GitHub - asdfjkl/ArdEBoard: Arduino Leonardo / Pro-Micro (ATmega32U4) based electronic chess board with Reed switches](https://github.com/asdfjkl/ArdEBoard) by [Dominik Klein](/Dominik_Klein "Dominik Klein")
25. [↑](#cite_ref-25) [Arduino - AnalogRead](http://arduino.cc/en/Reference/AnalogRead)
26. [↑](#cite_ref-26) [Chess Mate](https://hackaday.io/project/8705-chess-mate) • [Hackaday.io](https://en.wikipedia.org/wiki/Hackaday#Hackaday.io)

**[Up one Level](/Hardware "Hardware")**