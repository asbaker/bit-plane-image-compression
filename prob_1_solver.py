#!/usr/bin/python

from lib.GrayScaleBitPlane import *

bitPlaneConverter = GrayScaleBitPlane()



for plane in range(0, 8):
  print "for plane 2^{0} ".format(plane)

  for i in range(0, 256):
    (r,g,b) = bitPlaneConverter.transformPixel(plane, (i,i,i))
    if r == 255:
      print i


