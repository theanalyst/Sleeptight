#!/usr/bin/python
import argparse
import datetime
from datetime import timedelta
from datetime import datetime

# Some Global Definitions
SleepCycleTime = 90 
sleepCycles = (1,7)
wakeCycles  = (3,7) #Assumes a minimal 2 cycle sleep before waking up
dozeTime = 14
day_str  = datetime.today().strftime("%Y-%m-%d")

def CalculateCycles(tstart,sleep,countCycles):
# Calculate the sleep cycles required given a sleeptime 
     cycle = timedelta(minutes = SleepCycleTime)
     doze  = timedelta(minutes = dozeTime)
     SleepCycles = [cycle*i for i in range(*countCycles)]
     tstart = tstart + doze
     if sleep is True:
         return [(tstart+epoch).strftime("%I:%M %p")for epoch in SleepCycles]
     else:
         return [(tstart-epoch).strftime("%I:%M %p")for epoch in SleepCycles]

SleepNow = lambda sleeptime: CalculateCycles(sleeptime,True,sleepCycles)
WakeUp   = lambda waketime : CalculateCycles(waketime,False,wakeCycles)     

def init_parser():
     parser = argparse.ArgumentParser(
     prog = 'sleeptight',
     conflict_handler = 'resolve',
     description = ("sleepyti.me based bedtime calculator" 
     "Find the best time to set the alarm when you hit the sacks or "
     "find the best time to sleep in order to wake up when you desire"),
     epilog = "Sleep Tight :) zzzz....")

     parser.add_argument('-w','--wake', type = str, nargs = '?',
                         help="Wake Up Time HH:MM(AM/PM) eg. 06:00AM ")
     parser.add_argument('-n','--now',type = str, nargs = '?',
                         help="Sleep now, find the wake up time" 
     "if you hit the sacks now,assumes you doze off in an avg 14 minutes") 
     parser.add_argument('-t','--time',type = str, nargs = '?',
                         help="Find out the wake up time when you sleep at"
     "time HH:MM(AM/PM) eg 11:00PM")
     parser.set_defaults(now = True)
     args = parser.parse_args()
     return args

if __name__ == "__main__":
     args = init_parser()
     if args.wake:
          waketime = datetime.strptime(args.wake+day_str,"%I:%M%p%Y-%m-%d")
          print "Try falling asleep at these times in order to wake up refreshed"
          print "\n".join(WakeUp(waketime))
     elif args.time:
          print "Optimal Wake up times considering a 14 min avg. to doze off"
          sleeptime = datetime.strptime(args.time+day_str,"%I:%M%p%Y-%m-%d")
          print "\n".join(SleepNow(sleeptime))
     elif args.now:
          print "Wake up at these times (assumes an avg. 14 minutes to doze off)"
          sleeptime = datetime.now()
          print "\n".join(SleepNow(sleeptime))    


