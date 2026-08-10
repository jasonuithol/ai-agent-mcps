# ProbCut

Source: https://www.chessprogramming.org/ProbCut

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Selectivity](/Selectivity "Selectivity") \* [Pruning](/Pruning "Pruning") \* ProbCut**

[![](/images/thumb/d/dc/MProbeCut.JPG/300px-MProbeCut.JPG)](/File:MProbeCut.JPG)

[Search Trees](/Search_Tree "Search Tree") with two ProbCut generalizations [[1]](#cite_note-1)

**ProbCut**,  
a selective search enhancement of the [alpha-beta](/Alpha-Beta "Alpha-Beta") algorithm created in 1994 by [Michael Buro](/Michael_Buro "Michael Buro") as introduced in his Ph.D. thesis [[2]](#cite_note-2). It permits to exclude probably irrelevant subtrees from beeing searched deeply. ProbCut and its improved variant **Multi–ProbCut** (MPC) have been shown to be effective in [Othello](/Othello "Othello") [[3]](#cite_note-3) and [Shogi](/Shogi "Shogi") [[4]](#cite_note-4), and a technique similar to ProbCut is used in the [checkers](/Checkers "Checkers") program [Chinook](/index.php?title=Chinook&action=edit&redlink=1 "Chinook (page does not exist)") by [Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer") et al. (1992) [[5]](#cite_note-5) described their approach in a footnote: Chinook performs forward cuts in positions with a [material](/Material "Material") deficit, where a shallow search does not show an escape. ProbCut is a generalization of this method in that it is game independent. It was tested by incorporating it in Buro's already strong Othello program *Logistello* [[6]](#cite_note-6) and increased the program's playing strength [[7]](#cite_note-7). Despite some promising results reported by [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang") and Michael Buro with [Crafty](/Crafty "Crafty") [[8]](#cite_note-8), it seemed not that successful in chess programs which already perform [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning") and [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions"), until [Stockfish](/Stockfish "Stockfish") proved otherwise as implemened by [Gary Linscott](/Gary_Linscott "Gary Linscott") [[9]](#cite_note-9) [[10]](#cite_note-10).

# The Idea

ProbCut is based on the idea that the result *v **of a shallow search with [depth](/Depth "Depth")*** **d** is a rough estimate of the result *v* of a deeper search with depth *d > d'*. A way to model this relationship is by means of a [linear model](https://en.wikipedia.org/wiki/Linear_model):

```
v = a*v' + b + e
```

where e is a [normally distributed](https://en.wikipedia.org/wiki/Normal_distribution) [error variable](https://en.wikipedia.org/wiki/Standard_error_%28statistics%29) with [mean](https://en.wikipedia.org/wiki/Mean) 0 and [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) σ ([sigma](https://en.wikipedia.org/wiki/Sigma)) or [variance](https://en.wikipedia.org/wiki/Variance) σ². If the evaluation function is relative stable, the [slope](https://en.wikipedia.org/wiki/Slope) a is about 1.0, offset b about 0.0 and a small variance σ². The cutoff condition of depth d

```
v ≥ β
```

becomes

```
(v' + b - β)/σ ≥ -e/σ
```

since -e/σ is normally distributed with mean 0 and variance 1 (and [distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) Φ, [phi](https://en.wikipedia.org/wiki/Phi)), the condition holds true with [probability](https://en.wikipedia.org/wiki/Probability) of at least *p* [iff](https://en.wikipedia.org/wiki/If_and_only_if)

```
(v' + b - β)/σ ≥ Φ-1(p)
```

which is equivalent to

```
v' ≥ (Φ-1(p) * σ + β - b) / a
```

Similar for

```
v ≤ α
```

the condition becomes

```
v' ≤ (-Φ-1(p) * σ + α - b) / a
```

# Pseudo Code

This observation immediately leads to the implementation of the ProbCut alpha-beta extension for one depth and reduced depth pair using [floats](/Float "Float"). Before [sigma](https://en.wikipedia.org/wiki/Sigma), a and b are estimated by [linear regression](https://en.wikipedia.org/wiki/Linear_regression) likely for different [game phases](/Game_Phases "Game Phases"), the search depths d and d' < d and cut threshold must be chosen or be determined [empirically](https://en.wikipedia.org/wiki/Empirical), by checking the performance of the program with various parameter settings [[11]](#cite_note-11) .

```
int alphaBetaProbCut(int α, int β, int depth) {
   const float T(1.5);
   const int DP(4);
   const int D(8);

   if ( depth == 0 ) return evaluate();

   if ( depth == D ) {
      int bound;

      /* v >= β with prob. of at least p? yes => cutoff */
      bound = round( ( T * σ + β - b) / a );
      if ( alphaBetaProbCut( bound-1, bound, DP) >= bound )
         return β;

      /* v <= α with prob. of at least p? yes => cutoff */
      bound = round( (-T * σ + α - b) / a );
      if ( alphaBetaProbCut( bound, bound+1, DP) <= bound )
         return α;
   }
   /* the remainder of alpha-beta goes here */
   ...
}
```

# Multi–ProbCut

Multi–ProbCut (MPC) enhances ProbCut by

- Allowing different regression parameters and cut thresholds for different stages of the game
- Using more than one depth pair
- Using [internal iterative deepening](/Internal_Iterative_Deepening "Internal Iterative Deepening") for shallow searches

```
struct Param {
   int d;         /* shallow search depth */
   float t;       /* cut threshold */
   float a, b, σ; /* slope, offset, standard deviation */
} param[MAX_STAGE+1][MAX_HEIGHT+1][NUM_TRY];

int alphaBetaMPC(int α, int β, int depth)
{
   if ( depth == 0 ) return evaluate();

   if ( depth <= MAX_D ) {
      for (int i=0; i < NUM_TRY; i++) {
         int bound;
         const Param &pa = param[stage][depth][i];

         if (pa.d < 0 )
            break; /* no more parameters available */

         /* v >= β with prob. of at least p? yes => cutoff */
         bound = round( ( pa.t * pa.σ + β - pa.b) / pa.a );
         if ( alphaBetaMPC( bound-1, bound, pa.d) >= bound )
            return β;

         /* v <= α with prob. of at least p? yes => cutoff */
         bound = round( (-pa.t * pa.σ + α - pa.b) / pa.a );
         if ( alphaBetaMPC( bound, bound+1, pa.d) <= bound )
            return α;
      }
   }
   /* the remainder of alpha-beta goes here */
   ...
}
```

# ProbeCut or MPC in Chess

In 2003, [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang") implemented ProbCut and MPC in [Crafty](/Crafty "Crafty") by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"). In his thesis he introductory elaborates on ProbCut in Chess [[12]](#cite_note-12) :

```
There has been no report of success for ProbCut or MPC in chess thus far. There are at least two reasons for this:
```

1. `Null-move is available for chess. Null-move and ProbCut are based on similar ideas, as a result they tend to prune the same type of positions. Part of the reason why ProbCut is so successful in Othello is that null-move does not work in Othello. But in chess, ProbCut and MPC have to compete with null-move, which is way better than brute-force alpha-beta.`
2. `Chess searches tend to make more mistakes than Othello searches` [[13]](#cite_note-13)`. This leads to a larger standard deviation in the linear relationship between shallow and deep search results, which makes it harder to get ProbCut cuts`.

In his research, Albert Xin Jiang further determined following parameters by [linear regression](https://en.wikipedia.org/wiki/Linear_regression). The about 2700 positions were chosen randomly from some computer chess tournament games and some of Crafty’s games against human grandmasters on internet chess servers:

[![CraftyLinearReg.JPG](/images/a/ac/CraftyLinearReg.JPG)](/File:CraftyLinearReg.JPG)

v' versus v for depth pair (4,8) [[14]](#cite_note-14)

Linear regression results. The evaluation function’s scale is 100 = one pawn. r is the [regression correlation coefficient](https://en.wikipedia.org/wiki/Correlation_and_dependence), a measure of how good the data fits the linear model:

| Pairs | Stage | a | b | σ | r |
| --- | --- | --- | --- | --- | --- |
| (3,5) | [Middlegame](/Middlegame "Middlegame") | 0.998 | -7.000 | 55.80 | 0.90 |
| (3,5) | [Endgame](/Endgame "Endgame") | 1.026 | -4.100 | 51.80 | 0.94 |
| (4,8) | Middlegame | 1.020 | 2.360 | 82.00 | 0.82 |
| (4,8) | Endgame | 1.110 | 1.750 | 75.00 | 0.90 |

While ProbCut did not result in better playing strength of Crafty, Albert Xin Jiang and Michael Buro report an improvement with MPC while playing two times three 64-game [matches](/Match_Statistics "Match Statistics") with three Crafty versions and two time controls versus [Dieter Bürßner's](/Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") program [Yace](/Yace "Yace") [[15]](#cite_note-15) :

| Pairing | Crafty % | |
| --- | --- | --- |
| 2min +  10sec/move | 8min +  20sec/move |
| Crafty - Yace | 42.0 | 50.8 |
| MPC Crafty(1.2, 1.0) - Yace | 53.1 | 56.3 |
| MPC Crafty(1.0, 1.0) - Yace | 57.0 | 55.5 |

However, [Robert Hyatt](/Robert_Hyatt "Robert Hyatt") first stated results were inconclusive [[16]](#cite_note-16) , and later that MPC was somewhat worse in every test he tried [[17]](#cite_note-17) , also confirmed by [Robert Allgeuer](/index.php?title=Robert_Allgeuer&action=edit&redlink=1 "Robert Allgeuer (page does not exist)"), who performed Crafty MPC tests with following conclusion in [CCC](/CCC "CCC") [[18]](#cite_note-18) :

```
My tests indicate that the overall playing strength of Crafty 18.15 remains more or less unchanged by the addition of Multi-ProbCut. However, the characteristic of the engine changes significantly due to ProbCut: Even though nominal search depth is increased by one to two plies, tactical strength is severely reduced.
```

```
Furthermore with ProbCut match results become more unpredictable and inconsistent: Apparently there are types of opponents against which ProbCut works very well and results in significantly improved results, but there are also other opponents (the tactically stronger ones?) where ProbCut has exactly the opposite effect.
```

# See also

- [Enhanced Forward Pruning](/Enhanced_Forward_Pruning "Enhanced Forward Pruning")
- [Futility Pruning](/Futility_Pruning "Futility Pruning")
- [Late Move Reductions](/Late_Move_Reductions "Late Move Reductions")
- [Match Statistics](/Match_Statistics "Match Statistics")
- [Multi-Cut](/Multi-Cut "Multi-Cut")
- [Null Move Pruning](/Null_Move_Pruning "Null Move Pruning")
- [RankCut](/RankCut "RankCut")

# Publications

[[19]](#cite_note-19) [[20]](#cite_note-20)

- [Michael Buro](/Michael_Buro "Michael Buro") (**1994**). *Techniken für die Bewertung von Spielsituationen anhand von Beispielen.* Ph.D. Thesis. [Paderborn University](/Paderborn_University "Paderborn University"), Paderborn, Germany. (German), [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/mics_dis.pdf)
- [Michael Buro](/Michael_Buro "Michael Buro") (**1995**). *ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm.* [ICCA Journal, Vol 18, No. 2](/ICGA_Journal#18_2 "ICGA Journal"), [pdf](https://skatgame.net/mburo/ps/probcut.pdf)
- [Michael Buro](/Michael_Buro "Michael Buro") (**1997**). *Experiments with Multi-ProbCut and a New High-quality Evaluation Function for Othello.* Technical Report No. 96, NEC Research Institute, [pdf](https://skatgame.net/mburo/ps/improve.pdf)
- [Michael Buro](/Michael_Buro "Michael Buro") (**2000**). *Experiments with Multi-ProbCut and a new High-Quality Evaluation Function for Othello.* Games in AI Research
- [Kazutomo Shibahara](/Kazutomo_Shibahara "Kazutomo Shibahara"), [Nobuo Inui](/index.php?title=Nobuo_Inui&action=edit&redlink=1 "Nobuo Inui (page does not exist)"), [Yoshiyuki Kotani](/Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2002**). *Effect of ProbCut in Shogi - by changing parameters according to position category*. [7th Game Programming Workshop](/Conferences#GPW "Conferences")
- [Michael Buro](/Michael_Buro "Michael Buro") (**2002**). *Multi-ProbCut Search*. slides as [pdf](https://skatgame.net/mburo/ps/mpc.pdf)
- [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang") (**2003**). *Implementation of Multi-ProbCut in Chess*. CPSC 449 Thesis, [pdf](http://www.cs.ubc.ca/%7Ejiang/papers/thesis.pdf)
- [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang"), [Michael Buro](/Michael_Buro "Michael Buro") (**2003**). *First Experimental Results of ProbCut Applied to Chess*. [Advances in Computer Games 10](/Advances_in_Computer_Games_10 "Advances in Computer Games 10")
- [Maarten Schadd](/index.php?title=Maarten_Schadd&action=edit&redlink=1 "Maarten Schadd (page does not exist)"), [Mark Winands](/Mark_Winands "Mark Winands"), [Jos Uiterwijk](/Jos_Uiterwijk "Jos Uiterwijk") (**2009**). *ChanceProbCut: Forward Pruning in Chance Nodes*. in IEEE Symposium on Computational Intelligence and Games (CIG 2009)

# Forum Posts

- [whats probcut?](https://www.stmintz.com/ccc/index.php?id=66467) by vitor, [CCC](/CCC "CCC"), August 29, 1999
- [muliti probcut](https://www.stmintz.com/ccc/index.php?id=178124) by [Martin Fierz](/Martin_Fierz "Martin Fierz"), [CCC](/CCC "CCC"), July 04, 2001
- [Multi-ProbCut and Crafty : does it work ?](https://www.stmintz.com/ccc/index.php?id=303536) by [Frédéric Louguet](/Fr%C3%A9d%C3%A9ric_Louguet "Frédéric Louguet"), [CCC](/CCC "CCC"), June 28, 2003
- [Crafty MPC tests (long post)](https://www.stmintz.com/ccc/index.php?id=322133) by [Robert Allgeuer](/index.php?title=Robert_Allgeuer&action=edit&redlink=1 "Robert Allgeuer (page does not exist)"), [CCC](/CCC "CCC"), October 18, 2003
- [ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm](https://www.stmintz.com/ccc/index.php?id=378283) by [Albert Silver](/Albert_Silver "Albert Silver"), [CCC](/CCC "CCC"), July 21, 2004
- [Re: Possible search improvment](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=274486&t=28459) by [Ryan Benitez](/Ryan_Benitez "Ryan Benitez"), [CCC](/CCC "CCC"), June 17, 2009 » [History Leaf Pruning](/History_Leaf_Pruning "History Leaf Pruning")
- [Bad Pruning](http://www.talkchess.com/forum/viewtopic.php?t=38407) by [Onno Garms](/Onno_Garms "Onno Garms"), [CCC](/CCC "CCC"), March 13, 2011
- [Probcut](http://www.talkchess.com/forum/viewtopic.php?p=518426) by [Gary](/Gary_Linscott "Gary Linscott"), [CCC](/CCC "CCC"), May 24, 2013 » [Stockfish](/Stockfish "Stockfish")

# External Links

- [Writing an Othello program](http://radagast.se/othello/howto.html) by [Gunnar Andersson](/Gunnar_Andersson "Gunnar Andersson")
- [SmartGame Library: SgProbCut.h File Reference](http://fuego.sourceforge.net/fuego-doc-1.1/smartgame-doc/SgProbCut_8h.html#_details), [Fuego Documentation](http://fuego.sourceforge.net/fuego-doc-1.1/) [[21]](#cite_note-21)

# References

1. [↑](#cite_ref-1) Illustrations of the first two ProbCut generalizations: a) allowing forward cuts at several heights and b) performing a sequence of check searches of increasing depth from [Michael Buro](/Michael_Buro "Michael Buro") (**1997**). *Experiments with Multi-ProbCut and a New High-quality Evaluation Function for Othello.* Technical Report No. 96, NEC Research Institute, Princeton, N.J. [pdf](http://skatgame.net/mburo/ps/improve.pdf), 8 Multi-ProbCut, pp 7.
2. [↑](#cite_ref-2) [Michael Buro](/Michael_Buro "Michael Buro") (**1994**). *Techniken für die Bewertung von Spielsituationen anhand von Beispielen.* Ph.D. Thesis. [Paderborn University](/Paderborn_University "Paderborn University"), Paderborn, Germany. (German), Kapitel 4. Selektive Suche
3. [↑](#cite_ref-3) [Michael Buro](/Michael_Buro "Michael Buro") (**1997**). *Experiments with Multi-ProbCut and a New High-quality Evaluation Function for Othello.* Technical Report No. 96, NEC Research Institute, Princeton, N.J. [pdf](https://skatgame.net/mburo/ps/improve.pdf)
4. [↑](#cite_ref-4) [Kazutomo Shibahara](/Kazutomo_Shibahara "Kazutomo Shibahara"), [Nobuo Inui](/index.php?title=Nobuo_Inui&action=edit&redlink=1 "Nobuo Inui (page does not exist)"), [Yoshiyuki Kotani](/Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2002**). *Effect of ProbCut in Shogi - by changing parameters according to position category*. [7th Game Programming Workshop](/Conferences#GPW "Conferences")
5. [↑](#cite_ref-5) [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Joe Culberson](/Joe_Culberson "Joe Culberson"), [Norman Treloar](/index.php?title=Norman_Treloar&action=edit&redlink=1 "Norman Treloar (page does not exist)"), [Brent Knight](/index.php?title=Brent_Knight&action=edit&redlink=1 "Brent Knight (page does not exist)"), [Paul Lu](/Paul_Lu "Paul Lu"), [Duane Szafron](/Duane_Szafron "Duane Szafron") (**1992**). *A World Championship Caliber Checkers Program*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 53, Nos. 2-3, pp. 6, "If a line leads to a material deficit and there is insufficient positional compensation (the positional assessment of the position does not reach a fixed threshold) then the remaining search depth is cut in half. If the result of this search does not restore the material deficit, or result in sufficient positional compensation, this line is abandoned. Otherwise, the line is researched to the full search depth".
6. [↑](#cite_ref-6) [LOGISTELLO's Homepage](http://skatgame.net/mburo/log.html)
7. [↑](#cite_ref-7) [Michael Buro](/Michael_Buro "Michael Buro") (**1995**). *ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm.* [ICCA Journal, Vol 18, No. 2](/ICGA_Journal#18_2 "ICGA Journal"), [pdf](https://skatgame.net/mburo/ps/probcut.pdf)
8. [↑](#cite_ref-8) [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang"), [Michael Buro](/Michael_Buro "Michael Buro") (**2003**). *First Experimental Results of ProbCut Applied to Chess*. [Advances in Computer Games 10](/Advances_in_Computer_Games_10 "Advances in Computer Games 10")
9. [↑](#cite_ref-9) [Probcut](http://www.talkchess.com/forum/viewtopic.php?p=518426) by [Gary](/Gary_Linscott "Gary Linscott"), [CCC](/CCC "CCC"), May 24, 2013
10. [↑](#cite_ref-10) [Stockfish/search.cpp at master · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/blob/master/src/search.cpp), Step 9. ProbCut
11. [↑](#cite_ref-11) [Michael Buro](/Michael_Buro "Michael Buro") (**1995**). *ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm.* [ICCA Journal, Vol 18, No. 2](/ICGA_Journal#18_2 "ICGA Journal"), [pdf](https://skatgame.net/mburo/ps/probcut.pdf)
12. [↑](#cite_ref-12) [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang") (**2003**). *Implementation of Multi-ProbCut and Chess*. CPSC 449 Thesis, [pdf](http://www.cs.ubc.ca/%7Ejiang/papers/thesis.pdf), 2.5 ProbeCut in Chess, pp. 6
13. [↑](#cite_ref-13) [Andreas Junghanns](/Andreas_Junghanns "Andreas Junghanns"), [Jonathan Schaeffer](/Jonathan_Schaeffer "Jonathan Schaeffer"), [Mark Brockington](/Mark_Brockington "Mark Brockington"), [Yngvi Björnsson](/Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](/Tony_Marsland "Tony Marsland") (**1997**). *Diminishing Returns for Additional Search in Chess.* [Advances in Computer Chess 8](/Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
14. [↑](#cite_ref-14) Image from [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang") (**2003**). *Implementation of Multi-ProbCut in Chess*. CPSC 449 Thesis, [pdf](http://www.cs.ubc.ca/%7Ejiang/papers/thesis.pdf)
15. [↑](#cite_ref-15) Page 30 in [Albert Xin Jiang](/Albert_Xin_Jiang "Albert Xin Jiang"), [Michael Buro](/Michael_Buro "Michael Buro") (**2003**). *First Experimental Results of ProbCut Applied to Chess*. [Advances in Computer Games 10](/Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://cs.ubc.ca/%7Ejiang/papers/mpc_main.pdf)
16. [↑](#cite_ref-16) [Re: Multi-ProbCut and Crafty : does it work ?](https://www.stmintz.com/ccc/index.php?id=303565) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), June 28, 2003
17. [↑](#cite_ref-17) [Re: ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm](https://www.stmintz.com/ccc/index.php?id=378374) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/CCC "CCC"), July 21, 2004
18. [↑](#cite_ref-18) [Crafty MPC tests (long post)](https://www.stmintz.com/ccc/index.php?id=322133) by [Robert Allgeuer](/index.php?title=Robert_Allgeuer&action=edit&redlink=1 "Robert Allgeuer (page does not exist)"), [CCC](/CCC "CCC"), October 18, 2003
19. [↑](#cite_ref-19) [Michael Buro's Publication List](http://skatgame.net/mburo/publications.html)
20. [↑](#cite_ref-20) [Albert Xin Jiang - publications](http://www.cs.ubc.ca/%7Ejiang/)
21. [↑](#cite_ref-21) [Fuego](http://www.grappa.univ-lille3.fr/icga/program.php?id=535), [Go](/Go "Go") playing program by [Markus Enzenberger](/Markus_Enzenberger "Markus Enzenberger"), [Martin Müller](/Martin_M%C3%BCller "Martin Müller"), [Broderick Arneson](/index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), [Richard Segal](/index.php?title=Richard_Segal&action=edit&redlink=1 "Richard Segal (page does not exist)"), [Gerald Tesauro](/Gerald_Tesauro "Gerald Tesauro") and [Arpad Rimmel](/index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)")

**[Up one Level](/Pruning "Pruning")**