# Manuel Cristóbal López-Michelone

Source: https://www.chessprogramming.org/Manuel_Cristóbal_López-Michelone

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Manuel Cristóbal López-Michelone**

[![](/images/5/59/ManuelLopezMichelone.jpg)](https://es.chessbase.com/post/-quin-puede-ser-gran-maestro-)

Manuel López-Michelone [[1]](#cite_note-1)

**Manuel Cristóbal López-Michelone**, (Morsa)  
a Mexican [FIDE](/FIDE "FIDE") [master of chess](https://en.wikipedia.org/wiki/FIDE_titles#FIDE_Master_.28FM.29) [[2]](#cite_note-2), blogger and chess columnist, computer scientist and professor at department of computer science, [National Autonomous University of Mexico](https://en.wikipedia.org/wiki/National_Autonomous_University_of_Mexico) (UNAM).

# Description Language for Chess

Along with [Jorge Luis Ortega-Arjona](/Jorge_Luis_Ortega-Arjona "Jorge Luis Ortega-Arjona"), Manuel Cristóbal López-Michelone introduced a pattern description language for [chess positions](/Chess_Position "Chess Position"), published in [ICGA Journal, Vol. 42, No. 1](/ICGA_Journal#42_1 "ICGA Journal") [[3]](#cite_note-3):

```
The game of chess involves patterns. In this article we develop a simple description language for chess positions as patterns. It seems useful to catalogue similar positions in a generic form, based on common elements, in order to simplify the search for chess positions. A simple chess pattern language is used here to develop a computer program to find similar chess configurations. The aim is to avoid a commonly-used brute force approach. Further, this language could explain why some typical maneuvers actually work in some patterns. This could also be a step forward to model and build chess programs, which perform in a way closer to what a human being does.
```

The instructions of the language are:

- A(B) – Piece A attacks/defends Piece B
- A(square) – Piece A attacks square
- A square – Piece A at square
- taboo(square) – Make a square unavailable to defender
- action(chess movement) – The recommended move for the pattern
- structw([list of pawns]) – Defines the structure of the white pawns on the board
- structb([list of pawns]) – Defines the structure of black pawns on the board
- Logical connectors(“,”, “;”) – “,” is AND, “;” is OR.
- Single line comments can be made with the “//” delimiter, for example, //This is a comment.

# Selected Publications

[[4]](#cite_note-4)

- Manuel Cristóbal López-Michelone, [Jorge Luis Ortega-Arjona](/Jorge_Luis_Ortega-Arjona "Jorge Luis Ortega-Arjona") (**2016**). *[Patterns for the game of chess](https://www.semanticscholar.org/paper/Patterns-for-the-game-of-chess-L%C3%B3pez-Michelone-Ortega-Arjona/3b7d115e187dbefc55f0979ba87908b6fe421ecc)*. SugarLoaf PLoP'16
- Manuel Cristóbal López-Michelone, [Jorge Luis Ortega-Arjona](/Jorge_Luis_Ortega-Arjona "Jorge Luis Ortega-Arjona") (**2020**). *[A description language for chess](https://content.iospress.com/articles/icga-journal/icg190141)*. [ICGA Journal, Vol. 42, No. 1](/ICGA_Journal#42_1 "ICGA Journal")

# External Links

- [Lopez Michelone, Manuel FIDE Chess Profile](https://ratings.fide.com/card.phtml?event=5100305)
- [Blog de La\_Morsa](http://la-morsa.blogspot.com/)
- [M. en C. Manuel Cristóbal López Michelone](http://www.fciencias.unam.mx/directorio/11246)
- [Manuel López Michelone, Autor en Proceso Portal de Noticias](https://www.proceso.com.mx/author/manuel-lopez-michelone)
- Morsa VS [Kaspárov](/Garry_Kasparov "Garry Kasparov") en la UNAM, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [¿Quién puede ser gran maestro?](https://es.chessbase.com/post/-quin-puede-ser-gran-maestro-) [ChessBase](/ChessBase "ChessBase")
2. [↑](#cite_ref-2) [Lopez Michelone, Manuel FIDE Chess Profile](https://ratings.fide.com/card.phtml?event=5100305)
3. [↑](#cite_ref-3) Manuel Cristóbal López-Michelone, [Jorge Luis Ortega-Arjona](/Jorge_Luis_Ortega-Arjona "Jorge Luis Ortega-Arjona") (**2020**). *[A description language for chess](https://content.iospress.com/articles/icga-journal/icg190141)*. [ICGA Journal, Vol. 42, No. 1](/ICGA_Journal#42_1 "ICGA Journal")
4. [↑](#cite_ref-4) [dblp: Manuel Cristóbal López-Michelone](https://dblp.uni-trier.de/pers/hd/l/L=oacute=pez=Michelone:Manuel_Crist=oacute=bal)

**[Up one level](/People "People")**