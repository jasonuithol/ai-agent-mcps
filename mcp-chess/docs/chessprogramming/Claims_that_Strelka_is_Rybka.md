# Claims that Strelka is Rybka

Source: https://www.chessprogramming.org/Claims_that_Strelka_is_Rybka

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* Claims that Strelka is Rybka**

Quote by [Vasik Rajlich](/Vasik_Rajlich "Vasik Rajlich") on [Strelka 2.0](/Strelka "Strelka"), January 11, 2008 [[1]](#cite_note-1)

|  |
| --- |
| I've taken a look this morning at the *Strelka* 2.0 sources. The picture is quite clear Vast sections of these sources started their life as a decompiled Rybka 1.0. The traces of this are everywhere. The board representation is identical, and all sorts of absolutely unique Rybka code methods, bitboard tricks and even exact data tables are used throughout. Significant portions of the search and evaluation logic are not fully disassembled - the author has left in hardcoded constants and used generic names (such as "PawnStruScore0" & "PawnStruScore1", "PassedPawnValue0" through "PassedPawnValue7", etc) which show that he hasn't yet fully understood what is happening.  In some cases, these traces do also extend beyond the inner search and evaluation kernel. For instance, Rybka and *Strelka* are the only engines which I know about which don't report "seldepth" and "hashfull". Rybka's UCI strings are used throughout.  The author did at first make attempts to hide the Rybka origins, for example by masking the table values in earlier *Strelka* versions. He also made significant attempts to improve the program. The attempts at improvement are not very original, but they are everywhere. They include PV collection, null verification (and in fact changes to the null implementation itself), some endgame drawishness heuristics, a handful of new evaluation term, a new approach to blending between opening and endgame eval terms, and so on. They also do include various structural changes, such as knight underpromotions, on-the-fly calculations of many tables, the setting of piece-square table values, etc. These changes are extensive and no doubt lead to differences in playing style and perhaps a useful engine for users to have, but they do not change the illegality of the code base.  In light of the above, I am claiming *Strelka* 2.0 as my own and will release it in the next few days under my own name. The name of the author with the pen name "Osipov" will be included if he comes forward with hiw own real name, otherwise an anonymous contribution will be noted. The contributions of Igor Korshunov will also be confirmed and noted if appropriate. All usage permissions will be granted with this release.  I do not see obvious signs of other code usage, but perhaps this deserves a closer look. Some of the transplanted ideas, such as the null verification search, are rather naive implementations of the approach in Fruit/Toga, although my first impression is that that code itself is original. The Winboard parser from Beowolf which was added to *Strelka* 1.0 seems to have been completely removed. If someone else does find other signs of code theft, please get in touch with me and I will give proper credit in the upcoming release.  If someone has suggestions about an appropriate license, and in particular the pros and cons of the GPL for a chess engine and for this unusual scenario, or if someone would be willing to help in preparing this code and license for release, please also get in touch with me.  As this code is two years and several hundred Elo old, I am not going to launch any major action. However, 'Osipov' has already threatened to repeat the procedure with Rybka 2.3.2a. (He did this after I declined to grant him rights to commercialize *Strelka*.) If this situation does repeat with a newer Rybka version, I will not just stand and watch any more. In the meantime, if someone has information about 'Osipov', please get in touch with me.  Vas |

# See also

- [Claims of Rybka Originality](/Claims_of_Rybka_Originality "Claims of Rybka Originality")
- [Pre-Fruit Rybka and Crafty](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty")
- [Rybka](/Rybka "Rybka")
- [Strelka](/Strelka "Strelka")

# References

1. [↑](#cite_ref-1) [Strelka 2.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=39198) by [Vasik Rajlich](/Vasik_Rajlich "Vasik Rajlich"), [Rybka Rorum](/Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008

**[Up one level](/Rybka_Controversy "Rybka Controversy")**