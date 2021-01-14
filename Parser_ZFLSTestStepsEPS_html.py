"""
────────────────────────────────────────────────────────────────────────────────
The script will parse the library from the [filename_xml_path] link AND
the information will be saved to [path_saved_file] path as txt file.
Author: Florin Malutan
Rev: 1.0
History:
    1.1:
    1.0: First File
────────────────────────────────────────────────────────────────────────────────
"""

import xml.etree.ElementTree as ET
from pathlib import Path

filename_xml_path = r'C:\Users\MAF1CLJ\Documents\Python\ZFLSTestStepsEPS_2020A\ZFLSTestStepsEPS.adlx'

max_depth = 0


def depth(elem, level):
    global max_depth
    if level == max_depth:
        max_depth += 1
    # recursive call to function to get the depth
    for child in elem:
        depth(child, level + 1)
    return str(max_depth)


def remove_string_empty_line(input_string):
    no_empty_lines_string = input_string.strip()
    return no_empty_lines_string


def get_description(filename_desc, new_xml):
    p = Path(filename_desc)
    lib_folder = str(p.parent)
    lib_folder = lib_folder + '\\' + new_xml
    pass
    tree = ET.parse(lib_folder)
    root = tree.getroot()
    child1 = root[0]
    return remove_string_empty_line(child1.text)


def shift_string(shift_char, string_in):
    # print(shift_char, '╔════════════════════════════════════════════════════════════╗')
    # entire_text = f'{shift_char}╔════════════════════════════════════════════════════════════╗\n'
    entire_text = f'\t{shift_char}┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐\n'
    for text_line in string_in.splitlines():
        # print(shift_char, text_line)
        entire_text += f'\t{shift_char} {text_line}\n'
    # print(shift_char, '╚════════════════════════════════════════════════════════════╝')
    entire_text += f'\t{shift_char}└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘\n'
    # entire_text += f'{shift_char}╚════════════════════════════════════════════════════════════╝\n'
    # print(entire_text)
    return entire_text


