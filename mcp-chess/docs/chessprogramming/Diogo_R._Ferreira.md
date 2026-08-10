# Diogo R. Ferreira

Source: https://www.chessprogramming.org/Diogo_R._Ferreira

**[Home](/Main_Page "Main Page") \* [People](/People "People") \* Diogo R. Ferreira**

[![](/images/a/a4/DiogoRFerreira.jpg)](http://web.ist.utl.pt/diogo.ferreira/)

Diogo R. Ferreira [[1]](#cite_note-1)

**Diogo R. Ferreira**,  
a Portuguese computer scientist and professor of [Information systems](https://en.wikipedia.org/wiki/Information_systems) at [Instituto Superior Técnico](https://en.wikipedia.org/wiki/Instituto_Superior_T%C3%A9cnico), [Technical University of Lisbon](https://en.wikipedia.org/wiki/Technical_University_of_Lisbon).
His research interests include [data science](https://en.wikipedia.org/wiki/Data_science), [deep learning](/Deep_Learning "Deep Learning"), [GPU](/GPU "GPU") computing, [data mining](https://en.wikipedia.org/wiki/Data_mining) and [process mining](https://en.wikipedia.org/wiki/Process_mining) applied to [nuclear fusion](https://en.wikipedia.org/wiki/Nuclear_fusion), [plasma](https://en.wikipedia.org/wiki/Plasma_(physics)) [tomography](https://en.wikipedia.org/wiki/Tomography), and [disruption](https://en.wikipedia.org/wiki/Disruption) [prediction](https://en.wikipedia.org/wiki/Prediction) [[2]](#cite_note-2).

# Chess Ratings

In 2010, Diogo R. Ferreira participated on a chess ratings competition offered by [Kaggle](https://en.wikipedia.org/wiki/Kaggle) [[3]](#cite_note-3) and made it to 4th place [[4]](#cite_note-4) . His approach is based on the [Bradley-Terry model](https://en.wikipedia.org/wiki/Pairwise_comparison), but with a slightly different interpretation of what the [strength](/Playing_Strength "Playing Strength") of a player is, and with a custom procedure for estimating that strength [[5]](#cite_note-5) . In his [ICGA Journal](/ICGA_Journal "ICGA Journal") paper, *Determining the Strength of Chess Players based on actual Play* [[6]](#cite_note-6) , Ferreira elaborates on strength estimation based on a per move basis with the help of a strong chess program and distribution of gain. A gain was defined by the [score](/Score "Score") difference of [Houdini's 1.5](/Houdini "Houdini") fixed depth 20 ply search of all consecutive positions along the game-record, alternating assigned to the player who made the move. Four algorithms for different purposes were defined:

1. Determine the relative strength between two players i and j.
2. Determine the relative strength of each player i, in terms of a perceived Elo rating r'i for a set of players in a tournament, where the actual Elo ratings ri are known.
3. Determine the engine strength based on the rating differences between the engine and a set of players whose Elo ratings and/or perceived ratings are known.
4. Determine the strength of a player after a number of moves, based on the rating difference between player and engine, when an estimate of engine strength is available.

Ratings of various chess players and programs were estimated based on the distribution of gains from various games, [The Game of the Century](https://en.wikipedia.org/wiki/The_Game_of_the_Century_%28chess%29) between [Donald Byrne](https://en.wikipedia.org/wiki/Donald_Byrne) and the 13 year old [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) was given as sample for algorithm 1 with game score differences, yielding in a rating difference of 113 points in favor to Fischer. The [London Chess Classic 2011](https://en.wikipedia.org/wiki/London_Chess_Classic#2011_Classic:_3-12_December) [[7]](#cite_note-7) [[8]](#cite_note-8) was used as sample for algorithm 2 and 3, while algorithm 4 was applied for [Kasparov versus Deep Blue 1997](/Kasparov_versus_Deep_Blue_1997 "Kasparov versus Deep Blue 1997"), which, despite [Garry Kasparov](/Garry_Kasparov "Garry Kasparov") lost the match, did result in a higher rating for him - 2754 versus 2741 for [Deep Blue](/Deep_Blue "Deep Blue").

# Selected Publications

[[9]](#cite_note-9)
[[10]](#cite_note-10) [[11]](#cite_note-11)

## 2000 ...

- Diogo R. Ferreira (**2004**). *Workflow Management Systems Supporting the Engineering of Business Networks*. Ph.D. Thesis
- Diogo R. Ferreira, [Daniel Gillblad](https://dblp.uni-trier.de/pers/hd/g/Gillblad:Daniel) (**2009**). *[Discovering Process Models from Unlabelled Event Logs](https://github.com/diogoff/unlabelled-event-logs)*. [BPM 2009](https://dblp.uni-trier.de/db/conf/bpm/bpm2009.html)

## 2010 ...

- [Michal Walicki](http://www.ii.uib.no/~michal/), Diogo R. Ferreira (**2010**). *Mining Sequences for Patterns with Non-Repeating Symbols*. IEEE Congress on Evolutionary Computation
- Diogo R. Ferreira (**2010**). *[Predicting the Outcome of Chess Games based on Historical Data](http://web.ist.utl.pt/diogo.ferreira/chess/)*. [IST](https://en.wikipedia.org/wiki/Instituto_Superior_T%C3%A9cnico) - [Technical University of Lisbon](https://en.wikipedia.org/wiki/Technical_University_of_Lisbon)
- [Michal Walicki](http://www.ii.uib.no/~michal/), Diogo R. Ferreira (**2011**). *[Sequence partitioning for process mining with unlabeled event logs](https://github.com/diogoff/sequence-partitioning)*. [Data & Knowledge Engineering](https://www.journals.elsevier.com/data-and-knowledge-engineering), Vol. 70, No. 10
- Diogo R. Ferreira (**2012**). *[Performance Analysis of Healthcare Processes through Process Mining](https://ercim-news.ercim.eu/en89/special/performance-analysis-of-healthcare-processes-through-process-mining)*. [RCIM News 2012](https://dblp.uni-trier.de/db/journals/ercim/ercim2012.html)
- Diogo R. Ferreira (**2012**). *Determining the Strength of Chess Players based on actual Play*. [ICGA Journal, Vol. 35, No. 1](/ICGA_Journal#35_1 "ICGA Journal") » [Match Statistics](/Match_Statistics "Match Statistics"), [Houdini](/Houdini "Houdini")
- Diogo R. Ferreira (**2013**). *The Impact of the Search Depth on Chess Playing Strength*. [ICGA Journal, Vol. 36, No. 2](/ICGA_Journal#36_2 "ICGA Journal") » [Depth](/Depth "Depth"), [Diminishing Returns](/Depth#DiminishingReturns "Depth"), [Match Statistics](/Match_Statistics "Match Statistics"), [Playing Strength](/Playing_Strength "Playing Strength"), [Houdini](/Houdini "Houdini") [[12]](#cite_note-12)
- Diogo R. Ferreira, [Rui M. Santos](https://dblp.uni-trier.de/pers/hd/s/Santos:Rui_M=) (**2016**). *[Parallelization of Transition Counting for Process Mining on Multi-core CPUs and GPUs](https://github.com/diogoff/transition-counting-gpu)*. [BPM 2016](https://dblp.uni-trier.de/db/conf/bpm/bpmw2016.html)
- [Francisco A. Matos](https://www.researchgate.net/profile/Francisco_Matos3), Diogo R. Ferreira, [Pedro J. Carvalho](https://www.researchgate.net/profile/P_Carvalho2), [JET](https://en.wikipedia.org/wiki/Joint_European_Torus) Contributors (**2017**). *Deep learning for plasma tomography using the bolometer system at JET*. [arXiv:1701.00322](https://arxiv.org/abs/1701.00322)
- Diogo R. Ferreira, [Pedro J. Carvalho](https://www.researchgate.net/profile/P_Carvalho2), [Horácio Fernandes](https://scholar.google.be/citations?user=fkoOZ80AAAAJ&hl=en), [JET](https://en.wikipedia.org/wiki/Joint_European_Torus) Contributors (**2018**). *Full-pulse Tomographic Reconstruction with Deep Neural Networks*. [arXiv:1802.02242](https://arxiv.org/abs/1802.02242)

# External Links

- [Diogo R. Ferreira | IST - Technical University of Lisbon](http://web.ist.utl.pt/diogo.ferreira/)
- [diogoff (Diogo R. Ferreira) · GitHub](https://github.com/diogoff)
- [How I did it: Diogo Ferreira on 4th place in Elo chess ratings competition | no free hunch](http://blog.kaggle.com/2010/11/30/how-i-did-it-diogo-ferreira-on-4th-place-in-elo-chess-ratings-competition/)
- [Inteview: Discover the Methodology and Mindset of a Kaggle Master](https://machinelearningmastery.com/discover-the-methodology-and-mindset-of-a-kaggle-master-an-interview-with-diogo-ferreira/), Interview with Diogo R. Ferreira by [Jason Brownlee](https://machinelearningmastery.com/about/), October 3, 2014

# References

1. [↑](#cite_ref-1) [Diogo R. Ferreira | IST - Technical University of Lisbon](http://web.ist.utl.pt/diogo.ferreira/)
2. [↑](#cite_ref-2) [Diogo R. Ferreira | IST - Technical University of Lisbon | Research Areas](http://web.ist.utl.pt/diogo.ferreira/#research)
3. [↑](#cite_ref-3) [Chess ratings - Elo versus the Rest of the World - Kaggle](http://www.kaggle.com/c/chess)
4. [↑](#cite_ref-4) [How I did it: Diogo Ferreira on 4th place in Elo chess ratings competition | no free hunch](http://blog.kaggle.com/2010/11/30/how-i-did-it-diogo-ferreira-on-4th-place-in-elo-chess-ratings-competition/)
5. [↑](#cite_ref-5) Diogo R. Ferreira (**2010**). *[Predicting the Outcome of Chess Games based on Historical Data](http://web.ist.utl.pt/diogo.ferreira/chess/)*. [IST](https://en.wikipedia.org/wiki/Instituto_Superior_T%C3%A9cnico) - [Technical University of Lisbon](https://en.wikipedia.org/wiki/Technical_University_of_Lisbon)
6. [↑](#cite_ref-6) Diogo R. Ferreira (**2012**). *Determining the Strength of Chess Players based on actual Play*. [ICGA Journal, Vol. 35, No. 1](/ICGA_Journal#35_1 "ICGA Journal")
7. [↑](#cite_ref-7) [London Chess Classic 2011](http://www.chess.co.uk/twic/chessnews/events/london-chess-classic-2011) | [The Week in Chess](https://en.wikipedia.org/wiki/The_Week_in_Chess)
8. [↑](#cite_ref-8) [London R9: Vlad All Over](http://www.chessbase.com/newsdetail.asp?newsid=7754), [ChessBase News](/ChessBase "ChessBase"), December 13, 2011
9. [↑](#cite_ref-9) [Diogo R. Ferreira | IST - Technical University of Lisbon | Publications](http://web.ist.utl.pt/diogo.ferreira/#publications)
10. [↑](#cite_ref-10) [dblp: Diogo R. Ferreira](https://dblp.uni-trier.de/pers/hd/f/Ferreira:Diogo_R=)
11. [↑](#cite_ref-11) [Diogo R. Ferreira - Google Scholar Citations](https://scholar.google.com/citations?user=CSEqKy8AAAAJ&hl=en)
12. [↑](#cite_ref-12) [Ply versus ELO](https://www.hiarcs.net/forums/viewtopic.php?t=10004) by Greg, [HIARCS Forum](/Computer_Chess_Forums "Computer Chess Forums"), May 30, 2020

**[Up one level](/People "People")**