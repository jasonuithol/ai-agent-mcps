# Analog Evaluation

Source: https://www.chessprogramming.org/Analog_Evaluation

**[Home](/Main_Page "Main Page") \* [Hardware](/Hardware "Hardware") \* Analog Evaluation**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Op-Amp_Summing_Amplifier.svg/330px-Op-Amp_Summing_Amplifier.svg.png)](/File:Op-Amp_Summing_Amplifier.svg)

Summing amplifier [[1]](#cite_note-1)

**Analog Evaluation**, (Analogue Evaluation)  
a hypothetical dedicated special purpose hardware to [evaluate](/Evaluation "Evaluation") a [chess position](/Chess_Position "Chess Position") using [analog circuits](https://en.wikipedia.org/wiki/Analogue_electronics) such as [resistive networks](https://en.wikipedia.org/wiki/Electrical_network), [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier) (op-amps), and in particular the analogous [FPGA](/FPGA "FPGA") counterparts [FPAA](https://en.wikipedia.org/wiki/Field-programmable_analog_array), to map digital or discrete input signals, [representing the board](/Board_Representation "Board Representation") or aspects of the board, to an analog output representing an evaluation [score](/Score "Score") along with some [noise](https://en.wikipedia.org/wiki/Noise_(electronics)) as input of an [analog-to-digital converter](https://en.wikipedia.org/wiki/Analog-to-digital_converter). [Jonathan Allen](/index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](/index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), and [Robert Levinson](/Robert_Levinson "Robert Levinson") mentioned a method to convert a chess [mobility](/Mobility "Mobility") graph to a resistive network which could be computed using the [residual resistance](https://en.wikipedia.org/wiki/Residual-resistance_ratio) property of interconnected chips within their [Morph III](/Morph "Morph") project [[2]](#cite_note-2). Using [memristors](https://en.wikipedia.org/wiki/Memristor), [memistors](https://en.wikipedia.org/wiki/Memistor), or even a kind of motorized [potentiometers](https://en.wikipedia.org/wiki/Potentiometer) [[3]](#cite_note-3) as used in [closed loop control](https://en.wikipedia.org/wiki/Control_theory) and [servomechanisms](https://en.wikipedia.org/wiki/Servomechanism), would allow the implementation of [physical](https://en.wikipedia.org/wiki/Physical_neural_network) [neural networks](/Neural_Networks "Neural Networks") as analog evaluation device with [machine learning](/Learning "Learning") features [[4]](#cite_note-4).

# Summing Amplifier

A [summing amplifier](https://en.wikipedia.org/wiki/Operational_amplifier_applications#Summing_amplifier) using an operational amplifier with [feedback](https://en.wikipedia.org/wiki/Feedback#Negative_feedback) [resistor](https://en.wikipedia.org/wiki/Resistor) Rf sums several (weighted by input resistors 1..n) voltages to an negated output ...

[![OpAmpFormula.jpg](/images/1/1b/OpAmpFormula.jpg)](/File:OpAmpFormula.jpg)

... and may be used to implement a classical [evaluation function](/Evaluation_Function "Evaluation Function") as [linear combination](https://en.wikipedia.org/wiki/Linear_combination) of independent features (F) and associated weights (W):

[![EvalLinearFormula1.jpg](/images/0/0e/EvalLinearFormula1.jpg)](/File:EvalLinearFormula1.jpg)

# See also

- [Arduino](/Arduino "Arduino")
- [Evaluation](/Evaluation "Evaluation")
- [FPGA](/FPGA "FPGA")
- [Neural Networks](/Neural_Networks "Neural Networks")
- [Pattern Recognition](/Pattern_Recognition "Pattern Recognition")
- [PIC Microcontroller](/PIC_Microcontroller "PIC Microcontroller")
- [Tapered Eval](/Tapered_Eval "Tapered Eval")

# Publications

- [Michael Gherrity](/Michael_Gherrity "Michael Gherrity") (**1989**). *[A Learning Algorithm for Analog, Fully Recurrent Neural Networks](https://ieeexplore.ieee.org/document/118645)*. [IEEE IJCNN 1989](/IEEE "IEEE")
- [Jonathan Allen](/index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](/index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), [Robert Levinson](/Robert_Levinson "Robert Levinson") (**1997**). *New Advances in Adaptive Pattern-Oriented Chess*. [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
- [Amir Yazdanbakhsh](https://scholar.google.com/citations?user=_WlPFxIAAAAJ&hl=en), [Renée St. Amant](https://www.linkedin.com/in/stamant), [Bradley Thwaites](https://www.linkedin.com/in/bthwaites), [Jongse Park](https://scholar.google.com/citations?user=4Fw2ma4AAAAJ&hl=en), [Hadi Esmaeilzadeh](https://scholar.google.com/citations?user=LnB5_AcAAAAJ&hl=en), [Arjang Hassibi](https://scholar.google.com/citations?user=NSbws80AAAAJ&hl=en), [Luis Ceze](https://scholar.google.com/citations?user=KzESVKwAAAAJ&hl=en), [Doug Burger](https://scholar.google.com/citations?user=5JtQbw0AAAAJ) (**2014**). *[Toward General-Purpose Code Acceleration with Analog Computation](http://dl.acm.org/citation.cfm?id=2665746)*. [ACM SIGARCH Computer Architecture News](/ACM#SIGARCH "ACM") - [ISCA '14](http://cag.engr.uconn.edu/isca2014/), Vol. 42, No. 3, [pdf](http://www.cc.gatech.edu/~hadi/doc/paper/2014-wacas-anpu.pdf)
- [George Rajna](/George_Rajna "George Rajna") (**2016**). *Neuro-Inspired Analog Computer*. [viXra:1610.0110](http://vixra.org/abs/1610.0110)
- [Alexantrou Serb](https://dblp.org/pers/hd/s/Serb:Alexander), [Edoardo Manino](/Edoardo_Manino "Edoardo Manino"), [Ioannis Messaris](https://dblp.org/pers/hd/m/Messaris:Ioannis), [Long Tran-Thanh](https://dblp.org/pers/hd/t/Tran=Thanh:Long), [Themis Prodromakis](https://www.orc.soton.ac.uk/people/tp1f12) (**2017**). *[Hardware-level Bayesian inference](https://eprints.soton.ac.uk/425616/)*. [NIPS 2017](https://nips.cc/Conferences/2017) [[5]](#cite_note-5)

# Forum Posts

- [Discussion of Special Purpose hardware for chess search](http://www.talkchess.com/forum/viewtopic.php?t=20841) by Rick Fadden, [CCC](/CCC "CCC"), April 25, 2008

:   [Re: Discussion of Special Purpose hardware for chess search](http://www.talkchess.com/forum/viewtopic.php?t=20841&start=1) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), April 25, 2008

- [How can you create an analog sigmoid voltage transfer function (from simple parts)?](https://www.reddit.com/r/AskElectronics/comments/217j2u/how_can_you_create_an_analog_sigmoid_voltage/), [AskElektonics](https://www.reddit.com/r/AskElectronics/), [Reddit](https://en.wikipedia.org/wiki/Reddit), March 24, 2014

# External Links

- [Analog computer from Wikipedia](https://en.wikipedia.org/wiki/Analog_computer)
- [Analogue electronics from Wikipedia](https://en.wikipedia.org/wiki/Analogue_electronics)
- [Analog-to-digital converter from Wikipedia](https://en.wikipedia.org/wiki/Analog-to-digital_converter)
- [Digital-to-analog converter from Wikipedia](https://en.wikipedia.org/wiki/Digital-to-analog_converter)
- [Field-programmable analog array from Wikipedia](https://en.wikipedia.org/wiki/Field-programmable_analog_array)
- [Field-Programmable Analog Array](http://opencircuitdesign.com/~tim/research/fpaa/fpaa.html)
- [Neuromorphic engineering from Wikipedia](https://en.wikipedia.org/wiki/Neuromorphic_engineering)
- [Operational amplifier from Wikipedia](https://en.wikipedia.org/wiki/Operational_amplifier)
- [Operational amplifier applications from Wikipedia](https://en.wikipedia.org/wiki/Operational_amplifier_applications)
- [Operational Amplifiers](http://www.electronics-tutorials.ws/category/opamp) from [Basic Electronics Tutorials and Revision](http://www.electronics-tutorials.ws/) by [AspenCore, Inc](http://www.aspencore.com/)

:   [Summing Amplifier is an Op-amp Voltage Adder](http://www.electronics-tutorials.ws/opamp/opamp_4.html)
:   [Operational Amplifier Summary, Op-amp basics](http://www.electronics-tutorials.ws/opamp/opamp_8.html)

- [Physical neural network from Wikipedia](https://en.wikipedia.org/wiki/Physical_neural_network)
- [SciDAC Review - HARDWARE: Cortical Computing with Memristive Nanodevices](http://www.scidacreview.org/0804/html/hardware.html)
- [Achim Zepezauer](/Category:Achim_Zepezauer "Category:Achim Zepezauer") - Rätsel [[6]](#cite_note-6), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) A [circuit diagram](https://en.wikipedia.org/wiki/Circuit_diagram) of a [Summing amplifier](https://en.wikipedia.org/wiki/Operational_amplifier_applications#Summing_amplifier) made using an [operational amplifier](https://en.wikipedia.org/wiki/Operational_amplifier), made by [Inductiveload](https://commons.wikimedia.org/wiki/User:Inductiveload), January 26 2009, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Jonathan Allen](/index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](/index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), [Robert Levinson](/Robert_Levinson "Robert Levinson") (**1997**). *New Advances in Adaptive Pattern-Oriented Chess*. [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
3. [↑](#cite_ref-3) [Motorized potentiometers for high precision proportional controls](http://www.onlinecontrols.com/mpots.htm)
4. [↑](#cite_ref-4) [SciDAC Review - HARDWARE: Cortical Computing with Memristive Nanodevices](http://www.scidacreview.org/0804/html/hardware.html)
5. [↑](#cite_ref-5) [Bayesian inference from Wikipedia](https://en.wikipedia.org/wiki/Bayesian_inference)
6. [↑](#cite_ref-6) [Rätsel - Wiikipedia.de](https://de.wikipedia.org/wiki/R%C3%A4tsel) (German) » [Riddle from Wikipedia](https://en.wikipedia.org/wiki/Riddle)

**[Up one Level](/Hardware "Hardware")**