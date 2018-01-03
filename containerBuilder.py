#!/usr/local/bin/python
import argparse 
import json 
import string
import itertools

#GNU GPL 3.0 
#Author: Bryn Ready 
#January 3, 2018

def iter_alphabet():
  size = 1
  while True:
    for s in itertools.product(string.ascii_lowercase, repeat=size):
      yield "".join(s)
    size += 1

#define generator 
gen = iter_alphabet()
def label_gen(): 
  for s in gen: 
    return s


parser = argparse.ArgumentParser(description='Tool to assist in creating json specifications for Opentron Robot')
parser.add_argument("-n", "--name", help="the name of the new container", default="new-container", action="store", dest="name")
parser.add_argument("-w", "--width", help="the number of voids along the x axis", type=int, default=0, action="store", dest="w")
parser.add_argument("-length", "--length", help="the number of voids along the y axis", type=int, default=0, action="store", dest="l")
parser.add_argument("-d", "--depth", help="the depth of the void in millimeters", type=float, default=0.0, action="store", dest="d")
parser.add_argument("-r", "--diameter", help="the diameter of the void in millimeters", type=float, default=0.0, action="store", dest="r")
parser.add_argument("-x", "--xoffset", help="origin x offset, i.e., mm in x direction to center of the first void", type=float, default=0.0, action="store", dest="xoffset")
parser.add_argument("-y", "--yoffset", help="origin y offset, i.e., mm in the y direction to the center of the first void", type=float, default=0.0, action="store", dest="yoffset")
parser.add_argument("-z", "--zoffset", help="origin z offset, ie., mm in the z direction to the center of the first void, usually set to 0", type=float, default=0.0, action="store", dest="zoffset")
parser.add_argument("-q", "--distance", help="distance between the center of one void to the next, assumes circular voids", type=float, default=1.0, action="store", dest="q")
parser.add_argument("-u", "--zdistance", help="z distance between the center of one void to the next, assumes flat, level voids", type=float, default=0.0, action="store", dest="u")
parser.add_argument("-v", "--volume", help="the total liquid volume of the void in microlitres", type=float, default=1.0, action="store", dest="v")

results = parser.parse_args()
#print results.w
#print type(results.w)
#print type(str(results.w))

container = {}
container["containers"] = {}
container["containers"][results.name] =  {"origin-offset" : { "x" : results.xoffset, "y" : results.yoffset, "z" : results.zoffset}}
container["containers"][results.name].update({"locations" : {}})

for xvalue in range(results.w):
  letter = label_gen()
  for yvalue in range(results.l):
    number = yvalue
    label = letter + str(number + 1)
    container["containers"][results.name]["locations"].update({label : { "x" : xvalue * results.q, "y" : yvalue * results.q, "z" : results.u, "depth" : results.d, "diameter" : results.r, "total-liquid-volume" : results.v}})
print json.dumps(container, indent=4, sort_keys=True)
