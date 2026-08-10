# Rybka-Crafty Evidence VI

Source: https://www.chessprogramming.org/Rybka-Crafty_Evidence_VI

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* [Pre-Fruit Rybka and Crafty](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty") \* NextMove and NextEvasion**

**[< Prev](/Rybka-Crafty_Evidence_V "Rybka-Crafty Evidence V")**

by [Mark Watkins](/Mark_Watkins "Mark Watkins")

The NextMove() and NextEvasions() functions in [Crafty](/Crafty "Crafty") also re-appear in pre-Beta [Rybka](/Rybka "Rybka"). I will give the latter completely, and for reasons of length just point out one identical element in NextMove().

# Phases

First, we have Crafty's numbering of phases.

```
#define NONE                      0
#define HASH_MOVE                 1
#define GENERATE_CAPTURE_MOVES    2
#define CAPTURE_MOVES             3
#define KILLER_MOVE_1             4
#define KILLER_MOVE_2             5
#define GENERATE_ALL_MOVES        6
#define SORT_ALL_MOVES            7  
#define HISTORY_MOVES_1           8
#define HISTORY_MOVES_2           9
#define REMAINING_MOVES          10
#define ROOT_MOVES               11
```

# NextEvasion

Crafty uses phases 1, 4, and 10 in NextEvasion(). Here is high-level logic in pre-Beta Rybka.

```
0x00459c70: sub    $0xc,%esp            # NextEvasion() function
0x00459c75: mov    0x18(%esp),%esi
0x00459c7a: mov    0x20(%esp),%edi
0x00459c7e: lea    (%edi,%edi,2),%eax  	
0x00459c81: lea    (%esi,%eax,4),%ebx
0x00459c8b* mov    %ebx,0xc(%esp)
0x00459c84: mov    0xb20(%ebx),%eax     # get current phase
0x00459c8a: dec    %eax                 # (sub 1 from it)
0x00459c8f: je     0x459ca8             # if phase was 1, then ...
0x00459c91: sub    $0x6,%eax   	       	# (sub 6 more)
0x00459c94: je     0x459cea    	       	# if phase was 7, then...
0x00459c96: sub    $0x3,%eax   	       	# (sub 3 more)
0x00459c99: je     0x459e9c    	       	# if phase was 10, then...
0x00459ca1: xor    %eax,%eax   	       	# phase	is bad,	return 0
0x00459ca7: ret
```

Here is the first part of NextEvasion(), for the case HASH\_MOVE:

```
int NextEvasion(TREE * RESTRICT tree, int ply, int wtm) {
  register int *movep, *sortv;
  switch (tree->next_status[ply].phase) {
  case HASH_MOVE:
    tree->last[ply]=GenerateCheckEvasions(tree, ply, wtm, tree->last[ply-1]);
    if (tree->hash_move[ply]) {
      tree->next_status[ply].phase=SORT_ALL_MOVES;
      tree->current_move[ply]=tree->hash_move[ply];
      if (ValidMove(tree,ply,wtm,tree->current_move[ply])) return(HASH_MOVE);
      else Print(128,"bad move from hash table, ply=%d\n",ply);
    }
```

```
0x00459ca8: mov    0x137c(%esi,%edi,4),%ecx    # ptr to tree->last[ply-1]
0x00459caf: mov    0x24(%esp),%edx
0x00459cb3: push   %ecx, %edx, %edi, %esi
0x00459cb7: call   0x452860                    # call GenerateCheckEvasions()
0x00459cbc: mov    %eax,0x1380(%esi,%edi,4)    # save ptr in tree->last[ply]
0x00459cc3: mov    (%esi,%edi,4),%eax          # load tree->hash_move[ply]
0x00459cc9: test   %eax,%eax                   # if this is zero
0x00459ccb: je     0x459cea                      # then goto the next phase
0x00459ccd: mov    %eax,0x1060(%esi,%edi,4)    # tree->current_move[ply] = tree->hash_move[ply]
0x00459cd6: movl   $0x7,0xb20(%ebx)            # set phase to 7 (SORT_ALL_MOVES)
0x00459ce0: mov    $0x1,%eax                   # return 1
0x00459ce9: ret
```

Note that this pre-Beta Rybka seems not to have a ValidMove routine.
Here is the SORT\_ALL\_MOVES case.

```
  case SORT_ALL_MOVES:
    tree->next_status[ply].phase=REMAINING_MOVES;
    if (tree->hash_move[ply]) {
      for (movep=tree->last[ply-1],sortv=tree->sort_value;
           movep<tree->last[ply];movep++,sortv++)
        if (*movep == tree->hash_move[ply]) {
          *sortv=-999999;
          *movep=0;
        }
        else {
          if (p_values[Piece(*movep)+7] < p_values[Captured(*movep)+7]) 
            *sortv=p_values[Captured(*movep)+7]-p_values[Piece(*movep)+7];
          else *sortv=Swap(tree,From(*movep),To(*movep),wtm);
        }
    }
    else {
      for (movep=tree->last[ply-1],sortv=tree->sort_value;
           movep<tree->last[ply];movep++,sortv++)
        if (p_values[Piece(*movep)+7] < p_values[Captured(*movep)+7]) 
          *sortv=p_values[Captured(*movep)+7]-p_values[Piece(*movep)+7];
        else *sortv=Swap(tree,From(*movep),To(*movep),wtm);
    }
```

Note that pre-Beta Rybka also uses -999999 as the sentinel.

```
0x00459cea: mov    (%esi,%edi,4),%eax         # load tree->hash_move[ply]
0x00459cee: mov    0x137c(%esi,%edi,4),%ebp
0x00459cf5: movl   $0xa,0xb20(%ebx)           # tree->next_status[ply].phase=REMAINING_MOVES;
0x00459cff: test   %eax,%eax                  
0x00459d01: mov    0x1380(%esi,%edi,4),%eax
0x00459d08: lea    0x1564(%esi),%ebx
0x00459d0e: je     0x459d87                   # if (tree->hash_move[ply])
0x00459d10: cmp    %eax,%ebp
0x00459d12: jae    0x459de9                     # set up for loop
0x00459d18: mov    0x0(%ebp),%eax            LOOP
0x00459d1b: cmp    (%esi,%edi,4),%eax           # if (*movep == tree->hash_move[ply]
0x00459d1e: jne    0x459d2f
0x00459d20: movl   $0xfff0bdc1,(%ebx)             # *sortv = -999999
0x00459d26: movl   $0x0,0x0(%ebp)                 # *movep = 0
0x00459d2d: jmp    0x459d74                     # else
0x00459d2f: mov    %eax,%ecx
0x00459d31: sar    $0xf,%ecx                      # Captured(*movep)
0x00459d34: mov    %eax,%edx
0x00459d36: sar    $0xc,%edx                      # Piece(*movep)
0x00459d39: and    $0x7,%ecx
0x00459d3c: mov    0x5ffed4(,%ecx,4),%ecx         # y = p_values[Captured(*movep) + 7]
0x00459d43: and    $0x7,%edx
0x00459d46: mov    0x5ffed4(,%edx,4),%edx         # x = p_values[Captured(*movep) + 7]
0x00459d4d: cmp    %ecx,%edx
0x00459d4f: jge    0x459d57                       # if (x < y) 
0x00459d51: sub    %edx,%ecx
0x00459d53: mov    %ecx,(%ebx)                      # *sortv= y - x
0x00459d55: jmp    0x459d74                       # else
0x00459d57: mov    0x28(%esp),%ecx                  # load tree pointer
0x00459d5b: mov    %eax,%edx
0x00459d5e: sar    $0x6,%edx
0x00459d61: and    $0x3f,%edx                       # To(*movep)
0x00459d65: and    $0x3f,%eax                       # From(*movep)
0x00459d69* push   %ecx, %edx, %eax, %esi
0x00459d6a: call   0x45ad80                         # Swap(tree,From(*movep),To(*movep),wtm)
0x00459d6f: add    $0x10,%esp
0x00459d72: mov    %eax,(%ebx)
0x00459d74: mov    0x1380(%esi,%edi,4),%eax     # determine if loop is done
0x00459d7b: add    $0x4,%ebp
0x00459d7e: add    $0x4,%ebx
0x00459d81: cmp    %eax,%ebp
0x00459d83: jb     0x459d18                     # if not done, goto LOOP
0x00459d85: jmp    0x459de9
0x00459d87: cmp    %eax,%ebp                  # else [that is, tree->hash_move[ply] is zero]
0x00459d89: jae    0x459de9
0x00459d8b: jmp    0x459d90
0x00459d8d: lea    0x0(%ecx),%ecx
0x00459d90: mov    0x0(%ebp),%eax            LOOP2 START
0x00459d93: mov    %eax,%ecx
0x00459d95: sar    $0xf,%ecx                    # Captured(*movep)
0x00459d98: mov    %eax,%edx
0x00459d9a: sar    $0xc,%edx
0x00459d9d: and    $0x7,%ecx                    # Piece(*movep)
0x00459da0: mov    0x5ffed4(,%ecx,4),%ecx       # y = p_values[Captured(*movep) + 7]
0x00459da7: and    $0x7,%edx
0x00459daa: mov    0x5ffed4(,%edx,4),%edx       # x = p_values[Captured(*movep) + 7]
0x00459db1: cmp    %ecx,%edx                    # if (x < y)
0x00459db3: jge    0x459dbb
0x00459db5: sub    %edx,%ecx
0x00459db7: mov    %ecx,(%ebx)                    # *sortv = y - x
0x00459db9: jmp    0x459dd8                     # else
0x00459dbb: mov    0x28(%esp),%ecx
0x00459dbf: mov    %eax,%edx
0x00459dc2: sar    $0x6,%edx
0x00459dc5: and    $0x3f,%edx                     # To(*movep)
0x00459dc9: and    $0x3f,%eax                     # From(*movep)
0x00459dcd: push   %ecx, %edx, %eax, %esi
0x00459dce: call   0x45ad80                       # call Swap()
0x00459dd6: mov    %eax,(%ebx)                    # *sortv = value from Swap()
0x00459dd8: mov    0x1380(%esi,%edi,4),%eax     # determine if loop is done
0x00459ddf: add    $0x4,%ebp
0x00459de2: add    $0x4,%ebx
0x00459de5: cmp    %eax,%ebp
0x00459de7: jb     0x459d90                     # if not, goto LOOP2
```

Next Crafty does an insertion sort in this SORT\_ALL\_MOVES phase.

```
    if (tree->last[ply] > tree->last[ply-1]+1) {
      int temp1, temp2, *tmovep, *tsortv;
      int *end;
      sortv=tree->sort_value+1;
      movep=tree->last[ply-1]+1;
      end=tree->last[ply];
      for (;movep<end;movep++,sortv++) {
        temp1=*movep;
        temp2=*sortv;
        tmovep=movep-1;
        tsortv=sortv-1;
        while (tmovep>=tree->last[ply-1] && *tsortv<temp2) {
          *(tsortv+1)=*tsortv;
          *(tmovep+1)=*tmovep;
          tmovep--;
          tsortv--;
        }
        *(tmovep+1)=temp1;
        *(tsortv+1)=temp2;
      }
    }
    tree->next_status[ply].last=tree->last[ply-1];
```

As does pre-Beta Rybka -- I'm not sure comments are that useful.

```
0x00459de9: mov    0x137c(%esi,%edi,4),%eax
0x00459df0: lea    0x4(%eax),%edx
0x00459df3: mov    0x1380(%esi,%edi,4),%eax
0x00459dfa: cmp    %eax,%edx
0x00459dfc: mov    %eax,0x18(%esp)
0x00459e00: jae    0x459e88
0x00459e06: lea    -0x4(%edx),%eax
0x00459e09: lea    0x1568(%esi),%ebp
0x00459e0f: mov    %eax,0x24(%esp)
0x00459e13: jmp    0x459e20
0x00459e15: mov    0x24(%esp),%eax
0x00459e19: lea    0x0(%esp),%esp
0x00459e20: mov    (%edx),%ecx
0x00459e22: cmp    0x137c(%esi,%edi,4),%eax
0x00459e29: mov    %ecx,0x14(%esp)
0x00459e2d: mov    0x0(%ebp),%ecx
0x00459e30: mov    %ecx,0x20(%esp)
0x00459e34: lea    -0x4(%ebp),%ecx
0x00459e37: jb     0x459e61
0x00459e39: lea    0x0(%esp),%esp
0x00459e40: mov    (%ecx),%ebx
0x00459e42: cmp    0x20(%esp),%ebx
0x00459e46: jge    0x459e61
0x00459e48: mov    %ebx,0x4(%ecx)
0x00459e4b: mov    (%eax),%ebx
0x00459e4d: mov    %ebx,0x4(%eax)
0x00459e50: mov    0x137c(%esi,%edi,4),%ebx
0x00459e57: sub    $0x4,%eax
0x00459e5a: sub    $0x4,%ecx
0x00459e5d: cmp    %ebx,%eax
0x00459e5f: jae    0x459e40
0x00459e61: mov    0x14(%esp),%ebx
0x00459e65: mov    %ebx,0x4(%eax)
0x00459e68: mov    0x20(%esp),%eax
0x00459e6c: mov    0x24(%esp),%ebx
0x00459e70: mov    %eax,0x4(%ecx)
0x00459e73: mov    0x18(%esp),%eax
0x00459e77: add    $0x4,%edx
0x00459e7a: add    $0x4,%ebx
0x00459e7d: add    $0x4,%ebp
0x00459e80: cmp    %eax,%edx
0x00459e82: mov    %ebx,0x24(%esp)
0x00459e86: jb     0x459e15
0x00459e88: mov    0x10(%esp),%edx
0x00459e8c: mov    0x137c(%esi,%edi,4),%ecx
0x00459e93: mov    %ecx,0xb18(%edx)
0x00459e99: mov    %edx,%ebx
```

And finally the REMAINING\_MOVES case.

```
  case REMAINING_MOVES:
    for (;tree->next_status[ply].last<tree->last[ply];
           tree->next_status[ply].last++)
      if ((*tree->next_status[ply].last)) {
        tree->current_move[ply]=*tree->next_status[ply].last++;
        return(REMAINING_MOVES);
      }  
    return(NONE);
```

```
0x459e9c: mov   0xb18(%ebx),%eax          # get tree->next_status[ply].last
0x459ea2: cmp   0x1380(%esi,%edi,4),%eax  # if tree->next_status[ply].last >= tree->last[ply]
0x459ea9: jae   0x459c9f                  # return 0 [see above]
0x459eb0: mov   0xb18(%ebx),%eax      LOOP
0x459eb6: cmpl  $0x0,(%eax)               # if NOT *tree->next_status[ply].last
0x459eb9: jne   0x459ed8
0x459ebb: add   $0x4,%eax                 # increment the loop counter
0x459ebe: mov   %eax,%ecx
0x459ec0: mov   %eax,0xb18(%ebx)               
0x459ec6: cmp   0x1380(%esi,%edi,4),%ecx  # if tree->next_status[ply].last < tree->last[ply]
0x459ecd: jb    0x459eb0                      # continue LOOP
0x459ed1: xor   %eax,%eax                 # return 0
0x459ed7: ret    
0x459ed8: mov   0xb18(%ebx),%eax          # else
0x459ede: mov   (%eax),%edx
0x459ee0: mov   %edx,0x1060(%esi,%edi,4)  # tree->current_move[ply]=*tree->next_status[ply].last++;
0x459ee8: add   $0x4,%eax
0x459eeb: mov   %eax,0xb18(%ebx)
0x459ef2: mov   $0xa,%eax                 # return phase 10 (REMAINING_MOVES)
0x459efb: ret
```

# NextMove

Here is the 9th phase in both Crafty and pre-Beta Rybka. It is already somewhat odd to have this HISTORY\_MOVES\_2 phase.

```
  case HISTORY_MOVES_2:
    bestval=0;
    bestp=0;
    for (movep=tree->last[ply-1];movep<tree->last[ply];movep++)
      if (*movep) {
        index=*movep&4095;
        history_value= (wtm) ? history_w[index] : history_b[index];
        if (history_value > bestval) {
          bestval=history_value;
          bestp=movep;
        }
      }
    if (bestval) {
      tree->current_move[ply]=*bestp;
      *bestp=0;
      tree->next_status[ply].remaining++;
      if (tree->next_status[ply].remaining > 3) {
        tree->next_status[ply].phase=REMAINING_MOVES;
        tree->next_status[ply].last=tree->last[ply-1];
      }
      return(HISTORY_MOVES_2);
    }
```

In the second segment, the condition that the number of moves be greater than 3 cannot be said to be typical. Here is the pre-Beta Rybka code for this segment:

```
[...]
0x44bbd4: test   %ebp,%ebp                  # if (bestval)
0x44bbd6: je     0x44bc22
0x44bbd8: mov    (%edx),%eax
0x44bbda: lea    0x2c7(%edi,%edi,2),%ecx
0x44bbe1: mov    %eax,0x1060(%esi,%edi,4)     # tree->current_move[ply]=*bestp;
0x44bbe8: lea    (%esi,%ecx,4),%eax
0x44bbeb: movl   $0x0,(%edx)                  # *bestp = 0
0x44bbf1: mov    (%eax),%edx
0x44bbf3: inc    %edx                         # increment #remaining
0x44bbf4: mov    %edx,%ecx
0x44bbf6: cmp    $0x3,%ecx                    # if #remaining > 3
0x44bbf9: mov    %edx,(%eax)
0x44bbfb: jle    0x44bc14                         
0x44bbfd: mov    0x137c(%esi,%edi,4),%edx       # load tree->last[ply-1]
0x44bc04: movl   $0xa,0xb20(%ebx)               # set phase to 10 (REMAINING_MOVES)
0x44bc0e: mov    %edx,0xb18(%ebx)               # tree->next_status[ply].last = tree->last[ply-1];
0x44bc14: mov    0x80(%esp),%ebp
0x44bc1b: mov    $0x9,%eax                    # phase 9 is HISTORY_MOVES_2
0x44bc20: jmp    0x44bc71                     # return (HISTORY_MOVES_2)
```

The exact similarity with the totality of NextMove() is yet to be determined, but the above should suffice to give an example of code re-use.

**[Up one level](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty")**