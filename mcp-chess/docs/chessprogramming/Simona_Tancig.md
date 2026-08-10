# Simona Tancig

Source: https://www.chessprogramming.org/Simona_Tancig

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Simona Tancig**

[![](/images/a/ab/Simona_Tancig.jpg)](https://www.simpoziji.jivatma.si/predstavitev_simona_tancig.php)

Simona Tancig [[1]](#cite_note-1)

**Simona Tancig**,   
a Slovenian [psychologist](/Category:Psychologist "Category:Psychologist"), since 1991 associate professor of [developmental psychology](https://en.wikipedia.org/wiki/Developmental_psychology) at Faculty of Education of [University of Ljubljana](/University_of_Ljubljana "University of Ljubljana"), where she already received her Ph.D. in psychology in 1983 with the thesis title *Some Cognitive Processes in the Game of Chess* [[2]](#cite_note-2).
She was the main researcher and collaborator at multiple research projects in the areas of [cognition](/Cognition "Cognition"), [decision making](https://en.wikipedia.org/wiki/Decision_making), [learning](/Learning "Learning"), [education](https://en.wikipedia.org/wiki/Education), [psychomotor development](https://en.wikipedia.org/wiki/Psychomotor_learning), and [mathematical cognition](https://en.wikipedia.org/wiki/Numerical_cognition).
Her current research interests are in [metacognition](https://en.wikipedia.org/wiki/Metacognition), [self-regulation](https://en.wikipedia.org/wiki/Self-regulated_learning), [collaborative learning](https://en.wikipedia.org/wiki/Collaborative_learning) and [expert knowledge](https://en.wikipedia.org/wiki/Expert_system), [embodiment](https://en.wikipedia.org/wiki/Embodied_cognition) and [empathy](https://en.wikipedia.org/wiki/Empathy) [[3]](#cite_note-3). In 2010, Simona Tancig received the [Award of the Republic of Slovenia in the field of education](https://sl.wikipedia.org/wiki/Nagrada_Republike_Slovenije_na_podro%C4%8Dju_%C5%A1olstva).

# Chess experiments

Along with [Ivan Bratko](/Ivan_Bratko "Ivan Bratko") and [Peter Tancig](/Peter_Tancig "Peter Tancig") in the early 80s, Simona Tancig researched on cognitive processes in the game of chess and on detection of positional patterns and [chunks](/Chunking "Chunking"). Similar to the attempts of [Adriaan de Groot](/Adriaan_de_Groot "Adriaan de Groot") [[4]](#cite_note-4), and [William Chase](/William_Chase "William Chase") and [Herbert Simon](/Herbert_Simon "Herbert Simon") [[5]](#cite_note-5) [[6]](#cite_note-6), they conducted experiments where chess players had to reconstruct complicated [middlegame](/Middlegame "Middlegame") [positions](/Chess_Position "Chess Position") after a short view on diagrams, with the novel aspects of collective reconstruction, as published in the [ICCA Journal](/ICGA_Journal "ICGA Journal") [[7]](#cite_note-7) and [Advances in Computer Chess 4](/Advances_in_Computer_Chess_4 "Advances in Computer Chess 4").
24 positions were chosen from a chess magazine with 28 [pieces](/Pieces "Pieces") on average.
The positions were of four types according to the [opening](/Opening "Opening") from which the position arose (6 each [Ruy Lopez](https://en.wikipedia.org/wiki/Ruy_Lopez), [Sicilian](https://en.wikipedia.org/wiki/Sicilian_Defence), [King's Indian](https://en.wikipedia.org/wiki/King%27s_Indian_Defence) and [Queen's Indian](https://en.wikipedia.org/wiki/Queen%27s_Indian_Defense)).
20 players in two groups were the subjects, one group rated from 2300 to over 2500, the second from 1800 to 2100.

## Reconstruction Factor

The success of reconstruction was measured by the so-called reconstruction factor:

[![ReconstructionFactor.png](/images/thumb/4/44/ReconstructionFactor.png/140px-ReconstructionFactor.png)](/File:ReconstructionFactor.png)

where P is the set of pieces (including the square information) in the original, and R is the set of pieces in the reconstructed position, with 0 <= F <= 1. Using a standard [bitboard board-definition](/Bitboard_Board-Definition "Bitboard Board-Definition") with arrays of 12 [bitboards](/Bitboards "Bitboards") for each [piece-type](/Pieces#PieceTypeCoding "Pieces") and [color](/Color "Color"), the reconstruction factor could be calculated with following routine aggregating [population counts](/Population_Count "Population Count") of [intersections](/General_Setwise_Operations#Intersection "General Setwise Operations") and [unions](/General_Setwise_Operations#Union "General Setwise Operations"), and the final [double floating point](/Double "Double") division:

```
double reconstructionFactor(const BitBoard* P, const BitBoard* R) {
  int i = 0, u = 0;
  for (int pt = 0; pt < 12; pt++) {
    i += popcount(P[pt] & R[pt]);
    u += popcount(P[pt] | R[pt]);
  }
  return (i == u) ? 1.0 : ((double) i / (double) u); /* considers i == u == 0 */
}
```

The measure is different from those used by De Groot, Chase and Simon. Its advantage is that it not only rewards correctly recalled pieces, but it also penalizes incorrectly added pieces, where the previous used measure was not sensitive of.

## Individual Results

Following individual reconstruction results were determined for the two groups:

| Group | n | F | [Std.dev](https://en.wikipedia.org/wiki/Standard_deviation) x √n | Std.dev in F |
| --- | --- | --- | --- | --- |
| 1 | 240 | 0.552 | 0.205 | 0.013 |
| 2 | 240 | 0.236 | 0.131 | 0.008 |

For each piece type the table indicates that pawns play a major role in human positional perception:

| Piece type | Group 1 | Group 2 |
| --- | --- | --- |
| [King](/King "King") | 0.785 | 0.354 |
| [Pawn](/Pawn "Pawn") | 0.565 | 0.255 |
| [Queen](/Queen "Queen") | 0.464 | 0.143 |
| [Rook](/Rook "Rook") | 0.462 | 0.274 |
| [Bishop](/Bishop "Bishop") | 0.439 | 0.082 |
| [Knight](/Knight "Knight") | 0.383 | 0.107 |

# See also

- [Chunking](/Chunking "Chunking")
- [Cognition](/Cognition "Cognition")
- [Psychology](/index.php?title=Psychology&action=edit&redlink=1 "Psychology (page does not exist)")

# Selected Publications

- [Peter Tancig](/Peter_Tancig "Peter Tancig"), Simona Tancig (**1976**). *[Analysis of symbolic structures with computers](https://psycnet.apa.org/record/1978-26430-001)*. Revija za Psihologiju, Vol. 6, No. 1-2
- Simona Tancig (**1983**). *[Nekateri kognitivni procesi v šahovski igri](https://books.google.com/books/about/Nekateri_kognitivni_procesi_v_%C5%A1ahovski.html?id=41VDNAAACAAJ&redir_esc=y)*. Some Cognitive Processes in the Game of Chess. Ph.D. thesis, [University of Ljubljana](/University_of_Ljubljana "University of Ljubljana") (Slovenian)
- [Ivan Bratko](/Ivan_Bratko "Ivan Bratko"), [Peter Tancig](/Peter_Tancig "Peter Tancig"), Simona Tancig (**1984**). *[Detection of Positional Patterns in Chess](#ChessExperiment)*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 7, No. 2 (abridged version)
- [Ivan Bratko](/Ivan_Bratko "Ivan Bratko"), [Peter Tancig](/Peter_Tancig "Peter Tancig"), Simona Tancig (**1986**). *[Detection of Positional Patterns in Chess](#ChessExperiment)*. [Advances in Computer Chess 4](/Advances_in_Computer_Chess_4 "Advances in Computer Chess 4") (full paper)
- Simona Tancig (**2009**). *Expert Team Decision Making and Problem Solving: Development and Learning*. in Interdisciplinary Description of Complex Systems, Vol. 7, No. 2, [pdf](http://www.indecs.eu/2009/indecs_7_2.pdf)

# External Links

- [Faculty of Education: EAEN Conference: Dr. Simona Tancig](http://www.pef.uni-lj.si/index.php?id=475)
- [Pedagoška fakulteta: Simona Tancig](http://www.pef.uni-lj.si/index.php?id=628) (Slovenian)
- [Predstavitev: Simona Tancig](https://www.simpoziji.jivatma.si/predstavitev_simona_tancig.php)

# References

1. [↑](#cite_ref-1) [Predstavitev: Simona Tancig](https://www.simpoziji.jivatma.si/predstavitev_simona_tancig.php)
2. [↑](#cite_ref-2) Simona Tancig (**1983**). *[Nekateri kognitivni procesi v šahovski igri](http://books.google.com/books/about/Nekateri_kognitivni_procesi_v_%C5%A1ahovski.html?id=41VDNAAACAAJ&redir_esc=y)*. Some Cognitive Processes in the Game of Chess. Ph.D. thesis, [University of Ljubljana](/University_of_Ljubljana "University of Ljubljana") (Slovenian)
3. [↑](#cite_ref-3) [Faculty of Education: EAEN Conference: Dr. Simona Tancig](http://www.pef.uni-lj.si/index.php?id=475)
4. [↑](#cite_ref-4)  [Adriaan de Groot](/Adriaan_de_Groot "Adriaan de Groot") (**1965, 1978**). *Thought and Choice in Chess*. Mouton & Co Publishers
5. [↑](#cite_ref-5) [William Chase](/William_Chase "William Chase"), [Herbert Simon](/Herbert_Simon "Herbert Simon") (**1973**). *[The Mind’s Eye in Chess](http://psycnet.apa.org/psycinfo/1974-08328-004)*. Visual Information Processing: Proceedings of the Eighth Annual Carnegie Psychology Symposium (ed. W. G. Chase), pp. 215-281. Academic Press, New York. Reprinted (**1988**) in Readings in Cognitive Science (ed. A.M. Collins). Morgan Kaufmann, San Mateo, CA.
6. [↑](#cite_ref-6) [William Chase](/William_Chase "William Chase"), [Herbert Simon](/Herbert_Simon "Herbert Simon") (**1973**). *[Perception in chess](http://www.sciencedirect.com/science/article/pii/0010028573900042)*. [Cognitive Psychology](http://www.elsevier.com/wps/find/journaldescription.cws_home/622807/description#description), Vol. 4, No. 1, [pdf](http://matt.colorado.edu/teaching/highcog/fall8/cs73.pdf)
7. [↑](#cite_ref-7) [Ivan Bratko](/Ivan_Bratko "Ivan Bratko"), [Peter Tancig](/Peter_Tancig "Peter Tancig"), Simona Tancig (**1984**). *[Detection of Positional Patterns in Chess](#ChessExperiment)*. [ICCA Journal](/ICGA_Journal "ICGA Journal"), Vol. 7, No. 2, (abridged version)

**[Up one level](/People "People")**