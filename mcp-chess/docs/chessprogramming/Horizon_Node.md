# Horizon Node

Source: https://www.chessprogramming.org/Horizon_Node

**[Home](/Main_Page "Main Page") \* [Search](/Search "Search") \* [Node](/Node "Node") \* Horizon Node**

**Horizon nodes** are [nodes](/Node "Node") at [depth](/Depth "Depth") zero, where a [quiescence search](/Quiescence_Search "Quiescence Search") is performed. The definition is taken from the papers of [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") [[1]](#cite_note-1) depth == 0 nodes [[2]](#cite_note-2). If the horizon node is an expected [Cut-Node](/Node_Types#CUT "Node Types"), confirmed by the evaluated [standing pat](/Quiescence_Search#StandPat "Quiescence Search") [score](/Score "Score") already greater or equal than [beta](/Beta "Beta"), the horizon node is a [leaf](/Leaf_Node "Leaf Node") with the [lower bound](/Lower_Bound "Lower Bound") score of beta ([fail-hard](/Fail-Hard "Fail-Hard")) or the stand pat score ([fail-soft](/Fail-Soft "Fail-Soft")). Otherwise, winning captures (or checks) may either cause a [beta-cutoff](/Beta-Cutoff "Beta-Cutoff") or raise [alpha](/Alpha "Alpha") with an [exact score](/Exact_Score "Exact Score") at [PV-Nodes](/Node_Types#PV "Node Types"). At expected [All-Nodes](/Node_Types#ALL "Node Types") with evaluated score (far) below alpha, if no [tactical move](/index.php?title=Tactical_moves&action=edit&redlink=1 "Tactical moves (page does not exist)") is available, or due to [Delta Pruning](/Delta_Pruning "Delta Pruning") good enough to raise alpha, those [leaves](/Leaf_Node "Leaf Node") return alpha ([fail-hard](/Fail-Hard "Fail-Hard")) as an [upper bound](/Upper_Bound "Upper Bound"). This may also appear, if this horizon node was not a leaf, since some captures were not pruned, but tried without raising alpha.

# Horizon Observatory

[![Hoheward-Panorama.jpg](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Hoheward-Panorama.jpg/1280px-Hoheward-Panorama.jpg)](/File:Hoheward-Panorama.jpg)

[Horizon Observatory](https://de.wikipedia.org/wiki/Halde_Hoheward#Horizontobservatorium) (left) and horizontal [Sundial](https://en.wikipedia.org/wiki/Sundial) with [Obelisk](https://en.wikipedia.org/wiki/Obelisk) (right), [Hoheward Spoil tip](https://de.wikipedia.org/wiki/Halde_Hoheward), [The Industrial Heritage Trail](/Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") [[3]](#cite_note-3)

# See also

- [Frontier Nodes](/Frontier_Nodes "Frontier Nodes")
- [Horizon Effect](/Horizon_Effect "Horizon Effect")
- [Leaf Node](/Leaf_Node "Leaf Node")
- [Quiescent Node](/Quiescent_Node "Quiescent Node")

# External Links

- [Karl Jenkins](/Category:Karl_Jenkins "Category:Karl Jenkins") - [In These Stones Horizons Sing](https://en.wikipedia.org/wiki/In_These_Stones_Horizons_Sing) (4th movement), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

:   Commissioned for the opening of [Wales Millennium Centre](https://en.wikipedia.org/wiki/Wales_Millennium_Centre), first performed at its opening on November 29, 2004

# References

1. [↑](#cite_ref-1) [Ernst A. Heinz](/Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended futility pruning](http://people.csail.mit.edu/heinz/dt/node18.html)*. [ICCA Journal, Vol. 21, No 2](/ICGA_Journal#21_2 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/ext_fut.ps.gz)
2. [↑](#cite_ref-2) [Re: simple node definitions question](https://www.stmintz.com/ccc/index.php?id=387518) by [Robert Hyatt](/Robert_Hyatt "Robert Hyatt"), [CCC](/Computer_Chess_Forums "Computer Chess Forums"), September 13, 2004
3. [↑](#cite_ref-3) 360–degree [Panorama](https://en.wikipedia.org/wiki/Panorama) Photo by [Panofreak](https://commons.wikimedia.org/wiki/User:Panofreak), April 12, 2009, [Hoheward Spoil tip](https://de.wikipedia.org/wiki/Halde_Hoheward) in [Herten](https://en.wikipedia.org/wiki/Herten), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), Germany, [The Industrial Heritage Trail](/Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") , view over the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr). The observatory consists of a circular, flat surface of 88 m diameter, and a center forum lowered by 1.50 m with 35 m diameter with two arcs spanning [meridian](https://en.wikipedia.org/wiki/Meridian_%28astronomy%29) and [celestial equator](https://en.wikipedia.org/wiki/Celestial_equator). The horizon observatory is a modern version of [prehistoric](https://en.wikipedia.org/wiki/Prehistory) [stone circles](https://en.wikipedia.org/wiki/Stone_circle) and monuments such as [Stonehenge](https://en.wikipedia.org/wiki/Stonehenge). If the observer is located exactly in the lowered center, the plateau of the tip spreads in all directions like an artificial horizon, and with the help of bearing points the [sunrise](https://en.wikipedia.org/wiki/Sunrise) and [sunset](https://en.wikipedia.org/wiki/Sunset) at [summer solstice](https://en.wikipedia.org/wiki/Summer_solstice), [winter solstice](https://en.wikipedia.org/wiki/Winter_solstice) or [equinox](https://en.wikipedia.org/wiki/Equinox) can be observed, by means of further bearing points also [moon](https://en.wikipedia.org/wiki/Moon) solstices and the [precession](https://en.wikipedia.org/wiki/Precession) of [Earth's axis](https://en.wikipedia.org/wiki/Earth%27s_rotation) based on bearings of [fixed stars](https://en.wikipedia.org/wiki/Fixed_stars). The arcs divide the [celestial sphere](https://en.wikipedia.org/wiki/Celestial_sphere) in eastern and western half as well as in [northern](https://en.wikipedia.org/wiki/Northern_Hemisphere) and [southern hemisphere](https://en.wikipedia.org/wiki/Southern_Hemisphere) and therefore serve as a [solar calendar](https://en.wikipedia.org/wiki/Solar_calendar) at day, and at night, with the help of a [self-luminous](https://en.wikipedia.org/wiki/Luminous_paint) scale as a guide of the [night sky](https://en.wikipedia.org/wiki/Night_sky), [Halden im Ruhrgebiet](http://www.halden.ruhr/halden.html) (German)

**[Up one Level](/Node "Node")**