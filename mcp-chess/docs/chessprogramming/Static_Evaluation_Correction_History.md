# Static Evaluation Correction History

Source: https://www.chessprogramming.org/Static_Evaluation_Correction_History

**Static Evaluation Correction History**,  
also known as **Correction History** or **CorrHist** for short. It records the difference between static evaluation and search score of a position to a table indexed by the corresponding board feature, then uses the difference to adjust future static evaluations in positions with the same feature. Correction history was first introduced in [Caissa](/index.php?title=Caissa&action=edit&redlink=1 "Caissa (page does not exist)") in Oct 2023 and quickly adopted by other engines. Correction history has been shown to exhibit non-linear  [scaling](/index.php?title=Scaling&action=edit&redlink=1 "Scaling (page does not exist)") behavior with respect to increasing time control, with larger gains in longer searches.

# Correction Conditions

An update to correction history happens when the following conditions are satisfied:

- Side-to-move is not in check
- Best move either does not exist or is quiet
- If score type is [Lower bound](/Lower_Bound "Lower Bound"), then score should not be below static evaluation
- If score type is [Upper bound](/Upper_Bound "Upper Bound"), then score should not be above static evaluation

# Implementations

## Correction History Updates

Correction History was initially implemented as a exponential moving average. A version as seen in Alexandria is shown below:

```
void updateCorrHistScore(const Position *pos, SearchData *sd, const int depth, const int diff) {
    int &entry = sd->corrHist[pos->side][pos->pawnKey % CORRHIST_SIZE];
    const int scaledDiff = diff * CORRHIST_GRAIN;
    const int newWeight = std::min(depth * depth + 2 * depth + 1, 128);
    assert(newWeight <= CORRHIST_WEIGHT_SCALE);

    entry = (entry * (CORRHIST_WEIGHT_SCALE - newWeight) + scaledDiff * newWeight) / CORRHIST_WEIGHT_SCALE;
    entry = std::clamp(entry, -CORRHIST_MAX, CORRHIST_MAX);
}
```

