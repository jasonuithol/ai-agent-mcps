# Zeta

Source: https://www.chessprogramming.org/Zeta

**[Home](/Main_Page "Main Page") \* [Engines](/Engines "Engines") \* Zeta**

[![](/images/9/91/Zetalogo.png)](/File:Zetalogo.png)

Zeta Logo

**Zeta**, (Zeta OpenCL Chess)  
an experimental [open source chess engine](/Category:Open_Source "Category:Open Source") by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), written in [OpenCL](/OpenCL "OpenCL"). The engine has been in development since 2010 and was first released July 13, 2011 under the [GNU GPL](/Free_Software_Foundation#GPL "Free Software Foundation"), later MIT license.
Zeta supports some basic commands of the [Chess Engine Communication Protocol](/Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](/WinBoard "WinBoard") and [XBoard](/XBoard "XBoard").
It features [Quad-Bitboards](/Quad-Bitboards "Quad-Bitboards"), and its ability to run on a [GPU](/GPU "GPU").

# Features v099

- C99 (host) + OpenCL 1.x (device)
- XBoard (CECP v2) protocol
- Quad-Bitboards board presentation
- vectorized Kogge-Stone move generation
- RMO parallel AlphaBeta search
- Simplified Evaluation Function
- 64 gpu-threads are coupled to one worker, to work on the same node in parallel during move generation, selection and evaluation
- MIT license

# Features v097-v098

- C99 (host) + OpenCL 1.x (device)
- XBoard (CECP v2) protocol
- Quad-Bitboards board presentation
- vectorized Kogge-Stone move generation
- parallel Best-First Minimax Search
- Simplified Evaluation Function
- one thread one board, with thousands of threads working together on the search tree stored in VRAM
- GPL license

# Origins Ideas

- [Quad-Bitboards](/Quad-Bitboards "Quad-Bitboards") idea by [Gerd Isenberg](/Gerd_Isenberg "Gerd Isenberg")
- [Kogge-Stone Algorithm](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") move generator based on work by [Steffan Westcott](/Steffan_Westcott "Steffan Westcott")
- RMO parallel search[[1]](#cite_note-1) as mix in from [ABDADA](/ABDADA "ABDADA") and Radomized Best-First-MiniMax[[2]](#cite_note-2)
- parallel [Best-First Minimax Search](/Best-First_Minimax_Search "Best-First Minimax Search") search inspired by Radomized Best-First-MiniMax[[3]](#cite_note-3)

# Origins Code

- [Simplified Evaluation Function](/Simplified_Evaluation_Function "Simplified Evaluation Function") based on proposal by [Tomasz Michniewski](/Tomasz_Michniewski "Tomasz Michniewski")

# See also

- [Zeta Dva](/Zeta_Dva "Zeta Dva")

# Forum Posts

## 2010 ...

- [Zeta, a chess engine in OpenCL](http://www.talkchess.com/forum/viewtopic.php?t=33315) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), March 17, 2010
- [Possible Board Presentation and Move Generation for GPUs?](http://www.talkchess.com/forum/viewtopic.php?t=38478) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), March 19, 2011
- [Zeta plays chess on a gpu](http://www.talkchess.com/forum/viewtopic.php?t=39459) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), June 23, 2011
- [LIFO stack based parallel processing?](http://www.talkchess.com/forum/viewtopic.php?t=40493) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), September 22, 2011
- [Possible Search Algorithms for GPUs?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=442052&t=41853) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), January 07, 2012 [[4]](#cite_note-4) [[5]](#cite_note-5)
- [Help with Best-First Select-Formula](http://www.talkchess.com/forum/viewtopic.php?t=44165) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), June 23, 2012
- [Kogge Stone, Vector Based](http://www.talkchess.com/forum/viewtopic.php?t=46974) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), January 22, 2013 » [Kogge-Stone Algorithm](/Kogge-Stone_Algorithm "Kogge-Stone Algorithm") [[6]](#cite_note-6) [[7]](#cite_note-7)
- [GPU chess update, local memory...](http://www.talkchess.com/forum/viewtopic.php?t=60386) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), June 06, 2016
- [RMO - Randomized Move Order - yet another Lazy SMP derivate](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72684) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), December 30, 2019 » [Lazy SMP](/Lazy_SMP "Lazy SMP")

## 2020 ...

- [Zeta with NNUE on GPU?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76986) by [Srdja Matovic](/Srdja_Matovic "Srdja Matovic"), [CCC](/CCC "CCC"), March 31, 2021 » [NNUE](/NNUE "NNUE"), [GPU](/GPU "GPU")

# External Links

## Chess Engine

- [GitLab - smatovic/Zeta: Experimental chess engine written in OpenCL](https://gitlab.com/smatovic/Zeta)
- [Zeta Chess blog](https://zeta-chess.app26.de/)
- [Zeta - Milestones](https://zeta-chess.app26.de/post/zeta-milestones/)

## Misc

- [Zeta from Wikipedia](https://en.wikipedia.org/wiki/Zeta)
- [Zeta (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Zeta_(disambiguation))
- [Zeta distribution from Wikipedia](https://en.wikipedia.org/wiki/Zeta_distribution)
- [Riemann zeta function from Wikipedia](https://en.wikipedia.org/wiki/Riemann_zeta_function)
- [List of zeta functions from Wikipedia](https://en.wikipedia.org/wiki/List_of_zeta_functions)

**[Up one level](/Engines "Engines")**

1. [↑](#cite_ref-1) [RMO - Randomized Move Order - yet another Lazy SMP derivate](https://talkchess.com/viewtopic.php?t=72684)
2. [↑](#cite_ref-2) [Parallel Randomized Best-First Minimax Search](http://www.cs.tau.ac.il/~stoledo/Pubs/rbf-ai.pdf)
3. [↑](#cite_ref-3) [Parallel Randomized Best-First Minimax Search](http://www.cs.tau.ac.il/~stoledo/Pubs/rbf-ai.pdf)
4. [↑](#cite_ref-4) [Yaron Shoham](/index.php?title=Yaron_Shoham&action=edit&redlink=1 "Yaron Shoham (page does not exist)"), [Sivan Toledo](/index.php?title=Sivan_Toledo&action=edit&redlink=1 "Sivan Toledo (page does not exist)") (**2002**). *[Parallel Randomized Best-First Minimax Search](https://www.sciencedirect.com/science/article/pii/S0004370202001959)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 137, Nos. 1-2
5. [↑](#cite_ref-5) [Alberto Maria Segre](/Alberto_Maria_Segre "Alberto Maria Segre"), [Sean Forman](/index.php?title=Sean_Forman&action=edit&redlink=1 "Sean Forman (page does not exist)"), [Giovanni Resta](/index.php?title=Giovanni_Resta&action=edit&redlink=1 "Giovanni Resta (page does not exist)"), [Andrew Wildenberg](/index.php?title=Andrew_Wildenberg&action=edit&redlink=1 "Andrew Wildenberg (page does not exist)") (**2002**). *[Nagging: A Scalable Fault-Tolerant Paradigm for Distributed Search](https://www.sciencedirect.com/science/article/pii/S000437020200228X)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 140, Nos. 1-2
6. [↑](#cite_ref-6) [Parallel Thread Execution from Wikipedia](https://en.wikipedia.org/wiki/Parallel_Thread_Execution)
7. [↑](#cite_ref-7) NVIDIA Compute PTX: Parallel Thread Execution, ISA Version 1.4, March 31, 2009, [pdf](https://www.nvidia.com/content/CUDA-ptx_isa_1.4.pdf)