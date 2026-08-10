# Dog

Source: https://www.chessprogramming.org/Dog

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Dog**

**Dog**,  
an [UCI](/UCI "UCI") compliant chess engine by [Folkert van Heusden](/Folkert_van_Heusden "Folkert van Heusden"), first released in 2022. It is mainly targeted for running on [ESP32](/index.php?title=ESP32&action=edit&redlink=1 "ESP32 (page does not exist)") [microcontrollers](/index.php?title=Microcontrollers&action=edit&redlink=1 "Microcontrollers (page does not exist)") altough it can be compiled for [Linux](/Linux "Linux") (and other OSes) as well.
It is called Dog as the writer acquiered a dog.
Initially, Dog was Micah with some parts removed and some things added. As time goes on the differences get bigger, especially when the NNUE was added (and the HCE was removed).

# Forum Posts

- [announcement](http://talkchess.com/forum3/viewtopic.php?f=2&t=80779), 02 Oct 2022

# Selected Games

```
[Event "example"]
[Site "laptop"]
[Date "2022.10.24"]
[Round "-"]
[White "Embla-5142"]
[Black "Dog v0.9-d5a00b0"]
[Result "0-1"]
[WhiteElo "?"]
[BlackElo "?"]
[Variant "Standard"]
[TimeControl "-"]
[ECO "A45"]
[Opening "Amazon Attack: Siberian Attack"]
[Termination "Unknown"]
[Annotator "lichess.org"]

1. Nc3 { [%eval -0.13] } 1... Nf6 { [%eval 0.12] } 2. d4 { [%eval -0.08] } 2... d5 { [%eval -0.02] } 3. Qd3?! { (-0.02 → -0.88) Inaccuracy. Bf4 was best. } { [%eval -0.88] } { A45 Amazon Attack: Siberian Attack } (3. Bf4 e6 4. Nb5 Na6 5. e3 Be7 6. Nf3 O-O 7. h3 c6) 3... b6?! { (-0.88 → 0.07) Inaccuracy. c5 was best. } { [%eval 0.07] } (3... c5 4. dxc5 Nc6 5. a3 d4 6. Ne4 Nxe4 7. Qxe4 g6 8. Qd3) 4. Nf3?! { (0.07 → -0.85) Inaccuracy. Bg5 was best. } { [%eval -0.85] } (4. Bg5 e6 5. e4 Ba6 6. Qf3 Bxf1 7. Kxf1 dxe4 8. Nxe4 Nxe4) 4... Ba6 { [%eval -0.78] } 5. Qe3 { [%eval -1.07] } 5... e6 { [%eval -1.12] } 6. Ne5 { [%eval -1.56] } 6... Nbd7 { [%eval -1.24] } 7. Qf4 { [%eval -1.67] } 7... c5 { [%eval -1.58] } 8. Nf3 { [%eval -2.05] } 8... cxd4 { [%eval -2.09] } 9. Qxd4 { [%eval -2.07] } 9... Bb7 { [%eval -1.57] } 10. Bf4?! { (-1.57 → -2.65) Inaccuracy. Bg5 was best. } { [%eval -2.65] } (10. Bg5 a6 11. e3 h6 12. Bh4 Rc8 13. a3 b5 14. Be2 Be7 15. O-O O-O 16. Qd1 Re8) 10... Rc8 { [%eval -2.07] } 11. e3 { [%eval -1.85] } 11... Ne4?? { (-1.85 → 0.00) Blunder. Bc5 was best. } { [%eval 0.0] } (11... Bc5 12. Qd1) 12. Bb5?? { (0.00 → -1.95) Blunder. Nxe4 was best. } { [%eval -1.95] } (12. Nxe4 dxe4 13. Ne5 Nxe5 14. Bxe5 Qxd4 15. Bxd4 f6 16. Bc3 Be7 17. Bb5+ Kf7 18. O-O-O Rc7) 12... Nxc3 { [%eval -1.98] } 13. bxc3 { [%eval -1.83] } 13... f6 { [%eval -1.99] } 14. Kd2?? { (-1.99 → -4.53) Blunder. Bg3 was best. } { [%eval -4.53] } (14. Bg3 Kf7) 14... a6?! { (-4.53 → -3.56) Inaccuracy. Kf7 was best. } { [%eval -3.56] } (14... Kf7 15. Bxd7 Qxd7 16. a4 Ba6 17. a5 Bc5 18. Qe5 h5 19. axb6 Kg8 20. Rxa6 fxe5 21. Rxa7) 15. Bxd7+ { [%eval -3.66] } 15... Kxd7 { [%eval -3.0] } 16. Rab1 { [%eval -3.02] } 16... Bc5 { [%eval -2.88] } 17. Qd3 { [%eval -3.52] } 17... e5 { [%eval -3.37] } 18. Qf5+ { [%eval -3.35] } 18... Ke7?? { (-3.35 → 0.00) Blunder. Ke8 was best. } { [%eval 0.0] } (18... Ke8 19. Qe6+) 19. Nxe5 { [%eval 0.0] } 19... g6 { [%eval 0.0] } 20. Qg4 { [%eval -0.15] } 20... g5 { [%eval 0.11] } 21. Bg3?? { (0.11 → -1.93) Blunder. Bxg5 was best. } { [%eval -1.93] } (21. Bxg5) 21... fxe5 { [%eval -1.79] } 22. Qxg5+?! { (-1.79 → -2.73) Inaccuracy. Bxe5 was best. } { [%eval -2.73] } (22. Bxe5) 22... Kd7 { [%eval -2.49] } 23. Qf5+ { [%eval -2.83] } 23... Kc6 { [%eval -2.5] } 24. Bxe5 { [%eval -2.78] } 24... Re8 { [%eval -2.44] } 25. g3?! { (-2.44 → -3.29) Inaccuracy. f4 was best. } { [%eval -3.29] } (25. f4 Qe7 26. Qd3 Rcd8 27. Rhf1 Bc8 28. a4 Kb7 29. a5 Bd7 30. g4 b5 31. h3 Rc8) 25... Qe7 { [%eval -2.95] } 26. f4 { [%eval -3.25] } 26... Rf8?! { (-3.25 → -2.13) Inaccuracy. Ba8 was best. } { [%eval -2.13] } (26... Ba8 27. a4 a5 28. Rb5 Kb7 29. Rxc5 Rxc5 30. Rb1 Ka7 31. Bd4 Bb7 32. g4 Rec8 33. h4) 27. Qh5 { [%eval -2.46] } 27... Qf7?! { (-2.46 → -1.35) Inaccuracy. Kd7 was best. } { [%eval -1.35] } (27... Kd7 28. Qg4+ Kc6 29. Qh5 Ba8 30. Bd4 Rfe8 31. Qh6+ Kd7 32. Rhe1 Bc6 33. f5 Qf7 34. Rf1) 28. Qh6+ { [%eval -1.34] } 28... Qg6 { [%eval -1.54] } 29. Qxg6+ { [%eval -1.52] } 29... hxg6 { [%eval -1.51] } 30. h4 { [%eval -1.8] } 30... Rce8 { [%eval -1.62] } 31. h5?! { (-1.62 → -2.46) Inaccuracy. g4 was best. } { [%eval -2.46] } (31. g4 Bc8) 31... gxh5 { [%eval -2.07] } 32. Rxh5 { [%eval -2.32] } 32... Bc8 { [%eval -2.05] } 33. Rh6+ { [%eval -2.26] } 33... Re6 { [%eval -2.45] } 34. Rxe6+?! { (-2.45 → -3.17) Inaccuracy. Rbh1 was best. } { [%eval -3.17] } (34. Rbh1 Kb5 35. Rxe6 Bxe6 36. Rh5 Rf7 37. Bd4 Bf5 38. g4 Bxg4 39. Rxd5 Kc4 40. Re5 Rf5) 34... Bxe6 { [%eval -3.36] } 35. Rh1 { [%eval -3.35] } 35... Rg8 { [%eval -3.31] } 36. Rh6 { [%eval -3.26] } 36... Kd7 { [%eval -3.46] } 37. Rh5 { [%eval -3.72] } 37... Rxg3 { [%eval -3.45] } 38. f5 { [%eval -3.57] } 38... Bf7 { [%eval -3.84] } 39. Rh7 { [%eval -3.71] } 39... Rg2+ { [%eval -3.5] } 40. Kd3 { [%eval -4.0] } 40... Ke7 { [%eval -3.68] } 41. Rh6 { [%eval -3.64] } 41... Rf2 { [%eval -3.81] } 42. Bf6+?! { (-3.81 → -5.00) Inaccuracy. Bc7 was best. } { [%eval -5.0] } (42. Bc7 Rxf5 43. Bxb6 Bd6 44. Ba5 Kd7 45. Bb4 Be5 46. Rxa6 Rf2 47. c4 dxc4+ 48. Ke4 Bc7) 42... Kd7 { [%eval -4.79] } 43. Bd4 { [%eval -5.4] } 43... Rxf5 { [%eval -5.37] } 44. Bxc5 { [%eval -5.36] } 44... bxc5 { [%eval -5.32] } 45. Ke2 { [%eval -6.39] } 45... Rg5 { [%eval -6.0] } 46. Rh7 { [%eval -6.49] } 46... Ke6 { [%eval -6.64] } 47. Kf2 { [%eval -7.76] } 47... Rh5 { [%eval -8.06] } 48. Rxh5 { [%eval -9.91] } 48... Bxh5 { [%eval -11.94] } 49. Ke1 { [%eval -13.05] } 49... c4 { [%eval -13.49] } 50. Kd2 { [%eval -14.28] } 50... Bf3 { [%eval -13.48] } 51. Ke1 { [%eval -14.14] } 51... Ke5 { [%eval -14.75] } 52. a3 { [%eval -16.68] } 52... a5 { [%eval -18.32] } 53. Kf1 { [%eval -21.94] } 53... Ke4 { [%eval -23.31] } 54. Kf2 { [%eval -24.01] } 54... a4 { [%eval -23.56] } 55. Kf1 { [%eval -24.17] } 55... Kxe3 { [%eval -31.09] } 56. Kg1 { [%eval -23.87] } 56... Kd2 { [%eval #-15] } 57. Kf2 { [%eval #-26] } 57... Be4 { [%eval #-20] } 58. Kf1 { [%eval #-13] } 58... Bxc2 { [%eval #-15] } 59. Kf2 { [%eval -37.0] } 59... Kxc3 { [%eval #-15] } 60. Kg3 { [%eval #-14] } 60... d4 { [%eval #-10] } 61. Kh3 { [%eval #-12] } 61... d3 { [%eval #-11] } 62. Kg3 { [%eval #-10] } 62... d2 { [%eval #-8] } 63. Kf4 { [%eval #-8] } 63... d1=Q { [%eval #-7] } 64. Ke5 { [%eval #-7] } 64... Qh1 { [%eval #-9] } 65. Kd6 { [%eval #-8] } 65... Kb2 { [%eval #-7] } 66. Ke6 { [%eval #-7] } 66... c3 { [%eval #-6] } 67. Ke5 { [%eval #-6] } 67... Bd3 { [%eval #-5] } 68. Ke6 { [%eval #-5] } 68... c2 { [%eval #-4] } 69. Ke7 { [%eval #-4] } 69... Qb7+ { [%eval #-3] } 70. Kf6 { [%eval #-3] } 70... c1=Q { [%eval #-2] } 71. Ke5 { [%eval #-2] } 71... Qe7+ { [%eval #-1] } 72. Kd4 { [%eval #-1] } 72... Qc4# { Black wins. } 0-1
```

# External Links

- [website](https://vanheusden.com/chess/Dog/)
- [GitHub repository](https://github.com/folkertvanheusden/Dog)

# References

**[Up one Level](/Engines "Engines")**