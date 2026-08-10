# Rybka-Crafty Evidence V

Source: https://www.chessprogramming.org/Rybka-Crafty_Evidence_V

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* [Pre-Fruit Rybka and Crafty](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty") \* The EvaluateWinner function**

**[< Prev](/Rybka-Crafty_Evidence_IV "Rybka-Crafty Evidence IV") [Next >](/Rybka-Crafty_Evidence_VI "Rybka-Crafty Evidence VI")**

by [Mark Watkins](/Mark_Watkins "Mark Watkins")

This is a function of about 100 lines of operative C code in [Crafty](/Crafty "Crafty") 19.2. It is replicated in pre-Beta [Rybka](/Rybka "Rybka"). It determines whether or not the sides have winning chances. It is fairly clearly part of "evaluation", and thus not of merely tangential interest. This should suffice for an example of a "large chunk" of code directly copied from Crafty in pre-Beta Rybka.

# Part I

```
int EvaluateWinner(TREE * RESTRICT tree) {
  register int can_win=3;
/*  ----------------------------------------------------------
  |   if one side is a piece up, but has no pawns, then that |
  |   side can not possibly win.                             |
   ---------------------------------------------------------- */
  if (WhiteMajors == BlackMajors) {
    if (TotalWhitePawns==0 && WhiteMinors-BlackMinors==1) can_win&=2;
    if (TotalBlackPawns==0 && BlackMinors-WhiteMinors==1) can_win&=1;
    if (can_win == 0) return(can_win);
  }
```

```
0x00401630:     push   %ebp               # start EvaluateWinner function
0x00401631:     mov    %esp,%ebp
0x00401633:     sub    $0x24,%esp
0x00401647*     push   %ebx
0x00401648*     push   %esi
0x00401649*     mov    $0x3,%esi          # "can_win" = 3
0x0040164e*     push   %edi
0x00401636:     mov    0x8(%ebp),%ecx
0x00401639:     mov    0xb0e(%ecx),%al    # load WhiteMajors
0x0040163f:     mov    0xb0f(%ecx),%dl    # load BlackMajors
0x00401645:     cmp    %dl,%al            # if these are equal
0x0040164f:     mov    %esi,-0x4(%ebp)
0x00401652:     jne    0x4016a7             
0x00401654:     mov    0xb10(%ecx),%bl      # load TotalWhitePawns
0x0040165a:     test   %bl,%bl              # if TotalWhitePawns is 0
0x0040165c:     jne    0x40167b
0x0040165e:     movsbl 0xb0d(%ecx),%edi       # load BlackMinors
0x00401665:     movsbl 0xb0c(%ecx),%ebx       # load WhiteMinors
0x0040166c:     sub    %edi,%ebx              # compute WhiteMinors-BlackMinors
0x0040166e:     cmp    $0x1,%ebx              # if result is 1
0x00401671:     jne    0x40167b
0x00401673:     mov    $0x2,%esi
0x00401678:     mov    %esi,-0x4(%ebp)          # set "can_win" to 2
0x0040167b:     mov    0xb11(%ecx),%bl      # load TotalBlackPawns
0x00401681:     test   %bl,%bl              # if TotalBlackPawns is 0
0x00401683:     jne    0x40169f
0x00401685:     movsbl 0xb0d(%ecx),%edi       # load BlackMinors
0x0040168c:     movsbl 0xb0c(%ecx),%ebx       # load WhiteMinors
0x00401693:     sub    %ebx,%edi              # compute BlackMinors-WhiteMinors
0x00401695:     cmp    $0x1,%edi              # if result is 1
0x00401698:     jne    0x40169f
0x0040169a:     and    %edi,%esi              # AND "can_win" with 1
0x0040169c:     mov    %esi,-0x4(%ebp)
0x0040169f:     test   %esi,%esi            # if can_win is 0
0x004016a1:     je     0x4016e7               # return 0
[...]
```

# Part II

```
/* ----------------------------------------------------------
  |   if one side is an exchange up, but has no pawns, then  |
  |   that side can not possibly win.                        |
   ---------------------------------------------------------- */
  if (WhiteMajors != BlackMajors) {
    if ((WhiteMajors-BlackMajors) == (BlackMinors-WhiteMinors)) {
      if (TotalBlackPawns==0) can_win&=1;
      if (TotalWhitePawns==0) can_win&=2;
    }
    if (can_win == 0) return(can_win);
  }
```

```
0x00401639:     mov    0xb0e(%ecx),%al    # load WhiteMajors
0x0040163f:     mov    0xb0f(%ecx),%dl    # load BlackMajors
[...]
0x004016a3:     cmp    %dl,%al            # if WhiteMajors != BlackMajors
0x004016a5:     je     0x4016f0
0x004016a7:     movsbl 0xb0d(%ecx),%edi     # load BlackMinors
0x004016ae:     movsbl 0xb0c(%ecx),%ebx     # load WhiteMinors
0x004016b5:     movsbl %dl,%edx             
0x004016b8:     movsbl %al,%eax
0x004016bb:     sub    %ebx,%edi            # BlackMinors-WhiteMinors
0x004016bd:     sub    %edx,%eax            # WhiteMajors-BlackMajors
0x004016bf:     cmp    %edi,%eax            # compare these last 2
0x004016c1:     jne    0x4016e3             # if equal
0x004016c3:     mov    0xb11(%ecx),%al        # load TotalBlackPawns
0x004016c9:     test   %al,%al                # if TotalBlackPawns is 0
0x004016cb:     jne    0x4016d3
0x004016cd:     and    $0x1,%esi                # AND "can_win" with 1
0x004016d0:     mov    %esi,-0x4(%ebp)
0x004016d3:     mov    0xb10(%ecx),%al        # load TotalWhitePawns
0x004016d9:     test   %al,%al                # if TotalWhitePawns is 0
0x004016db:     jne    0x4016e3
0x004016dd:     and    $0x2,%esi                # AND "can_win" with 2
0x004016e0:     mov    %esi,-0x4(%ebp)
0x004016e3:     test   %esi,%esi            # if "can_win" is 0
0x004016e5:     jne    0x4016f0
0x004016e9:     xor    %eax,%eax              # return 0
0x004016ef:     ret   
[...]
```

Note that Rybka checks TotalBlackPawns before TotalWhitePawns here, just like Crafty, and the opposite of the order in the first part.

# Part III

```
/* ************************************************************
*   if neither side has any pieces, and both sides have    *
*   non-rookpawns, then either side can win.  also, if one *
*   has a piece and the other side has one pawn, then that *
*   piece can sac itself for the pawn so that the side     *
*   with a pawn can't win.                                 *
************************************************************ */
  if (TotalWhitePieces == 0 && TotalBlackPieces == 0) {
    if (WhitePawns & not_rook_pawns && BlackPawns & not_rook_pawns)
      return (can_win);
  }
  if (!TotalBlackPieces) {
    if (!TotalBlackPawns)
      can_win &= 1;
    if (TotalBlackPawns == 1 && TotalWhitePieces)
      can_win &= 1;
  }
  if (!TotalWhitePieces) {
    if (!TotalWhitePawns)
      can_win &= 2;
    if (TotalWhitePawns == 1 && TotalBlackPieces)
      can_win &= 2;
  }
```

```
0x004016f0: mov    0xb0a(%ecx),%bl     # load TotalWhitePieces
0x004016f6: test   %bl,%bl
0x004016f8: jne    0x40173e
0x004016fa: mov    0xb0b(%ecx),%al     # load TotalBlackPieces
0x00401700: test   %al,%al
0x00401702: jne    0x40173e            # if both are zero
0x00401704: mov    0xa78(%ecx),%eax      # load WhitePawns bitboard
0x0040170a: mov    0xa7c(%ecx),%edx      # ... in 2 steps of course
0x00401710: and    $0x7e7e7e7e,%eax      # AND this bitboard
0x00401715: and    $0x7e7e7e7e,%edx      # with "not_rook_pawns"
0x0040171b: or     %edx,%eax             # if result is nonempty
0x0040171d: je     0x40173e             
0x0040171f: mov    0xa80(%ecx),%eax        # load BlackPawns bitboard
0x00401725: mov    0xa84(%ecx),%edx
0x0040172b: and    $0x7e7e7e7e,%eax        # AND this bitboard
0x00401730: and    $0x7e7e7e7e,%edx        # with "not_rook_pawns"
0x00401736: or     %edx,%eax               # if result is nonempty
0x00401738: jne    0x4020b2                  # return current "can_win"

0x0040173e: mov    0xb0b(%ecx),%dl     # load TotalBlackPieces (again)
0x00401744: test   %dl,%dl             # if nonzero
0x00401746: jne    0x401766
0x00401748: mov    0xb11(%ecx),%al       # load TotalBlackPawns
0x0040174e: test   %al,%al               # if nonzero
0x00401750: jne    0x401758
0x00401752: and    $0x1,%esi               # AND "can_win" with 1
0x00401755: mov    %esi,-0x4(%ebp)
0x00401758: cmp    $0x1,%al              # if TotalBlackPawns is 1
0x0040175a: jne    0x401766
0x0040175c: test   %bl,%bl               # and TotalWhitePieces is nonzero
0x0040175e: je     0x40176a
0x00401760: and    $0x1,%esi               # AND "can_win" with 1
0x00401763: mov    %esi,-0x4(%ebp)

0x00401766: test   %bl,%bl             # if TotalWhitePieces is nonzero
0x00401768: jne    0x401788
0x0040176a: mov    0xb10(%ecx),%al       # load TotalWhitePawns
0x00401770: test   %al,%al               # if nonzero
0x00401772: jne    0x40177a
0x00401774: and    $0x2,%esi               # AND "can_win" with 2
0x00401777: mov    %esi,-0x4(%ebp)
0x0040177a: cmp    $0x1,%al              # if TotalWhitePawns is 1
0x0040177c: jne    0x401788
0x0040177e: test   %dl,%dl               # and TotalBlackPieces is nonzero
0x00401780: je     0x401788
0x00401782: and    $0x2,%esi               # AND "can_win" with 2
0x00401785: mov    %esi,-0x4(%ebp)
[...]
```

Note again that Rybka and Crafty both choose to compare TotalWhitePieces then TotalBlackPieces on the first line, but then both switch the order in the latter two segments.

# Parts IV and V

The next parts of the Crafty code are quite long. They determine blind bishops, one segment for White, and the other for Black. And in each segment, there is replication of code for a8 versus h8. Furthermore, the compiler used for pre-Rybka Beta seems not to recognise the common subexpression in something like \_\_Distance(LastOne(),A8)\_\_ where Distance is a macro of the max of Rank and File distance, which themselves involve a macro for absolute value. So this section is quite hairy.

```
/* ----------------------------------------------------------
  |   if white has a pawn, then either the pawn had better   |
  |   not be a rook pawn, or else white had better have the  |
  |   right color bishop or any other piece, otherwise it is |
  |   not winnable if the black king can get to the queening |
  |   square first.                                          |
   ---------------------------------------------------------- */
  if (TotalWhitePawns) do {
    if (WhitePawns&not_rook_pawns) continue;
    if (TotalWhitePieces>3 || (TotalWhitePieces==3 && WhiteKnights)) continue;
    if (TotalWhitePieces==0) {
      if (file_mask[FILEA]&WhitePawns &&
          file_mask[FILEH]&WhitePawns) continue;
    }
    if (!(WhitePawns&not_rook_pawns)) {
      if (WhiteBishops) {
        if (!BlackBishops) {
          if (WhiteBishops&dark_squares) {
            if (file_mask[FILEH]&WhitePawns) continue;
          }
          else if (file_mask[FILEA]&WhitePawns) continue;
        }
        else {
          if (WhiteBishops&dark_squares && !(BlackBishops&dark_squares)) {
            if (file_mask[FILEH]&WhitePawns) continue;
          }
          else if (file_mask[FILEA]&WhitePawns) continue;
        }
      }
      if (!(WhitePawns&file_mask[FILEA]) ||
          !(WhitePawns&file_mask[FILEH])) {
        if (WhitePawns&file_mask[FILEA]) {
          int bkd, wkd, pd;
          bkd=Distance(BlackKingSQ,A8);
          if (bkd <= 1) can_win&=2;
          else {
            wkd=Distance(WhiteKingSQ,A8);
            pd=Distance(LastOne(WhitePawns&file_mask[FILEA]),A8);
            if (bkd<(wkd-wtm) && bkd<=(pd-wtm)) can_win&=2;
          }
          continue;
        }
        else {
          int bkd, wkd, pd;
          bkd=Distance(BlackKingSQ,H8);
          if (bkd <= 1) can_win&=2;
          else {
            wkd=Distance(WhiteKingSQ,H8);
            pd=Distance(LastOne(WhitePawns&file_mask[FILEH]),H8);
            if (bkd<(wkd-wtm) && bkd<=(pd-wtm)) can_win&=2;
          }
          continue;
        }
      }
    }
  } while (0);
```

```
0x004016f0: mov    0xb0a(%ecx),%bl   # load TotalWhitePieces
[...]
0x00401788: mov    0xb10(%ecx),%al   # load TotalWhitePawns
0x0040178e: test   %al,%al           # if TotalWhitePawns is nonzero
0x00401790: je     0x401bae
0x00401796: mov    0xa78(%ecx),%esi    # load WhitePawns bitboard
0x0040179c: mov    0xa7c(%ecx),%edi    # ... in 2 steps of course
0x004017a2: mov    %esi,%eax
0x004017a4: mov    %edi,%edx
0x004017a6: and    $0x7e7e7e7e,%eax    # AND WhitePawns with not_rook_pawns
0x004017ab: and    $0x7e7e7e7e,%edx
0x004017b1: or     %edx,%eax
0x004017b3: jne    0x401bab            # if result is nonzero, skip the rest
0x004017b9: cmp    $0x3,%bl               
0x004017bc: jg     0x401bab            # if TotalWhitePieces > 3
0x004017c2: jne    0x4017d6            #    or (TotalWhitePieces ==3
0x004017c4: mov    0xa88(%ecx),%edx    #            and WhiteKnights)
0x004017ca: or     0xa8c(%ecx),%edx    # [other 32-bit of WhiteKnights]
0x004017d0: jne    0x401bab              # then skip the rest
0x004017d6: test   %bl,%bl             
0x004017d8: jne    0x401804            # if TotalWhitePieces is 0
0x004017da: mov    %esi,%eax
0x004017dc: mov    %edi,%edx
0x004017de: and    $0x1010101,%eax       # AND WhitePawns with FILEA filemask
0x004017e3: and    $0x1010101,%edx
0x004017e9: or     %edx,%eax
0x004017eb: je     0x401804
0x004017ed: mov    %esi,%eax
0x004017ef: mov    %edi,%edx
0x004017f1: and    $0x80808080,%eax      # AND WhitePawns with FILEH filemask
0x004017f6: and    $0x80808080,%edx
0x004017fc: or     %edx,%eax
0x004017fe: jne    0x401bab              # if both are nonzero, skip the rest
0x00401804: mov    0xa98(%ecx),%eax    # load WhiteBishops
0x0040180a: mov    0xa9c(%ecx),%edx
0x00401810: mov    %eax,%ebx
0x00401812: or     %edx,%ebx
0x00401814: mov    %edx,-0x10(%ebp)
0x00401817: je     0x401896            # if WhiteBishops is nonzero
0x00401819: mov    0xaa0(%ecx),%ebx      # load BlackBishops
0x0040181f: mov    0xaa4(%ecx),%edx
0x00401825: mov    %ebx,-0xc(%ebp)
0x0040182d: or     %edx,%ebx
0x0040182f: jne    0x40184f              # if BlackBishops is 0
0x00401828* and    $0xaa55aa55,%eax
0x00401831: mov    -0x10(%ebp),%edx
0x00401834: and    $0xaa55aa55,%edx        # AND WhiteBishops with dark_squares
0x0040183a: or     %edx,%eax
0x0040183c: mov    %edi,%edx
0x0040183e: mov    %esi,%eax
0x00401840: je     0x401883                # if result is nonzero
0x00401842: and    $0x80808080,%eax          # AND WhitePawns with FILEH
0x00401847: and    $0x80808080,%edx        # else AND WhitePawns with FILEA 
0x0040184d: jmp    0x40188e                # if result is non-0, skip the rest
0x0040184f: mov    -0x10(%ebp),%ebx      # else [a BlackBishop exists]
0x00401852: and    $0xaa55aa55,%ebx
0x00401858: or     %ebx,%eax
0x0040185a: je     0x40187f                # if (WhiteBishop & dark_squares)
0x0040185c: mov    -0xc(%ebp),%eax
0x0040185f: and    $0xaa55aa55,%eax
0x00401864: and    $0xaa55aa55,%edx
0x0040186a: or     %edx,%eax
0x0040186c: jne    0x40187f                # and !(BlackBishops & dark_squares)
0x0040186e: mov    %esi,%eax
0x00401870: mov    %edi,%edx
0x00401872: and    $0x80808080,%eax          # AND WhitePawns with FILEH
0x00401877: and    $0x80808080,%edx        # else AND WhitePawns with FILA   
0x0040187d: jmp    0x40188e                # if result is non-0, skip the rest
0x0040187f: mov    %esi,%eax
0x00401881: mov    %edi,%edx
0x00401883: and    $0x1010101,%eax          [AND with FILEA, see 401840 above]
0x00401888: and    $0x1010101,%edx
0x0040188e: or     %edx,%eax
0x00401890: jne    0x401bab                 
0x00401896: mov    %esi,%ebx           # So, blind bishops are applicable...
0x00401898: and    $0x1010101,%ebx
0x0040189e: mov    %edi,%eax
0x004018a0: and    $0x1010101,%eax     # AND WhitePawns with FILEA
0x004018a5: mov    %ebx,%edx
0x004018a7: or     %eax,%edx
0x004018a9: mov    %eax,-0x18(%ebp)
0x004018ac: je     0x4018c8
0x004018ae: mov    %esi,%eax
0x004018b0: mov    %edi,%edx
0x004018b2: and    $0x80808080,%eax    # AND WhitePawns with FILEH
0x004018b7: and    $0x80808080,%edx
0x004018bd: or     %edx,%eax
0x004018bf: jne    0x401bab            # if neither is zero, skip the rest
0x004018c5: mov    -0x18(%ebp),%eax
0x004018c8: mov    %ebx,%edx           # about to split into two cases...
0x004018ca: or     %eax,%edx
0x004018cc: je     0x401a34            # if (WhitePawns & file_mask[FILEA])
0x004018d2: movsbl 0xb09(%ecx),%edi      # load BlackKingSQ
0x004018d9: mov    %edi,%eax
0x004018db: sar    $0x3,%eax
0x004018de: sub    $0x7,%eax             # compute Distance(BlackKingSq, A8)
0x004018e1: cltd   
0x004018e2: mov    %eax,%esi
0x004018e4: xor    %edx,%esi
0x004018e6: mov    %edi,%eax
0x004018e8: and    $0x7,%eax
0x004018eb: sub    %edx,%esi
0x004018ed: cltd   
0x004018ee: xor    %edx,%eax
0x004018f0: sub    %edx,%eax
0x004018f2: cmp    %esi,%eax
0x004018f4: mov    %eax,0x8(%ebp)
0x004018f7: jg     0x4018fc
0x004018f9: mov    %esi,0x8(%ebp)        # distance is now in 0x8(%ebp)
0x004018fc: cmpl   $0x1,0x8(%ebp)        # compare this distance to 1
0x00401900: jle    0x401ba7              # if distance <= 1
0x00401ba7* andl   $0x2,-0x4(%ebp)         # AND "can_win" with 2
0x00401bab* mov    -0x4(%ebp),%esi         # and ignore the rest
0x00401906: movsbl 0xb08(%ecx),%edi      # else load WhiteKingSQ
0x0040190d: mov    %edi,%eax             
0x0040190f: sar    $0x3,%eax
0x00401912: sub    $0x7,%eax
0x00401915: cltd   
0x00401916: mov    %eax,%esi
0x00401918: xor    %edx,%esi
0x0040191a: mov    %edi,%eax
0x0040191c: and    $0x7,%eax
0x0040191f: sub    %edx,%esi
0x00401921: cltd   
0x00401922: xor    %edx,%eax
0x00401924: sub    %edx,%eax
0x00401926: cmp    %esi,%eax
0x00401928: jle    0x40192c
0x0040192a: mov    %eax,%esi
0x0040192c: mov    -0x18(%ebp),%eax      # have Distance(WhiteKingSQ,A8)
0x0040192f: mov    %ebx,-0x24(%ebp)      # now the next Distance
0x00401932: mov    %eax,-0x20(%ebp)
0x00401935: bsf    -0x24(%ebp),%edx      # get LastOne(WhitePawns & FILEA)
0x00401939: mov    $0x0,%eax
0x0040193e: jne    0x401950
0x00401940: bsf    -0x20(%ebp),%edx
0x00401944: mov    $0x20,%eax
0x00401949: jne    0x401950              # HORRORS, the compiler is going
0x0040194b: mov    $0x20,%edx            # to split the Distance computation
0x00401950: add    %edx,%eax             # with Max(FileDist,RankDist)
0x00401952: mov    0xa78(%ecx),%edx      # and then FileDist as abs(x,y)
0x00401958: mov    %eax,%edi             # into four different parts...!
0x0040195a: mov    0xa7c(%ecx),%eax
0x00401960: and    $0x1010101,%edx
0x00401966: and    $0x1010101,%eax
0x0040196b: mov    %edx,-0x24(%ebp)
0x0040196e: mov    %eax,-0x20(%ebp)
0x00401971: bsf    -0x24(%ebp),%edx      # get LastOne(WhitePawns & FILEA) a second time
0x00401975: mov    $0x0,%eax
0x0040197a: jne    0x40198c
0x0040197c: bsf    -0x20(%ebp),%edx
0x00401980: mov    $0x20,%eax
0x00401985: jne    0x40198c
0x00401987: mov    $0x20,%edx
0x0040198c: add    %edx,%eax
0x0040198e: sar    $0x3,%eax
0x00401991: sub    $0x7,%eax
0x00401994: cltd   
0x00401995: mov    %eax,%ebx
0x00401997: xor    %edx,%ebx
0x00401999: sub    %edx,%ebx
0x0040199b: mov    %edi,%eax
0x0040199d: and    $0x7,%eax
0x004019a0: cltd   
0x004019a1: xor    %edx,%eax
0x004019a3: sub    %edx,%eax
0x004019a5: mov    0xa78(%ecx),%edx
0x004019ab: and    $0x1010101,%edx
0x004019b1: cmp    %ebx,%eax
0x004019b3: mov    0xa7c(%ecx),%eax
0x004019b9: mov    %edx,-0x24(%ebp)
0x004019bc: jle    0x4019e8
0x004019be: and    $0x1010101,%eax
0x004019c3: mov    %eax,-0x20(%ebp)
0x004019c6: bsf    -0x24(%ebp),%edx      # get LastOne(WhitePawns & FILEA) a third time
0x004019ca: mov    $0x0,%eax
0x004019cf: jne    0x4019e1
0x004019d1: bsf    -0x20(%ebp),%edx
0x004019d5: mov    $0x20,%eax
0x004019da: jne    0x4019e1
0x004019dc: mov    $0x20,%edx
0x004019e1: add    %edx,%eax
0x004019e3: and    $0x7,%eax
0x004019e6: jmp    0x401a13
0x004019e8: and    $0x1010101,%eax
0x004019ed: mov    %eax,-0x20(%ebp)
0x004019f0: bsf    -0x24(%ebp),%edx      # get LastOne(WhitePawns & FILEA) a fourth time
0x004019f4: mov    $0x0,%eax
0x004019f9: jne    0x401a0b
0x004019fb: bsf    -0x20(%ebp),%edx
0x004019ff: mov    $0x20,%eax
0x00401a04: jne    0x401a0b
0x00401a06: mov    $0x20,%edx
0x00401a0b: add    %edx,%eax
0x00401a0d: sar    $0x3,%eax
0x00401a10: sub    $0x7,%eax
0x00401a13: mov    0x8(%ebp),%edi
0x00401a16: cltd   
0x00401a19: sub    %edx,%eax           
0x00401a1b: mov    0x6aa02c,%edx         # load wtm
0x00401a21: sub    %edx,%esi             
0x00401a23: cmp    %esi,%edi             # if (bkd < wkd-wtm)
0x00401a25: jge    0x401bab
0x00401a2b: sub    %edx,%eax
0x00401a2d: cmp    %eax,%edi             # and (bkd <= pd-wtm)
0x00401a2f: jmp    0x401ba5             
0x00401ba5* jg     0x401bab
0x00401ba7* andl   $0x2,-0x4(%ebp)         # AND "can_win" with 2, skip rest
0x00401a34: movsbl 0xb09(%ecx),%eax      # else case 2, the same for H8/FILEH (omitted)
[...]
```

I also omit the analogous code for determining if Black has a blind bishop.

# Part VI

```
/* ----------------------------------------------------------
  |   if both sides have pawns, the game is not a draw for   |
  |   lack of material.  also, if one side has at least a    |
  |   B+N, then it's not a drawn position.                   |
  |                                                          |
  |   if one side has a rook, while the other side has a     |
  |   minor + pawns, then the rook can't possibly win.       |
   ---------------------------------------------------------- */
  if (TotalWhitePawns && TotalBlackPawns) return(can_win);
```

```
0x00401fc5: mov    -0x4(%ebp),%esi
0x00401fc8: mov    0xb10(%ecx),%al    # load TotalWhitePawns
0x00401fce: test   %al,%al
0x00401fd0: je     0x401fe0
0x00401fd2: mov    0xb11(%ecx),%dl    # load TotalBlackPawns
0x00401fd8: test   %dl,%dl
0x00401fda: jne    0x4020b2           # if both nonzero, return "can_win"
```

# Part VII

```
/* ----------------------------------------------------------
  |   if one side has two bishops, and the other side has    |
  |   a single kinght, the two bishops win.                  |
   ---------------------------------------------------------- */
  if (TotalWhitePawns==0 && TotalWhitePieces==6 &&
      TotalBlackPieces==3) {
    if (WhiteKnights || !BlackKnights) can_win&=2;
  }
  else if (TotalBlackPawns==0 && TotalBlackPieces==6 &&
      TotalWhitePieces==3) {
    if (BlackKnights || !WhiteKnights) can_win&=1;
  }
```

```
0x00401fe0: test   %al,%al            # if TotalWhitePawns == 0
0x00401fe4: jne    0x402018
0x00401fe2* mov    $0x6,%dl       
0x00401fe6: cmp    %dl,0xb0a(%ecx)    # and TotalWhitePieces == 6
0x00401fec: jne    0x402018           
0x00401fee: cmpb   $0x3,0xb0b(%ecx)   # and TotalBlackPieces == 3
0x00401ff5: jne    0x402018
0x00401ff7: mov    0xa88(%ecx),%edi     
0x00401ffd: or     0xa8c(%ecx),%edi
0x00402003: jne    0x402013             # if WhiteKinghts
0x00402005: mov    0xa90(%ecx),%edi
0x0040200b: or     0xa94(%ecx),%edi
0x00402011: jne    0x402052             # or !BlackKnights
0x00402013: and    $0x2,%esi              # AND "can_win" with 2
0x00402016: jmp    0x402052           # else
0x00402018: mov    0xb11(%ecx),%bl    # if TotalBlackPawns == 0
0x0040201e: test   %bl,%bl
0x00402020: jne    0x402052
0x00402022: cmp    %dl,0xb0b(%ecx)
0x00402028: jne    0x402052           # and TotalBlackPieces == 6
0x0040202a: cmpb   $0x3,0xb0a(%ecx)
0x00402031: jne    0x402052           # and TotalWhitePieces == 3
0x00402033: mov    0xa90(%ecx),%edi
0x00402039: or     0xa94(%ecx),%edi
0x0040203f: jne    0x40204f             # if BlackKnights
0x00402041: mov    0xa88(%ecx),%edi
0x00402047: or     0xa8c(%ecx),%edi
0x0040204d: jne    0x402052             # or !WhiteKnights
0x0040204f: and    $0x1,%esi              # AND "can_win" with 1
```

# Part VIII

```
/* ----------------------------------------------------------
  |   if one side is two knights ahead and the opponent has  |
  |   no remaining material, it is a draw.                   |
   ---------------------------------------------------------- */
  if (TotalWhitePawns==0 && TotalWhitePieces==6 && !WhiteBishops &&
      TotalBlackPieces+TotalBlackPawns==0) can_win&=2;
  if (TotalBlackPawns==0 && TotalBlackPieces==6 && !BlackBishops &&
      TotalWhitePieces+TotalWhitePawns==0) can_win&=1;
  return(can_win);
}
```

```
0x00402052: test   %al,%al
0x00402054: jne    0x402081           # if TotalWhitePawns == 0
0x00402056: cmp    %dl,0xb0a(%ecx)   
0x0040205c: jne    0x402081           # and TotalWhitePieces == 6
0x0040205e: mov    0xa98(%ecx),%edi
0x00402064: or     0xa9c(%ecx),%edi
0x0040206a: jne    0x402081           # and !WhiteBishops
0x0040206c: movsbl 0xb0b(%ecx),%edi   # and TotalBlackPieces +
0x00402073: movsbl 0xb11(%ecx),%ebx   #     TotalBlackPawns
0x0040207a: add    %ebx,%edi         
0x0040207c: jne    0x402081           #     is zero
0x0040207e: and    $0x2,%esi          #  then AND "can_win" with 2
0x00402081: mov    0xb11(%ecx),%bl
0x00402087: test   %bl,%bl            # if TotalBlackPawns == 0
0x00402089: jne    0x4020b2
0x0040208b: cmp    %dl,0xb0b(%ecx)    # and TotalBlackPieces == 6
0x00402091: jne    0x4020b2
0x00402093: mov    0xaa0(%ecx),%edx
0x00402099: or     0xaa4(%ecx),%edx
0x0040209f: jne    0x4020b2           # and !BlackBishops
0x004020a1: movsbl 0xb0a(%ecx),%ecx   # and TotalWhitePieces +
0x004020a8: movsbl %al,%edx           #     TotalWhitePawns
0x004020ab: add    %edx,%ecx
0x004020ad: jne    0x4020b2           #     is zero
0x004020af: and    $0x1,%esi          #  then AND "can_win" with 1
0x004020ba: ret
```

**[Up one level](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty")**