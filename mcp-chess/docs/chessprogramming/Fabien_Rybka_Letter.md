# Fabien Rybka Letter

Source: https://www.chessprogramming.org/Fabien_Rybka_Letter

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* Open Letter**

Open letter by [Fabien Letouzey](/Fabien_Letouzey "Fabien Letouzey"), January 23, 2011 [[1]](#cite_note-1)

---

Hello,

Long time no see.

First, I am not back to computer chess, sorry about that. I just want to clarify a few things. Sorry if that's old but there is some misunderstanding I need to fix, and I found out only yesterday. Bear in mind that I am mostly unaware of what has happened for five years though.

First there was the [Strelka](/Strelka "Strelka") case. [Dann](/Dann_Corbit "Dann Corbit") approached me with some "Strelka" source code for me to check. I had never heard of it. I assumed it was some closed-source free engine and that people wanted to know whether it was based on the [Fruit](/Fruit "Fruit") source code.

The short answer was "no", it was not a verbatim copy of the source code. All the code had been typed (can't say "designed" though, see below) by an individual. So legally there was no issue that I knew of. It was however a whole re-write (copy with different words if you like, similar to a translation) of the algorithms. Not just an extraction of a couple of ideas as is common, and normal.

That being said, some original changes and ideas were also included in the program. So it was, as has since been stated many times in fora I suppose, a bitboard re-write of Fruit with some personal (or otherwise) ideas. Also note that the source code Dann sent me might not be the from the 2.0 version.

Edit: I've just had a look at the 2.0 sources. On top of what I said above, there are many constant and function names that are identical to Fruit's. I remember noticing it back then as well.

Hope it helps, because my email answer to Dann was unusually short and cryptic even by my standards. And Dann, please next time make it clear when you want a public statement instead of a private opinion, thanks.

I want to point out something immediately: there was no mention of [Rybka](/Rybka "Rybka") whatsoever. Indeed I was unaware of any relation between Strelka and Rybka, this is precisely what I learned only yesterday. I insist because it seems I have often been quoted about "not caring" about the (possible) Fruit/Rybka relationship, but this is not so. Strelka did not look like a problem because I assumed it was free.

Next, I was approached by [Ryan](/Ryan_Benitez "Ryan Benitez") (I think) and [Christophe Theron](/Christophe_Th%C3%A9ron "Christophe Théron") about whether I could help with some "possible Fruit code inside Rybka" issues. I answered "yes, but how?", but did not get a reply. This did not make me really aware of a clone possibility however because I thought they were talking about some insignificant UCI-handling code or whatnot. Also this was several years after the initial Rybka release, and I guess quite a few people had a close look at it. Apparently [Chrilly](/Chrilly_Donninger "Chrilly Donninger") did?

Now if someone could tell me a bit more about the major events last five years and the current state of affairs, I'd be much obliged.

A few things I noticed yesterday, can you confirm?
- Rybka search info was obfuscated in some way (like displaying depth-3 or something), any pointers on details please?
- [Vasik](/Vasik_Rajlich "Vasik Rajlich") claimed that Strelka 2.0 is a clone of Rybka 1.0 (and you know what that would imply!)
- [Zach Wegner](/Zach_Wegner "Zach Wegner") found many Fruit ideas (and nearly identical code) in Rybka 1.0; I think someone else did, too
- Some even stronger open-source program appeared as a decompilation of Rybka (with own ideas, sounds familiar), what came up of looking at those?

Any questions, now is the one time to ask.

Thanks for your attention,

Fabien Letouzey

# References

1. [↑](#cite_ref-1) [Fabien's open letter to the community](http://www.talkchess.com/forum/viewtopic.php?t=37762) by [Tord Romstad](/Tord_Romstad "Tord Romstad"), [CCC](/CCC "CCC"), January 23, 2011

**[Up one level](/ICGA_Investigations "ICGA Investigations")**