# Rybka-Crafty Evidence IV

Source: https://www.chessprogramming.org/Rybka-Crafty_Evidence_IV

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* [Pre-Fruit Rybka and Crafty](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty") \* Rybka-Crafty Evidence IV**

**[< Prev](/Rybka-Crafty_Evidence_III "Rybka-Crafty Evidence III") [Next >](/Rybka-Crafty_Evidence_V "Rybka-Crafty Evidence V")**

by [Mark Watkins](/Mark_Watkins "Mark Watkins")

Copied code from the start of [Crafty's](/Crafty "Crafty") Evaluate in pre-Beta [Rybka](/Rybka "Rybka").

# Crafty Source

Here is the start of the Evaluate() code in Crafty 19.1, with some comments removed:

```
int Evaluate(TREE * RESTRICT tree, int ply, int wtm, int alpha, int beta) {
  register BITBOARD temp;
  register int square, file, score, tscore, w_tropism=0, b_tropism=0;
  register int w_spread, b_spread, trop, can_win=3;
// ... comments and #if stuff omitted
  if (TotalWhitePieces<13 && TotalBlackPieces<13) {
    can_win=EvaluateWinner(tree);
    if (EvaluateStalemate(tree,wtm)) can_win=0;
  }
  if (can_win == 0) return(DrawScore(wtm));
```

# Pre-Beta Rybka Assembly

Here is the comparative code for pre-Beta Rybka:

```
0x00402a00:     push   %ebp                   # start of pre-Beta Rybka Evaluate()
0x00402a01:     mov    %esp,%ebp
0x00402a03:     sub    $0x44,%esp
0x00402a06:     push   %ebx
0x00402a07:     mov    0x10(%ebp),%ebx
0x00402a0a:     push   %esi
0x00402a0b:     mov    0x8(%ebp),%esi
0x00402a0e:     mov    0xb0a(%esi),%cl        # load "TotalWhitePieces"
0x00402a14:     mov    $0xd,%al               # 0xd is 13
0x00402a16:     cmp    %al,%cl                # compare "TotalWhitePieces" to 13
0x00402a18:     push   %edi
0x00402a19:     movl   $0x3,-0x1c(%ebp)       # set "can_win" to 3
0x00402a20:     jge    0x402a53
0x00402a22:     cmp    %al,0xb0b(%esi)        # compare "TotalBlackPieces" to 13
0x00402a28:     jge    0x402a53               # if both < 13
0x00402a2a:     push   %esi                       
0x00402a2b:     call   0x401630                 # call EvaluateWinner()
0x00402a30:     mov    %eax,%edi
0x00402a32:     push   %ebx
0x00402a33:     push   %esi
0x00402a34:     mov    %edi,-0x1c(%ebp)         # store function result in "can_win"
0x00402a37:     call   0x401130                 # call EvaluateStalemate()
0x00402a3c:     add    $0xc,%esp
0x00402a3f:     test   %eax,%eax                # if EvaluateStalemate() result is nonzero
0x00402a41:     jne    0x402a47                   # jump to loading DrawScore(wtm) and returning
0x00402a43:     test   %edi,%edi                # if "can_win" is now zero
0x00402a45:     jne    0x402a53                 # then do the next two lines (else skip)
0x00402a47:     mov    0x6b8d78(,%ebx,4),%eax   # get DrawScore(wtm), it seems
0x00402a4e:     jmp    0x402b9a                 # jump to function exit...
```

As can be seen, the use of "can\_win" is the same (see also the page regarding 99999), as is the comparison to 13.

# ToDo

Either Zach or Mark will disentangle EvaluateWinner() and EvaluateStalemate() to strengthen the evidence here.

# Sidenote

As noted by Zach, this pre-Beta Rybka does not return the \_\_DrawScore(wtm)\_\_ value directly, but first does some manipulations with it.

```
0x00402b9a:     cltd   
0x00402b9b:     sub    %edx,%eax
0x00402b9d:     sar    %eax
0x00402b9f:     test   %eax,%eax
0x00402ba1:     jle    0x404519
0x00402ba7:     cmp    $0x80,%eax
0x00402bac:     jl     0x404531
0x00402bb2:     add    $0xffffff80,%eax
0x00402bb5:     cltd   
0x00402bb6:     and    $0xf,%edx
0x00402bb9:     add    %edx,%eax
0x00402bbc:     sar    $0x4,%eax
0x00402bc0:     add    $0x80,%eax
0x00402bc9:     ret   
[...]
0x00404519:     cmp    $0xffffff80,%eax
0x0040451c:     jg     0x404531
0x0040451e:     add    $0x80,%eax
0x00404523:     cltd   
0x00404524:     and    $0xf,%edx
0x00404527:     add    %edx,%eax
0x00404529:     sar    $0x4,%eax
0x0040452c:     sub    $0x80,%eax
0x00404537:     ret
```

I omitted the "pop" and %esp instructions in the last here, as they only have to do with preparing the stack for subroutine exit.

**[Up one level](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty")**