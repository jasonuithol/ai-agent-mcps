# OpenBench

Source: https://www.chessprogramming.org/OpenBench

**[Home](/Main_Page "Main Page") \* [Engine Testing](/Engine_Testing "Engine Testing") \* OpenBench**

**OpenBench**,  
an [open source chess engine](/Category:Open_Source "Category:Open Source") testing framework authored by [Andrew Grant](/Andrew_Grant "Andrew Grant"), written in [Python](/Python "Python") and licensed under the [GNU GPL](/Free_Software_Foundation#GPL "Free Software Foundation").
It is inspired [Fishtest](/Stockfish#TestingFramework "Stockfish") and makes use of [distributed computing](https://en.wikipedia.org/wiki/Distributed_computing),
allowing anyone to contribute [CPU time](https://en.wikipedia.org/wiki/CPU_time) to further improve the development of open source chess engines.
OpenBench uses the [Django Web Framework](https://en.wikipedia.org/wiki/Django_(web_framework)) and [Cutechess](/Cute_Chess "Cute Chess") and applies the [sequential probability ratio test](/Match_Statistics#SPRT "Match Statistics") in engine versus engine matches,
and supports [Chess960](/Chess960 "Chess960"). OpenBench was the primary testing framework used for the development of [Ethereal](/Ethereal "Ethereal") [[1]](#cite_note-1).

# Clients

OpenBench client PCs need to be [POSIX](https://en.wikipedia.org/wiki/POSIX) compliant - that is [Windows](/Windows "Windows") clients require [MinGW](https://en.wikipedia.org/wiki/MinGW) [[2]](#cite_note-2) -
to build chess engine binaries on the fly assuming that [gcc](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)/g++ and [make](https://en.wikipedia.org/wiki/Make_(software)) are on the system path.
To get the sources, OpenBench will pull down a [zip file](https://en.wikipedia.org/wiki/ZIP_(file_format)) from [GitHub](https://en.wikipedia.org/wiki/GitHub).
Further, the client PC requires [Python 3](/Python "Python") and finally the OpenBench Client software itself [[3]](#cite_note-3).
The client is started with four arguments specifying the registered user name and password, the server [URL](https://en.wikipedia.org/wiki/URL) and the number of [threads](/Thread "Thread") used for engine matches [[4]](#cite_note-4):

```
python3 OpenBench.py -U username -P password -S http://chess.grantnet.us/ -T 4
```

# See also

- [Ethereal](/Ethereal "Ethereal")
- [Fishtest](/Stockfish#TestingFramework "Stockfish")
- [SPRT](/Match_Statistics#SPRT "Match Statistics")
- [Engines using OpenBench](/Category:OpenBench "Category:OpenBench")

# Forum Posts

## 2016 ...

- [SPRT when not used for self testing](http://www.talkchess.com/forum/viewtopic.php?t=61781) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), October 21, 2016 » [SPRT](/Match_Statistics#SPRT "Match Statistics")
- [A question about SPRT](http://www.talkchess.com/forum/viewtopic.php?t=62598) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), December 25, 2016
- [Testing A against B by playing a pool of others](http://www.talkchess.com/forum/viewtopic.php?t=64394) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), June 24, 2017 » [Match Statistics](/Match_Statistics "Match Statistics")
- [Basic automated testing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68531) by odomobo, [CCC](/CCC "CCC"), September 28, 2018

:   [Re:Basic automated testing](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68531&start=6) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), September 30, 2018

- [Any testing framwork similair to Fishtest that can be run locally ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70383) by [Mahmoud Uthman](/index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](/CCC "CCC"), April 02, 2019

## 2020 ...

- [Re: Looking for automatic Engine Testing Software](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74503&start=3) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), July 19, 2020
- [Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), October 09, 2020 » [Ethereal](/Ethereal "Ethereal")
- [OpenBench question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77074) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), April 13, 2021

# External Links

## OpenBench

- [GitHub - AndyGrant/OpenBench: OpenBench is a Distributed SPRT Testing Framework for Chess Engines](https://github.com/AndyGrant/OpenBench)
- [OpenBench/Client.py at master · AndyGrant/OpenBench · GitHub](https://github.com/AndyGrant/OpenBench/blob/master/Client/Client.py)
- [OpenBench](http://chess.grantnet.us/index/)

## Misc

- [Benchmark (computing) from Wikipedia](https://en.wikipedia.org/wiki/Benchmark_(computing))

# References

1. [↑](#cite_ref-1) [OpenBench/README.md at master · AndyGrant/OpenBench · GitHub](https://github.com/AndyGrant/OpenBench/blob/master/README.md)
2. [↑](#cite_ref-2) [GitHub - AndyGrant/OpenBench: OpenBench is a Distributed SPRT Testing Framework for Chess Engines - Setting Up The Client For Windows](https://github.com/AndyGrant/OpenBench#setting-up-the-client-for-windows)
3. [↑](#cite_ref-3) [OpenBench/Client.py at master · AndyGrant/OpenBench · GitHub](https://github.com/AndyGrant/OpenBench/blob/master/Client/Client.py)
4. [↑](#cite_ref-4) [GitHub - AndyGrant/OpenBench: OpenBench is a Distributed SPRT Testing Framework for Chess Engines - Running The Client](https://github.com/AndyGrant/OpenBench#running-the-client)

**[Up one Level](/Engine_Testing "Engine Testing")**