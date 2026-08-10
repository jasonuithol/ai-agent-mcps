# NNUE

Source: https://www.chessprogramming.org/NNUE

**[Home](/Main_Page "Main Page") \* [Learning](/Learning "Learning") \* [Neural Networks](/Neural_Networks "Neural Networks") \* NNUE**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/SekienNue.jpg/250px-SekienNue.jpg)](/File:SekienNue.jpg)

[Toriyama Sekien](/Category:Toriyama_Sekien "Category:Toriyama Sekien") - Nue (鵺) [[1]](#cite_note-1) [[2]](#cite_note-2)

**NNUE**, (ƎUИИ Efficiently Updatable Neural Networks)  
a Neural Network architecture intended to replace the [evaluation](/Evaluation "Evaluation") of [Shogi](/Shogi "Shogi"), [chess](/Chess "Chess") and other board game playing [alpha-beta](/Alpha-Beta "Alpha-Beta") searchers running on a CPU. Inspired by [Kunihito Hoki's](/Kunihito_Hoki "Kunihito Hoki") approach of [piece-square tables](/Piece-Square_Tables "Piece-Square Tables") indexed by king location, and further two-piece locations and side to move as applied in his Shogi engine [Bonanza](/Bonanza "Bonanza") [[3]](#cite_note-3), **NNUE** was introduced in 2018 by [Yu Nasu](/Yu_Nasu "Yu Nasu") [[4]](#cite_note-4), and was used in Shogi adaptations of [Stockfish](/Stockfish "Stockfish") such as [YaneuraOu](/YaneuraOu "YaneuraOu") [[5]](#cite_note-5),
and [Kristallweizen](/Kristallweizen "Kristallweizen") [[6]](#cite_note-6), apparently with [AlphaZero](/AlphaZero "AlphaZero") strength [[7]](#cite_note-7).

# [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE")

As reported by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)") [[8]](#cite_note-8),
[Nodchip](/Hisayori_Noda "Hisayori Noda") incorporated NNUE into the chess playing [Stockfish](/Stockfish "Stockfish") 10 as a proof of concept.
[Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE") was born, and in summer 2020, the computer chess community burst out enthusiastically due to its rapidly rising [playing strength](/Playing_Strength "Playing Strength") with different networks trained using a mixture of [supervised](/Supervised_Learning "Supervised Learning") and [reinforcement learning](/Reinforcement_Learning "Reinforcement Learning") methods -
despite the approximately halved search speed, it became stronger than its original [[9]](#cite_note-9), finally responsible for the huge [strength](/Playing_Strength "Playing Strength") improvement of **Stockfish 12**.

# Adoption

*see [Category:NNUE](/Category:NNUE "Category:NNUE")*

Being tempted by the success of [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE") and attracted by how easy the method and small the code is, many engine developers have started testing and applying NNUE. For quick trials and evaluating before going into serious development, some of them borrowed and/or rewrote the NNUE code and used networks from Stockfish NNUE. Most of them reported positive results, such as [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)") with [Orion](/Orion "Orion") [[10]](#cite_note-10), [Ehsan Rashid](/index.php?title=Ehsan_Rashid&action=edit&redlink=1 "Ehsan Rashid (page does not exist)") with [DON](/DON "DON") [[11]](#cite_note-11), various [Stockfish derivatives](/Stockfish#Derivatives "Stockfish") by [Michael Byrne](/Michael_Byrne "Michael Byrne") [[12]](#cite_note-12), and [Volodymyr Shcherbyna](/Volodymyr_Shcherbyna "Volodymyr Shcherbyna") with [Igel](/Igel "Igel") [[13]](#cite_note-13) using the *Night Nurse* NNUE net by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe") [[14]](#cite_note-14). [Daniel Shawul](/Daniel_Shawul "Daniel Shawul") added NNUE support à la [CFish](/CFish "CFish") into his [egbbdll](/Scorpio#Bitbases "Scorpio") probing library of [Scorpio](/Scorpio "Scorpio") [[15]](#cite_note-15) [[16]](#cite_note-16), making it even easier to use NNUE. The promising engines [Halogen](/Halogen "Halogen") 7 and 8 by [Kieren Pearson](/Kieren_Pearson "Kieren Pearson"), and [Seer](/Seer "Seer") by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle") came with their own, distinct NNUE implementations, and on November 10, 2020, the commercial [Dragon by Komodo Chess](/Dragon_by_Komodo_Chess "Dragon by Komodo Chess") aka [Komodo](/Komodo "Komodo") NNUE appeared [[17]](#cite_note-17), trying to close the gap to Stockfish NNUE. The commercial [Fat Fritz 2.0](/Fat_Fritz#Fat_Fritz_2 "Fat Fritz"), based on a slightly modified Stockfish 12 using a customized, double-sized network, was released by [ChessBase](/ChessBase "ChessBase") in February 2021.

# Architecture

## Basic NNUE

The most basic form of an NNUE network consists of three layers: an input layer of length 768 (768 = 6 pieces x 2 colors x 64 squares), one hidden layer of arbitrary size, and an output layer consisting of one neuron, representing the evaluation of the position. A NNUE network also commonly consists of two perspectives. That is, two hidden layers representing both sides are concatenated into a single hidden layer of twice the length, before being forwarded to the output layer.

```
#define INPUT_SIZE 768
#define HL_SIZE ...

// These parameters are part of the training configuration
// These are the commonly used values as of 2024
#define SCALE 400
#define QA 255
#define QB 64

struct Network {
    int16_t accumulator_weights[INPUT_SIZE][HL_SIZE];
    int16_t accumulator_biases[HL_SIZE];
    int16_t output_weights[2 * HL_SIZE];
    int16_t output_bias;
};
```

### Input Layer

The input layer of a basic NNUE network contains 768 neurons of binary values, each representing one possible combination of piece, square, and color. Each neuron can be either on or off, depending on whether a piece with the corresponding combination exists on the board. The following is a common encoding scheme seen in most NNUE engines.

```
// Square: 0 - 63
// PieceType: Pawn = 0, Knight = 1, Bishop, Rook, Queen, King
// Side: White = 0, Black = 1

int calculateIndex(Square square, PieceType pieceType, Side side)
{
    return side * 64 * 6 + pieceType * 64 + square;
}
```

### Accumulator

The first hidden layer of a NNUE is also called the accumulator. The accumulator can be of arbitrary size, but integer multiples of powers of 2 are preferred as they allow the inference to be optimized more effectively. A large hidden layer trades speed for higher evaluation accuracy, and vice versa. Larger hidden layers are usually preferred as Elo gain from speedup tends to scale inversely with respect to time and computational power. Most top engines have accumulator sizes of more than 1024 neurons, with some even using accumulators as wide as 3072. A large accumulator is important as it is the only hidden layer that can be  **efficiently updated**.

```
struct Accumulator {
    int16_t values[HL_SIZE];
};
```

### Perspective

The vast majority of NNUE architectures require two accumulators to be maintained separately. Each represents the board from the "perspective", or point-of-view, from each side. The current board position is always from the white perspective. To calculate the input values from the perspective of black, the board is flipped vertically. This means that the piece's color is inverted, and its square is mirrored across the centre of the board (e.g., A1 becomes A8). Both perspectives use identical input weights and biases. During inference, the two accumulators are concatenated, with the accumulator representing the side to move being first. This resulting vector of double the accumulator width is the "true" hidden layer, and is the vector that gets forwarded to the output layer.

```
int calculateIndex(Side perspective, Square square, PieceType pieceType, Side side)
{
    if (perspective == BLACK)
    {
        side   = 1 - side;          // Flip side
        square = square ^ 0b111000; // Vertically flip the square
    }
    
    return side * 64 * 6 + pieceType * 64 + square;
}

struct AccumulatorPair {
    Accumulator white;
    Accumulator black;
};
```

### Efficient Updates

The format of the input layer allows the accumulators to be efficiently updated, meaning that the neural network does not need to be fully re-evaluated after making a move. Quiet moves and promotions can only change the values of two neurons in the input layers, while captures and castling can change the values of three and four input neurons, respectively. Therefore, instead of fully calculating the accumulator values, one can take the values of the accumulator from the previous ply, subtract the weight contributions from neurons that will be turned off, and add the weights from neurons that will be turned on. Due to the nonlinearity introduced by the activation function, these efficient updates can only be performed on the first hidden layer of the neural network.

The following is a basic implementation of efficient single add/sub:

```
void accumulatorAdd(const struct Network* const network, struct Accumulator* accumulator, size_t index)
{
    for (int i = 0; i < HL_SIZE; i ++)
        accumulator->values[i] += network->accumulator_weights[index][i];
}

void accumulatorSub(const struct Network* const network, struct Accumulator* accumulator, size_t index)
{
    for (int i = 0; i < HL_SIZE; i ++)
        accumulator->values[i] -= network->accumulator_weights[index][i];
}
```

### Output Layer

Most NNUE networks have exactly one output neuron, indicating the heuristic score of a position. The accumulator values are passed through an activation function, then forwarded to the output layer by taking the dot product with the output weights, and adding the output bias.

During training, the final evaluation is passed through a sigmoid activation to be trained on a target value. The target value is the result of a linear interpolation of the game result (0, 0.5, 1), and sigmoid(evaluation/eval\_scale).

However, during inference, the sigmoid function is unused, and the final evaluation is scaled by eval\_scale. This will produce a reasonable evaluation with a large range and sufficient precision.

| Activation Function | Notes |
| --- | --- |
| ReLU (Rectified Linear Unit): f(x) = max(x, 0) | Rarely used due to potential to overflow. |
| CReLU (Clipped ReLU): f(x) = clamp(x, 0, 1) | Used less commonly. Easy to implement and can be auto-vectorized. |
| SCReLU (Squared Clipped ReLU): f(x) = clamp(x, 0, 1)^2 | Most prevalent and produces the strongest network. Cannot be auto-vectorized, and requires hand-written SIMD code to optimize. |

```
int16_t CReLU(int16_t value, int16_t min, int16_t max)
{
    if (value <= min)
        return min;

    if (value >= max)
        return max;

    return value;
}

// Example: CReLU activation
int32_t activation(int16_t value)
{
    return CReLU(value, 0, QA);
}

// When forwarding the accumulator values, the network does not consider the color of the perspectives.
// Rather, we are more interested in whether the accumulator is from the perspective of the side-to-move.
int32_t forward(const struct Network*     const network,
                const struct Accumulator* const stm_accumulator,
                const struct Accumulator* const nstm_accumulator)
{
    int32_t eval = 0;

    // Dot product to the weights
    for (int i = 0; i < HL_SIZE; i++)
    {
        // BEWARE of integer overflows here.
        eval += activation( stm_accumulator->values[i]) * network->output_weights[i];
        eval += activation(nstm_accumulator->values[i]) * network->output_weights[i + HL_SIZE];
    }

    // Uncomment the following dequantization step when using SCReLU
    // eval /= QA;
    eval += network->output_bias;

    eval *= SCALE;
    eval /= QA * QB;

    return eval;
}
```

### Quantization

You may be wondering where the constants QA and QB came from, or why the final evaluation is divided by their product. This is because most NNUE networks are **quantized**. During training, the weights of the network are represented in floating points, since they offer a continuous range of values and reasonable accuracy. However, floating points are slow, and since floating point operations are not completely accurate, small errors could build up on each accumulator update, resulting in inaccurate evaluation. Therefore, trained floating-point weights are quantized before loading the network.

Quantization of a NNUE proceeds as follows: multiply weights and biases by some amount, then round the values into an integer. This will lose some precision, but not enough to significantly affect evaluation accuracy. Suppose we quantize the input-accumulator weights by QA, then one floating point at the accumulator will correspond to QA after quantization. Therefore, the accumulator biases are also scaled by QA, and the activation function no longer clips the value to 1, but to QA. Suppose we then quantize the accumulator-output weights by QB. Then, assuming CReLU activation, one floating-point value at the output node will correspond to QA \* QB after quantization. Thus, the output bias is scaled by QA \* QB. At the end of inference, we divide out the quantization, leaving us a very close approximation of the network evaluation.

SCReLU activation makes things messier. A floating point value of the accumulator values after SCReLU is actually QA \* QA, so the output bias is scaled by QA \* QA \* QB. However, this does not fit inside a 16-bit integer. To prevent this, some trainers will still scale the output bias by QA \* QB, so you would divide the dot product by QA preliminarily. This puts the output scaling back to QA \* QB, and the dequantization can continue as usual.

## Advanced NNUE Techniques

### Output Buckets

In a network with output buckets, the output weights and biases are split into several versions. The index of the active output weights is typically chosen by considering the number of non-king pieces left on the board. The following code illustrates one simple formula:

```
const int OUTPUT_BUCKETS = 8; // can be adjusted
const int DIVISOR = (32 + OUTPUT_BUCKETS - 1) / OUTPUT_BUCKETS;

int choose_output_buckets(uint64_t occupancy_bb)
{
    return (bit_count(occupancy_bb) - 2) / DIVISOR;
}
```

### Horizontal Mirroring

In a network with horizontal mirroring, the king will always be on the left side of the board. If the king goes over the middle line, then the entire board is flipped horizontally (from the accumulator's perspective), so that the king remains on one side of the board. This reduces the network's input space, which makes the training data between one and two times more effective, depending on the architecture. Note that the accumulator cannot be efficiently updated when the king crosses the vertical line of symmetry, as the index of every input neuron would be recalculated.

### King Input Buckets

An application of the mixture of experts technique. With king input buckets, several versions of accumulator weights are generated. The board is divided into regions, and the king's location in the region determines which set of accumulator weights are used. Like horizontal mirroring, a boundary-crossing king move is not efficiently updatable, and the accumulator must undergo a full refresh. However, the improvements in evaluation accuracy are often worth the slowdown.

### Feature Factorizer

A technique for training king-bucketed nets. During training, a "shadow" bucket called the factorizer is added to the network. The factorizer is always activated and contributes to the evaluation of every position. When the training run finishes, the factorizer weights are added back into each bucket. Factorizers allow faster learning for buckets, especially those with low training data coverage.

### Pairwise Multiplication

Before concatenating the accumulators, divide each accumulator into two parts of equal length. Multiply each element in the first part by a corresponding element in the second part, resulting in a vector half the size of the original accumulator. The hidden layer becomes the result of concatenating two such vectors. With pairwise multiplication, the hidden layer is reduced to the same width as each of the accumulators. At the same accumulator size, this speeds up inference but decreases evaluation accuracy. However, it allows even wider HL sizes as well as more complex architectures with multiple hidden layers.

### Multiple Layers

Some engines, such as Stockfish, [Ethereal](/Ethereal "Ethereal") and [Viridithas](/index.php?title=Viridithas&action=edit&redlink=1 "Viridithas (page does not exist)"), use networks that consist of multiple hidden layers. These networks are generally stronger than simple three-layer networks. However, the increased computational complexity may result in weaker results at short testing time controls (10s+0.1s).

Compared to simple networks, multi-layer NNUE enables greater architectural flexibility, as well as new opportunities for speed improvements.

### LayerStacks

Stockfish's *LayerStacks* is a concept where the network parameters after the first hidden layer is dynamically switched based on the material count of the evaluated position. It can be seen as a generalization of the traditional output buckets. Similar techniques are employed in most top engines that utilizes multi-layer networks.

## Performance Improvements

### Fused Updates

Instead of calling accumulatorAdd or accumulatorSub multiple times to update the counter, merge these updates into a single function such as accumulatorAddSub or accumulatorAddSubSub. This improves the performance of efficient updates, since it reduces loop overhead and allows register reuse.

### [Copy-Make](/Copy-Make "Copy-Make")

Store a ply-indexed array of accumulators and only perform the update once during make move. This approach is faster compared to make/unmake and allows optimizations such as [Lazy Updates](#Lazy_Updates).

### Lazy Updates

Delay accumulator updates until evaluation call. There are variants of lazy updates, but the following implementation is the simplest and most common. On make-move, instead of updating the accumulator, only mark it as dirty and save the features that were changed by the current move. Before the network is evaluated, travel back through the accumulator stack until reaching a clean accumulator. Do incremental updates from that clean accumulator back to the current accumulator, refreshing every accumulator in between. This is a speedup because evaluation is not necessary in certain nodes, as most engines cache static evaluation in Transposition Tables. Lazy updates are especially important in multi-threading because of the shared Transposition Table in [Lazy SMP](/Lazy_SMP "Lazy SMP").

### Accumulator Refresh Table

Introduced by Koivisto author Finn Eggers, and colloquially referred to as **Finny Tables**. When performing lazy updates on architectures with king bucketed inputs, it may not be possible to reach a clean accumulator via efficient updates. Since a full refresh is very expensive, one could save some computation by storing a king-bucket-indexed table of accumulators and their associated bitboards. Whenever one reaches a point without a clean accumulator, probe the cached accumulator and bitboards from the refresh table, and update from the cached accumulator by computing the difference between the cached bitboards and the current bitboards. Once an updated accumulator has been obtained, update the cache entry with the current accumulator and bitboards.

### SIMD

SIMD is an acronym for Single Instruction, Multiple Data. It allows the CPU to process multiple data simultaneously. Compilers can automatically generate SIMD instructions to improve the speed of NNUE inference. However, it is not perfect, and there are still opportunities to optimize NNUE inference with hand-written SIMD code.

#### Lizard SCReLU

This optimization is introduced by Liam McGuire in [Lizard](/index.php?title=Lizard&action=edit&redlink=1 "Lizard (page does not exist)") chess engine. It significantly speeds up inference on a simple NNUE architecture with SCReLU activation.

Consider the following loop to forward a SCReLU-activated hidden layer:

```
const int QA = 255;
const int QB = 64;

for (int i = 0; i < HL_SIZE; i++)
{
    const int us_clamped = clamp(stm_accumulator->values[i], 0, QA);
    const int them_clamped = clamp(mstm_accumulator->values[i], 0, QA);
    eval += us_clamped * us_clamped * network->output_weights[i];
    eval += them_clamped * them_clamped * network->output_weights[i + HL_SIZE];
}
```

How can one vectorize this loop? Since QA = 255, SCReLU(x) can be as large as 65025, which is outside of the range of 16-bit integers. One may consider using a lower quantization factor, but the loss of precision will be too much to account for the Elo loss. Fortunately, there is another way to approach this problem.

Say the value after clamping is v, and the output weight is w. Instead of calculating (v \* v) \* w, one can instead calculate in a different order: (v \* w) \* v. This way, as long as v \* w is in range, the code will not overflow. Therefore, during training, we can clip w to ensure it is always between [-1.98, 1.98]. And since we know that v has a maximum of QA, and that w is scaled by QB, the maximum of v \* w is QA \* QB \* 1.98, which is within the maximum representable value of 16-bit integers. To finish the last step, we can use the multiply-add-adjacent intrinsic such as vpmaddwd or \_mm256\_madd\_epi16 to multiply the elements pairwise (producing intermediary 32-bit results), then sum adjacent pairs in the result vector to yield a result vector of identical length. In code, this looks like the following

```
const int QA = 255;
const int QB = 64;

const __m256i vec_zero = _mm256_setzero_si256();
const __m256i vec_qa   = _mm256_set1_epi16(QA);
__m256i sum      = vec_zero;

for (int i = 0; i < ...; i ...)
{
    const __m256i us   = ...; // Load from accumulator
    const __m256i them = ...;
    const __m256i us_weights   = ...; // Load from net
    const __m256i them_weights = ...;

    const __m256i us_clamped   = _mm256_min_epi16( _mm256_max_epi16(   us, vec_zero ), vec_qa );
    const __m256i them_clamped = _mm256_min_epi16( _mm256_max_epi16( them, vec_zero ), vec_qa );

    const __m256i us_results   = _mm256_madd_epi16( _mm256_mullo_epi16(   us_weights,   us_clamped ),   us_clamped );
    const __m256i them_results = _mm256_madd_epi16( _mm256_mullo_epi16( them_weights, them_clamped ), them_clamped );

    sum = _mm256_add_epi32(sum,   us_results);
    sum = _mm256_add_epi32(sum, them_results);
}
```

# Notable Trainers

Several notable trainers have been developed since the introduction of NNUE. As of 2025, [Bullet](/index.php?title=Bullet&action=edit&redlink=1 "Bullet (page does not exist)") stands as the most widely adopted trainer among top chess engines.

- **[Bullet](/index.php?title=Bullet&action=edit&redlink=1 "Bullet (page does not exist)")** - A high-performance NNUE trainer written in Rust by [Jamie Whiting](/index.php?title=Jamie_Whiting&action=edit&redlink=1 "Jamie Whiting (page does not exist)").
- **[nnue-pytorch](/index.php?title=Nnue-pytorch&action=edit&redlink=1 "Nnue-pytorch (page does not exist)")** - A trainer based on PyTorch, originally written for [Stockfish](/Stockfish "Stockfish") and has since been adopted by [Torch](/Torch "Torch").
- **[marlinflow](/index.php?title=Marlinflow&action=edit&redlink=1 "Marlinflow (page does not exist)")** - The trainer developed by [Doruk Şekercioğlu](/index.php?title=Doruk_%C5%9Eekercio%C4%9Flu&action=edit&redlink=1 "Doruk Şekercioğlu (page does not exist)") for his engine [Black Marlin](/Black_Marlin "Black Marlin"). It has also been adopted by [Carp](/index.php?title=Carp&action=edit&redlink=1 "Carp (page does not exist)"), [Svart](/index.php?title=Svart&action=edit&redlink=1 "Svart (page does not exist)"), and was historically used by [Viridithas](/index.php?title=Viridithas&action=edit&redlink=1 "Viridithas (page does not exist)").
- **[Grapheus](/index.php?title=Grapheus&action=edit&redlink=1 "Grapheus (page does not exist)")** - A C++ NNUE trainer developed by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [Finn Eggers](/Finn_Eggers "Finn Eggers"), and [Rafid Ahsan](/index.php?title=Rafid_Ahsan&action=edit&redlink=1 "Rafid Ahsan (page does not exist)").
- **[CudAD](/index.php?title=CudAD&action=edit&redlink=1 "CudAD (page does not exist)")** - The original trainer for the [Koivisto](/Koivisto "Koivisto") chess engine, now superseded by Grapheus.
- **[NNTrainer](/index.php?title=NNTrainer&action=edit&redlink=1 "NNTrainer (page does not exist)")** - The official trainer for the [Ethereal](/Ethereal "Ethereal") chess engine.
- **[Starway](/index.php?title=Starway&action=edit&redlink=1 "Starway (page does not exist)")** - The official trainer for the [Starzix](/index.php?title=Starzix&action=edit&redlink=1 "Starzix (page does not exist)") chess engine.

# See also

- [Cerebrum](/index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)")
- [SANE](/David_E._Moriarty#SANE "David E. Moriarty")
- [Stockfish HalfKAv2](/Stockfish_NNUE#HalfKA "Stockfish NNUE")

# Publications

- [Yu Nasu](/Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf), [pdf](https://www.apply.computer-shogi.org/wcsc28/appeal/the_end_of_genesis_T.N.K.evolution_turbo_type_D/nnue.pdf) (Japanese with English abstract) [GitHub - asdfjkl/nnue translation](https://github.com/asdfjkl/nnue) [[18]](#cite_note-18)
- [Dominik Klein](/Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) [[19]](#cite_note-19)

# Forum Posts

## 2020

### January ...

- [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), January 07, 2020 » [Stockfish](/Stockfish "Stockfish"), [Shogi](/Shogi "Shogi")

:   [Re: The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754&start=18) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), January 18, 2020

- [Stockfish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74058) by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](/CCC "CCC"), May 31, 2020 » [Stockfish](/Stockfish "Stockfish")
- [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](/CCC "CCC"), May 31, 2020
- [NNUE shared library and tools](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74148) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), June 10, 2020

### July

- [Lizard-NNUE Experiment NOT bad with NNUE Net Evaluation...](http://talkchess.com/forum3/viewtopic.php?t=74480) by Nancy M Pichardo, [CCC](/CCC "CCC"), July 15, 2020
- [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](/CCC "CCC"), July 16, 2020
- [NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531) by [Martin Fierz](/Martin_Fierz "Martin Fierz"), [CCC](/CCC "CCC"), July 21, 2020

:   [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=1) by [Jonathan Rosenthal](/Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](/CCC "CCC"), July 23, 2020
:   [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=5) by [Jonathan Rosenthal](/Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](/CCC "CCC"), July 24, 2020
:   [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=8) by [Jonathan Rosenthal](/Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](/CCC "CCC"), August 03, 2020

- [BrainLearn NNUE 1.0](https://groups.google.com/d/msg/fishcooking/Wpk-9COzk64/ez643VTkAAAJ) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), July 25, 2020 » [BrainLearn](/index.php?title=BrainLearn&action=edit&redlink=1 "BrainLearn (page does not exist)")
- [ShashChess NNUE 1.0](https://groups.google.com/d/msg/fishcooking/yWtpz_FY5_Y/RMTG56fkAAAJ) by [Andrea Manzo](/Andrea_Manzo "Andrea Manzo"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), July 25, 2020 » [ShashChess](/ShashChess "ShashChess")
- [LC0 vs. NNUE - some tech details...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74607) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), July 29, 2020 » [Lc0](/Leela_Chess_Zero#Lc0 "Leela Chess Zero")
- [What does NNUE actually mean](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74611) by Paloma, [CCC](/CCC "CCC"), July 29, 2020

### August

- [What happens with my hyperthreading?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74705) by [Kai Laskos](/Kai_Laskos "Kai Laskos"), [CCC](/CCC "CCC"), August 06, 2020 » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE")
- [Re: Minic version 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73521&start=59) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), August 08, 2020 » [Minic](/Minic "Minic")
- [Neural Networks weights type](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74777) by [Fabio Gobbato](/Fabio_Gobbato "Fabio Gobbato"), [CCC](/CCC "CCC"), August 13, 2020 » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE")
- [Re: Introducing Igel chess engine - Igel and NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=17) by [Volodymyr Shcherbyna](/Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](/CCC "CCC"), August 19, 2020 » [Igel](/Igel "Igel")
- [Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), August 19, 2020 » [Orion](/Orion "Orion")
- [Night Nurse 0.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), August 19, 2020 » [A0lite](/A0lite "A0lite"), [Igel](/Igel "Igel")
- [NNUE](http://laatste.info/bb3/viewtopic.php?f=53&t=8298) by [Bert Tuyt](/index.php?title=Bert_Tuyt&action=edit&redlink=1 "Bert Tuyt (page does not exist)"), [World Draughts Forum](http://laatste.info/bb3/viewforum.php?f=53), August 19, 2020 » [Draughts](/Draughts "Draughts")

### September

- [Train a neural network evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74955) by [Fabio Gobbato](/Fabio_Gobbato "Fabio Gobbato"), [CCC](/CCC "CCC"), September 01, 2020 » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [RubiChess NNUE player implemented](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75016) by [Andreas Matthies](/Andreas_Matthies "Andreas Matthies"), [CCC](/CCC "CCC"), September 06, 2020 » [RubiChess](/RubiChess "RubiChess")
- [Toga III 0.4 NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75027) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), September 07, 2020 » [Toga](/Toga "Toga")
- [Neural network quantization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75042) by [Fabio Gobbato](/Fabio_Gobbato "Fabio Gobbato"), [CCC](/CCC "CCC"), September 08, 2020 » [Neural Networks](/Neural_Networks "Neural Networks")
- [AVX-512 and NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75049) by [Gian-Carlo Pascutto](/Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](/CCC "CCC"), September 08, 2020 » [AVX-512](/AVX-512 "AVX-512")
- [First success with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75190) by [Jonathan Kreuzer](/Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](/CCC "CCC"), September 23, 2020 » [Neural Networks](/Neural_Networks "Neural Networks")

:   [Re: First success with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75190&start=21) by [Jonathan Kreuzer](/Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](/CCC "CCC"), November 11, 2020 » [Checkers](/Checkers "Checkers")

- [Nemorino 6 (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75241) by [Florentino](/index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](/CCC "CCC"), September 28, 2020 » [Nemorino](/Nemorino "Nemorino")
- [A Crossroad in Computer Chess; Or Desperate Flailing for Relevance](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75247) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), September 29, 2020
- [NNUE variation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75248) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), September 29, 2020

### October

- [BONA\_PIECE\_ZERO](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75296) by [elcabesa](/Marco_Belli "Marco Belli"), [CCC](/CCC "CCC"), October 04, 2020
- [Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=91) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), October 09, 2020 » [Ethereal](/Ethereal "Ethereal")
- [Request for someone to train an NNUE for Ethereal](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75345) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), October 09, 2020
- [Ethereal Tuning - Data Dump](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75350) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), October 10, 2020
- [Dangerous turn](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75358) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), October 10, 2020
- [Black crushing white, weird ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75393) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), October 14, 2020 » [MinicNNUE](/Minic#MinicNNUE "Minic")
- [Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 15, 2020 » [CFish](/CFish "CFish")

:   [Re: Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400&start=22) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), October 15, 2020 » [Scorpio](/Scorpio "Scorpio")

- [How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 17, 2020

:   [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), October 17, 2020

- [Embedding Stockfish NNUE to ANY CHESS ENGINE: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75418) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 17, 2020 » [BBC](/BBC "BBC")
- [Seer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75433) by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg"), [CCC](/CCC "CCC"), October 18, 2020 » [Seer](/Seer "Seer")
- [BBC 1.3 + Stockfish NNUE released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75482) by [Maksim Korzh](/Maksim_Korzh "Maksim Korzh"), [CCC](/CCC "CCC"), October 21, 2020 » [BBC](/BBC "BBC")
- [Mayhem NNUE - New NN engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75500) by [JohnWoe](/Toni_Helminen "Toni Helminen"), [CCC](/CCC "CCC"), October 22, 2020 » [Mayhem](/Mayhem "Mayhem")
- [Centipawns vs Millipawns with NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75501) by Madeleine Birchfield, [CCC](/CCC "CCC"), October 23, 2020 » [Centipawns](/Centipawns "Centipawns"), [Millipawns](/Millipawns "Millipawns")
- [NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), October 23, 2020 » [Stockfish NNUE - NNUE Structure](/Stockfish_NNUE#NNUE_Structure "Stockfish NNUE")

:   [July 01, 2021 continuation](#KingPlacementsCont)

### November

- [Komodo 14.1 Release and Dragon Announcement](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75651) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), November 02, 2020 » [Komodo](/Komodo "Komodo")
- [NNUE outer product vs tensor product](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75653) by Madeleine Birchfield, [CCC](/CCC "CCC"), November 02, 2020 [[20]](#cite_note-20) [[21]](#cite_note-21)
- [Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724) by [Gary Linscott](/Gary_Linscott "Gary Linscott"), [CCC](/CCC "CCC"), November 08, 2020 [[22]](#cite_note-22)
- [TucaNNo: neural network research](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75725) by [Alcides Schulz](/Alcides_Schulz "Alcides Schulz"), [CCC](/CCC "CCC"), November 08, 2020
- [Dragon by Komodo Chess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75748) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), November 10, 2020 » [Dragon by Komodo Chess](/Dragon_by_Komodo_Chess "Dragon by Komodo Chess")
- [Tensorflow NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75751) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), November 10, 2020 [[23]](#cite_note-23)
- [Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890) by Madeleine Birchfield, [CCC](/CCC "CCC"), November 11, 2020

:   [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=6) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), November 12, 2020
:   [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=9) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), November 12, 2020 » [Dragon by Komodo Chess](/Dragon_by_Komodo_Chess "Dragon by Komodo Chess"), [Seer](/Seer "Seer"), [Halogen](/Halogen "Halogen")

- [Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=134) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), November 12, 2020
- [Maybe not the best diversity of strongest chess engines under development](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75797) by [Kai Laskos](/Kai_Laskos "Kai Laskos"), [CCC](/CCC "CCC"), November 14, 2020 » [Engine Similarity](/Engine_Similarity "Engine Similarity")
- [CPU Vector Unit, the new jam for NNs...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75862) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), November 18, 2020 » [SIMD](/SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [You've trained a brilliant NN(UE) King-Piece Network. Now what?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75870) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), November 19, 2020
- [Pawn King Neural Network](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75925) by [Tamás Kuzmics](/Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](/CCC "CCC"), November 26, 2020

### December

- [Orion 0.8 + The Cerebrum release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75953) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), December 01, 2020 » [Orion](/Orion "Orion"), [Cerebrum](/index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)")
- [The NNUE split programmers are in](https://prodeo.actieforum.com/t104-the-nnue-split-programmers-are-in) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [ProDeo Forum](/Computer_Chess_Forums "Computer Chess Forums"), December 02, 2020
- [Introducing the "Cerebrum" library (NNUE-like trainer and inference code)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76006) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), December 07, 2020
- [Dispelling the Myth of NNUE with LazySMP: An Analysis](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76190) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), December 30, 2020 » [Lazy SMP](/Lazy_SMP "Lazy SMP")

## 2021

### January

- [Translation of Yu Nasu's NNUE paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76250) by [Dominik Klein](/Dominik_Klein "Dominik Klein"), [CCC](/CCC "CCC"), January 07, 2021
- [Re: Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724&start=60) by [Gary Linscott](/Gary_Linscott "Gary Linscott"), [CCC](/CCC "CCC"), January 09, 2021
- [More experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76263) by [Jonathan Kreuzer](/Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](/CCC "CCC"), January 09, 2021 » [Slow Chess](/Slow_Chess "Slow Chess")
- [Shouldn't positional attributes drive SF's NNUE input features (rather than king position)?](https://groups.google.com/g/fishcooking/c/cad1MGSdpU4/m/Ury4iBqSBgAJ) by [Nick Pelling](/Nick_Pelling "Nick Pelling"), [FishCooking](/Computer_Chess_Forums "Computer Chess Forums"), January 10, 2021 » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE")
- [HalfKP Structure in NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76285) by Roger Stephenson, [CCC](/CCC "CCC"), January 12, 2021
- [Andscacs nnue 0.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76346) by [Daniel José Queraltó](/Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](/CCC "CCC"), January 17, 2021 » [Andscacs](/Andscacs "Andscacs")
- [It's NNUE era (sharing my thoughts)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76353) by Basti Dangca, [CCC](/CCC "CCC"), January 18, 2021
- [NNUE and game phase](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76356) by [Dann Corbit](/Dann_Corbit "Dann Corbit"), [CCC](/CCC "CCC"), January 18, 2021 » [Game Phases](/Game_Phases "Game Phases")
- [correspondence chess in the age of NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76382) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), January 21, 2021
- [One for Andrew Grant et al. - NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76386) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), January 21, 2021
- [256 in NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76437) by Ted Wong, [CCC](/CCC "CCC"), January 28, 2021
- [So what do we miss in the traditional evaluation?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76446) by [Ferdinand Mosca](/Ferdinand_Mosca "Ferdinand Mosca"), [CCC](/CCC "CCC"), January 29, 2021 » [Evaluation](/Evaluation "Evaluation")
- [Latest Night Nurse released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76447) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), January 29, 2021
- [None-GPL NNUE probing code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76456) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), January 31, 2021

### February

- [Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76537) by [Jouni Uski](/Jouni_Uski "Jouni Uski"), [CCC](/CCC "CCC"), February 09, 2021 » [Fat Fritz 2.0](/Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
- [How much work is it to train an NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76552) by [Gabor Szots](/Gabor_Szots "Gabor Szots"), [CCC](/CCC "CCC"), February 11, 2021
- [HCE and NNUE and vectorisation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76556) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), February 11, 2021 » [Minic](/Minic "Minic")
- [nnue reading code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76570) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), February 13, 2021
- [New net: The White Rose](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76648) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), February 20, 2021
- [Are neural nets (the weights file) copyrightable?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76664) by [Adam Treat](/Adam_Treat "Adam Treat"), [CCC](/CCC "CCC"), February 21, 2021
- [My first NNUE nn-f0c1c3cbf2f1.nnue](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76731) by [MikeB](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), February 27, 2021
- [How to make a double-sized net as good as SF NNUE in a few easy steps](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76742) by [Chris Whittington](/Chris_Whittington "Chris Whittington"), [CCC](/CCC "CCC"), February 28, 2021 » [Fat Fritz 2.0](/Fat_Fritz#Fat_Fritz_2 "Fat Fritz")

### March

- [A random walk down NNUE street …](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76790) by [MikeB](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), March 06, 2021
- [NNUE Research Project](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76833) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), March 10, 2021 » [Engine Similarity](/Engine_Similarity "Engine Similarity")
- [Simex including NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76840) by jjoshua2, [CCC](/CCC "CCC"), March 11, 2021 » [Engine Similarity](/Engine_Similarity "Engine Similarity")
- [NNUE ranking](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76844) by Jim Logan, [CCC](/CCC "CCC"), March 12, 2021 » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE")
- [FEN compression](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76892) by lucasart, [CCC](/CCC "CCC"), March 17, 2021 » [FEN Compression](/BMI2#FEN_Compression "BMI2"), [NNUE Training](#Training)
- [Mabigat - hyperparameter optimizer for NNUE net](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76917) by [Ferdinand Mosca](/Ferdinand_Mosca "Ferdinand Mosca"), [CCC](/CCC "CCC"), March 22, 2021 » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [nnue-trainer](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76964) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), March 27, 2021
- [Zeta with NNUE on GPU?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76986) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), March 31, 2021 » [Zeta](/Zeta "Zeta"), [GPU](/GPU "GPU")

