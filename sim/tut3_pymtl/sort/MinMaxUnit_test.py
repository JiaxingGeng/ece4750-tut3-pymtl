#=========================================================================
# MinMaxUnit_test
#=========================================================================

from random     import randint

from pymtl      import *
from pclib.test import run_test_vector_sim
from MinMaxUnit import MinMaxUnit

#-------------------------------------------------------------------------
# test_basic
#-------------------------------------------------------------------------

def test_basic( dump_vcd, test_verilog ):
  run_test_vector_sim( MinMaxUnit(), [
    ('in0   in1   min_* max_*'),
    [ 0x00, 0x00, 0x00, 0x00  ],
    [ 0x04, 0x03, 0x03, 0x04  ],
    [ 0x09, 0x06, 0x06, 0x09  ],
    [ 0x0a, 0x0f, 0x0a, 0x0f  ],
    [ 0xff, 0x10, 0x10, 0xff  ],
  ], dump_vcd, test_verilog )

#-------------------------------------------------------------------------
# test_random
#-------------------------------------------------------------------------

def test_random( dump_vcd, test_verilog ):

  test_vector_table = [( 'in0', 'in1', 'min_*', 'max_*' )]
  for i in xrange(20):
    in0 = Bits( 8, randint(0,0xff) )
    in1 = Bits( 8, randint(0,0xff) )
    test_vector_table.append( [ in0, in1, min(in0,in1), max(in0,in1) ] )

  run_test_vector_sim( MinMaxUnit(), test_vector_table,
                       dump_vcd, test_verilog )

