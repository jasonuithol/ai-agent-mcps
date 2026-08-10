# ChessCore

Source: https://www.chessprogramming.org/ChessCore

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* ChessCore**

[![](/images/4/49/OnlineChessSmall.jpg)](https://web.archive.org/web/20120105083121/http://www.chessbin.com/)

ChessBin.com chess [[1]](#cite_note-1)

**ChessCore**, (ChessBin.com)  
a chess engine by [Adam Berent](/Adam_Berent "Adam Berent"), written in [C#](/C_sharp "C sharp").
The *ChessBin.com* chess engine was documented in a blog format [[2]](#cite_note-2), and has been converted to cross-platform [.NET Core](https://en.wikipedia.org/wiki/.NET_Core) dubbed **ChessCore**, [open source](/Category:Open_Source "Category:Open Source") under the [MIT License](/Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") published on [GitHub](https://en.wikipedia.org/wiki/GitHub) [[3]](#cite_note-3).
The program makes heavy use of the .NET Core [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) (GC)
[[4]](#cite_note-4) and is mentioned as buggy in [Ron Murawski's](/Ron_Murawski "Ron Murawski") engine list [[5]](#cite_note-5).

# Evaluate Moves

One sample of ChessCore's extensive GC usage demonstrates its [Alpha-Beta](/Alpha-Beta "Alpha-Beta") search - at each [node](/Node "Node") it [generates](/Move_Generation "Move Generation") and sorts all moves (or [captures](/Captures "Captures") in [quiescence](/Quiescence_Search "Quiescence Search")) [[6]](#cite_note-6), and allocates the [move list](/Move_List "Move List") and each generated [move](/Moves "Moves") on the [heap](/Data#Dynamic_Data "Data") [[7]](#cite_note-7):
For some reason, internal class *position* encapsulates the move.

```
private static List<Position> EvaluateMoves(Board examineBoard, byte depth) {
  ...
  List<Position> positions = new List<Position>();
  for (byte x = 0; x < 64; x++) { ...
    Piece piece = examineBoard.Squares[x].Piece;
    ... continue if empty or opponent piece
    foreach (byte dst in piece.ValidMoves) { ...
      Position move = new Position(x, dst);
      ... Score move, killers, etc ..
      positions.Add(move); 
    }
  }
  return positions;
}
```

# Publications

- [Adam Berent](/Adam_Berent "Adam Berent") (**2014**). *Guide to Programming a Chess Engine*. [pdf](https://www.adamberent.com/wp-content/uploads/2019/02/GuideToProgrammingChessEngine.pdf)

# Forum Posts

- [New Member Introduction](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29027) by [Adam Berent](/Adam_Berent "Adam Berent"), [CCC](/CCC "CCC"), July 19, 2009
- [I need help, performance wall!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=30265) by [Adam Berent](/Adam_Berent "Adam Berent"), [CCC](/CCC "CCC"), October 21, 2009
- [ChessBin 00.59](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=31312) by [Harun Taner](/Harun_Taner "Harun Taner"), [CCC](/CCC "CCC"), December 28, 2009

# External Links

- [GitHub - 3583Bytes/ChessCore: Chess Engine Implemented in .net core](https://github.com/3583Bytes/ChessCore)
- [Chess – Adam Berent](https://www.adamberent.com/home/chess/)
- [Computer Chess – Adam Berent](https://www.adamberent.com/home/chess/computer-chess/)
- [Computer Chess Information and Resources](https://web.archive.org/web/20120105083121/http://www.chessbin.com/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

# References

1. [↑](#cite_ref-1) [Computer Chess Information and Resources](https://web.archive.org/web/20120105083121/http://www.chessbin.com/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
2. [↑](#cite_ref-2) [Adam Berent](/Adam_Berent "Adam Berent") (**2014**). *Guide to Programming a Chess Engine*. [pdf](https://www.adamberent.com/wp-content/uploads/2019/02/GuideToProgrammingChessEngine.pdf)
3. [↑](#cite_ref-3) [GitHub - 3583Bytes/ChessCore: Chess Engine Implemented in .net core](https://github.com/3583Bytes/ChessCore)
4. [↑](#cite_ref-4) [.NET Core - Garbage Collection - Tutorialspoint](https://www.tutorialspoint.com/dotnet_core/dotnet_core_garbage_collection.htm)
5. [↑](#cite_ref-5) [Chess Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:chess_engine_list) from [Ron Murawski's](/Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
6. [↑](#cite_ref-6) [Re: I need help, performance wall!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=30265&start=4) by [Sven Schüle](/Sven_Sch%C3%BCle "Sven Schüle"), [CCC](/CCC "CCC"), October 21, 2009
7. [↑](#cite_ref-7) [ChessCore/Search.cs at master · 3583Bytes/ChessCore · GitHub - private static List<Position> EvaluateMoves(Board examineBoard, byte depth)](https://github.com/3583Bytes/ChessCore/blob/master/ChessCoreEngine/Search.cs#L406)

**[Up one level](/Engines "Engines")**