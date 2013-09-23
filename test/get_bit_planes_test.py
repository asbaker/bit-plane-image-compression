import unittest
from GrayScaleBitPlane import *
from SimpleCV import *

class GrayScaleBitPlaneTest(unittest.TestCase):
  def setUp(self):
    self.testImage = Image("lenna").grayscale()
    self.subject = GrayScaleBitPlane()

  def test_get_bit_plane(self):
    bitPlane0 = self.subject.getBitPlane(self.testImage, 0)
    self.assertNotEqual(bitPlane0[0,0], self.testImage[0,0])

  def test_transform_pixel_returns_black_when_not_in_plane_0(self):
    res = self.subject.transformPixel(0, (0,0,0))
    self.assertGrayPixel(res, 0)

    res = self.subject.transformPixel(0, (2,2,2))
    self.assertGrayPixel(res, 0)

  def test_transform_pixel_returns_white_when_in_plane_0(self):
    res = self.subject.transformPixel(0, (1,1,1))
    self.assertGrayPixel(res, 255)

    res = self.subject.transformPixel(0, (3,3,3))
    self.assertGrayPixel(res, 255)

  def test_transform_pixel_returns_black_when_not_in_plane_1(self):
    res = self.subject.transformPixel(1, (8,8,8))
    self.assertGrayPixel(res, 0)

  def test_transform_pixel_returns_white_when_in_plane_1(self):
    res = self.subject.transformPixel(1, (2,2,2))
    self.assertGrayPixel(res, 255)


  def test_convert_to_8_bit_little_endian_binary_string_0(self):
    res = self.subject.convertToLsbfBinary(0)
    self.assertEqual(res, "00000000")

  def test_convert_to_8_bit_little_endian_binary_string_16(self):
    res = self.subject.convertToLsbfBinary(16)
    self.assertEqual(res, "00001000")

  def test_convert_to_8_bit_little_endian_binary_string_128(self):
    res = self.subject.convertToLsbfBinary(128)
    self.assertEqual(res, "00000001")

  def assertGrayPixel(self, actual, expected):
    self.assertEqual(actual[0], expected)
    self.assertEqual(actual[1], expected)
    self.assertEqual(actual[2], expected)

