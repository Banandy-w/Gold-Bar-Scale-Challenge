# Gold-Bar-Scale-Challenge
This program solves the following challenge:

Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar,
but you know they all weigh the same, except for one fake bar. It weighs less than others. You need to find the fake
gold bar by only bars and balance scales.
You can only place gold bars on scale plates (bowls) and find which scale weighs more or less.

Website http://sdetchallenge.fetch.com/ allows you to simulate the scaling process. You can write gold bar number(s)
in left and right bowl grids. Press the “Weigh” button and it will tell you which side weighs more or less or the same.
The weighing result will be shown in the “Weighing” list so you can track records.
After you are done with one weighing you can press the “Reset” button to reset the plates grid to empty values so you
can do another weighing.
When you find the fake gold bar click on the button with a number corresponding to the fake gold bar at the bottom of
the screen and check if you were right or wrong: an alert will pop up with two possible messages: “Yay! You found it!”
or “Oops! Try Again!”.

NOTE: Do not refresh the page as it will reset the fake bar to a random

NOTE: Buttons at the bottom with numbers DO NOT represent weights. It’s just the sequential number.

## Requirements / Prereqs
* [Mozilla browser](https://www.mozilla.org/en-US/firefox/new/) or [Microsft Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FJ) or [Google Chrome](https://www.google.com/chrome/) installed
* [Python 3.12.3](https://www.python.org/downloads/)
# Packages used
* [Selenium 4.20.0](https://pypi.org/project/selenium/#files)
* Math, Time, Sys

## How to run. After installing python with pip.
1. Open a command line terminal
2. Install selenium with if it is not already installed.
```
pip install selenium
```
3. Fork this project
4. On your terminal
```
cd path\to\this\forked\project
```
5. Run the program with the command below. Replace browser with "edge", "firefox", "chrome", or "safari" to test with the respective browser. This is not case sensitive and not tested on safari.
```
python .\BalanceAutomation.py browser
#EG python .\BalanceAutomation.py firefox
```
