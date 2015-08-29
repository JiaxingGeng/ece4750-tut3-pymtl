#=========================================================================
# RegIncr2stage
#=========================================================================
# Two-stage registered incrementer that uses structural composition to
# instantitate and connect two instances of the single-stage registered
# incrementer.

from pymtl   import *
from RegIncr import RegIncr

class RegIncr2stage( Model ):

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  (8)
    s.out = OutPort (8)

    # First stage

    s.reg_incr_0 = RegIncr()

    s.connect( s.in_, s.reg_incr_0.in_ )

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will add code
    # to connect the second stage of this two-stage registered
    # incrementer.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  # Line Tracing

  def line_trace( s ):
    return "{} ({}|{}) {}".format(
      s.in_,
      s.reg_incr_0.line_trace(),
      s.reg_incr_1.line_trace(),
      s.out
    )