### April

- [Rubichess NN questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77157) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), April 23, 2021 » [RubiChess](/RubiChess "RubiChess")
- [Crafty NNUE Chess Engine?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77200) by supersharp77, [CCC](/CCC "CCC"), April 29, 2021 » [Crafty](/Crafty "Crafty"), [Vafra](/index.php?title=Vafra&action=edit&redlink=1 "Vafra (page does not exist)") [[24]](#cite_note-24)

### May

- [Komodo Dragon 2 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77244) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), May 04, 2021 » [Komodo Dragon](/Dragon_by_Komodo_Chess "Dragon by Komodo Chess")
- [Stockfish with new NNUE architecture and bigger net released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77344) by [Stefan Pohl](/index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](/CCC "CCC"), May 19, 2021 » [Stockfish](/Stockfish "Stockfish"), [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE") [[25]](#cite_note-25)
- [NNUE scoring (egbb lib)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77348) by [Desperado](/Michael_Hoffmann "Michael Hoffmann"), [CCC](/CCC "CCC"), May 19, 2021 » [Scorpio NNUE](/Scorpio#ScorpioNNUE "Scorpio")

### June

- [Re: Booot progress](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77243&start=20) by [Alex Morozov](/Alex_Morozov "Alex Morozov"), [CCC](/CCC "CCC"), June 01, 2021 » [Booot](/Booot "Booot")
- [Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), June 04, 2021 » [Ethereal 13.00 (NNUE)](/Ethereal#Ethereal_13_.28NNUE.29 "Ethereal")

:   [Re: Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438&start=17) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), June 04, 2021 » [HalfKP](/Stockfish_NNUE#NNUE_Structure "Stockfish NNUE")

- [Dark Horse Update](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77467) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), June 11, 2021
- [Some more experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77492) by [Jonathan Kreuzer](/Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](/CCC "CCC"), June 15, 2021 » [Slow Chess](/Slow_Chess "Slow Chess")
- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), June 17, 2021 » [Stockfish](/Stockfish "Stockfish"), [Komodo Dragon](/Dragon_by_Komodo_Chess "Dragon by Komodo Chess"), [Ethereal](/Ethereal "Ethereal"), [Seer](/Seer "Seer")

:   [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=63) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), June 18, 2021 » [Scorpio](/Scorpio "Scorpio")
:   [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=68) by [Vivien Clauzon](/Vivien_Clauzon "Vivien Clauzon"), [CCC](/CCC "CCC"), June 18, 2021 » [Minic](/Minic "Minic")

