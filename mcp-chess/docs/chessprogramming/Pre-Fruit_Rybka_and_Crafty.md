# Pre-Fruit Rybka and Crafty

Source: https://www.chessprogramming.org/Pre-Fruit_Rybka_and_Crafty

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* Pre-Fruit Rybka and Crafty**

Written by [Bob Hyatt](/Robert_Hyatt "Robert Hyatt") with significant help from [Mark Watkins](/Mark_Watkins "Mark Watkins")

There was also an ongoing investigation regarding pre-Beta [Rybkas](/Rybka "Rybka"). There appears to be no direct [Fruit](/Fruit "Fruit") link here, but the evidence is still relevant as it shows a pattern of improper code re-use by the [Rybka author](/Vasik_Rajlich "Vasik Rajlich"). [Zach Wegner](/Zach_Wegner "Zach Wegner") had looked at the binary for a pre-fruit version of Rybka, the version that supposedly eventually led to Rybka 1 beta that we have been discussing. He found interesting pieces of code. It seemed relevant to look at this version since we have seen references to the "weaker" version of Rybka, with a sudden "leap to the top" soon after Fruit source became available. The obvious question to ask would be "was that version of Rybka original?" The answer is becoming more clear with investigation.

# Copied from Crafty

In particular, initially, Zach Wegner found two examples of copied code from [Crafty](/Crafty "Crafty"), one in some code to ensure *en passant* was not problematic with obsolete [Edwards tablebases](/Edwards%27_Tablebases "Edwards' Tablebases"), and one in checking if a mating score was equal to 99999, when such a score could not possibly be returned by the function-call in question.

A curious commonality of repeated zeroing of a structure-element when clearing pawn hash has also been uncovered, though some of the contextual parts differ. The first part of the Evaluation functions also yields evidence of code copied, with EvaluateWinner(), a function of about 100 lines of C code, being identical in Crafty and pre-Beta Rybka.

## Examples of Evidence

- [Rybka-Crafty Evidence](/Rybka-Crafty_Evidence "Rybka-Crafty Evidence") - re-use of code to tablebase use in KP vs KP when *en passant* was possible
- [Rybka-Crafty Evidence II](/Rybka-Crafty_Evidence_II "Rybka-Crafty Evidence II") - checking whether the return value of EvaluateMate() was 99999
- [Rybka-Crafty Evidence III](/Rybka-Crafty_Evidence_III "Rybka-Crafty Evidence III") - repeated zeroing of an element in a pawn hash structure
- [Rybka-Crafty Evidence IV](/Rybka-Crafty_Evidence_IV "Rybka-Crafty Evidence IV") - the first part of the Evaluation functions
- [Rybka-Crafty Evidence V](/Rybka-Crafty_Evidence_V "Rybka-Crafty Evidence V") - the EvaluateWinner() function
- [Rybka-Crafty Evidence VI](/Rybka-Crafty_Evidence_VI "Rybka-Crafty Evidence VI") - NextMove() and NextEvasions() functions

### Example 1

First, code from Crafty version 19.0, module "init.c":

```
  for (i = 0; i < pawn_hash_table_size; i++) {
    (pawn_hash_table + i)->key = 0;
    (pawn_hash_table + i)->p_score = 0;
    (pawn_hash_table + i)->protected = 0;
    (pawn_hash_table + i)->black_defects_k = 0;
    (pawn_hash_table + i)->black_defects_q = 0;
    (pawn_hash_table + i)->white_defects_k = 0;
    (pawn_hash_table + i)->white_defects_q = 0;
    (pawn_hash_table + i)->passed_w = 0;
    (pawn_hash_table + i)->passed_w = 0;
    (pawn_hash_table + i)->outside = 0;
    (pawn_hash_table + i)->candidates_w = 0;
    (pawn_hash_table + i)->candidates_b = 0;
}
```

Do you see the rather obvious bug?

Look here:

```
    (pawn_hash_table + i)->passed_w = 0;
    (pawn_hash_table + i)->passed_w = 0;
```

Obviously one of those should be \_b to clear the passed pawn flags for black. Notice that any variable that has a white or \_w in the name is matched with the same variable with black or \_b. A simple bug. What if you found this identical code in a different program? Say, for example, a pre-fruit version of Rybka? What would you conclude?

Zach will post a follow-up showing where/how he found this code in one of the pre-fruit versions of Rybka.

