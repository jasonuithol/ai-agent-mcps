# Kristallweizen

Source: https://www.chessprogramming.org/Kristallweizen

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Kristallweizen**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Hefeweizen_and_kristallweizen.jpg/330px-Hefeweizen_and_kristallweizen.jpg)](/File:Hefeweizen_and_kristallweizen.jpg)

Kristallweizen and Hefeweizen (right) [[1]](#cite_note-1) [[2]](#cite_note-2)

**Kristallweizen**,  
a [Shogi](/Shogi "Shogi") engine, or more precisely a Shogi evaluation function by team **Barrel house**, a beer bar in front of the [Okayama](https://en.wikipedia.org/wiki/Okayama) [station](https://en.wikipedia.org/wiki/Okayama_Station) [[3]](#cite_note-3),
due to the developers around [Seiji Shiba](/index.php?title=Seiji_Shiba&action=edit&redlink=1 "Seiji Shiba (page does not exist)"), [Mitsunori Matsushita](/index.php?title=Mitsunori_Matsushita&action=edit&redlink=1 "Mitsunori Matsushita (page does not exist)") and [Yasuhiro Tajima](/Yasuhiro_Tajima "Yasuhiro Tajima") [[4]](#cite_note-4).
Kristallweizen became runner-up at the [WCSC29](/index.php?title=WCSC29&action=edit&redlink=1 "WCSC29 (page does not exist)") in 2019, where it run in the [Amazon Elastic Compute Cloud](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud) and applied [multi pondering](/Pondering "Pondering").
Kristallweizen is a [NNUE](/NNUE "NNUE") HalfKP-256x2-32-32 type of evaluation function, used within [YaneuraOu's](/YaneuraOu "YaneuraOu") [search](/Search "Search"), a Shogi adaptation of [Stockfish's](/Stockfish "Stockfish") search.
Further [CSA](/CSA "CSA") available engines and libraries used to train and prepare Kristallweizen mentioned on the WCSC29 site [[5]](#cite_note-5)
were [Apery](/Apery "Apery"), [Tanuki](/index.php?title=Tanuki&action=edit&redlink=1 "Tanuki (page does not exist)"), [Qhapaq](/index.php?title=Qhapaq&action=edit&redlink=1 "Qhapaq (page does not exist)"), [Elmo](/index.php?title=Elmo&action=edit&redlink=1 "Elmo (page does not exist)"), dlshogi [[6]](#cite_note-6), python-shogi [[7]](#cite_note-7) and the *Android Go Player No. 18* [[8]](#cite_note-8).
Kristallweizen may also used with *Dolphin*, also based on YaneuraOu's (version 4.82) search [[9]](#cite_note-9)
[[10]](#cite_note-10).

# Hefeweizen

Kristallweizen's forerunner, the more unfiltered **Hefeweizen** uses an [Apery](/Apery "Apery") type of KPP/KKP indexed [Piece-Square Tables](/Piece-Square_Tables "Piece-Square Tables") approach, initially introduced by [Bonanza](/Bonanza "Bonanza").
Hefeweizen won the [WCSC28](/index.php?title=WCSC28&action=edit&redlink=1 "WCSC28 (page does not exist)") in 2018, also on the [Amazon Elastic Compute Cloud](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud) with [multi ponder](/Pondering "Pondering") [[11]](#cite_note-11).

# Forum Posts

- [The Stockfish of shogi](http://talkchess.com/forum3/viewtopic.php?t=72754) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), January 07, 2020
- [Dolphin software](https://groups.google.com/g/shogi-l/c/WG2qwzMh3C8/m/kzMeImwlAwAJ) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [SHOGI-L](/Computer_Chess_Forums "Computer Chess Forums"), February 02, 2020

# External Links

## Shogi Engine

- [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen/)
- [Kristallweizen – 第29回世界コンピュータ将棋選手権 (wcsc29)](http://sizer.main.jp/wcsc29/services/kristallweizen/)

## Misc

- [Wheat beer from Wikipedia](https://en.wikipedia.org/wiki/Wheat_beer)

# References

1. [↑](#cite_ref-1) A [photograph](https://commons.wikimedia.org/wiki/File:Hefeweizen_and_kristallweizen.jpg) of two varieties of [wheat beer](https://en.wikipedia.org/wiki/Wheat_beer): Kristallweizen (left) and Hefeweizen (right), filtered and unfiltered [German wheat beers](https://en.wikipedia.org/wiki/Beer_in_Germany)
2. [↑](#cite_ref-2) [Erdinger from Wikipedia](https://en.wikipedia.org/wiki/Erdinger)
3. [↑](#cite_ref-3) [Beer Bar Barrel house - Facebook](https://www.facebook.com/Beer-Bar-Barrel-house-304149502997804/)
4. [↑](#cite_ref-4) [The 29th World Computer Shogi Championship Applicant List](https://groups.google.com/d/msg/shogi-l/qL5i9rYFXyw/TqDOnZZSDAAJ) by [Reijer Grimbergen](/Reijer_Grimbergen "Reijer Grimbergen") on behalf of [Takenobu Takizawa](/Takenobu_Takizawa "Takenobu Takizawa"), [SHOGI-L](/Computer_Chess_Forums "Computer Chess Forums"), February 03, 2019
5. [↑](#cite_ref-5) [第29回世界コンピュータ将棋選手権 - 29th World Computer Shogi Championship](http://www2.computer-shogi.org/wcsc29/)
6. [↑](#cite_ref-6) [GitHub - TadaoYamaoka/python-dlshogi](https://github.com/TadaoYamaoka/python-dlshogi)
7. [↑](#cite_ref-7) [GitHub - gunyarakun/python-shogi: A pure Python shogi library with move generation and validation and handling of common formats.](https://github.com/gunyarakun/python-shogi)
8. [↑](#cite_ref-8) [人造棋士１８号 - django-\/\/ i K | Android Go Player No.18](https://www.qhapaq.org/shogi/shogiwiki/softs/jk18/)
9. [↑](#cite_ref-9) [Re: Strongest free shogi engine?](https://www.reddit.com/r/shogi/comments/ew3nic/strongest_free_shogi_engine/?sort=confidence) by [km0010](https://www.reddit.com/user/km0010/), [Reddit](https://en.wikipedia.org/wiki/Reddit)
10. [↑](#cite_ref-10) [使用ソフト | shogi-engines](https://www.uuunuuun.com/blank-2)
11. [↑](#cite_ref-11) [第28回世界コンピュータ将棋選手権 - 28th World Computer Shogi Championship](http://www2.computer-shogi.org/wcsc28/)

**[Up one Level](/Engines "Engines")**