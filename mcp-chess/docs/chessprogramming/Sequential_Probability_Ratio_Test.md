# Sequential Probability Ratio Test

Source: https://www.chessprogramming.org/Sequential_Probability_Ratio_Test

**[Home](/Main_Page "Main Page") \* [Engine Testing](/Engine_Testing "Engine Testing") \* Sequential Probability Ratio Test**

**Sequential Probability Ratio Test**, or **SPRT**, is a sequential hypothesis testing method. Generally regarded as the most important process in modern engine development, it is used by virtually all top engines today, including [Stockfish](/Stockfish "Stockfish").

# Advantages

Compared to fixed games:

- SPRT guarantees that the end result is statistically significant, and therefore can be trusted
- SPRT does not require prior knowledge of how large the sample size should be

Compared to test positions:

- SPRT simulates real game play
- SPRT allows for statistical certainty that a patch gains strength
- SPRT provides a large sample size and low uncertainty
- SPRT allows time management testing
- SPRT is proven to work

# Disadvantages

- No local GUI support (Refer to [OpenBench](/OpenBench "OpenBench") for self-hosted web application)

# Testing Methodology

Generally, SPRT is performed on every proposed functional change. Some non-functional speedup changes can also be performed using SPRT, although a speedup script may take less resources than a SPRT test.

In order to perform an SPRT test, four parameters are generally provided:

- **Elo\_0** - This represents our null hypothesis that the elo difference is exactly **Elo\_0**.
- **Elo\_1** - This represents our alternative hypothesis that the elo difference is exactly **Elo\_1**.
- **alpha** - This represents our tolerated type I (false positive) error rate.
- **beta** - This represents our tolerated type II (false negative) error rate.

First, two **LLR (Log Likelihood Ratio)** bounds are calculated from alpha and beta. The log likelihood ratio is the logarithmic value of (likelihood that Elo = Elo\_1) / (likelihood that Elo = Elo\_0). When the log likelihood ratio is positive, then the likelihood that Elo=Elo\_1 is higher than that of Elo=Elo\_0, and vice versa. As more games are played, the LLR is updated continuously. The SPRT test will keep going until the LLR value reaches either bound. At which point, the test can guarantee, within the specified degree of confidence, whether or not a feature is more likely to change the strength of the by engine Elo\_1 Elo than it is to change the strength of the engine by Elo\_0 Elo. The choice of Elo\_0 and Elo\_1 is important as it both influences the number of tests to be run on, and the Elo gain needed for a patch to pass a SPRT test.

Note that the idea of using SPRTs to test changes is to be able stop the test when a statistically significant result is obtained, so when applicable some very large number of games (say, 999999) should be specified to avoid the test stopping prematurely.

There are many tools one can use to perform SPRT tests, the most popular ones are [OpenBench](/OpenBench "OpenBench"), [cutechess-cli](/Cutechess-cli "Cutechess-cli"), and [fast-chess](/Fast-chess "Fast-chess").

# Performing an SPRT Test

The following sections describe the procedure for local SPRT testing. For distributed SPRT testing, refer to [OpenBench](/OpenBench "OpenBench").

## Preparing an SPRT Test

In order to perform an SPRT test on the command line, there some programs and resources you would need.

- A [Tournament Manager](/Tournament_Manager "Tournament Manager") that supports SPRT testing. [fast-chess](/Fast-chess "Fast-chess") is recommended as it supports pentanomial statistics, which can make tests finish faster.
- An opening book (.pgn or .epd, **not** .bin). Some opening books can be found in the [Stockfish opening books repository](https://github.com/official-stockfish/books). Balanced books such as [8moves\_v3.pgn](https://github.com/official-stockfish/books/blob/master/8moves_v3.pgn.zip) are recommended for weaker engines, while more biased books such as [UHO\_Lichess\_4852\_v1.epd](https://github.com/official-stockfish/books/blob/master/UHO_Lichess_4852_v1.epd.zip) and [Pohl.epd](https://github.com/AndyGrant/openbench-books/blob/master/Pohl.epd.zip) are recommended with stronger engines to reduce draw rate.

## Performing an SPRT Test With Gainer Bounds

Say you want to introduce [LMR](/Late_Move_Reductions "Late Move Reductions") to your [UCI](/UCI "UCI") engine. Build a binary of your engine with LMR added, and a binary of your base engine (without LMR). We'll call the two binaries engine\_LMR and engine\_BASE respectively.

In your shell, run the following command

```
.\fast-chess -engine cmd=[Path to engine_LMR] name=engine_LMR -engine cmd=[Path to engine_BASE] name=engine_BASE -each tc=8+0.08 -rounds 15000 -repeat -concurrency [Number of Available Threads] -recover -randomseed -openings file=[Path to Opening Book] format=[Opening book format (pgn or epd)] -sprt elo0=0 elo1=5 alpha=0.05 beta=0.05
```

Here, elo0 and elo1 represent the test bounds, while alpha and beta represent the expected alpha and beta errors of the test. The test verifies if the elo difference with the proposed changes is closer to 0 elo or 5 elo. Therefore, if the test passes, we can be reasonably certain that it brings more than 0 elo.

## Performing an SPRT Test With Non-regression Bounds

Say you want to remove [Countermove Heuristic](/Countermove_Heuristic "Countermove Heuristic") from your [UCI](/UCI "UCI") engine, as it takes a large amount of code and does not necessarily gain elo. To verify that the removal doesn't lose elo below an accepted amount, a non-regression test is performed. Build a binary of your engine with Countermove Heuristic removed, and a binary of your base engine (without removal of Countermove Heuristic). We'll call the two binaries engine\_NOCM and engine\_BASE respectively.

```
.\fast-chess -engine cmd=[Path to engine_NOCM] name=engine_NOCM -engine cmd=[Path to engine_BASE] name=engine_BASE -each tc=8+0.08 -rounds 15000 -repeat -concurrency [Number of Available Threads] -recover -randomseed -openings file=[Path to Opening Book] format=[Opening book format (pgn or epd)] -sprt elo0=-5 elo1=0 alpha=0.05 beta=0.05
```

Here, the bounds [-5, 0] are a flipped version of the gainer bounds. This is equivalent to testing engine\_BASE against engine\_NOCM (notice the reverse order) with [0, 5] bounds. If the test fails, it means that Counter Moves is still worth more than an acceptable amount of elo, therefore it should not be simplified.

## Common Bounds

A good choice of bounds balances the expected number of games and the lowest elo gain needed for passing. Due to a variety of factors, including elo compression, bounds are generally looser for weaker engines and tighter for stronger engines.

| Gainer Bounds | Non-regression Bounds | Usage |
| --- | --- | --- |
| [0.5, 2.5] | [-1.75, 0.25] | Stockfish LTC |
| [0, 2] | [-1.75, 0.25] | Stockfish STC |
| [0, 3] | [-3, 1] | Top 30 engines |
| [0, 5] | [-5, 0] | Top 200 engines |
| [0, 10] | [-10, 0] | All other engines |

# Minimum UCI Requirements

For SPRT testing platforms such as [cutechess-cli](/Cutechess-cli "Cutechess-cli"), [fast-chess](/Fast-chess "Fast-chess") and [OpenBench](/OpenBench "OpenBench"), the minimum UCI requirements are as follows.

Commands to support:

```
go wtime <> btime <> winc <> binc <>
position startpos [moves <moves...>]
position fen <fen> [moves <moves...>]
quit
uci
ucinewgame
isready
```

# External Links

[Chess SPRT Calculator](https://tests.stockfishchess.org/sprt_calc) » [Fishtest](/Stockfish#Fishtest "Stockfish")