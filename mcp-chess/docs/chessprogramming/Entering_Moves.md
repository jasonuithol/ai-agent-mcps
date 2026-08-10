# Entering Moves

Source: https://www.chessprogramming.org/Entering_Moves

**[Home](/Main_Page "Main Page") \* [User Interface](/User_Interface "User Interface") \* Entering Moves**

[![](/images/thumb/1/15/Bernstein-alex.1958.l02645391.ibm-archives.jpg/300px-Bernstein-alex.1958.l02645391.ibm-archives.jpg)](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f6482e6)

[Alex Bernstein](/Alex_Bernstein "Alex Bernstein") entering moves into the [IBM 704](/IBM_704 "IBM 704") console, 1958 [[1]](#cite_note-1)

**Entering Moves** is the [user's](https://en.wikipedia.org/wiki/User_%28computing%29) primary input while [interacting](https://en.wikipedia.org/wiki/Interaction) with the chess program during [game play](/Chess_Game "Chess Game"), to [make a move](/Make_Move "Make Move"). Chess engines using a [command line interface](/CLI "CLI") may rely on external chess user interfaces or [GUIs](/GUI "GUI") and their [protocols](/Protocols "Protocols") without dealing with possible ambiguous and order dependent user interactions while entering [moves](/Moves "Moves"), and receive moves in a defined [notation](/Game_Notation "Game Notation") via a [standard input stream](https://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29). The [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and the [Universal Chess Interface](/UCI "UCI") both use simple to [parse](https://en.wikipedia.org/wiki/Parsing) [pure algebraic coordinate notation](/Algebraic_Chess_Notation#PureCoordinateNotation "Algebraic Chess Notation") [[2]](#cite_note-2). XBoard version 2 has the option to switch on [SAN](/Algebraic_Chess_Notation#SAN "Algebraic Chess Notation"). Entering moves inside an [event driven](https://en.wikipedia.org/wiki/Event-driven_architecture) GUI, more intuitive for the casual user not familiar with chess coordinates, requires more effort for the GUI programmer.

# CLI

In a sequential [command line interface](/CLI "CLI") the chess program prompts for input. Unless [redirected](https://en.wikipedia.org/wiki/Redirection_%28computing%29), input is expected from the [keyboard](https://en.wikipedia.org/wiki/Keyboard_%28computing%29). In CLI, [text input](https://en.wikipedia.org/wiki/Typing) is usually [buffered](https://en.wikipedia.org/wiki/Keyboard_buffer) and [echoed](https://en.wikipedia.org/wiki/Echo_%28computing%29) by the [operating system](https://en.wikipedia.org/wiki/Operating_system) until the user confirms it by pressing the [enter- or return key](https://en.wikipedia.org/wiki/Enter_key), causing the OS to transfer the whole text line via [standard streams](https://en.wikipedia.org/wiki/Standard_streams) to the program.

The user has to type in his move according to the syntax or [notation](/Game_Notation "Game Notation") the program or GUI understands, most common [pure algebraic coordinate notation](/Algebraic_Chess_Notation#PureCoordinateNotation "Algebraic Chess Notation") as used in the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and the [Universal Chess Interface](/UCI "UCI"), that is:

```
<move notation> ::= <from square><to square>[<promoted to>]
<square>        ::= <file letter><rank number>
<file letter>   ::= 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'
<rank number>   ::= '1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'
<promoted to>   ::= 'q'|'r'|'b'|'n'
```

A from-to delimiter, a dash, hyphen or space for [quiet moves](/Quiet_Moves "Quiet Moves") or 'x' or colon for [captures](/Captures "Captures"), is usually omitted and may only used in a [notation window](/GUI#NotationWindow "GUI") to make it easier to read for humans. Castles are given by king from-to coordinates ('e1g1', 'e1c1') or its own syntax of 'O-O' or 'O-O-O', also required for [Chess960](/Chess960 "Chess960").

# GUI

Event driven [graphical user interfaces](/GUI "GUI") allow more flexible interactions to enter moves. While this is more user friendly, it is more effort for the GUI programmer, due to the implementation of a [finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine) for various states, modes and actions of a sequence of move entering interactions by a [pointing device](https://en.wikipedia.org/wiki/Pointing_device) and/or keyboard, considering possible different [focus windows](https://en.wikipedia.org/wiki/Focus_%28computing%29) like [board window](/GUI#BoardWindow "GUI"), [notation window](/GUI#NotationWindow "GUI") or a dedicated CLI-like command window or [form](https://en.wikipedia.org/wiki/Form_%28programming%29), and also focus changes.

## Board Interactions

### Drag-and-drop

The "natural" way to enter moves, similar to the interactions of a real chessboard, is [drag-and-drop](https://en.wikipedia.org/wiki/Drag-and-drop) with the pointing device, also emulated by the keyboard. The user first selects the [piece](/Pieces "Pieces") on its [departure square](/Origin_Square "Origin Square"), grabs it by [clicking](https://en.wikipedia.org/wiki/Point-and-click) a device button, to drag it to the [destination square](/Target_Square "Target Square"), where the button is released to drop the piece. Another pointing device alternative without dragging is to select both squares in any order. A drag-and-drop or click-click keyboard simulation would require a square [cursor](https://en.wikipedia.org/wiki/Cursor_%28computers%29), navigated by [arrow keys](https://en.wikipedia.org/wiki/Arrow_keys) and/or entering square coordinates ([file](/Files "Files") letter and [rank](/Ranks "Ranks") number in any order), and for instance the space key to grab and drop the piece.

### Assistants

Some GUIs support casual players by indicating all possible destination squares after selecting the piece, or the other way around, after first selecting a destination square, highlighting all pieces on the board which may move to that square.

[![ChessForAndroidv1.png](/images/c/c4/ChessForAndroidv1.png)](/@http://www.aartbik.com/MISC/android.html "@http://www.aartbik.com/MISC/android.html")

[Aart Bik's](/Aart_Bik "Aart Bik") [Chess for Android](/Chess_for_Android "Chess for Android"), selecting f3 shows all queen targets highlighted [[3]](#cite_note-3)

Advanced modes for ambitious Blitz players may already confirm the move entering interaction, if only one piece can move to a selected destination square, or if a selected piece has only one move. Similar is possible for moves that seem plausible according to some move entering heuristics, for instance *Heumas* (Heuristic Move Assistant - developed by [Chrilly Donninger](/Chrilly_Donninger "Chrilly Donninger") [[4]](#cite_note-4) ), as used in [ChessBase](/ChessBase "ChessBase") or [Fritz GUI](/Fritz#FritzGUI "Fritz") [[5]](#cite_note-5) .

### Promotions

[Promotions](/Promotions "Promotions") require the additional interaction to chose a piece, which might be implemented via a [menu](https://en.wikipedia.org/wiki/Context_menu) popping up on the [promotion square](/Promotion_Square "Promotion Square"), temporarily grabbing the keyboard focus - or similar, but slightly less comfortable, using a [modal dialog](https://en.wikipedia.org/wiki/Modal_window) with a small [list box](https://en.wikipedia.org/wiki/List_box) or four [radio-buttons](https://en.wikipedia.org/wiki/Radio_button) and an [OK button](https://en.wikipedia.org/wiki/Okay#Computers) to confirm, in all cases queening as default. Entering a piece letter should be appropriate as well to finish the sequence of move entering interactions.

## Move List Interactions

If the notation window has the keyboard focus, pressing a none control key may activate a [text box](https://en.wikipedia.org/wiki/Text_box) to enter moves in various notations like [pure algebraic coordinates](/Algebraic_Chess_Notation#PureCoordinateNotation "Algebraic Chess Notation"), [LAN](/Algebraic_Chess_Notation#LAN "Algebraic Chess Notation") or [SAN](/Algebraic_Chess_Notation#SAN "Algebraic Chess Notation"). Further, a [Content assist](https://en.wikipedia.org/wiki/Content_assist) or [combo box](https://en.wikipedia.org/wiki/Combo_box) may list all possible moves, where the user may choose one.

# Dedicated Chess Computers

[Dedicated Chess Computers](/Dedicated_Chess_Computers "Dedicated Chess Computers") have their own move entering systems, the board computers likely [sensory boards](/Sensory_Board "Sensory Board") with pressure-sensitive switches or [piece recognition](/Piece_Recognition "Piece Recognition"). Small chess computers often have a dedicated coordinate keyboard, eight keys to enter file and rank in context of from- and then to-square.

[![ElektorCC.jpg](/images/0/03/ElektorCC.jpg)](http://www.andreadrian.de/schach/#Selbstbau_Schachcomputer_SHAH)

[Elektor](https://en.wikipedia.org/wiki/Elektor) Chess Computer with [Micro-Max](/Micro-Max "Micro-Max") inside [[6]](#cite_note-6)

More minimalistic systems, like [Harm Geert Muller's](/Harm_Geert_Muller "Harm Geert Muller") [Matchbox Usurpator](/Usurpator#Matchbox "Usurpator") [[7]](#cite_note-7) [[8]](#cite_note-8) , even managed move input with only one switch and some mode feedback from the display.

# Computer Vision

Chess playing [Robots](/Robots "Robots") may recognize the moves their (human) opponents made on an ordinary chess board in a more sophisticated way by [computer vision](https://en.wikipedia.org/wiki/Computer_vision) [[9]](#cite_note-9) and [real-time](https://en.wikipedia.org/wiki/Real-time) video [image processing](https://en.wikipedia.org/wiki/Image_processing).

# Parsing

While [parsing](https://en.wikipedia.org/wiki/Parsing) move notations, especially [SAN](/Algebraic_Chess_Notation#SAN "Algebraic Chess Notation") [[10]](#cite_note-10), it is handy to have a [list](/Move_List "Move List") of [legal moves](/Legal_Move "Legal Move") available for the current position the engine is pondering on. Programs may tolerate redundant, overdetermined from-square specifications in SAN like given by LAN, including dash or hyphen. Leading piece letters are supposed to be upper case, while file letters and promoted piece letters should be lower case characters.

# See also

- [Algebraic Chess Notation](/Algebraic_Chess_Notation "Algebraic Chess Notation")
- [Dedicated Chess Computers](/Dedicated_Chess_Computers "Dedicated Chess Computers")
- [Graphical User Interface](/GUI "GUI")
- [Protocols](/Protocols "Protocols")
- [Robots](/Robots "Robots")
- [Voice User Interface](/index.php?title=Voice_User_Interface&action=edit&redlink=1 "Voice User Interface (page does not exist)")

# Publications

- [Alex Bernstein](/Alex_Bernstein "Alex Bernstein"), [Michael de V. Roberts](/Michael_de_V._Roberts "Michael de V. Roberts") (**1958**). *[Computer vs. Chess-Player](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f690f16)*. [Scientific American](/Scientific_American "Scientific American"), Vol. 198, pp. 96-105. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-2.Computer_V_ChessPlayer.Bernstein_Roberts.Scientific_American.June-1958/Computer_V_ChessPlayer.Bernstein_Roberts.Scientific_American.June-1958.062303059.sm.pdf) from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum"), reprinted 1988 in [Computer Chess Compendium](/Computer_Chess_Compendium "Computer Chess Compendium")
- [Andrew Koenig](/Andrew_Koenig "Andrew Koenig") (**1978**). *Light-Pen used in game*. [Personal Computing, Vol. 2, No. 5](/Personal_Computing#2_5 "Personal Computing"), pp. 112 » [CCCP](/CCCP_(US) "CCCP (US)")

# External Links

- [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) by [Steven Edwards](/Steven_Edwards "Steven Edwards")
- [Input device from Wikipedia](https://en.wikipedia.org/wiki/Input_device)
- [Human interface device](https://en.wikipedia.org/wiki/Human_interface_device)
- [Computer keyboard](https://en.wikipedia.org/wiki/Computer_keyboard)
- [Mouse (computing)](https://en.wikipedia.org/wiki/Mouse_%28computing%29)
- [Touchscreen](https://en.wikipedia.org/wiki/Touchscreen)

# References

1. [↑](#cite_ref-1) [IBM programmer Alex Bernstein](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f6482e6) 1958 Courtesy of [IBM](/index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") Archives from [The Computer History Museum](/The_Computer_History_Museum "The Computer History Museum")
2. [↑](#cite_ref-2) see [CPW-Engine\_algebraic](/CPW-Engine_algebraic "CPW-Engine algebraic")
3. [↑](#cite_ref-3) [Aart's Android Page](http://www.aartbik.com/MISC/android.html)
4. [↑](#cite_ref-4) [Eingabehilfe "Heumas" bei ChessBase 7.0](http://www.scleinzell.schachvereine.de/p_wm_tipps/tipps0006.shtml#2) by [Peter Schreiner](/Peter_Schreiner "Peter Schreiner") (German), [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml)
5. [↑](#cite_ref-5) [Support - ChessBase: August 16th, 1998](http://www.chessbase.com/support/support.asp?pid=8)
6. [↑](#cite_ref-6) [Elektor](https://en.wikipedia.org/wiki/Elektor) Chess Computer from [Computer Schach](http://www.andreadrian.de/schach/) by [Andre Adrian](/Andre_Adrian "Andre Adrian") (German)
7. [↑](#cite_ref-7) [HGM's Chess Pages](http://home.hccnet.nl/h.g.muller/chess.html)
8. [↑](#cite_ref-8) [Harm Geert Muller](/Harm_Geert_Muller "Harm Geert Muller") (**1990**). *A Matchbox Chess Computer*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 13, No. 4
9. [↑](#cite_ref-9) [Chua Huiyan](http://de.scientificcommons.org/huiyan_chua), Le Vinh, [Wong Lai Kuan](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/k/Kuan:Wong_Lai.html) (**2007**). *Chess Vision*. [School of Computing](https://en.wikipedia.org/wiki/NUS_School_of_Computing), [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [slides as pdf](http://www.comp.nus.edu.sg/~cs4243/showcase/chess_vision/Chess-Vision-Presentation.pdf)
10. [↑](#cite_ref-10) [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) by [Steven Edwards](/Steven_Edwards "Steven Edwards") - 8.2.3: Movetext SAN (Standard Algebraic Notation)

**[Up one Level](/User_Interface "User Interface")**