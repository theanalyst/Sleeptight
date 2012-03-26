#Sleeptight
Python implementation of [sleepyti.me](http://sleepyti.me) inspired by
[yawn](http://github.com/jico/yawn) 

#Usage
Optimal sleep requires 5-6 sleep cycles, and sleepyti.me calculates in
terms of sleep cycles the optimal time for sleeping/waking up. 

If you plan to hit the sack right now just run
`python sleeptight.py` 
and get the optimal times to set your alarm

For waking up at a specific time run with `-wHH:MM(AM/PM)` switch
`python sleeptight.py -w06:30AM`

Also if you plan to sleep at a specified time, the optimal wake up
time is calculated as 
`python sleeptight.py -t11:00PM`
A 14 minute average time is assumed to fall asleep. 
