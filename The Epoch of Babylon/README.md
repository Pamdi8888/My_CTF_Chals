# The Epoch of Babylon

## Description
When I was going through MogamBro's PC, I found something strange in his calender application. Either he is a really busy person with lots of scheduled reminders, or maybe he is hiding something. I suspect it's the latter. I've attached the [file](timestamps.txt) containing the timestamps of all his reminders. Find out the secrets that MogamBro is hiding within them.
### Hint
Stuck?? Maybe you should try looking for answers in a library of some sort....

## Solution
We observe that the timestamps are in the format `YYYY-MM-DD HH:MM:SS`. We can convert the timestamps to epoch time using a python script.
When we append all the epoch times, we get one big number. We have done this in [solve.py](solve.py). <br>
The title (Babylon) and the hint (library) suggest that we should look for the flag in Library of Babylon. The Library of Babylon
has image archives where every image is addressed using a big number. When we check image at the address of the big number we got,
we get the following image with the flag in it. <br>

## Flag
```BITSCTF{53XY_M3RCH}```

## Author
[Pamdi](https://github.com/pamdi8888)
