# Visualisation-of-Lsystem
## Overview
This app is a simple visualisation of L system.
It has these flags:
* "+" - rotate by angle
* "-" - back rotate by angle
* "|" - rotate by 180 degrees
* "f" - move forward
* "F" - move forward and draw
* "[" - save current position
* "]" - restore remembered position

You could read more about L systems here:

[[RUS]](http://mech.math.msu.su/~shvetz/54/inf/perl-problems/chLSystems.xhtml#chLSystems_sCommons)

[[ENG]](https://en.wikipedia.org/wiki/L-system)
## Setup
install requirements:
```
 pip install -r requirements.txt
```
## Start
First of all make .txt file with data about L system
like this:
* angle - angle to rotate by "+" and "-"
* axiom
* rule1
* rule2
* ...
* ruleN

## Example
The dragon curve

90<br>
XY<br>
X->X+YF<br>
Y->FX-Y<br>

![Example](https://drive.google.com/uc?export=view&id=13BJXy3gV6pq5yLWU8UtR3exLMNJOBqdF)

