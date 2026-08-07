import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import make_the_main_zig_eb4ee as mod

def test_cli_runs():
    assert mod.cli([]) in (0, 1)
