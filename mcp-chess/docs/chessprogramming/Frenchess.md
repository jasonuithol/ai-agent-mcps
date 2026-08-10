# Frenchess

Source: https://www.chessprogramming.org/Frenchess

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Frenchess**

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/FrenchTop25Cities.png/330px-FrenchTop25Cities.png)](/File:FrenchTop25Cities.png)

French TOP 25 urban areas - 2010 [[1]](#cite_note-1)

**Frenchess**,  
a massively [parallel](/Parallel_Search "Parallel Search") chess program by [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), [Jean-Luc Seret](/Jean-Luc_Seret "Jean-Luc Seret") and [Michel Gondran](/Michel_Gondran "Michel Gondran"). It played the [WCCC 1995](/WCCC_1995 "WCCC 1995") in [Shatin](https://en.wikipedia.org/wiki/Sha_Tin), [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong), [China](https://en.wikipedia.org/wiki/China), and finished fourth, tied with [Deep Blue Prototype](/Deep_Blue "Deep Blue").

# Description

given in 1995 from the [ICGA](/ICGA "ICGA") site [[2]](#cite_note-2):

```
Frenchess is a parallel chess program which runs on a Cray T3D computer (128 Alpha processors, owned by the Commissariat a l'Energie Atomique located in Grenoble, France). It is written in C and is based on the parallel algorithm described by Jean Christophe Weill in his PhD thesis: [3] Alpha-Beta Distribue Avec Droit d'Ainesse (ABDADA). The evaluation relies mostly on an Oracle approach, which introduces strategy and is designed to be rewritten in the CHEVAL (CHess EVAluation Language) evaluation function description language currently under development (but CHEVAL will probably not be ready for the World Championships). Frenchess is written with the support of the "Direction des Etudes et Recherches (DER) d'Electrique de France (EDF)" as a research project on parallel computing.
```

# SHMEM vs PVM

First trials to port Frenchess to the [Cray T3D](/Cray_T3D "Cray T3D") used [PVM](https://en.wikipedia.org/wiki/Parallel_Virtual_Machine),
since the authors did not find anything to replace [mutex locks](https://en.wikipedia.org/wiki/Mutual_exclusion)
in [MPP](https://en.wikipedia.org/wiki/Massively_parallel) [C](/C "C"), but PVM implementation failed in setting channels between processors.
Eventually the Frenchess team got aware that mutex locks could be simulated using the atomic *shmem\_swap* call [[4]](#cite_note-4), and stuck with [SHMEM](https://en.wikipedia.org/wiki/SHMEM) and following routines to lock and unlock a [shared hash table](/Shared_Hash_Table "Shared Hash Table") entry from a processing element (PE) [[5]](#cite_note-5):

```
/*
 * locks a hash table entry on PE node, waiting for the entry
 * to be unlocked if necessary. The important property is
 * the atomicity of shmem_swap.
 *
 * In this example, shmem_swap replaces the value of
 * hashtable[entry].lockentry on PE node  with the value
 * of IsLocked on the current PE,
 * returning the value  hashtable[entry].lockentry on PE node had
 * before the swap.
 */
lock (int entry, int node)
{
  long IsLocked;
  IsLocked = 1;
  while (IsLocked == 1) {
    IsLocked = shmem_swap ( &(hashtable[entry].lockentry), IsLocked, node);
  }
}

/* unlocks a lock set with lock() */
unlock (int entry, int node)
{
 long IsLocked = 0;
 shmem_swap( &(hashtable[entry].lockentry), IsLocked, node);
}
```

# Selected Games

## Chess Genius

[WCCC 1995](/WCCC_1995 "WCCC 1995"), round 2, [Chess Genius](/Chess_Genius "Chess Genius") - Frenchess [[6]](#cite_note-6)

```
Frenchess, on the 128 PEs T3D exhibited a high level of play, but due to bad connection problems (which plagued all the remote machines), could not use its special tournament opening books. It had to use abook designed to play against humans with risky variations, and lost a game to Chess Genius due to a bad opening line [7].
```

```
[Event "WCCC 1995"]
[Site "Shatin, Hong Kong - China"]
[Date "1995.05.26"]
[Round "2"]
[White "Chess Genius"]
[Black "Frenchess"]
[Result "1-0"]

1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 Bb4 5.Nd5 e4 6.Nh4 Bc5 7.Bg2 d6 8.O-O Be6 9.Nxf6+ Qxf6 
10.Bxe4 Bxc4 11.Qa4 d5 12.d3 a6 13.Bf3 Bb5 14.Qf4 Ne7 15.Qxf6 gxf6 16.Bf4 Bb6 17.Be3 Ba7 
18.Bxa7 Rxa7 19.Rac1 Bc6 20.Ng2 O-O 21.Nf4 Rd8 22.d4 a5 23.e3 Ng6 24.Nh5 Rd6 25.Rc3 Ra6 
26.Rfc1 a4 27.Be2 Rb6 28.R1c2 f5 29.Bd3 Ne7 30.Rc5 Rd8 31.Ra5 Rc8 32.Nf4 Rd8 33.Bf1 f6
34.Ne6 Rc8 35.Nc5 Be8 36.Nxa4 Bxa4 37.Rxa4 Kf7 38.Bd3 Ke6 39.b4 Kd6 40.b5 c6 41.Ra5 h6 
42.Kg2 Rg8 43.a4 Rb8 44.Kh3 Ke6 45.Kh4 h5 46.Be2 Rh8 47.Ra7 cxb5 48.axb5 Kd6 49.Bd3 Rg8 
50.Rc5 Rf8 51.Bf1 Rb8 52.Bg2 Ng6+ 53.Kh3 Ne7 54.Bf3 Rh8 55.Be2 Kd7 56.Bd3 Kd6 57.Rc1 Rg8 
58.Ra5 Rb8 59.Kg2 Rg8 60.Kf3 Ke6 61.h4 Kd6 62.Rc5 Ke6 63.Ra2 Kd7 64.Ke2 Ke6 65.Kd2 Rh8 
66.Be2 Kd6 67.Bf3 Ke6 68.Ra7 Kd6 69.Kc3 Ke6 70.Kb3 f4 71.gxf4 Rd8 72.Ka4 Rb8 73.Bxh5 Nc8 
74.Ra5 Rd6 75.Rc7 Rd8 76.Bf3 Nb6+ 77.Kb4 Rdc8 78.Rh7 Rc2 79.Bg4+ Kd6 80.Rf7 Rxf2 81.Ra3 
1-0
```

## DarkThought

[WCCC 1995](/WCCC_1995 "WCCC 1995"), round 5, [DarkThought](/DarkThought "DarkThought") - Frenchess [[8]](#cite_note-8)

```
[Event "WCCC 1995"]
[Site "Shatin, Hong Kong - China"]
[Date "1995.05.29"]
[Round "5"]
[White "Dark Thought"]
[Black "Frenchess"]
[Result "0-1"]

1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.e3 e6 7.Bxc4 Bb4 8.O-O Nbd7 9.Nh4 Bg6 
10.Qb3 a5 11.g3 Qb6 12.Nxg6 hxg6 13.Rd1 O-O-O 14.Bf1 Rh5 15.Bg2 g5 16.f3 Rdh8 17.h3 
Rxh3 18.Bxh3 Rxh3 19.Ne2 g4 20.fxg4 Nxg4 21.e4 Rh2 22.Bf4 Rf2 23.Nc1 g5 24.Bxg5 Nde5 
25.Rd3 Nxd3 26.Qxd3 Be7 27.Qd1 Bxg5 28.Qxg4 Qxd4 0-1
```

# Publications

- [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), [Jean-Luc Seret](/Jean-Luc_Seret "Jean-Luc Seret"), [Michel Gondran](/Michel_Gondran "Michel Gondran") (**1995**). *Frenchess: A Cray T3D at the 8th World Computer Chess Championship*. First European Cray-T3D Workshop, [Citeseex](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.78.967)

# External Links

## Chess Program

- [Frenchess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=183)
- [A Short Story of JCW's Computer Chess Program](http://recherche.enac.fr/~weill/chess.html) by [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill")
- [Comp Frenchess chess games - 365Chess.com](http://www.365chess.com/players/Comp_Frenchess)

## Misc

- [French - Wiktionary](https://en.wiktionary.org/wiki/French)
- [French from Wikipedia](https://en.wikipedia.org/wiki/French)
- [Étude from Wikipedia](https://en.wikipedia.org/wiki/%C3%89tude)
- [Lee Ritenour](/Category:Lee_Ritenour "Category:Lee Ritenour") and [Paulinho da Costa](/Category:Paulinho_da_Costa "Category:Paulinho da Costa") - Etude, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   with [Anthony Jackson](/Category:Anthony_Jackson "Category:Anthony Jackson") and [Harvey Mason](https://en.wikipedia.org/wiki/Harvey_Mason), Live from [Coconuts Glove 1990](https://plus.google.com/+PeterBromberg/posts/B8EXoFjuZyQ)

# References

1. [↑](#cite_ref-1)  Les 25 plus grandes unité urbaines (agglomérations) françaises - 2010, by  [Monsieur Fou](https://commons.wikimedia.org/wiki/User:Monsieur_Fou), March 27, 2010, [France from Wikipedia](https://en.wikipedia.org/wiki/France)
2. [↑](#cite_ref-2) [Frenchess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=183)
3. [↑](#cite_ref-3) [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill") (**1995**). *Programmes d'Échecs de Championnat: Architecture Logicielle Synthèse de Fonctions d'Évaluations, Parallélisme de Recherche*. Ph.D. Thesis, [Université Paris 8](/University_of_Paris#8 "University of Paris"), Saint-Denis, [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/phdJCW.ps.gz) (French)
4. [↑](#cite_ref-4) [shmem\_swap(3) man page (version 3.0.2)](https://www.open-mpi.org/doc/v3.0/man3/shmem_swap.3.php)
5. [↑](#cite_ref-5) [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), [Jean-Luc Seret](/Jean-Luc_Seret "Jean-Luc Seret"), [Michel Gondran](/Michel_Gondran "Michel Gondran") (**1995**). *Frenchess: A Cray T3D at the 8th World Computer Chess Championship*. First European Cray-T3D Workshop, [Citeseex](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.78.967)
6. [↑](#cite_ref-6) [Shatin 1995 - Chess - Round 2 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=29&round=2&id=2)
7. [↑](#cite_ref-7) [Marc-François Baudot](/Marc-Fran%C3%A7ois_Baudot "Marc-François Baudot"), [Jean-Christophe Weill](/Jean-Christophe_Weill "Jean-Christophe Weill"), [Jean-Luc Seret](/Jean-Luc_Seret "Jean-Luc Seret"), [Michel Gondran](/Michel_Gondran "Michel Gondran") (**1995**). *Frenchess: A Cray T3D at the 8th World Computer Chess Championship*. First European Cray-T3D Workshop, [Citeseex](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.78.967)
8. [↑](#cite_ref-8) [Shatin 1995 - Chess - Round 5 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=29&round=5&id=3)

**[Up one Level](/Engines "Engines")**