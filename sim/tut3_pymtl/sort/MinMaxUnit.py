#=========================================================================
# MinMaxUnit
#=========================================================================

from pymtl import *

class MinMaxUnit( Model ):

  # Constructor

  def __init__( s, nbits=8 ):

    s.in0  = InPort  ( nbits )
    s.in1  = InPort  ( nbits )
    s.min_ = OutPort ( nbits )
    s.max_ = OutPort ( nbits )

    @s.combinational
    def block():

      if s.in0 >= s.in1:
        s.max_.value = s.in0
        s.min_.value = s.in1
      else:
        s.max_.value = s.in1
        s.min_.value = s.in0

  # Line tracing

  def line_trace( s ):
    return "{}|{}(){}|{}".format( s.in0, s.in1, s.min_, s.max_ )

