"""
Tests of SVG format.

For debug information use:
pytest-3 --log-cli-level debug
"""

import os
import sys
# Look for the 'utils' module from where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(script_dir))
# Utils import
from utils import context


PS_DIR = 'SVG'


def test_svg():
    prj = 'simple_2layer'
    ctx = context.TestContext('SVG', prj, 'svg', PS_DIR)
    ctx.run()

    f_cu = ctx.get_gerber_filename('F_Cu', '.svg')
    f_fab = ctx.get_gerber_filename('F_Fab', '.svg')
    ctx.expect_out_file(f_cu)
    ctx.expect_out_file(f_fab)
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())

    ctx.clean_up()