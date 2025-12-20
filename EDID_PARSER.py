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
                    1. --dumpEDID

                    """,
                    epilog='-------Thanks-------')

parser.add_argument('--EDID_Path', type=str)
parser.add_argument('--dumpEDID', action="store_true" )
parser.add_argument('--filename')

args = parser.parse_args()
EDID_Path = args.EDID_Path
Dump_Name = args.filename


def EDID_Collector(EDID_Path):
    Keyobject = (winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, EDID_Path, access=winreg.KEY_READ))
    EDID =winreg.EnumValue(Keyobject, 0)[1]
    Header = struct.unpack("<8B",EDID[0:8])
    if ((Header[0] & Header[-1]) == 0) & (sum(Header[1:7]) == 1530):
        return EDID
    else:
        print("Incorrect EDID format")

EDID = EDID_Collector(EDID_Path)
print(EDID)

def BinaryDump(EDID, filename='dump'):
    with open(filename, "wb") as f:
        f.write(EDID)

if args.dumpEDID:
    BinaryDump(EDID_Collector(EDID_Path), Dump_Name )