from argparse import *
import struct
import winreg
import re
from pathlib import Path
import argparse

parser = ArgumentParser(
                    prog='EDID Parser',
                    description=r"""This parses the provided EDID gives the required details, give the EDID path <SYSTEM\CurrentControlSet\Enum\DISPLAY\AOC3402\4&20696d67&0&UID24644\Device Parameters>
                    
                    Required Arguments:
                    1. --EDID_Path

                    Option Arguments:
                    1. --dump

                    """,
                    epilog='-------Thanks-------')

parser.add_argument('--EDID_Path', type=str)
parser.add_argument('--dump', action="store_true" )
parser.add_argument('--filename')

args = parser.parse_args()
EDID_Path = args.EDID_Path
Dump_Name = args.filename

def EDID_Collector(EDID_Path):
    Keyobject = (winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, EDID_Path, access=winreg.KEY_READ))
    EDID =winreg.EnumValue(Keyobject, 0)[1]
    return EDID

EDID = EDID_Collector(EDID_Path)

def BinaryDump(EDID, filename='dump'):
    with open(filename, "wb") as f:
        f.write(EDID)

if args.dump:
    BinaryDump(EDID_Collector(EDID_Path), Dump_Name )