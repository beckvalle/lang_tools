# this is a quick script to convert hindi
# into roman character transliteration

# input: text file written in hindi
# output: text file with roman characters (ending in '_rom.txt')

import sys
import io


def convert_line(in_line, in_conversion_dictionary):

    holding_line = in_line
    out_line = []

    for letter in holding_line:
        if in_conversion_dictionary.get(letter):
            out_line.append(in_conversion_dictionary.get(letter))
        else:
            out_line.append(letter)

    out_line = "".join(out_line)
    return out_line


hindi_conversion_dict = {' ': ' ',
                         '।': '.',
                         ':': ':',
                         'ँ': 'n',
                         'ं': 'n',

                         '०': '0',
                         '१': '1',
                         '२': '2',
                         '३': '3',
                         '४': '4',
                         '५': '5',
                         '६': '6',
                         '७': '7',
                         '८': '8',
                         '९': '9',

                         'ः': 'h',
                         'ः/t': ':/t',

                         'अ': 'a',
                         'आ': 'aa',
                         'ा': 'aa',
                         'इ': 'i',
                         'ि': 'i',
                         'ई': 'ii',
                         'ी': 'ii',
                         'उ': 'u',
                         'ु': 'u',
                         'ऊ': 'uu',
                         'ू': 'uu',
                         'ऋ': 'ri',
                         'ृ': 'ri',
                         'ॠ': 'rii',
                         'ॄ': 'rii',
                         'ऌ': 'li',
                         'ॢ': 'li',
                         'ॡ': 'lii',
                         'ॣ': 'lii',
                         'ए': 'e',
                         'े': 'e',
                         'ऐ': 'ai',
                         'ै': 'ai',
                         'ओ': 'o',
                         'ो': 'o',
                         'औ': 'au',
                         'ौ': 'au',

                         'ऍ': 'e',
                         'ॅ': 'e',
                         'ऑ': 'o',
                         'ॉ': 'o',
                         'ऎ': 'e',
                         'ॆ': 'e',
                         'ऒ': 'o',
                         'ॊ': 'o',

                         'क': 'ka',
                         'ख': 'kha',
                         'ग': 'ga',
                         'घ': 'gha',
                         'ङ': 'nga',

                         'च': 'ca',
                         'छ': 'cha',
                         'ज': 'ja',
                         'झ': 'jha',
                         'ञ': 'ña',

                         'ट': 'Ṭa',
                         'ठ': 'Ṭha',
                         'ड': 'Ḍa',
                         'ढ': 'Ḍha',
                         'ण': 'Ṇa',

                         'त': 'ta',
                         'थ': 'tha',
                         'द': 'da',
                         'ध': 'dha',
                         'न': 'na',

                         'प': 'pa',
                         'फ': 'pha',
                         'ब': 'ba',
                         'भ': 'bha',
                         'म': 'ma',

                         'क़': 'qa',
                         'ख़': 'Xa',
                         'ग़': 'Ya',
                         'ज़': 'za',
                         'ड़': 'Ṛa',
                         'ढ़': 'Ṛha',
                         'फ़': 'fa',

                         'य': 'ya',
                         'र': 'ra',
                         'ऱ': 'ra',
                         'ल': 'la',
                         'ळ': 'Ḷa',
                         'ऴ': 'Ḷa',
                         'व': 'va',
                         'ह': 'ha',

                         'श': 'śa',
                         'ष': 'Ṣa',
                         'स': 'sa',
                         }

FILENAME = sys.argv[1]
out_filename = sys.argv[1].split(".", maxsplit=1)[0]+"_rom.txt"

with io.open(FILENAME, 'r', encoding='utf8') as in_f:
    with io.open(out_filename, 'w', encoding='utf8') as out_f:
        out_f.write(convert_line(in_f.read(), hindi_conversion_dict))
