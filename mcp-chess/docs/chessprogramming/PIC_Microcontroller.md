# PIC Microcontroller

Source: https://www.chessprogramming.org/PIC_Microcontroller

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* PIC Microcontroller**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/PICKit3.jpg/330px-PICKit3.jpg)](/File:PICKit3.jpg)

[PICKit](https://en.wikipedia.org/wiki/PICkit) 3 Debug Express [[1]](#cite_note-1)

**PIC Microcontroller**,  
a family of [microcontrollers](https://en.wikipedia.org/wiki/Microcontroller) (MCUs) with a [Harvard architecture](https://en.wikipedia.org/wiki/Harvard_architecture) design, made by [Microchip Technology](https://en.wikipedia.org/wiki/Microchip_Technology), derived from the 1976 ancestor, the Programmable Interface Controller PIC1650 developed by [General Instrument](https://en.wikipedia.org/wiki/General_Instrument) [[2]](#cite_note-2). The PIC family includes various 8, 16 and 32-bit controllers with 12, 14, 16, or 24 bit instructions, [flash memory](/Memory#Flash "Memory") ([EEPROM](/Memory#ROM "Memory")), [RAM](/Memory#RAM "Memory"), [parallel I/O-ports](https://en.wikipedia.org/wiki/Parallel_port), [DMA](https://en.wikipedia.org/wiki/Direct_memory_access), [serial communication](https://en.wikipedia.org/wiki/Serial_communication), [ADC](https://en.wikipedia.org/wiki/Analog-to-digital_converter) and [DAC](https://en.wikipedia.org/wiki/Digital-to-analog_converter), and further peripherals such as timer, [interrupt controller](https://en.wikipedia.org/wiki/Programmable_interrupt_controller) and [PWM](https://en.wikipedia.org/wiki/Pulse-width_modulation) devices for [motor control](https://en.wikipedia.org/wiki/Motor_control).

# PIC24

The PIC24 is a 16-bit MCU. It has 16 16-bit working registers (W0-W15). W0-W3 act as div and mul result registers, W15 operates as a software stack pointer for interrupts and calls. The data space can be addressed as 32 Ki words or 64 KiB. Beside move ([memory mapped I/O](https://en.wikipedia.org/wiki/Memory-mapped_I/O)), [arithmetical](https://en.wikipedia.org/wiki/Instruction_set_architecture#Arithmetic_and_logic_operations), [bitwise logical](https://en.wikipedia.org/wiki/Bitwise_operation) and [shift/rotate](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts), [control flow](https://en.wikipedia.org/wiki/Control_flow) and stack instructions, PIC24 has bit instructions along with [bitscan](/BitScan "BitScan") aka "Find first one from left (MSb) side" (FF1L) and "Find first one from right (LSb) side" (FF1R), i.e. for [piece set](/Piece-Sets "Piece-Sets") traversal [[3]](#cite_note-3).

# Chess Engines

- [PICcolino](/PICcolino "PICcolino")

# See also

- [Analog Evaluation](/Analog_Evaluation "Analog Evaluation")

# Manuals

[[4]](#cite_note-4)

- [Microchip](https://en.wikipedia.org/wiki/Microchip_Technology) (**2009**). *[16-bit MCU and DSC Programmer’s Reference Manual](http://ww1.microchip.com/downloads/en/DeviceDoc/70157D.pdf)*. (pdf)
- [Microchip](https://en.wikipedia.org/wiki/Microchip_Technology) (**2009**). *PIC24F Family Reference Manual - Section 17. 10-Bit A/D Converter*. [pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/39705b.pdf)
- [Microchip](https://en.wikipedia.org/wiki/Microchip_Technology) (**2012**). *PIC24F Family Reference Manual - Section 62. 10-bit Digital-to-Analog Converter (DAC)*. [pdf](http://ww1.microchip.com/downloads/en/DeviceDoc/39615A.pdf)

# Publications

- [Lucio Di Jasio](http://blog.flyingpic24.com/about/) (**2011**). *[Programming 16-Bit PIC Microcontrollers in C, Learning to Fly the PIC 24](http://blog.flyingpic24.com/programming-16-bit/)*. [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [2nd edition from amazom](https://www.amazon.com/Programming-16-Bit-PIC-Microcontrollers-Second/dp/1856178706) [[5]](#cite_note-5)

# External Links

- [PIC microcontroller from Wikipedia](https://en.wikipedia.org/wiki/PIC_microcontroller)
- [16-bit PIC® Microcontrollers](http://www.microchip.com/design-centers/16-bit)
- [MPLAB from Wikipedia](https://en.wikipedia.org/wiki/MPLAB)
- [MPLAB- X IDE | Microchip Technology Inc.](http://www.microchip.com/mplab/mplab-x-ide)
- [PICkit from Wikipedia](https://en.wikipedia.org/wiki/PICkit)
- [A Guide To PIC Microcontroller Documentation - Wikibooks](https://en.wikibooks.org/wiki/A_Guide_To_PIC_Microcontroller_Documentation)
- [PIC micro controller board, PIC micro controller projects, and PIC microcontroller tutorials](http://www.microcontrollerboard.com/index.html)
- [PIC Microcontrollers Tutorials](https://electrosome.com/category/tutorials/pic-microcontroller/)
- Introduction to the 16-bit PIC24F Microcontroller Family, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [PICKit](https://en.wikipedia.org/wiki/PICkit) 3 Debug Express with demo board, [Image](https://commons.wikimedia.org/wiki/File:PICKit3.jpg) by Glossywhite, February 01, 2011, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [PIC microcontroller from Wikipedia](https://en.wikipedia.org/wiki/PIC_microcontroller)
3. [↑](#cite_ref-3)  [Microchip](https://en.wikipedia.org/wiki/Microchip_Technology) (**2009**). *[16-bit MCU and DSC Programmer’s Reference Manual](http://ww1.microchip.com/downloads/en/DeviceDoc/70157D.pdf)*. (pdf)
4. [↑](#cite_ref-4) [Microchip PIC Family Reference Manuals - Compiled - Microcontroller](https://eewiki.net/display/microcontroller/Microchip+PIC+Family+Reference+Manuals+-+Compiled) - [eewiki](https://eewiki.net/)
5. [↑](#cite_ref-5) [luciodj / FlyingPIC24 / source / — Bitbucket](https://bitbucket.org/luciodj/flyingpic24/src)

**[Up one Level](/Hardware "Hardware")**