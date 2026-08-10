# Shura-Bura's Program

Source: https://www.chessprogramming.org/Shura-Bura's_Program

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Shura-Bura's Program**

**Shura-Bura's Program**,  
an early Soviet chess program developed by a group of scientists at the [Steklov Institute of Mathematics](https://en.wikipedia.org/wiki/Steklov_Institute_of_Mathematics) headed by [Mikhail R. Shura-Bura](/Mikhail_R._Shura-Bura "Mikhail R. Shura-Bura"), including [Igor B. Zadyhailo](/index.php?title=Igor_B._Zadyhailo&action=edit&redlink=1 "Igor B. Zadyhailo (page does not exist)") and [Marat A. Evgrafov](/index.php?title=Marat_A._Evgrafov&action=edit&redlink=1 "Marat A. Evgrafov (page does not exist)"), with further support of physicist and science journalist [Volʹdemar Smilga](/index.php?title=Vol%CA%B9demar_Smilga&action=edit&redlink=1 "Volʹdemar Smilga (page does not exist)"). A brief description of the program was given in an interview with Shura-Bura on computer chess by V. Tumanov, published as part in the 8th Bulletin of the [Botvinnik Tal 1961 revenge-match](https://en.wikipedia.org/wiki/World_Chess_Championship_1961) for the [world chess championship](https://en.wikipedia.org/wiki/World_Chess_Championship) - entitled "The best move in 58 seconds", cited in [Jaap van den Herik's](/Jaap_van_den_Herik "Jaap van den Herik") Ph.D. thesis *Computerschaak, Schaakwereld en Kunstmatige Intelligentie* [[1]](#cite_note-1). Further, two games of the program were published. A more elaborate description was given by Evgrafov and Zadyhailo in 1965, featuring some [M-20](/M-20 "M-20") machine code with comments [[2]](#cite_note-2).

# Description

## [Board Representation](/Board_Representation "Board Representation")

The [chess position](/Chess_Position "Chess Position") structure obtains a [piece to square interaction map](/Attack_and_Defend_Maps "Attack and Defend Maps"), that includes seven different features to speed up [move generation](/Move_Generation "Move Generation") and [evaluation](/Evaluation "Evaluation") [[3]](#cite_note-3):

1. [Piece](/Pieces "Pieces") attacks and can move to [Square](/Squares "Squares")
2. Piece does not attack but can move to Square
3. Piece attacks and but can not move to Square
4. Piece indirectly attacks Square through a sliding piece
5. Piece indirectly attacks Square through a [pawn attack](/Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)")
6. Piece indirectly attacks Square through a Piece not attacking Square
7. Blocked pawn target

## [Evaluation](/Evaluation "Evaluation")

The program is reported to select the best move with the help of a [static evaluation function](/Evaluation "Evaluation"), which had seven distinct components:

1. [Material](/Material "Material") (Pawn 1; Knight, Bishop 3.5; Rook 5; Queen 9.5; King 109)
2. [Mobility](/Mobility "Mobility")
3. [Static Exchange Evaluation](/Static_Exchange_Evaluation "Static Exchange Evaluation")
4. [Pawn Structure](/Pawn_Structure "Pawn Structure")
5. [Center Control](/Center_Control "Center Control")
6. [King Safety - Patterns](/King_Safety#Patterns "King Safety")
7. [King Safety - Pawn Shield](/King_Safety#PawnShield "King Safety")

# See also

- [ITEP Chess Program](/ITEP_Chess_Program "ITEP Chess Program")

# Publications

- В. Туманов (**1961**). *«Лучший ход» — за 58 секунд*. Таль—Ботвинник: матч-реванш на первенство мира. Бюллетень Центрального шахматного клуба СССР, № 8

:   V. Tumanov (**1961**). *The best move in 58 seconds*. 8th Bulletin of the [Botvinnik Tal 1961 revenge-match](https://en.wikipedia.org/wiki/World_Chess_Championship_1961)

- [М. А. Евграфов](/index.php?title=Marat_A._Evgrafov&action=edit&redlink=1 "Marat A. Evgrafov (page does not exist)"), [И. Б. Задыхайло](/index.php?title=Igor_B._Zadyhailo&action=edit&redlink=1 "Igor B. Zadyhailo (page does not exist)") (**1965**). *Некоторые соображения о программировании шахматной игры*. / Сб. Проблемы кибернетики, №15

:   [Marat A. Evgrafov](/index.php?title=Marat_A._Evgrafov&action=edit&redlink=1 "Marat A. Evgrafov (page does not exist)"), [Igor B. Zadyhailo](/index.php?title=Igor_B._Zadyhailo&action=edit&redlink=1 "Igor B. Zadyhailo (page does not exist)") (**1965**). *Some Considerations for Chess Game Programming*. in Problems of Cybernetic, No. 15 [[4]](#cite_note-4)

- [David Levy](/David_Levy "David Levy"), [Monroe Newborn](/Monroe_Newborn "Monroe Newborn") (**1982**). *[All About Chess and Computers](http://link.springer.com/book/10.1007/978-3-642-85538-2)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") (**1983**). *Computerschaak, Schaakwereld en Kunstmatige Intelligentie*. Ph.D. thesis, [Delft University of Technology](/Delft_University_of_Technology "Delft University of Technology"). Academic Service, The Hague. ISBN 90 62 33 093 2 (Dutch), 2.2.9. Sjoera-Boera

# Forum Posts

- [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=5) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), June 08, 2019 » [Alex Bernstein](/Alex_Bernstein "Alex Bernstein")

:   [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=8) by Roman Zhukov, [CCC](/CCC "CCC"), June 08, 2019
:   [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=12) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), June 08, 2019

# External Links

- [Schachcomputer - Geschichte - 6](http://www.schachcomputer.at/gesch6.htm) by [Karsten Bauermeister](/Karsten_Bauermeister "Karsten Bauermeister") (German)
- [Computerschach - ein Überblick](http://www.dsk1931ev.de/Computerschach/computer.htm) von Mathias Grontzki (German)

# References

1. [↑](#cite_ref-1) [Jaap van den Herik](/Jaap_van_den_Herik "Jaap van den Herik") (**1983**). *Computerschaak, Schaakwereld en Kunstmatige Intelligentie*. Ph.D. thesis, [Delft University of Technology](/Delft_University_of_Technology "Delft University of Technology"). Academic Service, The Hague. ISBN 90 62 33 093 2 (Dutch), 2.2.9. Sjoera-Boera - translation from Russian by J.P. Warris, Russian teacher at TH Delft
2. [↑](#cite_ref-2) [М. А. Евграфов](/index.php?title=Marat_A._Evgrafov&action=edit&redlink=1 "Marat A. Evgrafov (page does not exist)"), [И. Б. Задыхайло](/index.php?title=Igor_B._Zadyhailo&action=edit&redlink=1 "Igor B. Zadyhailo (page does not exist)") (**1965**). *Некоторые соображения о программировании шахматной игры*. / Сб. Проблемы кибернетики, №15
3. [↑](#cite_ref-3) [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=12) by [Sergei S. Markoff](/Sergei_Markoff "Sergei Markoff"), [CCC](/CCC "CCC"), June 08, 2019
4. [↑](#cite_ref-4) [Re: The mystery of Alex Bernstein](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70939&start=8) by Roman Zhukov, [CCC](/CCC "CCC"), June 08, 2019

**[Up one level](/Engines "Engines")**