#!/usr/bin/python

import sys
from lib.GrayScaleBitPlane import *

def main(sourceFile, destFile):
  bitPlaneConverter = GrayScaleBitPlane()

  #Opens the source image
  img = Image(sourceFile)

  # slice the image into bit planes
  bitPlaneSlices = map(lambda pn: bitPlaneConverter.getBitPlane(img, pn), reversed(range(0, 8)))

  # create a compression mask using the 2 most significant bit planes
  compressionMask = bitPlaneSlices[0] + bitPlaneSlices[1]

  # save the compression mask to a file
  compressionMask.save("images/mask_out.png")

  # create a binary mask which can be applied to the image
  compressionMask = compressionMask.createBinaryMask(color1=(254,254,254), color2=(255,255,255));

  # apply the binary mask setting all the removed pixels to black
  compressed = img.applyBinaryMask(compressionMask, bg_color=(0,0,0))

  # save the compressed file
  compressed.save(destFile)


if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])