|  |
| --- |
| Edit: Mark Watkins notes that the structure in Rybka is not quite the same, so maybe the Crafty version is incorrect, or some of the PAWN\_HASH\_ENTRY fields were deleted. In any case, more analysis is needed to clarify exactly what is of interest here. Furthermore, it seems as though this pre-Beta Rybka only zeros some of the fields in the PAWN\_HASH\_ENTRY (4 bytes from 0x0, 4 bytes from 0x4, 2 bytes from 0x8, 1 byte from 0xf, 1 byte from 0xf [sic], 1 byte from 0xa, 1 byte from 0x11, 1 byte from 0x10), while the Crafty code always seem to ensure that all fields are zeroed. |

Further analysis shows that Rybka also clears these fields in three different places, just as Crafty does. Once on initial allocation, and in option.c if the pawn hash size is changed, and finally in utility.c in ClearHashTableScores(). The double zeroing of "passed\_w" was fixed in init.c in version 19.1 and in option.c in 19.16, but persisted in utility.c until this whole nomenclature was dumped in version 22.0. Of the three instances in the Rybka executable, two of them have this double zeroing of a specific byte.

See [Rybka-Crafty Evidence III](/Rybka-Crafty_Evidence_III "Rybka-Crafty Evidence III") for more details.

### Example 2

Here is another one from iterate.c:

```
  TB_use_ok = 1;
  if (TotalWhitePawns && TotalBlackPawns) {
    wpawn = FirstOne(WhitePawns);
    bpawn = FirstOne(BlackPawns);
    if (FileDistance(wpawn, bpawn) == 1) {
      if (((Rank(wpawn) == RANK2) && (Rank(bpawn) > RANK3)) ||
          ((Rank(bpawn) == RANK7) && (Rank(wpawn) < RANK6)) || EnPassant(1))
        TB_use_ok = 0;
    }
  }
```

Mark Watkins has made a disassembly of the Rybka 1.6 code (64 lines) [File:RYBKA16.EdwardsTBep.txt](/File:RYBKA16.EdwardsTBep.txt "File:RYBKA16.EdwardsTBep.txt")

That code was added to iterate.c when I first started to use the EGTB files from [Steven Edwards](/Steven_Edwards "Steven Edwards"). It was not needed after Eugene's files were released on my ftp machine, for several reasons. Eugene's were compressed and then decompressed on the fly as they were probed. Stevens were not. As a result, Eugene's files were \_\_far\_\_ smaller. Steven did not, at least while I was using them, release anything other than 3-4 piece files as they took forever to build (Eugene spent a ton of time optimizing his build speed). Steven did, for me, build krnkr and krbkr. But that was all.

Steven's kpkp file had one major short-coming, it did not consider en passant pawn captures. As a result, I had to add the above code to disable EGTB probes if an en passant capture could be a possibility anywhere in the tree. What the code does is to check to see if there are opposite-colored pawns on adjacent files, if one of the pawns is on its own second rank (so that it can move two squares at once), and the other pawn has not yet advanced past its 5th rank so that a double pawn push by the opponent might allow an en passant capture. If all of those were true, I had to disable egtb probes. Once Eugene's egtb files were released, which were first used in Crafty version 16.0, support for the Edwards tablebases was removed. But somehow this small vestige of the old support remained.

Mark Watkins pointed out a possible bug in the above that really isn't a bug. The wpawn/bpawn values could be wrong if one side had two pawns, because the FirstOne() call might not choose the correct pawn for the test. But in the Edwards tables, that was not possible. We only had kxkx (where x = pnbrq) or kxxk where one side could have two pawns but the other side has none. If you look at the above code, the first requirement was that both sides have pawns (TotalBlackPawns && TotalWhitePawns which are two counters that count the respective pawns. If either is zero, this code is skipped since no EP capture would be possible. When the Nalimov data was first made available, after I ran a million tests for Eugene to choose the optimal compression block size, we released the 3-4-5 piece files as a complete set. And the above test would not be appropriate both because he included EP captures in the generation process and because we then had kxpkp where x could also be a pawn, breaking that test in many cases. The conclusion? This code was specifically written to prevent errors when probing Steven's tables. It was inappropriate for Nalimov tables. Crafty v16 and beyond only included support for Nalimov files, and that code was inappropriate. Yes it represents a subtle bug in those versions of Crafty beyond Nalimov. But it was also copied into Rybka 1.6.1. There is no reasonable explanation for someone including this code when using Nalimov tables, other than that the code was copied from a programmer (me) that forgot to remove it from his program when he converted from Edwards to Nalimov. The only advantage is that it provides a clear "fingerprint" as to where the code came from, that it was not original at all.

