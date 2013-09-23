from SimpleCV import *
from functools import partial

class GrayScaleBitPlane():
  def convertToLsbfBinary(self, intVal):
    noZeroB = bin(intVal)[2:]
    padded = noZeroB.zfill(8)
    return padded[::-1]

  def getBitPlane(self, image, bitPlane):
    return image.applyPixelFunction( partial(self.transformPixel, bitPlane) )

  def transformPixel(self, bitPlane, (r,g,b)):
    littleEndianPixel = self.convertToLsbfBinary(r)

    if littleEndianPixel[bitPlane] == "0":
      return (0, 0, 0)
    return (255, 255, 255)

