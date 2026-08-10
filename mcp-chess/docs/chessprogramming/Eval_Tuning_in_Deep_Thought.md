# Eval Tuning in Deep Thought

Source: https://www.chessprogramming.org/Eval_Tuning_in_Deep_Thought

**[Home](/Main_Page "Main Page") \* [Automated Tuning](/Automated_Tuning "Automated Tuning") \* Eval Tuning in Deep Thought**

**Eval Tuning in Deep Thought**,  
this page is a formatted reprint of [Andreas Nowatzyk's](/Andreas_Nowatzyk "Andreas Nowatzyk") explanations of the [Eval Tuning](/Automated_Tuning "Automated Tuning") source code [[1]](#cite_note-1) of [Deep Thought](/Deep_Thought "Deep Thought") from January 2000 [[2]](#cite_note-2) , hosted by [Tim Mann](/Tim_Mann "Tim Mann") [[3]](#cite_note-3) :

```
Andreas Nowatzyk was one of the contributors to the Deep Thought project while he was in grad school. A few years ago when he and I were both working for Compaq's research labs in Palo Alto, Andreas sent me a copy of Deep Thought's evaluation function tuning program and asked me to put it on the Web for him, since he no longer has an interest in computer chess.
```

# The Files

in this directory constitute the tuning program that was used by [Deep Thought](/Deep_Thought "Deep Thought") to adjust its [evaluation function](/Evaluation "Evaluation") parameters based on a set of some 868 grand-master games. I forgot where these games came from, but we did not type them in. It was last used in the summer of 1988 and it is believed that this program might be of historical interest to some chess programmers. The Deep Thought hardware is probably no longer functional and without the actual Deep Thought program, this code can only show how DT evaluated [chess positions](/Chess_Position "Chess Position"), but it can not play any chess.

This program was written by me during the Spring of 1988 and included suggestions and feedback from the entire Deep Thought team ([Feng H. Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Thomas S. Anantharaman](/Thomas_Anantharaman "Thomas Anantharaman"), [Murray S. Campbell](/Murray_Campbell "Murray Campbell"), [Mike C. Browne](/Mike_Browne "Mike Browne") and [myself](/Andreas_Nowatzyk "Andreas Nowatzyk")). It includes the DT evaluation function, which was developed by Murray.

This file gives a brief description how this tuning program worked and how to use it. Expect some errors and omissions because I'm writing this from memory, 12 years after I last touched this code.

## The Basic Method

The basic method used the mathematical concept of [least square fitting](https://en.wikipedia.org/wiki/Least_squares). This was hardly new and it had been applied to chess evaluation functions before. However, there are plenty of details on exactly how to go about this, and our approach likely differed from earlier work.

Let's suppose that the evaluation function is a weighted sum of positional features (later referred to as a feature vector):

[![DTEValFormula.jpg](/images/8/8b/DTEValFormula.jpg)](/File:DTEValFormula.jpg)

For a given chess position

(= position of pieces on the board plus [castle](/Castling_Rights "Castling Rights") and [enpassant](/En_passant "En passant") status), the evaluation <E(P)> is the sum of the features recognized by Deep Thought <Fi(P)> times the weight given to each feature <Ai>. For example, a feature may be the number of white pawns minus the number of black pawns. The corresponding weight would be the value for one pawn. There were roughly 100 features that Deep Though used. Some were implemented via a [piece-placement table](/Piece-Square_Tables "Piece-Square Tables") that could give a different weight for each piece depending on where it is on the board. For example, a [gradient](https://en.wikipedia.org/wiki/Gradient) in the pawn value could be used to add a bonus for advanced pawns. [King centrality](/King_Centralization "King Centralization") was implemented likewise. There were five other tables in the hardware for more complex features, that could detect [open files](/Open_File "Open File"), [passed](/Passed_Pawn "Passed Pawn")/[doubled pawns](/Doubled_Pawn "Doubled Pawn") etc. (four [pawn structure](/Pawn_Structure "Pawn Structure") tables of 8192 entries each, a rook evaluation table with 2048 entries and the 1024 entry piece/placement table along with a few special bonus registers made up the DT evaluation hardware. While these nearly 40,000 programmable parameters of the DT hardware could be regarded as the components of DT's evaluation function, they all were derived from the 89 to ~100 parameters mentioned earlier). The basic DT move cycle consisted of computing these tables before every search so that the weights of the evaluation function could be adjusted according to the overall situation of the game (opening, mid-game, endgame, etc.). This took some time, so DT was not good at fast games (keep in mind that DT used '88 hardware and the VME interface from the host, a [Sun 3](/Sun#3 "Sun") or 4, was not a spead deamon).
  
  
Now suppose you had an [oracle](/Oracle "Oracle") that could give the correct evaluation for a position O(P). If we use this oracle on a sufficiently large set of positions <Pj> then we could minimize the [squared evaluation error](https://en.wikipedia.org/wiki/Mean_squared_error) sum:  

[![DTEValError.jpg](/images/3/3a/DTEValError.jpg)](/File:DTEValError.jpg)

via [partial differentiation](https://en.wikipedia.org/wiki/Partial_derivative) of this expression for each parameter <Ai>. This leads to a [linear equation system](https://en.wikipedia.org/wiki/System_of_linear_equations) with one equation for each unknown parameter of DT's evaluation function. If the positions are sufficiently varied (they usually were), then this equation system can be solved and out come the best values for our evaluation parameters.
  
  
The trouble was, we did not have such an oracle. So the next best thing we had is the evaluation of DT. Murray made some initial guesses for each parameter <Ai> and we used that as a starting point. Obviously, if we use our own <E(P)> as an oracle, we get the same parameters out of the least square fit as we put in. So this is just a cumbersome way to compute the identity: New(Ai) = Old(Ai) for all <i=1..100>. However, this was a great debugging tool to see that we got the mathematics right.
  
  
In the tuning case, we did not just take the top-level evaluation, rather we let DT [search](/Search "Search") shallow 3[ply](/Ply "Ply") trees with [quiescence extensions](/Quiescence_Search "Quiescence Search"). The evaluation function is then computed symbolically: rather then plugging in values, we propagated the feature vector of the best leaf node to the top. The search itself was controlled by the current best guess of the evaluation parameters. These were full [min/max](/Minimax "Minimax") searches, rather than [alpha/beta](/Alpha-Beta "Alpha-Beta") searches. The tuning program cannot actually search these trees because it does not know what a [legal chess move](/Legal_Move "Legal Move") is. Instead, the actual DT was used to pre-search these trees and the results were stored in a database (dbf\_all). The tuning program merely traverses these trees.
  
  
Now we are still lacking an oracle. Instead we assumed that in our collection of grand-master games, the winner of each games should serve as a substitute oracle for DT. Discarding the moves of the losing side and the first few [opening moves](/Opening_Book "Opening Book"), we considered all available moves for each positions. Each position was searched and evaluated. Suppose that there were 20 legal moves in one position <Px> then each of these moves lead to a new position <P0> ... <P19>, for which we get the evaluations <E(P0)> ... <E(P19)>. Let's assume that the winning GM played the move leading to <P0> from <Px>. Then there are two cases:

1. DT's evaluation concurs, that is: E(P0) > E(P1...19)
2. DT evaluated some other move as best.

So the objective of our tuning procedure was to maximize the first case and minimize the second case.
  
  
The GM games tell us which moves are better, relative to other moves. So rather than having an absolute oracle that assigns an absolute value to a position, we have a kind of relative oracle: The move from <Px> to <P0> is expected to be better than the moves from <Px> to <P1..19>. Hence <E(P0) - E(Px)> ought to be larger than <E(P1..19) - E(Px)>. These differences of evaluations were used for the tuning process, but this did not change much: we still end up with linear combinations of elements of the feature vector that can be dealt with via least square fitting. In the program and on the display, the evaluations <Ex>, <E0> and <En, n=1...> refer to the evaluation of the root position, the position of the winning GM move and the evaluation of move <n>.
  
  
Naturally, not all changes to the evaluation of the board are positional in nature and/or are captured by the evaluation function. The fact that the pre-computed search trees include the results after quiescence search should minimize differences due to exchanges, but this is not always the case. Therefore in order to avoid interference from elements that DT discovers via search and not via its evaluation function, the tuning program includes a threshold: if the evaluation of the [root position](/Root "Root") and the position after a move differ by too much (more than 64 = half of a pawn value), then it is assumed that there is something going on that the evaluation function cannot grasp and this data-point is ignored (out-of-bound).
  
  
The first idea was to apply a [force function](https://en.wikipedia.org/wiki/Forcing_function_%28differential_equations%29). Instead of using <E(P)> as an oracle, we used <E(P) + G(P)> as an oracle. A simple force function <G(P)> would be used to add a constant force value if the position is the result of the GM move and 0 otherwise.
  
  
This doesn't really work as it leads to a value inflation. So instead of adding no bonus for the wrong positions, we add <- force/n>, where <n> is the number of wrong moves (positions).
  
  
This is in fact what an early version of the tuning code did. Add a small force as described above, compute a new parameter set via least square approximation and iterate until the number of correctly evaluated positions does not increase anymore.
  
  
This works, but it did not really yield better play of DT. It became clear that maximizing the agreement between DT's evaluation and the GM move choices and better play were not really the same thing. Also, DT searched 9+ plys and we could tune only on 3ply searches due to compute time limitations.
  
  
We observed that deeper searches in the tuning code lead to better results, even though it could be argued that evaluations should be [orthogonal](https://en.wikipedia.org/wiki/Orthogonality#Statistics.2C_econometrics.2C_and_economics) to searching. Perhaps an explanation for this effect is that deeper searches lead to more differences in the positions that are being related because they are more moves apart. Therefore, the tuning process collects more information on how individual components of the evaluation relate to each other. For example, the tuning process did result in a better understanding of the [piece-values](/Point_Value "Point Value") with respect to each others and as a function of the amount of material left on the board (this was used to control the transitions from [opening](/Opening "Opening"), [mid-game](/Middlegame "Middlegame") to [end-game](/Endgame "Endgame")).
  
  
The next refinement was to make the force dependent on the amount of miss-evaluation. If DT is just a little bit off, use a small force, if DT misses the position in a big way, add more force. This relationship was subject to much debate and it is unclear which [monotonic function](https://en.wikipedia.org/wiki/Monotonic_function) is best suited. Hence, the tuning program gives a number of options from [linear](https://en.wikipedia.org/wiki/Linear_function), [quadratic](https://en.wikipedia.org/wiki/Quadratic_function), [square-root](https://en.wikipedia.org/wiki/Square_root), [logarithmic](https://en.wikipedia.org/wiki/Logarithm), to [reciprocal](https://en.wikipedia.org/wiki/Multiplicative_inverse) (the idea behind a reciprocal force function was this: if DT is just a little off then there is hope that it can [learn](/Learning "Learning") how to evaluate this position correctly. If it is off by a lot, don't bother to try - it will only screw up things elsewhere because this is likely due to a concept that is missing from DT's evaluation function). Which force-function to use eventually depended on which parameters were subjected to tuning and became more of a [trial and error](/Trial_and_Error "Trial and Error") procedure.
  
  
A somewhat different idea for a force function was to count how many moves were evaluated ahead of the GM-move. If this is 0, DT's evaluation function is on target. Numbers greater than 0 are undesirable and lead to an increased correcting force. This number was also used to compute a histogram to see how DT's evaluation function scores against GM moves (see the \*.stat files after a [multi-iteration](/Iteration "Iteration") tuning run). This is to be taken with a large [grain of salt](https://en.wikipedia.org/wiki/Grain_of_salt), because the 3ply searches are clearly not good enough to isolate positional evaluation from [tactics](/Tactics "Tactics").
  
  
At this point things started to improve somewhat (mostly measured via self-play tournaments starting from various seed positions). But also funny things happened to DT's evaluation function: the range of values that it would produce during a search became smaller. The evaluation function became less discriminative: the values for the good and bad moves were progressively moving closer together. It did match more GM moves and played slightly better, but it also became more erratic. Interestingly, this reduction in value range was not due to simply reducing the weight for the positional components of the evaluation function, rather it involved balancing the various components against each other.
  
  
So a compensating force was added to the correction force so that it would also encourage to keep a certain variance of evaluations. You see this in the code commented as variance compensation.
  
  
As we learned how to tune more effectively, it became clear that tuning all parameters at once was not necessarily a good idea. Certain parameters were used very infrequently in our set of GM games, so allowing these to be tuned can pick up the wrong idea for lack of sufficient data points. 868 games were not really enough to tune this many parameters.
  
  
It also became clear that the best parameter sets were usually obtained after 10-15 iterations, and before the maximum match to the GM games was reached, which typically required 20 to 30 iterations.
  
  
Finally, the last improvement of the tuning came after we added the ability to tune tables. In the DT evaluation function are a number of tables, for example the pawn advancement gradient, or the King centrality table. Instead of just making up a linear gradient, we allowed the tuning code to change the values of these table and allow more complex gradients. This resulted in some strange 3D curves that upon inspection by Murray were found to contain some known chess heuristics, which were not originally part of DT's evaluation function (for example: the pawn advancement gradient became more pronounced near the center and tapered off towards the promotion squares). However, the overall impact of table fitting was minor and was never fully exploited because the code became stable only near the end of DT's life and we did not have enough compute cycles to experiment a lot with it. The few experiments we did were great fun because we extracted some general rules out of the game database in an unbiased, neutral and fully automated way. This was quite important because we had to avoid the slightest hint of suspicion that we took anything from the competing [Hitech](/HiTech "HiTech") effort, which was the officially funded chess project at [CMU](/Carnegie_Mellon_University "Carnegie Mellon University") at that time. Because of our automated tuning process, we had a demonstratably independent and effective way to incorporate chess [knowledge](/Knowledge "Knowledge") into DT.

## Running the Code

I just compiled the tuning code on an Compaq/Alpha [Unix](/Unix "Unix") workstation and it survived 12 years of bit-rot. So you may get it to run as well. Here are a few hints on how to play with it:

- The database is a binary file and the moves are stored in 2 byte fields. These may need to be swapped depending on the [byte-order](/Endianness "Endianness") of your computer. Either enable or disable the "SUN\_ENDIANESS" #define.
- When it runs, it needs a very wide terminal window to show the board and all Eval-parameters (142 columns).
- After starting the tuning program via 'texam dbf\_all' you should see a small chess board and the set of parameters, their weights and contributions to the current position. At this point there are several single character commands available:

|  |  |  |
| --- | --- | --- |
| WWW | ' ' | (space bar) steps through all legal moves |
| n | steps through the move played by the GM |
| N | goes to the beginning of the next game |
| g | goes to a specific game, the number of which is prompted |
| f | does a parameter fit |
| S/R | saves and restores a parameter set to/from a file (\*.par) |
| F | does a multi-iteration fit (a \*.stat file will be generated  along with parameter file after each iteration. The \*.stat file  summarizes the fit, shows tends and gives the error-distributions) |
| q | exits the program |

:   For the other commands (there are several more, you would need to look into the source code. In particular, there are ways to edit parameters manually and to control if they should participate in a tuning run or not)

- All of this assumes a [Unix](/Unix "Unix") system with the [curses library](https://en.wikipedia.org/wiki/Curses_%28programming_library%29).
- There are 5 parameter files included in this directory. Q\*.par were certain starting points during development and the other ones appeared to be the most recent ones. I don't know which parameter set was used in what DT game: I have hundreds of them and no idea which one was used for what. The USO.par file is probably the set that was used by DT in the [1988 US open tournament](/ACM_1988 "ACM 1988").

I would like to thank [Feng H. Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu") and [Murray Campbell](/Murray_Campbell "Murray Campbell") for their permission to release this code. Also let me add a note of appreciation for the Computer Science Department at the [Carnegie Mellon University](/Carnegie_Mellon_University "Carnegie Mellon University"), its open and free-spirited environment made the Deep Thought project possible. If you would like to know more about the roots of [Chiptest](/ChipTest "ChipTest") and Deep Thought, look out for Feng Hsu's upcoming book on his [Deep Blue](/Deep_Blue "Deep Blue") experience [[4]](#cite_note-4) .

:   Share and enjoy,
:   -- A. Nowatzyk
:   January 2000

# Forum Posts

- [Deep Thought's tuning code and eval function!](https://www.stmintz.com/ccc/index.php?id=128297) by [Severi Salminen](/Severi_Salminen "Severi Salminen"), [CCC](/CCC "CCC"), September 05, 2000

# External Links

- [Deep Thought at Tim Mann's Chess Pages](http://www.tim-mann.org/deepthought.html)
- [Source code to tune Deep Thought's evaluation](http://www.tim-mann.org/DT_eval_tune.tar.gz) in tar.gz format.
- [Andreas Nowatzyk's explanations of the the source code](http://www.tim-mann.org/DT_eval_tune.txt), January 2000

# References

1. [↑](#cite_ref-1) [Source code to tune Deep Thought's evaluation](http://www.tim-mann.org/DT_eval_tune.tar.gz) in tar.gz format
2. [↑](#cite_ref-2) [Andreas Nowatzyk's explanations of the the source code](http://www.tim-mann.org/DT_eval_tune.txt), January 2000
3. [↑](#cite_ref-3) [Deep Thought at Tim Mann's Chess Pages](http://www.tim-mann.org/deepthought.html)
4. [↑](#cite_ref-4) [Feng-hsiung Hsu](/Feng-hsiung_Hsu "Feng-hsiung Hsu") (**2002**). *[Behind Deep Blue: Building the Computer that Defeated the World Chess Champion](http://press.princeton.edu/titles/7342.html)*. [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)

**[Up one Level](/Automated_Tuning "Automated Tuning")**