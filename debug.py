#!/usr/bin/etc python

import galbackend
#target = galbackend.GalInterface()
#print(target)
#gt = galbackend.Thread(target=galbackend.GalInterface)
galbackend.InitLogging()
galbackend.InitResource()
galbackend.LaunchQueryDebug("when did you move to new york")


print ""