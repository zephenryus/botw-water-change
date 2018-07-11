import argparse
import os
import struct
import tempfile

import SarcLib
import libyaz0


def change_water(path, water_type=0):
    water_types = [
        'Normal Water',
        'Hot Water',
        'Poison',
        'Lava',
        'Ice Water',
        'Mud',
        'Clear Water',
        'Sea Water'
    ]

    for parent_dir, dirs, files in os.walk(path):
        for file in files:
            current_path = '{0}{1}'.format(parent_dir, file)

            if 'water.extm.sstera' not in current_path:
                continue

            with open(current_path, 'rb') as infile:
                infile_binary = infile.read()

                while libyaz0.IsYazCompressed(infile_binary):
                    infile_binary = libyaz0.decompress(infile_binary)

                path, extension = os.path.splitext(current_path)
                filename = os.path.basename(current_path)

                if infile_binary[0x00:0x04] != b'SARC':
                    print('Not a sarc. :(')

                sarc = SarcLib.SARC_Archive()
                sarc.load(infile_binary)

                with tempfile.TemporaryDirectory() as temp_dir:
                    for sarc_file in sarc.contents:
                        if isinstance(sarc_file, SarcLib.File):
                            pos = 0
                            data = bytearray(sarc_file.data)
                            while pos + 8 <= len(sarc_file.data):
                                height, x_axis_flow_rate, z_axis_flow_rate, mate_check, mate = \
                                    struct.unpack('<3H2B', data[pos:pos + 0x08])

                                # height = 0x24cc
                                # x_axis_flow_rate = 0x8125
                                # z_axis_flow_rate = 0x8125
                                mate = water_type
                                mate_check = mate + 3

                                data[pos:pos + 0x08] = struct.pack('<3H2B',
                                                                   height, x_axis_flow_rate, z_axis_flow_rate,
                                                                   mate_check, mate)

                                pos += 0x08

                            with open('{0}/{1}'.format(temp_dir, sarc_file.name), 'wb+') as outfile:
                                outfile.write(data)

                    sarc = SarcLib.SARC_Archive(endianness='>')

                    for path, dirs, files in os.walk(temp_dir):
                        for file in files:
                            with open('{0}/{1}'.format(path, file), 'rb') as infile:
                                sarc.addFile(SarcLib.File(file, infile.read(), True))

                    data, alignment = sarc.save()
                    data = libyaz0.compress(data, alignment, 5)

                    destination = '{0}/output/MainField - {1}'.format(os.path.dirname(__file__), water_types[water_type])

                    if not os.path.exists('{0}/output/'.format(os.path.dirname(__file__))):
                        os.makedirs('{0}/output/'.format(os.path.dirname(__file__)))
                    if not os.path.exists('{0}/output/MainField - {1}'.format(os.path.dirname(__file__), water_types[water_type])):
                        os.makedirs('{0}/output/MainField - {1}'.format(os.path.dirname(__file__), water_types[water_type]))

                    with open('{0}/{1}'.format(destination, filename), 'wb+') as outfile:
                        print('saving {0}...'.format(filename))
                        outfile.write(data)


def main():
    parser = argparse.ArgumentParser(description="Change the water material for the Main Field")
    parser.add_argument("filename", type=str, help="Main Field tscb")
    args = parser.parse_args()
    tscb = args.filename.replace('.tscb', '\\')

    water_type = -1
    while water_type < 0 or water_type > 7:
        print('Please make a backup of your map data before running this program!\n'
              'Select water material type to change ALL water to\n'
              '    0. Normal Water\n'
              '    1. Hot Water\n'
              '    2. Poison\n'
              '    3. Lava\n'
              '    4. Ice Water\n'
              '    5. Mud\n'
              '    6. Clear Water\n'
              '    7. Sea Water')
        water_type = int(input('Water Material: '))

    change_water(tscb, water_type)


if __name__ == "__main__":
    main()
