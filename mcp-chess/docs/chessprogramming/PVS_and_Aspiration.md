# PVS and Aspiration

Source: https://www.chessprogramming.org/PVS_and_Aspiration

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Alpha-Beta](/Alpha-Beta "Alpha-Beta") \* [Aspiration Windows](/Aspiration_Windows "Aspiration Windows") \* PVS and Aspiration**

This is a discussion from [CCC](/CCC "CCC"), May 31, 2008 [[1]](#cite_note-1):

# Question

by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol")

```
Hi,
When using PVS together with the aspiration window it is sometimes possible to fail low on the first ply of aspirated search in the root node. When it happens, what is the correct course of action:
```

```
1) finish the aspirated search, hoping that something does not fail?
2) interrupt the aspirated search immediately and go for a full-window search?
```

# Answer

by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"):

```
You have two possibilities as you mentioned.
```

```
(1) search the entire root move list before lowering the aspiration window and starting over. This works well for positions where the best (previous) move fails low but there are other ways to avoid the loss.
```

```
(2) reset the aspiration window immediately. This makes you re-search the first move, before you search any other moves. If you are going to change your mind, this is less efficient. But it has advantages as well. At least you know how significant your expected loss is going to be, which gives you an idea of how much time you should spend to solve the problem...
```

```
I use (2) in Crafty, having tried (1) in the past. What I saw often enough to be a problem was the case where your opponent makes a deep move, that does not lose material, but shallow searches thinks it does and claims to (say) win a pawn. Once you get as deep as your opponent, that pawn+ score will fail low. If you search all moves, each and every one will fail low, and then you get to start over with a lowered alpha value after spending all that time. If you immediately re-aspire on the fail low, you find the true score faster and search the rest of the moves with a better set of bounds to dismiss them quicker.
```

```
Each approach has positions that favor them...
```

# Forum Posts

- [Aspiration window](https://www.stmintz.com/ccc/index.php?id=208714) by [Bas Hamstra](/Bas_Hamstra "Bas Hamstra"), [CCC](/CCC "CCC"), January 20, 2002
- [Aspiration search, PVS](https://www.stmintz.com/ccc/index.php?id=273558) by [Russell Reagan](/Russell_Reagan "Russell Reagan"), [CCC](/CCC "CCC"), December 28, 2002
- [Subject: Q. Aspiration, PVS, Fail-Soft](https://www.stmintz.com/ccc/index.php?id=373537) by [David B. Weller](/David_B._Weller "David B. Weller"), [CCC](/CCC "CCC"), July 02, 2004
- [PVS and aspiration windows](https://www.stmintz.com/ccc/index.php?id=381004) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [CCC](/CCC "CCC"), August 06, 2004
- [PVS and aspiration](http://www.talkchess.com/forum/viewtopic.php?t=21516) by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol"), [CCC](/CCC "CCC"), May 31, 2008
- [Your experience with PVS + Aspiration window](http://www.talkchess.com/forum/viewtopic.php?t=53972) by [Fabio Gobbato](/Fabio_Gobbato "Fabio Gobbato"), [CCC](/CCC "CCC"), October 07, 2014

# References

1. [↑](#cite_ref-1) [PVS and aspiration](http://www.talkchess.com/forum/viewtopic.php?t=21516) by [Pawel Koziol](/Pawel_Koziol "Pawel Koziol"), [CCC](/CCC "CCC"), May 31, 2008

**[Up one Level](/Aspiration_Windows "Aspiration Windows")**