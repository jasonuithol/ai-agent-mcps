# Botvinnik-Markoff Extension

Source: https://www.chessprogramming.org/Botvinnik-Markoff_Extension

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Extensions](/Extensions "Extensions") \* Botvinnik-Markoff Extension**

The **Botvinnik-Markoff Extension** is an extension proposed by [Sergei Markoff](/Sergei_Markoff "Sergei Markoff") [[1]](#cite_note-1), inspired by [Mikhail Botvinnik's](/Mikhail_Botvinnik "Mikhail Botvinnik") work and publications on the program [Pioneer](/Pioneer "Pioneer"), for instance to determine attack/defense targets for further analysis of attack/defense [trajectories](/Trajectory "Trajectory") [[2]](#cite_note-2). The extension is based on the [threat move detection](/Null_Move_Pruning#ThreatDetection "Null Move Pruning") in [null move pruning](/Null_Move_Pruning "Null Move Pruning"). If the [threat move](/Threat_Move "Threat Move") is the same on two consecutive plies (with one ply in between them to account for the side to move), the threat move is a serious one and the search is extended.

# See also

- [Mate Threat Extensions](/Mate_Threat_Extensions "Mate Threat Extensions")
- [Threat Detection](/Null_Move_Pruning#ThreatDetection "Null Move Pruning")

# Forum Posts

- [Markoff - Botvinnik - Kaissa - Hsu - ABC - Berliner](https://www.stmintz.com/ccc/index.php?id=299987) by [Walter Faxon](/Walter_Faxon "Walter Faxon"), [CCC](/CCC "CCC"), June 09, 2003
- [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), October 01, 2003, introducing the extension
- [Test match with the Botvinnik-Markoff extension](https://www.stmintz.com/ccc/index.php?id=318987) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [CCC](/CCC "CCC"), October 02, 2003
- [What is Botvinnik-Markov extension?](https://www.stmintz.com/ccc/index.php?id=457918) by [Maurizio Monge](/Maurizio_Monge "Maurizio Monge"), [CCC](/CCC "CCC"), October 26, 2005
- [Botvinnik Markov revisited](http://www.talkchess.com/forum/viewtopic.php?t=35124) by [Don Dailey](/Don_Dailey "Don Dailey"), [CCC](/CCC "CCC") , Jun 24, 2010

# References

1. [↑](#cite_ref-1) [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), October 01, 2003
2. [↑](#cite_ref-2) [Mikhail Botvinnik](/Mikhail_Botvinnik "Mikhail Botvinnik") (**1982**). *Decision Making and Computers.* [Advances in Computer Chess 3](/Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")

**[Up one level](/Extensions "Extensions")**