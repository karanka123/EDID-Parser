from argparse import *
import struct
import winreg

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

# EDID Collection and validate the EDID
def EDID_Collector(EDID_Path):
    Keyobject = (winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, EDID_Path, access=winreg.KEY_READ))
    EDID =winreg.EnumValue(Keyobject, 0)[1]
    Header = struct.unpack("<8B",EDID[0:8])
    if ((Header[0] & Header[-1]) == 0) & ((Header[1:7]) == (255,255,255,255,255,255)):
        return EDID
    else:
        print("Incorrect EDID format")

EDID = EDID_Collector(EDID_Path)

# Dump EDID
def BinaryDump(EDID, filename='dump'):
    with open(filename, "wb") as f:
        f.write(EDID)

if args.dumpEDID:
    BinaryDump(EDID_Collector(EDID_Path), Dump_Name )


def display_spec(EDID):

    # Product Code
    Product_Code_bytes = struct.unpack("<H", EDID[8:10])[0]
    Product_Code = ''.join([
        chr(((Product_Code_bytes >> 10) & 0x1F) +64),
        chr(((Product_Code_bytes >> 5) & 0x1F) +64),
        chr((Product_Code_bytes & 0x1F) + 64)
    ])

    # Product Serial Number \\ Product Named
    Display_Descriptor = struct.unpack('<18B', EDID[72:90])
    ProductSerial_Number = ''
    ProductName = ''
    if (Display_Descriptor[0:3]) == (0x00,0x00,0x00) and (Display_Descriptor[3] == 0xFF):
        for a in Display_Descriptor[5:18]:
            ProductSerial_Number += chr(a)
    elif (Display_Descriptor[0:3]) == (0x00,0x00,0x00) and (Display_Descriptor[3] == 0xFE):
        for b in Display_Descriptor[5:18]:
            if b == 0x0A:
                break
            ProductName += chr(b)

    return (Product_Code, ProductName)

print(display_spec(EDID))