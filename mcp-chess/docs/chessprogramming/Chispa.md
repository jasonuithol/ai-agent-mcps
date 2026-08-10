# Chispa

Source: https://www.chessprogramming.org/Chispa

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Chispa**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Lichtenberg_figure_in_block_of_Plexiglas.jpg/330px-Lichtenberg_figure_in_block_of_Plexiglas.jpg)](/File:Lichtenberg_figure_in_block_of_Plexiglas.jpg)

[Lichtenberg Figure](https://en.wikipedia.org/wiki/Lichtenberg_figure) [[1]](#cite_note-1) [[2]](#cite_note-2)

**Chispa**,  
a [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](/UCI "UCI") compatible chess engine by [Federico Andrés Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), written in [C++](/Cpp "Cpp").
Its development started in mid 2002, first released in January 2003 [[3]](#cite_note-3) as pure [WinBoard](/WinBoard "WinBoard") engine written in [C](/C "C"), rewritten to C++ in 2004 [[4]](#cite_note-4).
Chispa uses the common [negamax](/Negamax "Negamax") [PVS](/Principal_Variation_Search "Principal Variation Search") [alpha-beta](/Alpha-Beta "Alpha-Beta") with a two-level [transposition table](/Transposition_Table "Transposition Table"), [null-move pruning](/Null_Move_Pruning "Null Move Pruning") with [R = 2](/Depth_Reduction_R "Depth Reduction R"), [static exchange evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation"), [opening book](/Opening_Book "Opening Book"), is able to probe [Nalimov Tablebases](/Nalimov_Tablebases "Nalimov Tablebases"), and was one of the first engines to play [Chess960](/Chess960 "Chess960") [[5]](#cite_note-5).
Chispa is [Arena](/Arena "Arena") partner engine.

# See also

- [HeavyChess](/HeavyChess "HeavyChess")
- [Spark](/Spark "Spark")

# Forum Posts

## 2003

- [New WB Engine: Chispa 1.0 (ARG)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=40589&p=154903) by Ed Seid, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 04, 2003
- [I send to Ed the new Chispa 1.54](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=40827&p=155641) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 18, 2003
- [Chispa 2.0 needs 2-3 betatesters](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41516&p=158315) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 03, 2003
- [Chispa 2.1 is available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41627&p=158817) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 09, 2003
- [Chispa 3.0 beta 1 is available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41996&p=160389) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 31, 2003
- [Chispa 3.0 beta 5 is available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42286&p=161513) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), April 18, 2003
- [Chispa news](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43819&p=167366) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), August 18, 2003
- [Post Chispa questions here](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44007&p=168062) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 06, 2003
- [Chispa v3.93 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44128&p=168482) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 14, 2003
- [Chispa v3.95 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44290&p=169037) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 26, 2003
- [Chispa v3.98d released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45251&p=172103) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), November 22, 2003
- [Nifty little feature in Chispa](https://www.stmintz.com/ccc/index.php?id=335701) by Geoff, [CCC](/CCC "CCC"), December 13, 2003

:   [I use this in Chispa](https://www.stmintz.com/ccc/index.php?id=335845) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](/CCC "CCC"), December 13, 2003

## 2004

- [Today is Chispa's First Birthday](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45891&p=174306) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 04, 2004
- [I really need your help testing Chispa](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46000&p=174594) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 10, 2004
- [Chispa 4.0 Pre-Release 1 is ready](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=49061&p=185165) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), September 25, 2004
- [Chispa 4.0 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=972&p=4169) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 13, 2004

## 2005 ...

- [Chispa impressions and problems](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1226&p=5536) by [Peter Berger](/Peter_Berger "Peter Berger"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 02, 2005
- [Chispa 4.0.3 for Linux static available](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1634&p=7591) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), February 12, 2005
- [Question about obtaining Chispa](http://www.talkchess.com/forum/viewtopic.php?t=47404) by James I, [CCC](/CCC "CCC"), March 04, 2013

# External Links

## Chess Engine

- [Chispa Chess Engine](http://chispachess.blogspot.com)
- [Index of /fedecorigliano/ajedrez/chispa](http://www.oocities.org/ar/fedecorigliano/ajedrez/chispa/)
- [Chispa 4.0.3](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Chispa%204.0.3) in [CCRL 40/2](/CCRL "CCRL")
- [Chispa 4.0.3](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=Chispa+4.0.3) in [CCRL 40/15](/CCRL "CCRL")
- [Chispa 4.0.3](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Chispa+4.0.3) in [KCEC](/KCEC "KCEC")

## Misc

- [chispa - Wiktionary](https://en.wiktionary.org/wiki/chispa)
- [Descarga electrostática - Wikipedia.es](https://es.wikipedia.org/wiki/Descarga_electrost%C3%A1tica) (Spanish)

# References

1. [↑](#cite_ref-1) [High voltage](https://en.wikipedia.org/wiki/High_voltage) [dielectric breakdown](https://en.wikipedia.org/wiki/Electrical_breakdown) within a block of [plexiglas](https://en.wikipedia.org/wiki/Poly%28methyl_methacrylate%29) creates a beautiful [fractal pattern](https://en.wikipedia.org/wiki/Fractal) called a [Lichtenberg Figure](https://en.wikipedia.org/wiki/Lichtenberg_figure). The branching discharges ultimately become hairlike, but are thought to extend down to the molecular level, by [Bert Hickman](https://www.youtube.com/user/BertHickman), [Teslamania, Bert Hickman's site about Quarter Shrinking, Lichtenberg Figures, Tesla Coils, Nikola Tesla, Pulsed Power, and big Arcs and Sparks](http://www.capturedlightning.com/), [Electrical breakdown from Wikipedia](https://en.wikipedia.org/wiki/Electrical_breakdown)
2. [↑](#cite_ref-2) [Mathematician - Georg Christoph Lichtenberg](/Mathematician#Lichtenberg "Mathematician")
3. [↑](#cite_ref-3) [New WB Engine: Chispa 1.0 (ARG)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=40589&p=154903) by Ed Seid, [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 04, 2003
4. [↑](#cite_ref-4) [Today is Chispa's First Birthday](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45891&p=174306) by [Federico Corigliano](/Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [Winboard Forum](/Computer_Chess_Forums "Computer Chess Forums"), January 04, 2004
5. [↑](#cite_ref-5) [Arena Chess GUI 3.5 - Chispa](http://www.playwitharena.com/?Partner_Chess_Engines:Chispa%26nbsp%3B)

**[Up one Level](/Engines "Engines")**