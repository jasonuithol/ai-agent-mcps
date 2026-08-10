# ChessX

Source: https://www.chessprogramming.org/ChessX

**[Home](/Main_Page "Main Page") \* [User Interface](/User_Interface "User Interface") \* [GUI](/GUI "GUI") \* ChessX**  
**[Home](/Main_Page "Main Page") \* [Software](/Software "Software") \* [Databases](/Databases "Databases") \* ChessX**

[![](/images/thumb/b/b7/Chessx.jpg/300px-Chessx.jpg)](https://sourceforge.net/projects/chessx/)

ChessX GUI [[1]](#cite_note-1)

**ChessX**,  
a free open source chess [database](/Databases "Databases") and [GUI](/GUI "GUI") for [Windows](/Windows "Windows"), [Linux](/Linux "Linux") and [Mac OS X](/Mac_OS "Mac OS") licensed under the [GNU General Public License v2](/Free_Software_Foundation#GPL "Free Software Foundation").
Initially, ChessX has started as a continuation of [SCID](/SCID "SCID"), but after some development, it was decided to break away from the [Tcl/Tk](/index.php?title=Tcl-Tk&action=edit&redlink=1 "Tcl-Tk (page does not exist)") code and start to program in [C++](/Cpp "Cpp") with [Qt](https://en.wikipedia.org/wiki/Qt_%28software%29)
[[2]](#cite_note-2).
Initially developed by [Michal Rudolf](/Michal_Rudolf "Michal Rudolf"), current developers and maintainers include [James Coons](/index.php?title=James_Coons&action=edit&redlink=1 "James Coons (page does not exist)") and [Jens Nissen](/index.php?title=Jens_Nissen&action=edit&redlink=1 "Jens Nissen (page does not exist)") [[3]](#cite_note-3).

# GUI

The ChessX [GUI](/GUI "GUI") implements a [tabbed document interface](https://en.wikipedia.org/wiki/Tab_%28GUI%29), the frame-window with caption, [menu](https://en.wikipedia.org/wiki/Menu_bar)- and [toolbars](https://en.wikipedia.org/wiki/Toolbar), and [status bar](https://en.wikipedia.org/wiki/Status_bar) at the bottom. A document window represents a game, and consists of a [board window](/GUI#BoardWindow "GUI") with configurable [notation pane](/GUI#NotationWindow "GUI"), game list of the current database, [opening](/Opening_Book "Opening Book") tree and [ECO](/ECO "ECO") panes, up to two analyze panes, and a database list window.

# Database

ChessX has an abstract *Database* C++ class, providing a common interface with methods for loading and saving of games, and for performing searches and queries. The concrete classes *MemoryDatabase* and *PgnDatabase*, derived from *Database*, implement the interface for [PGN](/Portable_Game_Notation "Portable Game Notation") file based databases. Large PGN databases are indexed keeping persistent index files (.cxi) for faster re-opening and search.

# Features

[[4]](#cite_note-4)

- Load and save [PGN](/Portable_Game_Notation "Portable Game Notation") files
- Work with multiple databases simultaneously
- Browse [chess games](/Chess_Game "Chess Game"), including variations
- [Enter moves](/Entering_Moves "Entering Moves"), variations, and comments
- Setup [board](/Chessboard "Chessboard"), copy/paste [FEN](/Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
- Search in Databases for text or [positions](/Chess_Position "Chess Position")
- Display tree of [moves](/Moves "Moves") for the current position
- Analyze using [UCI](/UCI "UCI") and [WinBoard](/WinBoard "WinBoard")/[XBoard](/XBoard "XBoard") Chess engines
- Prepare for [openings](/Opening "Opening") or opponents
- Training mode (next move is hidden)
- Integrated [Stockfish](/Stockfish "Stockfish") engine

# See also

- [Chess Assistant](/Chess_Assistant "Chess Assistant")
- [Chess Query Language](/Chess_Query_Language "Chess Query Language")
- [ChessBase (Database)](/ChessBase_(Database) "ChessBase (Database)")
- [HIARCS Chess Explorer](/HIARCS_Chess_Explorer "HIARCS Chess Explorer")
- [jose](/index.php?title=Jose&action=edit&redlink=1 "Jose (page does not exist)")
- [SCID](/SCID "SCID")
  - [ChessDB](/index.php?title=ChessDB&action=edit&redlink=1 "ChessDB (page does not exist)")
  - [Scid vs. PC](/Scid_vs._PC "Scid vs. PC")
  - [Scidb](/Scidb "Scidb")

# Forum Posts

- [New free chess database is out - ChessX](http://www.talkchess.com/forum/viewtopic.php?t=11911) by whp, [CCC](/CCC "CCC"), February 27, 2007
- [ChessX 0.3.0 is out!](http://www.talkchess.com/forum/viewtopic.php?t=13342) by whp, [CCC](/CCC "CCC"), April 23, 2007
- [New ChessX release](http://www.talkchess.com/forum/viewtopic.php?t=29282) by whp, [CCC](/CCC "CCC"), August 06, 2009
- [HIARCS Chess Explorer!! vs ChessX Free Chess Database!!](http://www.talkchess.com/forum/viewtopic.php?t=45076) by [Jose mº Velasco](/Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](/CCC "CCC"), September 10, 2012
- [ChessX Install](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=45848) by [Ted Summers](/Ted_Summers "Ted Summers"), [CCC](/CCC "CCC"), November 04, 2012
- [Limit time that engines may use for analysis](http://sourceforge.net/p/chessx/mailman/message/32443500/) by [Louis Zulli](/Louis_Zulli "Louis Zulli"), ChessX / Mailing Lists, June 10, 2014

# External Links

- [ChessX | Free Chess Database](http://chessx.sourceforge.net/)
- [ChessX download | SourceForge.net](https://sourceforge.net/projects/chessx/)
- [ChessX / Wiki / ChessX Manual](https://sourceforge.net/p/chessx/wiki/ChessX%20Manual/)

# References

1. [↑](#cite_ref-1) [ChessX download | SourceForge.net](https://sourceforge.net/projects/chessx/)
2. [↑](#cite_ref-2) [Scid, ChessDB and ChessX - Chess Teacher Lessons](http://www.chessteacherlessons.com/scid-chessdb-and-chessx/)
3. [↑](#cite_ref-3) [Development | ChessX](http://chessx.sourceforge.net/node/7)
4. [↑](#cite_ref-4) [ChessX | Free Games software downloads at SourceForge.net](https://sourceforge.net/projects/chessx/)

**[Up one Level](/Databases "Databases")**