Later, as introduced by Stockfish, the [history gravity](/History_Heuristic#Update "History Heuristic") formula can also be used to scale correction history updates:

```
if (!ss->inCheck && (!bestMove || !pos.capture(bestMove))
    && !(bestValue >= beta && bestValue <= ss->staticEval)
    && !(!bestMove && bestValue >= ss->staticEval))
{
    auto bonus = std::clamp(int(bestValue - ss->staticEval) * depth / 8,
                            -CORRECTION_HISTORY_LIMIT / 4, CORRECTION_HISTORY_LIMIT / 4);
    thisThread->pawnCorrectionHistory[us][pawn_structure_index(pos)].apply_bonus(bonus);
}
```

## Applying Correction

In engines with exponential moving average, the correction value is applied by summing the unadjusted static evaluation and the correction history value normalized by correction grain.

```
int adjustEvalWithCorrHist(const Position *pos, const SearchData *sd, const int rawEval) {
    const int &entry = sd->corrHist[pos->side][pos->pawnKey % CORRHIST_SIZE];
    return std::clamp(rawEval + entry / CORRHIST_GRAIN, -MATE_FOUND + 1, MATE_FOUND - 1);
}
```

In engines with history gravity updates, the correction value is applied by summing the unadjusted static evaluation with a fraction of correction history value.

```
Value to_corrected_static_eval(Value v, const Worker& w, const Position& pos) {
    const auto cv =
      w.pawnCorrectionHistory[pos.side_to_move()][pawn_structure_index<Correction>(pos)];
    v += 66 * cv / 512;
    return std::clamp(v, VALUE_TB_LOSS_IN_MAX_PLY + 1, VALUE_TB_WIN_IN_MAX_PLY - 1);
}
```

# Types

Many types of correction histories have been discovered since its introduction. Although they have the same basic ideas, different pawn histories uses different feature hash as indices. In current day top engines, values from many different types of correction histories are combined in order to produce a more accurate and useful correction value.

| Type | Indexing Scheme | Notes |
| --- | --- | --- |
| Pawn Correction History | Color and Hash representing the locations of all pawns. | Introduced by Witek902 in [Caissa](/index.php?title=Caissa&action=edit&redlink=1 "Caissa (page does not exist)"). |
| Material Correction History | Color and Hash representing the material configuration of the position. | Introduced by Witek902 in [Caissa](/index.php?title=Caissa&action=edit&redlink=1 "Caissa (page does not exist)"). |
| Threats Correction History | Color and Hash of the bitboard of all capturable pieces. | Introduced by Martin Novák in [Motor](/index.php?title=Motor&action=edit&redlink=1 "Motor (page does not exist)") |
| Minor Piece Correction History | Color and Hash representing the location of King, Knights, and Bishops. | Introduced by mcthouacbb in [Sirius](/index.php?title=Sirius&action=edit&redlink=1 "Sirius (page does not exist)"). |
| Major Piece Correction History | Color and Hash representing the location of King, Rooks, and Queens. | Introduced by mcthouacbb in [Sirius](/index.php?title=Sirius&action=edit&redlink=1 "Sirius (page does not exist)"). |
| Non-Pawn Correction History | Color and Hash representing the location of all pieces belonging to one color, excluding Pawns. | Introduced by zzzzz151 in [Starzix](/index.php?title=Starzix&action=edit&redlink=1 "Starzix (page does not exist)"). Non-pawn correction histories usually comes in pairs, each representing one side of the board. |
| Last Move Correction History | Move on the previous ply, ply (optional), or threats (optional) | Introduced by MinusKelvin in [ice4](/index.php?title=Ice4&action=edit&redlink=1 "Ice4 (page does not exist)"). Tweaked further by zzzzz151 in [Starzix](/index.php?title=Starzix&action=edit&redlink=1 "Starzix (page does not exist)") and Ömer Faruk Tutkun in [Devre](/index.php?title=Devre&action=edit&redlink=1 "Devre (page does not exist)"). |
| Continuation Correction History | Move on the previous ply and the ply before it. | Introduced by Martin Novák in [Motor](/index.php?title=Motor&action=edit&redlink=1 "Motor (page does not exist)"). |

# Additional Uses

Apart from the most common use of adjusting the static evaluation, correction history values can also be treated as a proxy to the complexity of a position. Correction values can be used to tweak many search heuristics, such as [LMR](/Late_Move_Reductions "Late Move Reductions"), [RFP](/Reverse_Futility_Pruning "Reverse Futility Pruning"), and many more.

# External Links

- [Dynamic material score correction · Witek902/Caissa@6dd0552 · GitHub](https://github.com/Witek902/Caissa/commit/6dd05529dea17e7a675dc593e4e0ab99965a306e)
- [Correction history indexed by minor pieces and kings by mcthouacbb · Pull Request #176 · mcthouacbb/Sirius · GitHub](https://github.com/mcthouacbb/Sirius/pull/176)
- [Correction history indexed by major pieces and king by mcthouacbb · Pull Request #178 · mcthouacbb/Sirius · GitHub](https://github.com/mcthouacbb/Sirius/pull/178)
- [Pieces correction history by zzzzz151 · Pull Request #98 · zzzzz151/Starzix · GitHub](https://github.com/zzzzz151/Starzix/pull/98)
- [Don't average non pawns correction histories by zzzzz151 · Pull Request #104 · zzzzz151/Starzix · GitHub](https://github.com/zzzzz151/Starzix/pull/104)
- [Concorrde - Continuation correction history by martinnovaak · Pull Request #162 · martinnovaak/motor · GitHub](https://github.com/martinnovaak/motor/pull/162)
- [Introduce static evaluation correction history by Vizvezdenec · Pull Request #4950 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/4950)
- [Introduce Material Correction History by xu-shawn · Pull Request #5556 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/5556)
- [Introduce Various Correction Histories by xu-shawn · Pull Request #5598 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/5598)
- [Continuation Correction History by OmerFarukTutkun · Pull Request #5617 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/5617)