- [I declare that HCE is dead...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77571) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), June 29, 2021 » [Ethereal](/Ethereal "Ethereal"), [HCE](/Evaluation "Evaluation")

### July

- [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=39) by [Tomasz Sobczyk](/Tomasz_Sobczyk "Tomasz Sobczyk"), [CCC](/CCC "CCC"), July 01, 2021 » [NNUE Question](#KingPlacements)

:   [Re: NNUE Question - King Placements](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=40) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), July 01, 2021 » [ScorpioNNUE](/Scorpio#ScorpioNNUE "Scorpio")

- [Before things become more messy than they already are](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77602) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), July 02, 2021
- [NNUE training set generation](http://talkchess.com/viewtopic.php?f=7&t=77606) by [Edsel Apostol](/Edsel_Apostol "Edsel Apostol"), [CCC](/CCC "CCC"), July 03, 2021
- [Time to rethink what Albert Silver has done?](http://talkchess.com/viewtopic.php?f=2&t=77612) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), July 03, 2021 » [Fat Fritz 2](/Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
- [Would the ICGA have accepted today's NNUE engines?](http://talkchess.com/viewtopic.php?f=2&t=77639) by Madeleine Birchfield, [CCC](/CCC "CCC"), July 05, 2021 » [ICGA](/ICGA "ICGA")
- [Koivisto 5.0](http://talkchess.com/viewtopic.php?f=2&t=77664) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), July 07, 2021 » [Koivisto](/Koivisto "Koivisto")
- [NNUE one year retrospective](http://talkchess.com/viewtopic.php?f=2&t=77681) by Madeleine Birchfield, [CCC](/CCC "CCC"), July 09, 2021

### August ...

- [Basic NNUE questions](http://talkchess.com/viewtopic.php?f=7&t=77869) by [Amanj Sherwany](/Amanj_Sherwany "Amanj Sherwany"), [CCC](/CCC "CCC"), August 04, 2021
- [Alternatives to King-Pawn, King-All NNUE encoding](http://talkchess.com/viewtopic.php?f=7&t=78109) by [Andrew Grant](/Andrew_Grant "Andrew Grant"), [CCC](/CCC "CCC"), September 05, 2021
- [NNUE - Efficiently Updatable Network - understanding](https://talkchess.com/viewtopic.php?f=7&t=78394) by [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](/CCC "CCC"), October 11, 2021
- [NNUE - only from own engine?](https://talkchess.com/viewtopic.php?f=2&t=78497) by [Rebel](/Ed_Schroder "Ed Schroder"), October 25, 2021
- [Regarding AVX2](https://talkchess.com/viewtopic.php?f=2&t=78588) by [Rebel](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), November 03, 2021 » [AVX2](/AVX2 "AVX2")
- [Mantissa 3.0.0](https://talkchess.com/viewtopic.php?f=2&t=78855) by [Jeremy Wright](/index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCC](/CCC "CCC"), December 10, 2021 » [Mantissa](/Mantissa "Mantissa")
- [Are NNUE Nets Specific to Chess Engines or They Universal to All Engines?](https://talkchess.com/viewtopic.php?f=2&t=78979) by daniel71, [CCC](/CCC "CCC"), December 26, 2021

## 2022 ...

- [Why NNUE trainer requires an online qsearch on each training position?](https://talkchess.com/viewtopic.php?f=7&t=79020) by [Chao Ma](/Chao_Ma "Chao Ma"), [CCC](/CCC "CCC"), January 01, 2022
- [Rebel 14](https://talkchess.com/viewtopic.php?f=2&t=79107) by [Ed Schröder](/Ed_Schroder "Ed Schroder"), [CCC](/CCC "CCC"), January 12, 2022 » [Rebel 14](/Rebel#14 "Rebel")
- [Binary Neural Networks Sliding Piece Inference [Release](https://talkchess.com/viewtopic.php?t=79332)] by [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](/CCC "CCC"), February 10 2022
- [Failure of trivial approach to neural network move ordering](https://talkchess.com/viewtopic.php?t=79368) by Jost Triller, [CCC](/CCC "CCC"), February 16 2022
- [Koivisto 8.0](https://www.talkchess.com/viewtopic.php?f=2&t=79523) by [Finn Eggers](/Finn_Eggers "Finn Eggers"), [CCC](/CCC "CCC"), March 15, 2022 » [Koivisto](/Koivisto "Koivisto")
- [NNUE + Pawn-King Network](https://www.talkchess.com/viewtopic.php?f=7&t=79742) by Alvin Peng, [CCC](/CCC "CCC"), April 22, 2022
- [building NN for different chess positions](https://talkchess.com/viewtopic.php?t=79900) by [Uri Blass](/Uri_Blass "Uri Blass") [CCC](/CCC "CCC") May 18 2022
- [NNOM++ - Move Ordering Neural Networks?](https://talkchess.com/viewtopic.php?t=80364) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), July 24 2022
- [Neural network evaluation for a Monte Carlo Tree Search engine](https://talkchess.com/viewtopic.php?t=80372) by Ellie Moore, [CCC](/CCC "CCC"), July 27 2022
- [Neural network architectures HalfKP vs HalfKA](https://talkchess.com/viewtopic.php?t=81017) by Fabio Gobbato, [CCC](/CCC "CCC"), November 16 2022
- [nnue-pytorch](https://talkchess.com/viewtopic.php?t=81189) by [jdart](/index.php?title=Jdart&action=edit&redlink=1 "Jdart (page does not exist)") [CCC](/CCC "CCC") December 24 2022
- [NNUE — Newbie Questions...](https://talkchess.com/viewtopic.php?t=81221) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), December 28 2022

## 2023 ...

- [Games for Training NNUE?](https://talkchess.com/viewtopic.php?t=81330) by [Steve Maughan](/Steve_Maughan "Steve Maughan"), [CCC](/CCC "CCC"), January 11 2023
- [Choice of loss function to train a neural network evaluation](https://talkchess.com/viewtopic.php?t=81516) by Fabio Gobbato, [CCC](/CCC "CCC"), February 12 2023
- [AI performs poorly despite decent depth.](https://talkchess.com/viewtopic.php?t=81850) by Jayden Joo, [CCC](/CCC "CCC"), April 10 2023
- [Sigmoid scale in neural network training question](https://talkchess.com/viewtopic.php?t=81913) by Alcides Schulz , [CCC](/CCC "CCC"), April 21 2023
- [NNUE Poll](https://talkchess.com/viewtopic.php?t=81937) by Thomas Jahn, [CCC](/CCC "CCC"), April 24 2023
- [Stockfish NNUE net question: Why 40k input nodes?](https://talkchess.com/viewtopic.php?t=82074) by Richard Hoffmann, [CCC](/CCC "CCC"), May 23 2023
- [Making NNUE 60% faster](https://talkchess.com/viewtopic.php?t=82142) by [Daniel Infuehr](/index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](/CCC "CCC"), June 06 2023
- [A series of introduction articles about the original/old Stockfish NNUE networks in 2020](https://talkchess.com/viewtopic.php?t=82368) by Chao M., [CCC](/CCC "CCC"), July 24 2023
- [Using Neural or Graphical Processor Units in NNUE engines](https://talkchess.com/viewtopic.php?t=82430) by Roger C., [CCC](/CCC "CCC"), August 03 2023
- [King buckets for NN evaluation](https://talkchess.com/viewtopic.php?t=82780) by Fabio Gobbato, [CCC](/CCC "CCC"), October 27 2023

## 2024 ...

- [How to get started with NNUE](https://talkchess.com/viewtopic.php?f=7&t=83170) by Arjun Basandrai, [CCC](/CCC "CCC"), January 12, 2024
- [nnue evaluation question](https://talkchess.com/viewtopic.php?t=83530) by [Uri Blass](/Uri_Blass "Uri Blass"), [CCC](/CCC "CCC"), March 25 2024
- [The dumbest neural network there is](https://talkchess.com/viewtopic.php?t=83704) by PK, [CCC](/CCC "CCC"), April 26 2024
- [AI to explain chess positions to amateurs](https://talkchess.com/viewtopic.php?t=83960) by Gary Gauthier, [CCC](/CCC "CCC"), July 02 2024
- [How to understand 'perspective' in NNUE nets?](https://talkchess.com/viewtopic.php?t=83988) by Dan Kelsey, [CCC](/CCC "CCC"), July 08 2024
- [How to get started with NNUE](https://talkchess.com/viewtopic.php?t=83170) by Arjun Basandrai, [CCC](/CCC "CCC"), January 12 2024
- [Cwtch - an experimental NNUE Javascript engine](https://talkchess.com/viewtopic.php?t=83958) by op12no2, [CCC](/CCC "CCC"), July 02 2024
- [NN Eval functions/Embedding Leela/NNUE prebuilt models into Engine](https://talkchess.com/viewtopic.php?t=84285) by Michael Lewis , [CCC](/CCC "CCC"), September 24 2024
- [bullet trainer problems](https://talkchess.com/viewtopic.php?t=84370) by [jdart](/index.php?title=Jdart&action=edit&redlink=1 "Jdart (page does not exist)"), [CCC](/CCC "CCC"), October 17 2024
- [Thoughts on "Zero" training of NNUEs](https://talkchess.com/viewtopic.php?t=84431) by John Hamlen, [CCC](/CCC "CCC"), November 01, 2024

## 2025 ...

- [Attempting to implement NNUE into my engine](https://talkchess.com/viewtopic.php?t=84777) by sovaz1997, [CCC](/CCC "CCC"), January 28, 2025
- [Generating original training data](https://talkchess.com/viewtopic.php?t=84811) by Stuart Marshall, [CCC](/CCC "CCC"), February 07 2025
- [Using Neural Network or Syzygy tables](https://talkchess.com/viewtopic.php?t=85120) by Dr. Oliver Brausch, [CCC](/CCC "CCC"), May 25 2025
- [Understanding neural networks in chess... from RL point.](https://talkchess.com/viewtopic.php?t=85350) by Alex S, [CCC](/CCC "CCC"), August 13 2025
- [To NNUE or not to NNUE, that is the question](https://talkchess.com/viewtopic.php?t=85351) by Robert Pope, [CCC](/CCC "CCC"), August 13, 2025
- [Alternative NNUE inputs](https://talkchess.com/viewtopic.php?t=85584) by Salomon Dölle, [CCC](/CCC "CCC"), October 22 2025

## 2026 ...

- [On the design of NNUE and possible ML approaches for evaluation](https://talkchess.com/viewtopic.php?t=85866) by Lazar Radu, [CCC](/CCC "CCC"), January 08 2026
- [NNUE loss function why MSE?](https://talkchess.com/viewtopic.php?t=85963) by Matthijs Tijin, [CCC](/CCC "CCC"), February 02 2026
- [How to teach neural network not to lose?](https://talkchess.com/viewtopic.php?t=86052) by Jaroslav Tavgen, [CCC](/CCC "CCC"), February 27 2026

# External Links

## NNUE

- [Efficiently updatable neural network | Wikipedia](https://en.wikipedia.org/wiki/Efficiently_updatable_neural_network)
- [次世代の将棋思考エンジン、NNUE関数を学ぼう（その１．ネットワーク構造編） - コンピュータ将棋 Qhapaq](http://qhapaq.hatenablog.com/entry/2018/06/02/221612), June 02, 2018 (Japanese)

:   Learn Next Generation Shogi Thinking Engine, NNUE Function (Part 1. Network Structure) - Computer Shogi

- [次世代の将棋思考エンジン、NNUE関数を学ぼう（その2．改造/学習編） - コンピュータ将棋 Qhapaq](http://qhapaq.hatenablog.com/entry/2018/07/08/193316), July 08, 2018 (Japanese)

:   Let's Learn Next Generation Shogi Thinking Engine, NNUE Function (Part 2. Remodeling/Learning) - Computer Shogi

- [Stockfish NNUE – The Complete Guide](http://yaneuraou.yaneu.com/2020/06/19/stockfish-nnue-the-complete-guide/), June 19, 2020 (Japanese and English)
- [3 technologies in shogi AI that could be used for chess AI](http://yaneuraou.yaneu.com/2020/08/21/3-technologies-in-shogi-ai-that-could-be-used-for-chess-ai/) by [Motohiro Isozaki](/Motohiro_Isozaki "Motohiro Isozaki"), August 21, 2020 » [Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE")
- [Stockfish NNUE Wiki](https://www.qhapaq.org/shogi/shogiwiki/stockfish-nnue/)
- [nnue | Home of the Dutch Rebel](http://rebel13.nl/home/nnue.html) by [Ed Schröder](/Ed_Schroder "Ed Schroder")
- [NNUE Guide (nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub)](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md) hosted by [Gary Linscott](/Gary_Linscott "Gary Linscott")
- [How to Build a Chess Engine and Fail](https://obrhubr.org/chess-engine) by Niklas Oberhuber

## NNUE libraries

Some developers disintegrate and rewrite the Stockfish NNUE code into independent libraries which can be much easier to embed into other chess engines.

- [GitHub - david-carteau/cerebrum: The Cerebrum library](https://github.com/david-carteau/cerebrum) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)") » [Cerebrum](/index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)")
- [GitHub - dshawul/nncpu-probe](https://github.com/dshawul/nncpu-probe) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul")
- [GitHub - jdart1/nnue: NNUE reading code for chess](https://github.com/jdart1/nnue) by [Jon Dart](/Jon_Dart "Jon Dart")

## Source Code

- [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
- [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen)
- [GitHub - nodchip/Stockfish: UCI chess engine](https://github.com/nodchip/Stockfish) ([Stockfish NNUE](/Stockfish_NNUE "Stockfish NNUE") by [Nodchip](/Hisayori_Noda "Hisayori Noda"))
- [A Leela NNUE? Night Nurse and Others · dkappe/leela-chess-weights Wiki · GitHub](https://github.com/dkappe/leela-chess-weights/wiki/A-Leela-NNUE%3F-Night-Nurse-and-Others) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe")
- [GitHub - DanielUranga/TensorFlowNNUE](https://github.com/DanielUranga/TensorFlowNNUE) by [Daniel Uranga](/Daniel_Uranga "Daniel Uranga")
- [GitHub - glinscott/nnue-pytorch: NNUE (Chess evaluation) trainer in Pytorch](https://github.com/glinscott/nnue-pytorch) by [Gary Linscott](/Gary_Linscott "Gary Linscott")
- [GitHub - connormcmonigle/seer-nnue: UCI chess engine using neural networks for position evaluation](https://github.com/connormcmonigle/seer-nnue) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle") » [Seer](/Seer "Seer")
- [GitHub - bmdanielsson/nnue-trainer: PyTorch trainer for NNUE style neural networks](https://github.com/bmdanielsson/nnue-trainer) by [Martin Danielsson](/Martin_Danielsson "Martin Danielsson") » [Marvin](/Marvin "Marvin") [[26]](#cite_note-26)
- [GitHub - fsmosca/Mabigat: NNUE parameter optimizer](https://github.com/fsmosca/Mabigat) by [Ferdinand Mosca](/Ferdinand_Mosca "Ferdinand Mosca") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - jw1912/bullet: Neural Network Trainer](https://github.com/jw1912/bullet) by [Jamie Whiting](/index.php?title=Jamie_Whiting&action=edit&redlink=1 "Jamie Whiting (page does not exist)") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - jnlt3/marlinflow: Neural Network training repository for the Black Marlin chess engine](https://github.com/jnlt3/marlinflow) by [Doruk Şekercioğlu](/index.php?title=Doruk_%C5%9Eekercio%C4%9Flu&action=edit&redlink=1 "Doruk Şekercioğlu (page does not exist)") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - Luecx/Grapheus](https://github.com/Luecx/Grapheus) by [Jay Honnold](/Jay_Honnold "Jay Honnold"), [Finn Eggers](/Finn_Eggers "Finn Eggers"), and [Rafid Ahsan](/index.php?title=Rafid_Ahsan&action=edit&redlink=1 "Rafid Ahsan (page does not exist)") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - Luecx/CudAD](https://github.com/Luecx/CudAD) by [Finn Eggers](/Finn_Eggers "Finn Eggers") and [Jay Honnold](/Jay_Honnold "Jay Honnold") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - AndyGrant/NNTrainer](https://github.com/AndyGrant/NNTrainer) by [Andrew Grant](/Andrew_Grant "Andrew Grant") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - martinnovaak/forge: Simple chess NNUE trainer](https://github.com/martinnovaak/forge) by [Martin Novák](/index.php?title=Martin_Nov%C3%A1k&action=edit&redlink=1 "Martin Novák (page does not exist)") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - zzzzz151/Starway](https://github.com/zzzzz151/Starway) by zzzzz151 » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - lucametehau/CudaTest](https://github.com/lucametehau/CudaTest) by [Luca Metehau](/Luca_Metehau "Luca Metehau") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - xu-shawn/Cortex: Java NNUE Trainer](https://github.com/xu-shawn/Cortex) by [Shawn Xu](/index.php?title=Shawn_Xu&action=edit&redlink=1 "Shawn Xu (page does not exist)") » [Automated Tuning](/Automated_Tuning "Automated Tuning")
- [GitHub - xu-shawn/nnue-visualizer](https://github.com/xu-shawn/nnue-visualize) by [Shawn Xu](/index.php?title=Shawn_Xu&action=edit&redlink=1 "Shawn Xu (page does not exist)")

## Misc

- [Lower Numerical Precision Deep Learning Inference and Training](https://software.intel.com/content/www/us/en/develop/articles/lower-numerical-precision-deep-learning-inference-and-training.html) by [Andres Rodriguez](https://community.intel.com/t5/user/viewprofilepage/user-id/134067) et al., [Intel](/Intel "Intel"), January 19, 2018 » [AVX-512](/AVX-512 "AVX-512")
- [Nue from Wikipedia](https://en.wikipedia.org/wiki/Nue)
- [Hiromi](/Category:Hiromi_Uehara "Category:Hiromi Uehara") - [Spectrum](https://en.wikipedia.org/wiki/Spectrum_(Hiromi_album)), 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

# References

1. [↑](#cite_ref-1) [Nue](https://en.wikipedia.org/wiki/Nue) (鵺) from the [Konjaku Gazu Zoku Hyakki](https://en.wikipedia.org/wiki/Konjaku_Gazu_Zoku_Hyakki) (今昔画図続百鬼) by [Toriyama Sekien](/Category:Toriyama_Sekien "Category:Toriyama Sekien"), circa 1779, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Re: What does NNUE actually mean](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74611&start=2) by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](/CCC "CCC"), July 29, 2020
3. [↑](#cite_ref-3) [機械学習エンジニアのための将棋AI開発入門その1 Introduction to Shogi AI development for machine learning engineers Part 1](http://yaneuraou.yaneu.com/2020/05/03/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E5%B0%86%E6%A3%8Bai%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80%E3%81%9D%E3%81%AE1/), May 03, 2020 (Japanese)
4. [↑](#cite_ref-4) [Yu Nasu](/Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf) (Japanese with English abstract)
5. [↑](#cite_ref-5) [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
6. [↑](#cite_ref-6) [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen/)
7. [↑](#cite_ref-7) [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), January 07, 2020
8. [↑](#cite_ref-8) [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](/CCC "CCC"), May 31, 2020
9. [↑](#cite_ref-9) [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](/index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](/CCC "CCC"), July 16, 2020
10. [↑](#cite_ref-10) [Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828) by [David Carteau](/index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](/CCC "CCC"), August 19, 2020
11. [↑](#cite_ref-11) [Re: New engine releases 2020...Don NNUE 2020?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=320#p856640) by supersharp77, [CCC](/CCC "CCC"), August 19, 2020
12. [↑](#cite_ref-12) [... the last shall be first ...](http://talkchess.com/forum3/viewtopic.php?f=2&t=74825) by [MikeB](/Michael_Byrne "Michael Byrne"), [CCC](/CCC "CCC"), 19 Aug 2020
13. [↑](#cite_ref-13) [Introducing Igel chess engine](http://talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=10#p856742) by [Volodymyr Shcherbyna](/Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](/CCC "CCC"), 20 Aug 2020
14. [↑](#cite_ref-14) [Night Nurse 0.2](http://talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](/Dietrich_Kappe "Dietrich Kappe"), [CCC](/CCC "CCC"), August 19, 2020
15. [↑](#cite_ref-15) [Re: Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400&start=22) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), October 15, 2020
16. [↑](#cite_ref-16) [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](/Daniel_Shawul "Daniel Shawul"), [CCC](/CCC "CCC"), October 17, 2020
17. [↑](#cite_ref-17) [Dragon by Komodo Chess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75748) by [Larry Kaufman](/Larry_Kaufman "Larry Kaufman"), [CCC](/CCC "CCC"), November 10, 2020
18. [↑](#cite_ref-18) [Translation of Yu Nasu's NNUE paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76250) by [Dominik Klein](/Dominik_Klein "Dominik Klein"), [CCC](/CCC "CCC"), January 07, 2021
19. [↑](#cite_ref-19) [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](/CCC "CCC"), September 29, 2021
20. [↑](#cite_ref-20) [Outer product from Wikipedia](https://en.wikipedia.org/wiki/Outer_product)
21. [↑](#cite_ref-21) [Tensor product from Wikipedia](https://en.wikipedia.org/wiki/Tensor_product)
22. [↑](#cite_ref-22) [PyTorch from Wikipedia](https://en.wikipedia.org/wiki/PyTorch)
23. [↑](#cite_ref-23) [TensorFlow from Wikipedia](https://en.wikipedia.org/wiki/TensorFlow)
24. [↑](#cite_ref-24) [Vafra](http://www.jurjevic.org.uk/chess/vafra/index.html) by [Robert Jurjević](/index.php?title=Robert_Jurjevi%C4%87&action=edit&redlink=1 "Robert Jurjević (page does not exist)")
25. [↑](#cite_ref-25) [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474) by [Tomasz Sobczyk](/Tomasz_Sobczyk "Tomasz Sobczyk")
26. [↑](#cite_ref-26) [nnue-trainer](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76964) by [Jon Dart](/Jon_Dart "Jon Dart"), [CCC](/CCC "CCC"), March 27, 2021

**[Up one Level](/Neural_Networks "Neural Networks")**