def parse_lib(filepath_, file, description_level_, with_description_):
    # print(f'Parsing: {filepath_} with description: {with_description_} and description level: {description_level_}')
    with_description = with_description_
    description_level = description_level_
    filename = filepath_
    tree = ET.parse(filename)
    root = tree.getroot()
    level_ = depth(root, -1)

    # file.writelines('┌──────────────────────┐\n')
    # file.writelines(f' XML depth Level is: {level_}\n')
    # file.writelines('└──────────────────────┘\n')

    # print('┌─────────────────────┐')
    # print(f'XML depth Level is: {level_}')
    # print('└─────────────────────┘')

    lib_name = str(root.attrib['name'])
    # file.writelines(f' {lib_name}\n')
    # file.writelines('┌───────────────────────────────────────┐\n')
    # file.writelines(f' {lib_name}\n')
    # print('┌───────────────────────────────────────┐')
    # print(lib_name)

    s1 = ""
    for attrib in root.attrib:
        pass
        # file.writelines(f' {attrib}: {root.attrib[attrib]}\n')
        s1 += f' {attrib}: {root.attrib[attrib]}\n'
        # print(attrib, ':', root.attrib[attrib])
    # file.writelines('└───────────────────────────────────────┘\n')
    # file.writelines(s1)
    # print('└───────────────────────────────────────┘')
    lib_info = f"""
┌───────────────────────────────────────┐\n
{s1}
└───────────────────────────────────────┘
"""
    file.writelines(f'<pre>{lib_info}</pre>\n')

    # print('┌──────────────────────────────────────────────────────────────────────────────────────────────┐')
    # file.writelines('┌───────────────────────────────────────────────────┐\n')
    href_reference_tag = "blkx-reference"
    href_reference_tag1 = "Standard.LibraryFolder"
    root_name = root.attrib['name']
    # print(root_name)
    # file.writelines(f'{root_name}\n')
    file.write(f'<pre><h2> {root_name}</h2> </pre>\n')
    file.write(f'<ul>\n')
    for child in root:
        # level 1
        level = 1
        # file.write(f'\t<ul id= "{child.tag}">\n')

        for child1 in child:
            if child1.tag == href_reference_tag:
                pass
            # print("\t", child1.attrib['name'])
            child1_name = child1.attrib['name']
            # file.writelines(f'\t{child1_name}\n')

            file.write(f'\t<li> {child1_name}')
            # level 2
            level = 2
            # file.write(f'\t\t\t<ul id= "{child1_name}">\n')

            for child2 in child1:
                # level 3
                level = 3
                file.write(f'\n\t\t<ul>\n')
                for child3 in child2:
                    if child3.tag == href_reference_tag or href_reference_tag1:
                        # print("\t\t\t", child3.attrib['name'])
                        child3_name = child3.attrib['name']
                        # file.writelines(f'\t\t\t{child3_name}\n')
                        file.write(f'\t\t\t<li> {child3_name}')
                        # file.write(f'<ul>\n')
                        # file.write(f'<ul>\n')
                        try:
                            description_string = get_description(filename, child3.attrib['href'])
                            if description_string != "" and with_description and level <= description_level:
                                entire_string3 = shift_string("", description_string)
                                # file.write(f'\n\t\t\t\t<pre> \n{entire_string3}</pre>')

                        except KeyError:
                            pass
                    # level 4
                    level = 4
                    for child4 in child3:
                        # level 5
                        level = 5
                        file.write(f'\n\t\t\t<ul>\n')
                        for child5 in child4:
                            if child5.tag == href_reference_tag or href_reference_tag1:
                                # print("\t\t\t\t\t", child5.attrib['name'])
                                child5_name = child5.attrib['name']
                                file.write(f'\t\t\t\t<li> {child5_name}')
                                try:
                                    description_string = get_description(filename, child5.attrib['href'])
                                    if description_string != "" and with_description and level <= description_level:
                                        # entire_string5 = shift_string("\t\t\t\t\t\t", description_string)
                                        # file.writelines(entire_string5)
                                        entire_string5 = shift_string("", description_string)
                                        # file.write(f'\n<pre> \n{entire_string5}</pre>')
                                except KeyError:
                                    pass
                            # level 6
                            level = 6
                            for child6 in child5:
                                # print("    ", child6.tag)
                                # level 7
                                level = 7
                                file.write(f'\n\t\t\t\t<ul>\n')
                                for child7 in child6:
                                    if child7.tag == href_reference_tag or child7.tag == href_reference_tag1:
                                        # print("\t\t\t\t\t\t\t", child7.attrib['name'])
                                        child7_name = child7.attrib['name']
                                        file.write(f'\t\t\t\t\t<li> {child7_name}')
                                        # file.writelines(f'\t\t\t\t\t\t\t{child7_name}\n')
                                        try:
                                            description_string = get_description(filename, child7.attrib['href'])
                                            if description_string != "" and with_description and level <= description_level:
                                                entire_string7 = shift_string("\t\t\t\t\t\t\t\t\t",
                                                                              description_string)
                                                # file.writelines(entire_string7)
                                        except KeyError:
                                            pass
                                    # level 8
                                    level = 8
                                    for child8 in child7:
                                        # print("    ", child8.tag)
                                        # level 9
                                        level = 9
                                        file.write(f'\n\t\t\t\t\t<ul>\n')
                                        for child9 in child8:
                                            if child9.tag == href_reference_tag or child9.tag == href_reference_tag1:
                                                # print("\t\t\t\t\t\t\t\t\t", child9.attrib['name'])
                                                child9_name = child9.attrib['name']
                                                # file.writelines(f'\t\t\t\t\t\t\t\t\t{child9_name}\n')
                                                file.write(f'\t\t\t\t\t\t<li> {child9_name}')
                                                try:
                                                    description_string = get_description(filename,
                                                                                         child9.attrib['href'])
                                                    if description_string != "" and with_description and level <= description_level:
                                                        entire_string9 = shift_string("\t\t\t\t\t\t\t\t\t\t\t",
                                                                                      description_string)
                                                        # file.writelines(entire_string9)
                                                except KeyError:
                                                    pass
                                            # level 10
                                            level = 10
                                            for child10 in child9:
                                                # level 11
                                                level = 11
                                                file.write(f'\n\t\t\t\t\t\t<ul>\n')
                                                for child11 in child10:
                                                    # print("\t\t\t\t\t\t\t\t\t\t\t", child11.attrib['name'])
                                                    child11_name = child11.attrib['name']
                                                    # file.writelines(f'\t\t\t\t\t\t\t\t\t{child11_name}\n')
                                                    # file.write(f'\t\t\t\t\t\t<li> {child11_name}')
                                                    try:
                                                        description_string = get_description(filename,
                                                                                             child11.attrib['href'])
                                                        if description_string != "" and with_description and level <= description_level:
                                                            shift_string("\t\t\t\t\t\t\t\t\t\t\t\t\t",
                                                                         description_string)
                                                    except KeyError:
                                                        pass
                                                    file.write(f'</li>\n')
                                                file.write(f'\t\t\t\t\t</ul>\n')
                                            file.write(f'</li>\n')
                                        file.write(f'\t\t\t\t\t</ul>\n')
                                    file.write(f'</li>\n')
                                file.write(f'\t\t\t\t</ul>\n')
                            file.write(f'</li>\n')
                        file.write(f'\t\t\t</ul>\n')
                    file.write(f'</li>\n')
                file.write(f'\t\t</ul>\n')
            file.write(f'\t</li>\n')
    file.write(f'</ul>\n')
    # print('└───────────────────────────────────────────────────┘')
    print("Success!!!")


def parse_xml(path_saved_file):
    with_description = True  # Extract description or not
    desc_level = 10  # Set description level to be extracted
    # p = Path(path_saved_file).resolve().stem
    with open(path_saved_file, 'w', encoding="utf-8") as file_:
        parse_lib(filename_xml_path, file_, desc_level, with_description)
    file_.close()


path_saved_file_ = r"C:\Users\MAF1CLJ\Desktop\ZFLSTestStepsEPS_Parsed.html"
parse_xml(path_saved_file_)
