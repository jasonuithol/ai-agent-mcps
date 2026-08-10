# Rybka-Crafty Evidence II

Source: https://www.chessprogramming.org/Rybka-Crafty_Evidence_II

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* [Pre-Fruit Rybka and Crafty](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty") \* Equality of Even Score with 99999**

**[< Prev](/Rybka-Crafty_Evidence "Rybka-Crafty Evidence") [Next >](/Rybka-Crafty_Evidence_III "Rybka-Crafty Evidence III")**

by [Mark Watkins](/Mark_Watkins "Mark Watkins")

# Crafty Source

Here is the [Crafty](/Crafty "Crafty") 19.15 code. This code was also mentioned in the [ElChinito Case](/Historical_Examples#ElChinito "Historical Examples") [[1]](#cite_note-1):

```
  if ((TotalWhitePawns + TotalBlackPawns) == 0)
    do {
      int ms = EvaluateMate(tree);

      if (ms == 99999)
        break;
      score += ms;
#ifdef DEBUGEV
      printf("score[mater]=  %4d (%+d)\n", score,
          score - lastsc);
#endif
      if (score > DrawScore(1) && !(can_win & 1))
        score = score >> 2;
      if (score < DrawScore(1) && !(can_win & 2))
        score = score >> 2;
      return ((wtm) ? score : -score);
    } while (0);
```

# Rybka Assembly

Here is the function call to something like \_\_EvaluateMate\_\_ in a pre-Beta Rybka disassembly (Zach will likely provide details of how EvaluateMate works, and the closeness of the Rybka/Crafty match there).

```
0x00402b4b:     test   %ebx,%ebx              # test TotalWhitePawns + TotalBlackPawns
0x00402b59:     jne    0x402bca               # if nonzero, skip all this
0x00402b5b:     push   %esi
0x00402b5c:     call   0x404540               # function call: EvaluateMate
0x00402b61:     mov    0x8(%ebp),%ecx         # load "score" variable to ecx
0x00402b64:     add    $0x4,%esp
0x00402b67:     cmp    $0x1869f,%eax          # compare above return value to 99999
0x00402b6c:     je     0x402bcd               # if equal, then break
0x00402b6e:     add    %eax,%ecx              # score += ms
0x00402b70:     mov    0x6b8d7c,%eax          # load DrawScore(1)
0x00402b75:     cmp    %eax,%ecx              # compare score to DrawScore(1)
0x00402b77:     jle    0x402b84
0x00402b79:     testb  $0x1,-0x1c(%ebp)       # can_win & 1
0x00402b7d:     jne    0x402b82
0x00402b7f:     sar    $0x2,%ecx              # shift right by 2 if conditions met
0x00402b82:     cmp    %eax,%ecx              # compare score to DrawScore(1)
0x00402b84:     jge    0x402b8f
0x00402b86:     testb  $0x2,-0x1c(%ebp)       # can_win & 2
0x00402b8a:     jne    0x402b8f
0x00402b8c:     sar    $0x2,%ecx              # shift right by 2 if conditions met
0x00402b8f:     mov    0x10(%ebp),%eax        # load wtm
0x00402b92:     test   %eax,%eax              # determine by wtm whether score or -score
0x00402b94:     jne    0x402b98
0x00402b96:     neg    %ecx
0x00402b98:     mov    %ecx,%eax              # et cetera
```

## EvaluateMate

Here are some relevant parts of that function call (Zach may provide more), enough to show that the return value is always even.

```
FUNCTION_CALL:
0x00404540:     mov    0x4(%esp),%ecx
[...]
0x004046b6:     lea    0x0(%ebp,%ebp,1),%eax     # add ebp to itself for the return value
0x004046ba:     pop    %ebp
0x004046bb:     pop    %ebx
0x004046bc:     ret
[...]
0x00404717:     lea    (%edi,%edi,1),%eax        # double
0x0040471a:     pop    %edi
0x0040471b:     pop    %esi
0x0040471c:     pop    %ebp
0x0040471d:     pop    %ebx
0x0040471e:     ret   
[...]
0x00404729:     lea    (%edi,%edi,1),%eax        # double
0x0040472c:     pop    %edi
0x0040472d:     pop    %esi
0x0040472e:     pop    %ebp
0x0040472f:     pop    %ebx
0x00404730:     ret   
0x00404731:     pop    %edi
0x00404732:     lea    (%esi,%esi,1),%eax        # double
0x00404735:     pop    %esi
0x00404736:     pop    %ebp
0x00404737:     pop    %ebx
0x00404738:     ret
```

This is the only calling of 0x404540 in the code, and I've listed all the returns, with no jumps to instructions between a doubling and returning. In particular, the return value is always even, but then is compared for equality with 99999.

This code is largely relevant when mating KBN vs K.

# References

1. [↑](#cite_ref-1) [Re: Correction: List and ElChinito as Crafty clones, ... etc](https://www.stmintz.com/ccc/index.php?id=383344) by Paul H., [CCC](/CCC "CCC"), August 21, 2004

**[Up one level](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty")**