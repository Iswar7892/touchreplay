#!/usr/bin/env python
# coding: utf-8
import sys
import fileinput
import subprocess 
prefix = "sendevent "

inputline = ""
complete = ""
part1len = 0
part1 = ""
part2 = ""

num1 = 0
num2 = 0
num3 = 0
rawfile = ""
outfile = ""
filename = ""

rawfile = sys.argv[-1]

fo = open(rawfile, "r")

filename = rawfile.find(".");
outfile = rawfile[:filename] + ".scr"
# Output file
fw = open(outfile, "w")

# Puts into bash
fw.write("#!/bin/sh" + "\n")

fw.write("echo Running – drawing function " + "\n")

for inputline in fo.read().split("\n"):
        #print(inputline[0:16]) 
        if inputline[0:16] == "/dev/input/event" and len(inputline) >= 35:
                part1len = inputline.find(":");

                if part1len > -1:
                        # Only take the first part of the string up to the string
                        part1 = inputline[:part1len];
                        part2 = inputline.split(" ");
                        num1 = int(part2[1], 16)
                        num2 = int(part2[2], 16)
                        num3 = int(part2[3], 16)

                        complete = prefix + part1 + " " + str(num1) + " " + str(num2) + " " + str(num3)

                        fw.write(complete + "\n")


print ("Processing complete")
print ("File created: "), outfile
print
print ("Copy file to the device")
print ("adb push " + outfile + " /sdcard/" + outfile)
print
print ("Run the script")
print ("adb shell sh /sdcard/" + outfile)
fo.close()
fw.close()
