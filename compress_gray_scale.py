#!/usr/bin/python

import sys
import numpy as np
from lib.GrayScaleBitPlane import *

def main(sourceFile, destFile):
  bitPlaneConverter = GrayScaleBitPlane()
  img = Image(sourceFile)

  planeCounts = []

  for plane in range(0, 8):
    print "*** Processing for Bit Plane {0} ***".format(plane)

    plane = bitPlaneConverter.getBitPlane(img, plane)
    count = np.count_nonzero(plane.getGrayNumpy())

    planeCounts.append((plane, count))

  planeCounts = sorted(planeCounts, lambda x, y: cmp(x[1], y[1]), None, True)

  for (plane, count) in planeCounts:
    print "count is {0}".format(count)


  compressionMask = planeCounts[0][0]# + planeCounts[1][0] + planeCounts[2][0] + planeCounts[3][0] + planeCounts[4][0] + planeCounts[5][0] + planeCounts[6][0] + planeCounts[7][0]
  compressionMask.save("images/mask_out.png")

  compressionMask = compressionMask.createBinaryMask(color1=(254,254,254), color2=(255,255,255));
  masked = img.applyBinaryMask(compressionMask, bg_color=(0,0,0))

  masked.save(destFile)


  os.system("convert {0} -type Grayscale {0}".format(destFile))





if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])
