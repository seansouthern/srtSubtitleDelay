'''
Created on Sep 17, 2011

Finished on Sep 26, 2011

@author: sean

This is the main module for a movie subtitle altering program. I made this specifically to
move the subtitle timing in an srt file I downloaded for the Japanese action movie, Branded
To Kill. In this program I open the slow .srt file, search each line with a regular expression
and increment each seconds place by 13 seconds. I also increment the minutes by one when needed.
I did not address incrementing the hours place for this program because it was not needed.
This is a fairly specific program but I believe it may work for other .srt format files with
some minor tweaking.

Functions: addOne(num) , addThirteen(num)
'''
import re

with open("Branded To Kill.srt") as inFile:
    lineList = inFile.readlines()

pattern = re.compile("..(?=,[0-9][0-9][0-9])")
subPattern = re.compile("..(?=:([0][0-9]|[1][0-2]),[0-9][0-9][0-9])")

def addOne(num):
    x = int(num.group(0)) + 1
    if x < 10:
        x =  "0" + str(x)
    return str(x)
    
def addThirteen(num):
    if int(num.group(0)) < 47:
        subString = int(num.group(0)) + 13
        return str(subString)
    elif int(num.group(0)) >= 47:
        subString = int(num.group(0)) + 13 - 60
        if int(subString) < 10:
            subString = "0" + str(subString)
        return str(subString)
    else:
        return False

with open("output.srt", 'w') as outFile:
    for line in lineList:   
        line = re.sub(pattern, addThirteen, line)
        line = re.sub(subPattern, addOne, line)
        outFile.write(line)
    
print "Done!"