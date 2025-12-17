from argparse import *
import struct
import winreg
import re
from pathlib import Path
import argparse

parser = ArgumentParser(
                    prog='EDID Parser',
                    description=r'This parses the provided EDID gives the required details, give the EDID path <SYSTEM\CurrentControlSet\Enum\DISPLAY\AOC3402\4&20696d67&0&UID24644\Device Parameters>',
                    epilog='-------Thanks-------')


class DumpEDID(Action):
    def __init__(self, option_strings, dest, bytes, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r %r' % (namespace, values, bytes, option_string))
        setattr(namespace, self.dest, values)
        with open(f"{values}" "wb" ) as f:
            for i in bytes:
                f.write(i)

parser.add_argument('-EDID_Path', type=str)
parser.add_argument('--dump', action=DumpEDID)



def EDID_Collector(EDID_Path):
    Keyobject = (winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, EDID_Path, access=winreg.KEY_READ))
    EDID =winreg.EnumValue(Keyobject, 0)[1]
    return EDID
