# Visualisation-of-Lsystem
## Overview
This app is a simple visualisation of L system.
It has these flags:
* "+" - rotate by angle
* "-" - back rotate by angle
* "|" - rotate by 180 degrees
* "f" - move forward
* "F" - move and draw forward
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

![Example](https://downloader.disk.yandex.ru/preview/eba1d484f686a8211584d53dd42b64efdb43d92f4ae7b273306d7c1499efdab0/61e185a8/R6wRjfrkRQUazQCE3JjnfsMu00Qn7GYXNmndteD0PKM3ijEVkPkMgcwHMIUaluSQh2XA7Z60ZhXrx--IpT6veg%3D%3D?uid=0&filename=2022-01-14_13-15-10.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x1333)