Eventually, I discovered the oversight, removed the code, and in version 23.1 and later it was no longer present. How would a program that did not use the Edwards tablebases at all (since they were not available after Eugene's format came along as I was the primary source for distributing both sets and chose to just handle one) have such a piece of code? Eugene's tables \_\_always\_\_ supported EP.

See [Rybka-Crafty Evidence](/Rybka-Crafty_Evidence "Rybka-Crafty Evidence") for more details.

### Interlude

There is a lot of effort going into this investigation. The more we look, the more we find. Zach found the above code since we thought it would be useful to get a feel for the pre-fruit Rybkas structure since the claim has been that Rybka 1 beta took ideas but not code. The structure of Rybka changed \_\_dramatically\_\_ from the early version to the "fruity" version. I have been looking at older versions of Crafty to discover what bugs might have been present for a while, and which would \_\_not\_\_ have been a normal mistake if someone had written their own code (the passed\_w twice above is an example).

I have pointed out another place or two where there was \_\_very\_\_ unusual code in Crafty. We will post these examples whether or not they appear in pre-fruit Rybka, so that we can see either more evidence of copying, or evidence of original programming to go along with some of the copying.

For the record, the pawn hash entry above certainly suggests that in addition, EvaluatePawns(), EvaluateKingSafety() and EvaluatePassedPawns() were also copied since they depended on these values in the pawn hash table...

### Example 3

Zach has also noticed that this code, which appeared in versions 18.0 through 19.15, is bogus (this code is in evaluate.c, procedure Evaluate()):

```
  int ms=EvaluateMate(tree);
  if (ms == 99999) break;
```

EvaluateMate() can \_\_never\_\_ return a value of 99999. So the test is a waste of time. Yet it appears in Rybka 1.6.1. Zach pointed out that this was a giveaway in the El Chinito case which was also found to be a Crafty clone, with the \_same\_ bug included. This is another red flag as EvaluateMate() is only called from one place, in Evaluate(). And that test is only done one time in Crafty. And in Rybka 1.6.1... So another clear case of where code was copied (and not very smartly, either). This code was left over when EvaluateMate() had some tests in it that could say "do a normal evaluation, just chasing the weaker king to the side is not good enough). It would then return 99999 and that would avoid using the result score and instead do a full normal evaluation. At some point, when optimizing, things were changed so that EvaluateMate() was not called unless it was appropriate, rather than having EvaluateMate() itself determine whether the call was appropriate or not. But another vestige of old code was left in, and then copied, and there is no rational explanation for checking for that specific value since neither EvaluateMate() in Crafty, nor in Rybka 1.6.1 can return that value.

See [Rybka-Crafty Evidence II](/Rybka-Crafty_Evidence_II "Rybka-Crafty Evidence II") for more details.

### Example 4

In the [page](/Rybka-Crafty_Evidence_II "Rybka-Crafty Evidence II") Mark W. provided, he shows the EvaluateMate() == 99999 bug clearly. But he also shows a \_\_lot\_\_ more without realizing it.

|  |
| --- |
| Edit: Mark and Zach have now noted that the beginning of the Evaluate function in the pre-Rybka Beta copies from Crafty, including the "can\_win" issue below from EvaluateWinner() and EvaluateStalemate(), and also in comparing to 13 pieces left before applying these conditions. See [Rybka-Crafty Evidence IV](/Rybka-Crafty_Evidence_IV "Rybka-Crafty Evidence IV") for more details. |

In older versions of Crafty, I had a function EvaluateWinner() which was used to answer the questions (1) Can white win and (2) Can black win? I have a variable, "can\_win" that is initially set to 3 (1 = white can win, 2 = black can win, 3 = both can win, and 0 = dead draw). I use EvaluateWinner() to check for obvious draws and then set the corresponding bit to zero if that side has no winning chances at all. For example, KRN vs KR has white a knight up. In a drawn position. Suppose the preceding position was KRNP vs KRPP. You find a way to win both of blacks pawns and lose yours in the process. You are now one pawn better, but left with no chance to win. EvaluateWinner() sets the "can\_win" variable so that in the case of KRN vs KR, it will indicate that neither side can win, and the score is pulled drastically toward 0, making Crafty avoid "winning" that pawn, and turning a possible win into a draw.

This code is clearly present in Rybka 1.6.1 as well. Yet I have never heard of anyone publicly describing such an algorithm, and more specifically, implementing it exactly as I do inside Crafty with that two-bit flag "can\_win". This is yet another example of clear copying code and not ideas. And not of copying code that has a bug, but of copying code that is not going to be written in the same way by another programmer. I have changed the way this works more than once myself. At one point it forced the score to 0.00. But I would rather play a game with KRN vs KR where my opponent can screw up and lose, as opposed to just giving up the knight for nothing and still being in a drawn game but now with little hope of an opponent error. This is somewhat related to "swindle mode" in Crafty, an idea several copied, but which none have implemented the same way I did, for the ones I have looked at.

### Example 5

Mark has now examined the assembly language from Rybka's disassembly and compared it to the EvaluateWinner() function. And it has produced an almost perfect match, line by line. See [here](/Rybka-Crafty_Evidence_V "Rybka-Crafty Evidence V") for the full comparison. This represents a pretty significant block of code, and the probability of someone producing this independently is infinitesimal. The purpose of this code was to prevent Crafty from stepping into positions that looked good when you do a normal positional score + material, but which are actually not winnable. It evolved over several years of observations on ICC. I remember one example with Cray Blitz where it beat a master in 1981, the first time a computer had done this in OTB tournament play. We had a pawn left, and our opponent appeared to just throw away his h-pawn (we had a g pawn) in order to leave us with a h pawn + wrong colored bishop. CB recognized this in the eval, and we wanted to catch that case + others in Crafty as it is silly to take the pawn with our g-pawn, leaving us in a dead draw. If you look at the mid 19.x versions of Crafty, and then look inside evaluate.c, you will find this EvaluateWinner() function. And if you read the comments, you can see exactly what kinds of things once caused embarrassment and were fixed. :)

Some specifics. Case one, we are just a piece up. In the middlegame, this is likely a winning advantage, but when you drop into a reduced material ending, suddenly that extra piece is not enough. Classic example is KRN vs KR. Ditto for KQN vs KQ. The N is just not enough except for some rare positions. The idea is, then, if you are ahead a piece, don't trade pieces so that you get to the point where you are now in a draw. Also, if you have pawns, then we need to avoid dumping the pawns again converting to the draw. A piece advantage with no pawns is not good.

Being an exchange up is even worse. KR vs KB or KR vs KN is not winnable without pawns or some other advantage such as being a pawn down but you have an advanced passed pawn, etc. There are other "blended cases". If one side has a minor and no pawns, and the other side has one pawn, then neither side is going to win since the minor can exchange itself for the pawn. All of this qualified by total material so that KRN vs KP is clearly winnable since the knight can sac itself for the pawn and still leave you with enough material to win. If there are no pieces, you can't win with just a rook pawn, unless you have two of them, one on each side of the board.

Rook pawns are problematic in general. If your only pawn is a RP, you had better have a piece (and if the piece is a bishop it had better be the right color) if you are going to have any winning chances.

The final exceptions are pretty simple. KR vs K+minor+pawn can not be won by the rook. And could actually be lost with the potential promotion if the rook can't sac itself for the pawn.

Note that this function is not an absolute score. It just indicates whether one side (or the other) can win. This is used to modify the score, so that if one side has a scoring advantage according to normal evaluation code, but has no winning chances according to EvaluateWinner() then the score is pulled significantly toward a draw. Not to zero, because we still need to play reasonable chess. So, instead, we just reduce the overall score significantly. If a side has winning chances, and the score favors that side, it is unchanged. If a side has no winning chances, yet the score favors that side, the score is reduced. One should also look at how the score is modified. I divide by 4, which is a big reduction if you are at (say) +300 (KRN vs KR) but end up at +75 which looks like you dropped most of a piece by choosing to enter that particular ending. One could divide by any amount, or scale the score non-linearly, or assign a fixed static score. How likely is it that the same reduction is chosen by two different programmers?

What is the probability that someone would develop this code, doing \_exactly\_ the same tests, in exactly the same order, with exactly the same "holes" (one can look at later versions of this function to see how it has changed in subtle ways as either new examples of embarrassing behaviour or bugs were found and addressed)?? This was clearly a "cut and paste" operation, as were the preceding 4 examples.

### Example 6

The NextEvasion() function in pre-Beta Rybka is also the same as in Crafty, with the exception of ValidMove() being omitted. The NextMove() function again has many atypical points in common with Rybka 1.6.1. This structure came from Cray Blitz, although the implementation is different in Crafty, thanks to the differences between C and FORTRAN, and one **major** difference caused by the Crafty GenerateCheckEvasions() function. This is a legal-move generator that was added in early Crafty versions (it was phased in and improved over several months). When in check, Crafty switches to a legal-move generator, because most moves are illegal coming from the classic pseudo-legal move generators. NextEvasion() has a simpler job to do since there are no legality issues. As a result, it uses only a subset of the normal "phases" (the values given below). There are several unique (specific to crafty) ideas in this code that influence how it works. For example, I pass a pointer to a split block around so that every function will access the proper split block for the thread of execution that is doing the accessing. For the Next\* functions, this is very important, because for normal calls to them, from a single thread, we pass the current split block address. But in a parallel search, at a split point, we pass a pointer to the parent split block since the move list has to be shared with other threads splitting at the common split point. The overall structure is therefore quite unique and the SMP/non-SMP code is heavily intertwined.

The Rybka 1.6.1 implementation of these functions do not check the legality of the hash move. This is something that has always been in Crafty, since it is cheap and it helps catch bugs. For example, it made it crystal clear that SMP caused lots of invalid hash moves to be reported, which led to the lockless hash implementation to avoid the out-of-order-write problems that caused the errors. Actually going through a Make()/Unmake() on an illegal move can corrupt the board, so for safety the check has remained. It never reports an invalid move during our testing, unless we manage to break something. In Rybka, it was simply removed as unnecessary. Everything else in the hash move usage is identical.

In the second block of code addressed by Mark, the "sort\_all\_moves" case, again the code is identical. To find the highest score, I start with an initial pessimistic value of -999999. The Rybka 1.6.1 sort also includes this specific value, in addition to matching up exactly with the sort used in Crafty, which is not a particularly efficient one, but we often have no sorting to do and it shines when there are 0, 1 or few things to sort. The probability of two programmers using the same sort implementation, with the same early exit, with the same calculations to order moves is unusual. (Particularly when everyone today, Crafty included, uses SEE to weed out bad captures, but then sorts them on MVV/LVA scores.) Using the old Crafty trick of calling Swap() when value(attacker) < value(captured) and using value(captured) - value(attacker) when the attacker is not more valuable than the captured piece is unusual. And it is present in both programs.

In the discussion about the history\_moves\_2 phase in crafty, here is why I did that. In Crafty's move ordering, I do the following, in ordering moves.

(1) try the hash move, if present, before generating any moves at all.

(2) generate captures and pick the moves with SEE() >= 0 and sort on those values (in version 19.10, not today). As I do this, it is possible that the hash move was one of those captures. I zero that capture when I discover that capture(i) == hash\_move(ply) because it has already been tried.

(3) next, I try the killer moves (2 at each ply) before I generate any non-capture moves. And since killers are always non-captures, if I get no cutoff, I want to avoid searching them a second time, along with the hash move which also might not be a capture.

(4) next, I generate non-captures, which leaves the bad captures and possibly a killer or hash move on the move list as well.

(5) the next step is to look thru the list and select the entry with the highest history score to try next (Crafty tries 4 of these moves, total, before giving up. "4" is an ad hoc number with no basis behind it other than testing.) During this first pass, which is history\_moves\_1, as I check each move to extract it's history score, I also compare each move to the hash move and the two killer moves. If I find a match, the entry in the move list is zeroed since that move has already been searched once. After a single pass thru the move list for this phase, I have selected the move with the largest history counter, and zeroed any move that matched either the hash move or one of the two killers.

(6) the next step is the previously mentioned history\_moves\_2. Which is exactly the same as history\_moves\_1, except that I now do not need to compare each move to the history or hash moves, as those have already been removed. This is simply a performance optimization that eliminates 3 compares and 3 branches.

Rybka uses this exact structure for it's NextMove() function, something I have not seen in other open-source programs and which is probably unique to Crafty and anyone that has copied this code verbatim. The primary point here is that history\_moves\_2 checks for 3 history moves and then gives up and drops into the remaining\_moves phase. 3 + the original single history move where the hash/killer moves were removed gives a total of 4. 4 is a completely ad-hoc number, but it worked well in those versions of Crafty.

[Rybka-Crafty Evidence VI](/Rybka-Crafty_Evidence_VI "Rybka-Crafty Evidence VI")

## Other Examples

There are a couple of other examples where Crafty version 19.x code was copied directly into Rybka 1.6.1. The first is given below. The following strings appear in the Rybka 1.6.1 (you can use the Unix "strings Rybka-1.6.1.exe" command to get to these. They show some output formats, and some positions. If you look in bench.c in Crafty 19.0, you will find these 6 positions, exactly. The first 3 lines are from print statements in bench.c.

Rybka 1.6.1:

```
Total elapsed time: %d
Raw nodes per second: %d
Total nodes: %llu
```

Crafty 19.0:

```
Print(4095,"Total nodes: " BMF "\n",
Print(4095,"Raw nodes per second: %d\n",
Print(4095,"Total elapsed time: %d\n",
```

Rybka 1.6.1:

```
r1bqk2r/pp2bppp/2p5/3pP3/P2Q1P2/2N1B3/1PP3PP/R4RK1
2r2rk1/1bqnbpp1/1p1ppn1p/pP6/N1P1P3/P2B1N1P/1B2QPP1/R2R2K1
r3r1k1/ppqb1ppp/8/4p1NQ/8/2P5/PP3PPP/R3R1K1
4b3/p3kp2/6p1/3pP2p/2pP1P2/4K1P1/P3N2P/8
rnbqkb1r/p3pppp/1p6/2ppP3/3N4/2P5/PPP1QPPP/R1B1KB1R
3r1k2/4npp1/1ppr3p/p6P/P2PPPP1/1NR5/5K2/2R5

For the last one above, from bench.c:
strcpy(args[0],"3r1k2/4npp1/1ppr3p/p6P/P2PPPP1/1NR5/5K2/2R5");
(the others are all there as well)
```

The following lines are identical with the "perf command output" which is in option.c:

Rybka 1.6.1:

```
generated/made/unmade %d moves per second
generated/made/unmade %d moves, time=%.2f seconds
generated %d moves per second
generated %d moves, time=%.2f seconds
```

Crafty 19.0:

```
printf("generated %d moves, time=%.2f seconds\n",
printf("generated %d moves per second\n",
printf("generated/made/unmade %d moves, time=%.2f seconds\n",
printf("generated/made/unmade %d moves per second\n",
```

Those are in option.c around line 2700...

This is also there, but it has been changed just a "tad". This is from option.c, "perft" command that walks a tree and produces the "perft value" everyone quotes when doing "perft experiments." This was an original Crafty idea, for reference:

Rybka 1.6.1:

```
usage: verify <depth>
```

Crafty 19.0:

```
printf("usage: perftest <depth>\n");
```

So here, apparently the "perft" command was changed to a "verify" command in Rybka. But output is the same, as expected. While one can argue "this is not code used in the actual engine while playing a game" and have a valid point, it does show that significant blocks of code were copied, proving that the pre- Rybka-1-beta versions were anything but original code.

## General comments

A word on plagiarism vs original but duplicated code. Some believe that two different people could implement a function independently, and produce the same lines of code. While the probability of this does go up as the function becomes simpler, it really is not a reasonable explanation of what has happened here. First, anyone can suspect (and most actually know) that a chess program is a large program by most measures. No, it is not the most complex program around. Linux dwarfs Crafty's source by 100x or more. Ditto for even Microsoft Word(tm). But 50,000 lines of code or more is still quite large and complex. And finding these subtle bugs in two different programs, written exactly the same way, can not be explained away by serendipity. This is plagiarism in its simplest form, where code was copied and the copier did not even bother to look carefully at what he was copying to understand what the code was doing. "It works, I'll take that..." These "bugs" were not intentional in Crafty. Only a couple of intentional bugs were done long ago to expose some that were copying my parallel search code and claiming to have written their own. I stopped doing this years ago once the problem of plagiarism was shown to be one that would not go away no matter what the negative outcome was. But a chess program is a big project, and the concept of "debugged chess program" is an oxymoron. Crafty does not crash. It has played 100's of millions of games thanks to cluster testing. But we clearly have not expunged every bug, because not every bug causes a crash.

I will continue to look for these "fingerprint" ideas in Crafty's code, so that we can confirm they exist in Rybka 1.6.1 as well. One might be a coincidence. But several big ones (so far)? Not a chance. And while we are not through, I find it compelling to find bad code that was copied, as opposed to finding good code one could claim to have developed independently. Finding the same code with same bug is really beyond serendipity, and that is the kind of evidence we are carefully looking for. It is really important to realize that the source code of a chess engine is "syntax". What it does and how it does it (transform input to output through search and evaluation) is "semantics" Mapping syntax to semantics is what the programmer does as he writes the source. And for a given function, there are an infinite number of ways to write the function (different syntax) and producing different semantics. Same output, but computed in a different way. Finding identical semantics in two programs is far beyond random chance and shows copying.

I hate spending time looking at a version from several years ago, but I would like to see this issue resolved by providing enough evidence that anyone can look at it and draw conclusions with no reasonable doubts remaining.

## License

It is not yet ascertained which Crafty version was used, but the version numbers indicate something in early 19.x series, possibly a patchwork job. The user agreement in \_\_main.c\_\_ for these versions of Crafty is quite clear.

```
*  Crafty, copyright 1996-1999 by Robert M. Hyatt, Ph.D., Associate Professor *
*  of Computer and Information Sciences, University of Alabama at Birmingham. *
*                                                                             *
*  All rights reserved.  No part of this program may be reproduced in any     *
*  form or by any means, for other than your personal use, without the        *
*  express written permission of the author.  This program may not be used in *
*  whole, nor in part, to enter any computer chess competition without        *
*  written permission from the author.  Such permission will include the      *
*  requirement that the program be entered under the name "Crafty" so that    *
*  the program's ancestry will be known.                                      *
*                                                                             *
*  Copies of the source must contain the original copyright notice intact.    *
*                                                                             *
*  Any changes made to this software must also be made public to comply with  *
*  the original intent of this software distribution project.  These          *
*  restrictions apply whether the distribution is being done for free or as   *
*  part or all of a commercial product.  The author retains sole ownership    *
*  and copyright on this program except for 'personal use' explained below.   *
*                                                                             *
*  personal use includes any use you make of the program yourself, either by  *
*  playing games with it yourself, or allowing others to play it on your      *
*  machine,  and requires that if others use the program, it must be clearly  *
*  identified as "Crafty" to anyone playing it (on a chess server as one      *
*  example).  Personal use does not allow anyone to enter this into a chess   *
*  tournament where other program authors are invited to participate.  IE you *
*  can do your own local tournament, with Crafty + other programs, since this *
*  is for your personal enjoyment.  But you may not enter Crafty into an      *
*  event where it will be in competition with other programs/programmers      *
*  without permission as stated previously.                                   *
```

# Tournaments

A version of Rybka containing these Crafty code segments competed in [AEGT 3](http://iggor.110mb.com/aegt.php) (this link seems ready to disappear -- many things on that page are broken), and the same is likely true for [Chess War V-VII](http://www.open-aurec.com/chesswar/Chesswar006/Chesswar006DSt.htm), [Le Système du Suisse 3](http://americanfoot.free.fr/echecs/suisse/sui/sui3top200.htm), and [CCT6](http://www.vrichey.de/cct6/index_table.htm).

# Source of Executables

[Olivier](/Olivier_Deville "Olivier Deville") writes in open-chess [[1]](#cite_note-1) :

|  |
| --- |
| I have provided the ICGA secretariat with the pre-Fruit versions of Rybka I have here. These versions were meant to remain private, but I feel I have been cheated, and truth must be known. I am not going to send them to anyone else, though. Olivier |

# References

1. [↑](#cite_ref-1) [Re: Programmers Open Letter to ICGA on Rybka/Fruit](http://www.open-chess.org/viewtopic.php?f=3&t=1175&start=160#p11099) by [Olivier Deville](/Olivier_Deville "Olivier Deville"), [OpenChess Forum](/Computer_Chess_Forums "Computer Chess Forums"), March 05, 2011

**[Up one level](/Rybka_Controversy "Rybka Controversy")**