"""
Tests of Printing PCB files

We test:
- PDF for bom.kicad_pcb

For debug information use:
pytest-3 --log-cli-level debug

"""

import os
import sys
# Look for the 'utils' module from where the script is running
prev_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if prev_dir not in sys.path:
    sys.path.insert(0, prev_dir)
# Utils import
from utils import context

PDF_DIR = 'Layers'
PDF_FILE = 'bom-F_Cu+F_SilkS.pdf'
PDF_FILE_B = 'PCB_Bot.pdf'


def test_print_pcb_simple():
    prj = 'bom'
    ctx = context.TestContext('PrPCB', prj, 'print_pcb', PDF_DIR)
    ctx.run()
    # Check all outputs are there
    ctx.expect_out_file(os.path.join(PDF_DIR, PDF_FILE))
    ctx.clean_up()


def test_print_pcb_refill():
    prj = 'zone-refill'
    ctx = context.TestContext('PrPCB_Refill', prj, 'print_pcb_zone-refill', '')
    ctx.run()

    ctx.expect_out_file(PDF_FILE_B)
    ctx.compare_image(PDF_FILE_B)
