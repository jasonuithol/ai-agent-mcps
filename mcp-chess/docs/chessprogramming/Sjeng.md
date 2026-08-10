# Sjeng

Source: https://www.chessprogramming.org/Sjeng

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Sjeng**

**Sjeng**,  
an [open source engine](/Category:Open_Source "Category:Open Source") written by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto") with help from [Adrien Regimbald](/Adrien_Regimbald "Adrien Regimbald"), [Daniel Clausen](/index.php?title=Daniel_Clausen&action=edit&redlink=1 "Daniel Clausen (page does not exist)"), [Dann Corbit](/Dann_Corbit "Dann Corbit"), [Lenny Taelman](/index.php?title=Lenny_Taelman&action=edit&redlink=1 "Lenny Taelman (page does not exist)"), [Ben Nye](/index.php?title=Ben_Nye&action=edit&redlink=1 "Ben Nye (page does not exist)"), [Ronald de Man](/Ronald_de_Man "Ronald de Man"), [David Dawson](/index.php?title=David_Dawson&action=edit&redlink=1 "David Dawson (page does not exist)"), [Tim Foden](/Tim_Foden "Tim Foden") and [Georg von Zimmermann](/Georg_von_Zimmermann "Georg von Zimmermann") [[1]](#cite_note-1). Sjeng was initially based on [Faile 0.6](/Faile "Faile") by [Adrien Regimbald](/Adrien_Regimbald "Adrien Regimbald") [[2]](#cite_note-2), and an attempt to create a [Bughouse](/index.php?title=Bughouse&action=edit&redlink=1 "Bughouse (page does not exist)") & [Crazyhouse](/Crazyhouse "Crazyhouse") playing program. Sjeng 7 became open source under the [GPL](/Free_Software_Foundation#GPL "Free Software Foundation"), also playing [standard](/Chess "Chess") and [Antichess](/Losing_Chess "Losing Chess") [[3]](#cite_note-3). The [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant Sjeng 11.2 was the final open source program released in January 2002 [[4]](#cite_note-4), while Sjeng 12.7 was closed source, didn't play variants, and emerged to the commercial [Deep Sjeng](/Deep_Sjeng "Deep Sjeng") in 2003, initially market by [Lex Loep's](/Lex_Loep "Lex Loep") [Lokasoft](/Lokasoft "Lokasoft") [[5]](#cite_note-5).

# Description

