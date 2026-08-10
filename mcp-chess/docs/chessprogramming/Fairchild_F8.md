# Fairchild F8

Source: https://www.chessprogramming.org/Fairchild_F8

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* Fairchild F8**

**Fairchild F8**,  
an [8-bit](https://en.wikipedia.org/wiki/8-bit) multi-chip [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) by [Fairchild Semiconductor](https://en.wikipedia.org/wiki/Fairchild_Semiconductor) introduced and launched in 1975. The F8 consists of the **3850** [CPU](https://en.wikipedia.org/wiki/Central_processing_unit) with 8-bit [ALU](/Combinatorial_Logic#ALU "Combinatorial Logic"), 64-bytes [scratchpad RAM](/Memory#Latches "Memory") and two 8-bit [I/O](https://en.wikipedia.org/wiki/Input/output) ports, the **3851** program storage unit (PSU) with 2 KiB [ROM](/Memory#ROM "Memory"), the **3852** [dynamic memory](/Memory#DynamicRAM "Memory") interface (MI), and **3853** [static memory](/Memory#StaticRAM "Memory") (or ROM) interface (SMI) chip, the optional **3854** [DMA controller](https://en.wikipedia.org/wiki/Channel_I/O), and the **3861**/**3871** [parallel I/O](https://en.wikipedia.org/wiki/Parallel_I/O) (PIO) chips. A minimal system could be build from a 3850 with either a 3851 or a 3853 with external ROM. The [Mostek 3870](https://en.wikipedia.org/wiki/Mostek#Microprocessor_second_sourcing_deals) was a 3850/3851 single-chip implementation with some extra 64 bytes RAM, launched in 1977 [[1]](#cite_note-1) .

# Details

## Circuit Diagram

[![F8.JPG](/images/2/28/F8.JPG)](https://usermanual.wiki/Document/FairchildF8Kit1schematicrevC1975.1174772138/html)

F8 Kit [circuit diagram](https://en.wikipedia.org/wiki/Circuit_diagram) [[2]](#cite_note-2)

## Registers

The 3850 CPU has an 8-bit [accumulator](https://en.wikipedia.org/wiki/Accumulator_%28computing%29) as input and output of the ALU, as well a 5-bit [status register](https://en.wikipedia.org/wiki/Status_register) to indicate the flags [sign](https://en.wikipedia.org/wiki/Negative_flag), [carry](https://en.wikipedia.org/wiki/Carry_flag), [zero](https://en.wikipedia.org/wiki/Zero_flag) and [overflow](https://en.wikipedia.org/wiki/Overflow_flag) after arithmetical and logical operations, as well as an [interrupt control](https://en.wikipedia.org/wiki/Programmable_Interrupt_Controller) bit to enable or disable [interrupts](https://en.wikipedia.org/wiki/Interrupt). The 64 byte scratchpad memory allow [indirect addressing](https://en.wikipedia.org/wiki/Addressing_mode#Register_indirect_2) mode via the ISAR (indirect scratchpad register), which could be used as a kind of [stack](/Stack "Stack") pointer to a stack frame of 8 bytes.

16-bit [progam counter](https://en.wikipedia.org/wiki/Program_counter), stack register, data counter (DC to indirectly address up 64 KiB of memory), and address incrementer/adder were not part of the CPU, but in each PSU and/or MI. There is no [address bus](https://en.wikipedia.org/wiki/Address_bus) from the CPU, but a set of control signals, and transfer of addresses, i.e. branch targets, via the [data bus](https://en.wikipedia.org/wiki/Data_bus). The stack register is directly linked to the program counter and simplifies the creation of a [call stack](https://en.wikipedia.org/wiki/Call_stack).

## Instructions

Arithmetical and logical [instructions](https://en.wikipedia.org/wiki/Instruction_set) work on the accumulator. Source operands are either implicit, content of scratchpad register, indirect addressed via [post-incremented](https://en.wikipedia.org/wiki/Increment_and_decrement_operators) data counter (DC) register, or immediate :

| Mnemonic | Description | Operation | Bytes | Cycles |
| --- | --- | --- | --- | --- |
| NI ii | And with immediate | ACC &= ii | 2 | 2.5 |
| NS rn | And with scratchpad r0..63 | ACC &= rn | 1 | 1 |
| NM | And via post-incremented DC | ACC &= \*DC++ | 1 | 2.5 |

## Endianess

F8 is a [big-endian](/Big-endian "Big-endian") machine concerning the [byte](/Byte "Byte")-order of 16-bit [words](/Word "Word") in (scratchpad) memory. For instance, LR PO,Q, restore Q register contents to the program counter, has the upper byte in scratchpad register r14, and the lower byte in r15.

## Sample Assembly

A answer back program in F8 [Assembly](/Assembly "Assembly") as given by David Edwards, [Electronics Australia](https://en.wikipedia.org/wiki/Electronics_Australia) [[3]](#cite_note-3) :

```
ANSWER-BACK PROGRAM FOR MOSTEK F8 EVALUATION KIT
D. EDWARDS, ELECTRONICS AUSTRALIA 19/10/76

0400 20 FF       INIT,LI FF        /LOAD AC WITH FF
0402 OB               LR IS,A      /INITIALIZE ISAR TO 3F
0403 54               LR 4,A       /COPY AC INTO REG 4
0404 34               DS 4         /DECREMENT REG 4 TO FE
0405 56               LR 6,A       /COPY AC INTO REG 6
0406 71               LIS H'1'     /LOAD AC WITH 01
0407 B6               OUTS 6       /TRANSFER AC TO TIMER PORT TO ENABLE EXT INT
0408 1B               EI           /ENABLE I/O ROUTINES
0409 20 03 F3   START,PI 03F3      /CALL TTYIN SUBROUTINE
040C 4C               LR AS        /COPY CHAR INTO AC FROM RS
040D 25 OD            CI 'OD'      /COMPARE WITH CR
040F 84 06            BZ MESSAGE   /JUMP TO MESSAGE IF CR
0411 28 03 5D         PI 035D      /SEND CHAR TO TTYOUT SUBROUTINE
0414 90 F4            BR START     /LOOP BACK TO START
0416 2A 04 23 MESSAGE,DCI 0423     /LOAD DC WITH MESSAGE ADDRESS
0419 70        ANSWER,CLR          /CLEAR AC
041A 88               AM           /ADD CHAR TO AC AND INC DC
041B 84 ED            BZ START     /LOOP BACK TO START
041D 5C               LR S,A       /COPY CHAR INTO RS
041E 28 03 5D         PI 035D      /SEND CHAR TO TTYOUT SUBROUTINE
0421 90 F7            BR ANSWER    /LOOP BACK TO ANSWER
0423 OD 47 4F                      /START OF ANSWER BUFFER
0426 20 41 57
0429 41 59 2C
042C 20 49 27
043F 4D 20 42
0432 55 53 59
0435 21 OD 00                      /ANSWER MUST END WITH A ZERO BYTE
```

# F8 Chess Computers

The original [CompuChess](/CompuChess "CompuChess") [[4]](#cite_note-4) and its [clone](/Category:Clone "Category:Clone"), the [Novag](/Novag "Novag") [Chess Champion MK I](/Chess_Champion_MK_I "Chess Champion MK I") had the **3850** CPU and the **3853** SMI, addressing a 2 KiB 2316 compatible ROM, and 2 x 2111 [[5]](#cite_note-5) 256x4 each, in total 256 byte SRAM [[6]](#cite_note-6) . [Boris](/Boris "Boris") also used the 3850/3853 approach with 2 x 2112 for 256 byte SRAM, and 2 x 2 KiB ROM [[7]](#cite_note-7) . [David Kittinger](/David_Kittinger "David Kittinger") had to solve the 128 byte challenge (including scratchpad) for the [Novag Micro Chess](/Novag_Micro_Chess "Novag Micro Chess") with [Mostek 3870](https://en.wikipedia.org/wiki/Mostek#Microprocessor_second_sourcing_deals).

- [Category:F8](/Category:F8 "Category:F8")

# Publications

- [Fairchild](https://en.wikipedia.org/wiki/Fairchild_Semiconductor) (**1977**). *[F8 Guide To Programming](https://archive.org/details/bitsavers_fairchildfng1977_5888299)*. hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)

# External Links

- [Fairchild F8 from Wikipedia](https://en.wikipedia.org/wiki/Fairchild_F8)
- [Fairchild processor - BORIS IS KING](http://www.borischesscomputer.com/fairchildprocessor.htm)
- [Fairchild F8 (3850) microcontroller family from CPU world](http://www.cpu-world.com/CPUs/3850/index.html)
- [CPU of the Day: Fairchild F8 Microprocessor | The CPU Shack Museum](http://www.cpushack.com/2013/06/08/cpu-of-the-day-fairchild-f8-microprocessor/), June 8, 2013
- [Mostek 3870 (MK3870) microcontroller family from CPU world](http://www.cpu-world.com/CPUs/3870/index.html)
- [Patent US4086626 - Microprocessor system - Google Patents](http://www.google.com/patents/US4086626)
- [F8 info](http://seanriddle.com/f8info.html) by [Sean Riddle](/index.php?title=Sean_Riddle&action=edit&redlink=1 "Sean Riddle (page does not exist)")
- [Fairchild Channel F from Wikipedia](https://en.wikipedia.org/wiki/Fairchild_Channel_F)
- [the dasm macro assembler](http://dasm-dillon.sourceforge.net/)
- [asmx multi-CPU assembler](http://xi6.com/projects/asmx/)

# References

1. [↑](#cite_ref-1) [Mostek 3870 (MK3870) microcontroller family from CPU world](http://www.cpu-world.com/CPUs/3870/index.html)
2. [↑](#cite_ref-2) [Fairchild F8 Kit 1 Schematic, Revision C, 25 Sep 1975](https://usermanual.wiki/Document/FairchildF8Kit1schematicrevC1975.1174772138/html), [User Manual Wiki](https://usermanual.wiki/)
3. [↑](#cite_ref-3) David Edwards (**1976**). *The Mostek F8*. [Electronics Australia](https://en.wikipedia.org/wiki/Electronics_Australia), December, 1976
4. [↑](#cite_ref-4) [CompuChess](http://www.schach-computer.info/wiki/index.php/CompuChess) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) by [Mike Watters](/Mike_Watters "Mike Watters")
5. [↑](#cite_ref-5) [MM2111 pdf, MM2111 description, MM2111 datasheets, MM2111 view](http://pdf1.alldatasheet.com/datasheet-pdf/view/125751/NSC/MM2111.html)
6. [↑](#cite_ref-6) [Novag Chess Champion MK I](http://www.schach-computer.info/wiki/index.php/Novag_Chess_Champion_MK_I) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
7. [↑](#cite_ref-7) [Boris assembly manual](http://alain.zanchetta.free.fr/docs/AppliedConcepts/BorisKitAssemblyManualUS.pdf) (pdf) hosted by [Alain Zanchetta](/index.php?title=Alain_Zanchetta&action=edit&redlink=1 "Alain Zanchetta (page does not exist)")

**[Up one Level](/Hardware "Hardware")**