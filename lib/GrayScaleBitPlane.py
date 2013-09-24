from SimpleCV import *
from functools import partial

class GrayScaleBitPlane():

  #Returns a little endian (least significant bit first) binary representation as a string 
  #This make's it easy to access the bit planes using only array indexing.
  def convertToLsbfBinary(self, intVal):
    noZeroB = bin(intVal)[2:]
    padded = noZeroB.zfill(8)
    return padded[::-1]


  #Return a pixel intensity for a given bit plane. 
  #Since we have a gray scale image, the color channel that we use doesn't matter.
  #applyPixelFunction does not have a special call for grayscale pixels
  def transformPixel(self, bitPlane, (r,g,b)):
    littleEndianPixel = self.convertToLsbfBinary(r)

    if littleEndianPixel[bitPlane] == "0":
      return (0, 0, 0)
    return (255, 255, 255)

  #Returns a binary image of the bit plane.
  #Apply a transform function to all pixels in an image. 
  #Partial function application is used to create a function for the specific bitPlane. 
  def getBitPlane(self, image, bitPlane):
    return image.applyPixelFunction( partial(self.transformPixel, bitPlane) )

