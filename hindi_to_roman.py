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

                         'क': 'k',
                         'ख': 'kh',
                         'ग': 'g',
                         'घ': 'gh',
                         'ङ': 'ng',

                         'च': 'c',
                         'छ': 'ch',
                         'ज': 'j',
                         'झ': 'jh',
                         'ञ': 'ñ',

                         'ट': 'Ṭ',
                         'ठ': 'Ṭh',
                         'ड': 'Ḍ',
                         'ढ': 'Ḍh',
                         'ण': 'Ṇ',

                         'त': 't',
                         'थ': 'th',
                         'द': 'd',
                         'ध': 'dh',
                         'न': 'n',

                         'प': 'p',
                         'फ': 'ph',
                         'ब': 'b',
                         'भ': 'bh',
                         'म': 'm',

                         'क़': 'q',
                         'ख़': 'X',
                         'ग़': 'Y',
                         'ज़': 'z',
                         'ड़': 'Ṛ',
                         'ढ़': 'Ṛh',
                         'फ़': 'f',

                         'य': 'y',
                         'र': 'r',
                         'ऱ': 'r',
                         'ल': 'l',
                         'ळ': 'Ḷ',
                         'ऴ': 'Ḷ',
                         'व': 'v',
                         'ह': 'h',

                         'श': 'ś',
                         'ष': 'Ṣ',
                         'स': 's',
                         }

FILENAME = sys.argv[1]
out_filename = sys.argv[1].split(".", maxsplit=1)[0]+"_rom.txt"

with io.open(FILENAME, 'r', encoding='utf8') as in_f:
    with io.open(out_filename, 'w', encoding='utf8') as out_f:
        out_f.write(convert_line(in_f.read(), hindi_conversion_dict))
