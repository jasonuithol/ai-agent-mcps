# Tomasz Sobczyk

Source: https://www.chessprogramming.org/Tomasz_Sobczyk

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Tomasz Sobczyk**

**Tomasz Sobczyk**, (Sopel97, Sopel)  
a Polish computer scientist involved in recent [Stockfish](/Stockfish "Stockfish") development and documentation concerning [NNUE](/NNUE "NNUE")
[[1]](#cite_note-1).
He introduced new net architectures using the [HalfKA](/Stockfish_NNUE#HalfKA "Stockfish NNUE"), HalfKAv2 [[2]](#cite_note-2) [[3]](#cite_note-3) and HalfKAv2\_hm [[4]](#cite_note-4) [[5]](#cite_note-5) feature sets,
optimized the NNUE inference code for various [SIMD instruction sets](/SIMD_and_SWAR_Techniques#SIMD_Instruction_Sets "SIMD and SWAR Techniques") [[6]](#cite_note-6) [[7]](#cite_note-7) [[8]](#cite_note-8),
and contributed to [Gary Linscott's](/Gary_Linscott "Gary Linscott") [Pytorch NNUE](/Gary_Linscott#PyTorch_NNUE "Gary Linscott") project to train Stockfish, mostly working on optimizations which allowed nets to be trained within hours instead of days [[9]](#cite_note-9) [[10]](#cite_note-10)
[[11]](#cite_note-11). He also heavily contributed to the original NNUE trainer and data generator by [Yu Nasu](/Yu_Nasu "Yu Nasu"), cleaning up the codebase, updating the data generator, optimizing the trainer, and adding other useful tools [[12]](#cite_note-12) which are now available in the tools branch of the official-stockfish repository [[13]](#cite_note-13). He also introduced the [Binpack](/index.php?title=Binpack&action=edit&redlink=1 "Binpack (page does not exist)") storage format for training data [[14]](#cite_note-14) [[15]](#cite_note-15), comprising of position evaluations from chess games, which utilizes efficient delta encoding, and reduces the sizes of the datasets by 10 to 20 times compared to the previous solutions. His contributions span more than 200 pull requests over multiple repositories [[16]](#cite_note-16) [[17]](#cite_note-17) [[18]](#cite_note-18). He's also an author of a chess engine [Fat Titz](/Fat_Titz "Fat Titz"), which is based on [CFish](/CFish "CFish") and is a parody of [Fat Fritz](/Fat_Fritz "Fat Fritz") [[19]](#cite_note-19) [[20]](#cite_note-20).

# Forum Posts

## 2020 ...

- [Re: Removing Large Arrays](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73319&start=30) by Sopel, [CCC](/CCC "CCC"), March 12, 2020
- [Re: Compiler Optimization Question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73638&start=21) by Sopel, [CCC](/CCC "CCC"), April 14, 2020
- [Re: An actual interesting computer chess read about FF2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76730&start=22) by Sopel, [CCC](/CCC "CCC"), February 28, 2021
- [Re: It walks like a clone, it quacks like a clone ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76826&start=45) by Sopel, [CCC](/CCC "CCC"), March 14, 2021
- [Re: larger nets for SF?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77095&start=5) by Sopel, [CCC](/CCC "CCC"), April 16, 2021
- [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=39) by Sopel, [CCC](/CCC "CCC"), July 01, 2021 » [NNUE Question](/NNUE#KingPlacements "NNUE")
- [Fat Titz 1.0 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78026) by Sopel, [CCC](/CCC "CCC"), Aug 26, 2021
- [Fat Titz 1.1 released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78071) by Sopel, [CCC](/CCC "CCC"), Aug 31, 2021

## 2022 ...

- [Fat Titz 2 released!](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79112) by Tomasz Sobczyk, [CCC](/CCC "CCC"), January 13, 2022

# External Links

- [Sopel97 (Tomasz Sobczyk) · GitHub](https://github.com/Sopel97)

## Stockfish

- [GitHub - Sopel97/Stockfish: UCI chess engine](https://github.com/Sopel97/Stockfish)
- [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474)
- [Reduce the number of accumulator states from 3 to 2. Make the intent of the states clearer. by Sopel97 · Pull Request #3548 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3548)
- [New NNUE architecture and net by Sopel97 · Pull Request #3646 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3646)

## Pytorch NNUE

- [GitHub - Sopel97/nnue-pytorch: NNUE (Chess evaluation) trainer in Pytorch](https://github.com/Sopel97/nnue-pytorch)
- [Defer data preparation to native code. Use sparse input tensors. by Sopel97 · Pull Request #1 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/1)
- [A custom kernel for the feature transformer. by Sopel97 · Pull Request #96 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/96)
- [Update and enhance information about additional feature factors. by Sopel97 · Pull Request #109 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/109)
- [Update trainer to the new architecture. by Sopel97 · Pull Request #110 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/110)

# References

1. [↑](#cite_ref-1) [NNUE Guide (nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub)](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md) hosted by [Gary Linscott](/Gary_Linscott "Gary Linscott")
2. [↑](#cite_ref-2) [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474)
3. [↑](#cite_ref-3) [nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub - HalfKAv2 feature set](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#halfkav2-feature-set)
4. [↑](#cite_ref-4) [New NNUE architecture and net by Sopel97 · Pull Request #3646 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3646)
5. [↑](#cite_ref-5) [nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub - HalfKAv2 feature set](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#halfkav2_hm-feature-set)
6. [↑](#cite_ref-6) [Optimization of the affine transformations. by Sopel97 · Pull Request #3203 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3203)
7. [↑](#cite_ref-7) [AVX-512 optimizations. by Sopel97 · Pull Request #3218 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3218)
8. [↑](#cite_ref-8) [Optimize and tidy up affine transform code. by Sopel97 · Pull Request #3663 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3663)
9. [↑](#cite_ref-9) [Defer data preparation to native code. Use sparse input tensors. · Pull Request #1 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/1)
10. [↑](#cite_ref-10) [A custom kernel for the feature transformer. · Pull Request #96 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/96)
11. [↑](#cite_ref-11) [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), June 17, 2021
12. [↑](#cite_ref-12) [Pull Requests by Sopel97 · nodchip/Stockfish · GitHub](https://github.com/nodchip/Stockfish/pulls?q=is%3Apr+author%3ASopel97)
13. [↑](#cite_ref-13) [official-stockfish tools branch · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/tree/tools)
14. [↑](#cite_ref-14) [Sopel97/nnue\_data\_compress · GitHub](https://github.com/Sopel97/nnue_data_compress)
15. [↑](#cite_ref-15) [Introduce sfen\_format option for gensfen. Experimental support for binpack format in gensfen and learn. · Pull Request #129 · nodchip/Stockfish · GitHub](https://github.com/nodchip/Stockfish/pull/129)
16. [↑](#cite_ref-16) [Pull Requests by Sopel97 · nodchip/Stockfish · GitHub](https://github.com/nodchip/Stockfish/pulls?q=is%3Apr+author%3ASopel97)
17. [↑](#cite_ref-17) [Pull Requests by Sopel97 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pulls?q=is%3Apr+author%3ASopel97)
18. [↑](#cite_ref-18) [Pull Requests by Sopel97 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pulls?q=is%3Apr+author%3ASopel97)
19. [↑](#cite_ref-19) [Sopel97/FatTitz · GitHub](https://github.com/Sopel97/FatTitz)
20. [↑](#cite_ref-20) [Fat Titz 1.0 released by](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78026) Sopel[, [CCC](/CCC "CCC"), Aug 26, 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78026)

**[Up one level](/People "People")**