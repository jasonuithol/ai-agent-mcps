# Michael Chaly

Source: https://www.chessprogramming.org/Michael_Chaly

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Michael Chaly**

[![](/images/thumb/0/05/MichaelChaly.webp/300px-MichaelChaly.webp.png)](/File:MichaelChaly.webp)

Michael Chaly

Michael Chaly, known online as Vizvezdenec, is a prominent contributor to the Stockfish development community. Born and currently residing in Sevastopol, he has made significant contributions to the Stockfish development community. Demonstrating exceptional mathematical skills, he secured third place in the Ukrainian School Math Olympics in 2004 and 2005. Graduating at the age of 15, he pursued higher education at Moscow Institute of Physics and Technology and St. Petersburg State University before completing his studies at Moscow State University in 2013, specializing in engineering mathematics and physics. His impactful contributions continue to shape the field of [Stockfish](/Stockfish "Stockfish") development.

# Chess

Michael Chaly’s journey into the intricacies of the game began with casual matches against a co-worker, whose level of expertise closely mirrored his own. This initial engagement sparked his curiosity about the competitive chess scene, prompting him to delve deeper into the world of professional chess. Inspired by a colleague’s admiration for Magnus Carlsen, Chaly’s interest was further kindled, leading him to explore the evolving landscape of the sport.

# Stockfish

As an avid follower of top-tier competitions spanning various disciplines, Chaly’s exploration eventually led him to the [Top Chess Engine Championship](/TCEC "TCEC") (TCEC). During his observation of these matches, he was enthralled by the strategic brilliance exhibited by an engine named Stockfish. What caught his attention was not only Stockfish’s aggressive gameplay but also the fact that it operated on an open-source framework, allowing enthusiasts like Chaly to delve into its underlying mechanics.

Motivated by this newfound passion, Chaly embarked on a mission to contribute to the enhancement of Stockfish. With the valuable support from [Andrew Grant](/Andrew_Grant "Andrew Grant"), author of [Ethereal](/Ethereal "Ethereal"), he successfully established a robust system for crafting and implementing patches for Stockfish. This significant achievement took shape in late 2018, marking a milestone in Chaly’s journey as a chess enthusiast and contributor to the chess engine community.

Chaly’s impact in the realm of chess engines lies in his dedication to refining existing ideas within the domain of chess engine development. While he may not be the originator of groundbreaking concepts, his contributions have focused on the continuous improvement of chess engines. These enhancements span a range of aspects, from evaluating positions to optimizing search algorithms. Through his dedication and commitment, Chaly continues to play a vital role in the evolution of chess engines, shaping the future of this intellectually stimulating discipline.

# Stockfish development

Michael Chaly's main contributions to Stockfish:

- HCE
  - King Danger
    - Exclude pawn double protected squares from king ring
    - Bonus for rook x-ray attack on king ring during middle game
    - Rewriting safe checks evaluation so that positions where the same piece type are more valuable when it can check from multiple squares
    - King flank defense and attack concepts
  - Passed Pawns
    - Extra bonus for passed pawns that have a clear way to promote
    - Consider only the most advanced pawn in a file as a passed pawn
  - Space
    - Make space calculation dependent on how many squares are attacked in space area
  - Endgame
    - Consider endgames less winnable when king is opposing and pawns are only at the same flank
    - Consider endgames more winnable when king infiltrates opponent territory
    - Reduce middlegame score for positions which have extremely low endgame winnability
    - Make evaluation for opposite colored bishop endgames dependent on the number of passing pawns of the stronger side
- Search
  - Quiescence search
    - Quiet evasions movecount pruning
    - 3rd futility pruning
    - History-based Pruning
    - SEE pruning tweaks
  - Pruning
    - History Pruning
    - Reverse Futility Pruning Tweaks
      - Use history score to adjust RFP margin
      - Added a condition based on whether a TT entry exists
    - Reintroduction of razoring
    - Maximize usage of transposition table in Probcut
    - Probcut-inspired pruning idea using TT
    - Various additions to moves loop pruning
      - Futility pruning for captures
      - More aggressive history-based pruning
      - Use history in futility pruning and SEE pruning of quiet moves
  - Reductions / Extensions
    - IIR for expected cutnodes
    - Allow captures in Late Move Reductions
    - Adjusting full depth search after Late Move Reductions
    - Post-LMR deeper searches
    - Negative Extensions after singular search
    - Pre-qsearch PV extensions
  - Move Ordering
    - Post-LMR history adjustments
    - 3-ply Continuation History
    - 6-ply Continuation History
    - History for ordering quiet nodes at low plies
    - Use of static evaluation difference to improve move ordering of quiet moves (through history bonuses)
    - Bonus for moves that escape threats
  - Pioneer of hyperscaling tunings (ie tuning values at extremely long time controls, with results ranging from -10 elo at 10s + 0.1s increment to 10 elo at 180 + 1.8s increment)
  - Tweaks on existing heurstics that increased playing strength