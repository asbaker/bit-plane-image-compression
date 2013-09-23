#!/usr/bin/python

import sys
#from GrayScaleBitPlane import *
from lib.GrayScaleBitPlane import *

def main(sourceFile, destFile):
  bitPlaneConverter = GrayScaleBitPlane()
  img = Image(sourceFile)

  for plane in range(0, 8):
    print "*** Processing for Bit Plane {0} ***".format(plane)
    outFileName = "{0}_plane_{1}.{2}".format(destFile, plane, "tif")
    planeImage = bitPlaneConverter.getBitPlane(img, plane)
    planeImage.save(outFileName)


if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])
