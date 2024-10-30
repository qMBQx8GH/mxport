# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read(sys.argv[1])
path_to_game = config['Game']['folder']

xml_root = ET.parse(os.path.join(path_to_game, 'game_info.xml'))
xml_version = xml_root.findall(".//version[@name='client']")
version = xml_version[0].attrib['installed']

# C:\Games\World_of_Warships_RU>wowsunpack.exe -x bin/8601080/idx -p ..\..\..\res_packages -o res -I gui/unbound2/pc/lootboxes/*.*
content = [
    'gui/unbound2/pc/lootboxes/lootbox_elements.unbound',
    'gui/unbound2/pc/lootboxes/battlepass_main.unbound',
]
print(version)
for d in content:
    subprocess.run([
        'wowsunpack.exe',
        '-x', os.path.join(path_to_game, "bin", version.split(".")[-1], "idx"),
        '-I', d,
        '-p', '..\\..\\..\\res_packages',
        '-o', 'res',
    ],
        shell=True,
    )
    print(d, 'OK')