In it's [suicide and loser's](/Losing_Chess "Losing Chess") mode, Sjeng applies [proof-number search](/Proof-Number_Search "Proof-Number Search"). Otherwise it uses [alpha-beta](/Alpha-Beta "Alpha-Beta") with [aspiration window](/Aspiration_Windows "Aspiration Windows") and [PVS](/Principal_Variation_Search "Principal Variation Search"), [history heuristic](/History_Heuristic "History Heuristic"), [killer heuristic](/Killer_Heuristic "Killer Heuristic"), [transposition tables](/Transposition_Table "Transposition Table"), [SEE](/Static_Exchange_Evaluation "Static Exchange Evaluation") for [move ordering](/Move_Ordering "Move Ordering") and [pruning](/Pruning "Pruning"), [selective extensions](/Extensions "Extensions"), [adaptive null move pruning](/Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [extended futility pruning](/Futility_Pruning#Extendedfutilitypruning "Futility Pruning"), [limited razoring](/Razoring#LimitedRazoring "Razoring"), and [opening book learning](/Book_Learning "Book Learning") [[6]](#cite_note-6). Sjeng is the engine of [Apple's](/index.php?title=Apple&action=edit&redlink=1 "Apple (page does not exist)") chess application as shipped in [MacOS X 10.4](/Mac_OS "Mac OS") [[7]](#cite_note-7) [[8]](#cite_note-8) [[9]](#cite_note-9).

# Etymology

The name Sjeng, which is also a [Limburgish](https://en.wikipedia.org/wiki/Limburgish_language) masculine given name, is the reverse of the long time number one human Bughouse player, with the handle "Gnejs" [[10]](#cite_note-10) [[11]](#cite_note-11).

# See also

- [Deep Sjeng](/Deep_Sjeng "Deep Sjeng")

# Forum Posts

## 2000 ...

- [Sjeng 7 out - with sources now (GPL)](https://www.stmintz.com/ccc/index.php?id=106176) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), April 15, 2000
- [Sjeng 10 has been released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b9ebbbdba6c8b9f3) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), June 7, 2001
- [Sjeng 12.7 and 11.2 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/66707061247326df) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 2, 2002
- [Sjeng 12.10 released (UCI support!)](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1d26baa93648f128) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 22, 2002
- [Sjeng 12.11 Released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2989a0b857e92c94) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), April 2, 2002
- [sjeng's suicide tablebases](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/fe2e9d80451eb343) by [Jean Efpraxiadis](/index.php?title=Jean_Efpraxiadis&action=edit&redlink=1 "Jean Efpraxiadis (page does not exist)"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), July 11, 2002

## 2010 ...

- [Sjeng 11.2 and suicide chess](http://www.talkchess.com/forum/viewtopic.php?t=45003) by [Michel Van den Bergh](/Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](/CCC "CCC"), September 03, 2012

# External Links

## Chess Engine

- [Sjeng's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=72) (includes [Deep Sjeng](/Deep_Sjeng "Deep Sjeng"))
- [Sjeng : a chess-and-variants playing program](https://www.sjeng.org/indexold.html)
- [GitHub - gcp/sjeng: A chess and chess variants playing program](https://github.com/gcp/sjeng)
- [Sjeng (Chess) from Wikipedia](https://en.wikipedia.org/wiki/Sjeng_%28Chess%29)

## Chess Variants

- [Antichess from Wikipedia](https://en.wikipedia.org/wiki/Antichess)
- [Bughouse chess from Wikipedia](https://en.wikipedia.org/wiki/Bughouse_chess)
- [Crazyhouse from Wikipedia](https://en.wikipedia.org/wiki/Crazyhouse)

## Misc

- [Sjeng (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Sjeng)
- [Sjeng (name) from Wikipedia](https://en.wikipedia.org/wiki/Sjeng_%28name%29)

# References

1. [↑](#cite_ref-1) [Sjeng : a chess-and-variants playing program - 7. Who wrote Sjeng ?](http://sjeng.org/indexold.html)
2. [↑](#cite_ref-2) [Re: Dutch CC all games available](https://www.stmintz.com/ccc/index.php?id=195551) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), November 04, 2001
3. [↑](#cite_ref-3) [ICGA: Losing Chess](http://ilk.uvt.nl/icga/games/losingchess/) by [Guy Haworth](/Guy_Haworth "Guy Haworth")
4. [↑](#cite_ref-4) [Sjeng 12.7 and 11.2 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/66707061247326df) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), January 2, 2002
5. [↑](#cite_ref-5) [Deep Sjeng 1.0 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/261bfb217175033a) by [Lex](/Lex_Loep "Lex Loep"), [rgcc](/Computer_Chess_Forums "Computer Chess Forums"), March 3, 2003
6. [↑](#cite_ref-6) [Sjeng Download - Readme](http://sjeng.org/download.html)
7. [↑](#cite_ref-7) [Chess (application) from Wikipedia](https://en.wikipedia.org/wiki/Chess_%28application%29)
8. [↑](#cite_ref-8) [Chess - Source Browser](http://www.opensource.apple.com/source/Chess/Chess-110.0.6/)
9. [↑](#cite_ref-9) [README](http://www.opensource.apple.com/source/Chess/Chess-110.0.6/README)
10. [↑](#cite_ref-10) [Yes, there are](https://www.stmintz.com/ccc/index.php?id=298890) by [Georg von Zimmermann](/Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](/CCC "CCC"), June 01, 2003
11. [↑](#cite_ref-11) [Eric van Reem](/Eric_van_Reem "Eric van Reem") (**2001**). *Tiger und Rebel gleichauf in Leiden*. [Computerschach und Spiele](/Computerschach_und_Spiele "Computerschach und Spiele"), 6/2001 (German)

**[Up one Level](/Engines "Engines")**