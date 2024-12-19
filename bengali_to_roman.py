# this is a quick script to convert bengali (bangla)
# into roman character transliteration

# input: text file written in bengali
# output: text file with roman characters (ending in '_rom.txt')

import sys
import io


def convert_line(in_line, in_conversion_dictionary):

    holding_line = in_line
    out_line = []

    for letter in holding_line:
        if in_conversion_dictionary.get(letter):
            out_line.append(in_conversion_dictionary.get(letter))
        # else:
        #     out_line.append(letter)

    out_line = "".join(out_line)
    return out_line


bengali_conversion_dict = {' ': ' ',
                         '।': '.',
                         ':': ':',
                         'ँ': '~',
                         '্': '',

                         '০': '0',
                         '১': '1',
                         '২': '2',
                         '৩': '3',
                         '৪': '4',
                         '৫': '5',
                         '৬': '6',
                         '৭': '7',
                         '৮': '8',
                         '৯': '9',

                         'ঃ': 'h',
                         'ং': 'ṃ',
                         'ৎ': 't',

                         'অ': 'a',
                         'আ': 'ā',
                         'া': 'ā',
                         'ই': 'i',
                         'ি': 'i',
                         'ঈ': 'ī',
                         'ী': 'ī',
                         'উ': 'u',
                         'ু': 'u',
                         'ঊ': 'ū',
                         'ূ': 'ū',
                         'ঋ': 'ri',
                         'ৃ': 'ri',
                         'ৠ': 'rī',
                         'ৄ': 'rī',
                         'ঌ': 'li',
                         'ৢ': 'li',
                         'ৡ': 'lī',
                         'ৣ': 'lī',
                         'এ': 'e',
                         'ে': 'e',
                         'ঐ': 'oi',
                         'ৈ': 'oi',
                         'ও': 'o',
                         'ো': 'o',
                         'ঔ': 'ou',
                         'ৌ': 'ou',

                         'ক': 'k',
                         'খ': 'kh',
                         'গ': 'g',
                         'ঘ': 'gh',
                         'ঙ': 'ng',

                         'চ': 'c',
                         'ছ': 'ch',
                         'জ': 'j',
                         'ঝ': 'jh',
                         'ঞ': 'ñ',

                         'ট': 'Ṭ',
                         'ঠ': 'Ṭh',
                         'ড': 'Ḍ',
                         'ঢ': 'Ḍh',
                         'ণ': 'Ṇ',

                         'ত': 't',
                         'থ': 'th',
                         'দ': 'd',
                         'ধ': 'dh',
                         'ন': 'n',

                         'প': 'p',
                         'ফ': 'ph',
                         'ব': 'b',
                         'ভ': 'bh',
                         'ম': 'm',

                         'য়': 'Y',
                         'ড়': 'Ṛ',
                         'ঢ়': 'Ṛh',

                         'য': 'y',
                         'র': 'r',
                         'ল': 'l',
                         'হ': 'h',

                         'শ': 'ś',
                         'ষ': 'Ṣ',
                         'স': 's',
                         }

FILENAME = sys.argv[1]
out_filename = sys.argv[1].split(".", maxsplit=1)[0]+"_rom.txt"

with io.open(FILENAME, 'r', encoding='utf8') as in_f:
    with io.open(out_filename, 'w', encoding='utf8') as out_f:
        out_f.write(convert_line(in_f.read(), bengali_conversion_dict))
