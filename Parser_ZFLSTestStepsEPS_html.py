"""
────────────────────────────────────────────────────────────────────────────────
The script will parse the library from the  link AND
the information will be saved in the same path as .html file.
Author: Florin Malutan
Rev: 1.1
History:
    1.1 - Revision with GUI
    1.0 - Initial Revision
────────────────────────────────────────────────────────────────────────────────
"""

import xml.etree.ElementTree as ET
from pathlib import Path

import tkinter as tk

from tkinter import filedialog, messagebox
import os

max_depth = 0
list_depth_levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]


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
    entire_text = f'\t{shift_char}┌─────────────────────────────────────────────────' \
                  f'─────────────────────────────────────────────────────────────────────' \
                  f'─────────────────────────────────────────────────────────────────┐\n'
    for text_line in string_in.splitlines():
        entire_text += f'\t{shift_char} {text_line}\n'
    entire_text += f'\t{shift_char}└─────────────────────────────────────────────────' \
                   f'──────────────────────────────────────────────────────────────────' \
                   f'────────────────────────────────────────────────────────────────────┘\n'
    return entire_text


# with html lists
def parse_lib(filepath_, file, description_level_, with_description_):
    with_description = with_description_
    description_level = description_level_
    filename = filepath_
    tree = ET.parse(filename)
    root = tree.getroot()
    level_ = depth(root, -1)
    print(f'Depth level is: {level_}')

    s1 = ""
    for attrib in root.attrib:
        pass
        s1 += f' {attrib}: {root.attrib[attrib]}\n'

    lib_info = f"""
┌───────────────────────────────────────┐\n
{s1}
└───────────────────────────────────────┘
"""
    file.writelines(f'<pre>{lib_info}</pre>\n\n')
    href_reference_tag = "blkx-reference"
    href_reference_tag1 = "Standard.LibraryFolder"
    root_name = root.attrib['name']
    file.write(f'<pre><h2> {root_name}</h2> </pre>\n\n')
    file.write(f'<ul>\n')
    for child in root:
        # level 1
        level = 1
        for child1 in child:
            if child1.tag == href_reference_tag:
                pass
            child1_name = child1.attrib['name']
            file.write(f'\t<li> {child1_name}')
            # level 2
            level = 2
            for child2 in child1:
                # level 3
                level = 3
                file.write(f'\n\t\t<ul>\n')
                for child3 in child2:
                    if child3.tag == href_reference_tag or href_reference_tag1:
                        child3_name = child3.attrib['name']
                        file.write(f'\t\t\t<li> {child3_name}')
                        try:
                            description_string = get_description(filename, child3.attrib['href'])
                            if description_string != "" and with_description and level <= description_level:
                                entire_string3 = shift_string("", description_string)
                                file.write(f'\n\t\t\t\t<pre> \n{entire_string3}</pre>')

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
                                child5_name = child5.attrib['name']
                                file.write(f'\t\t\t\t<li> {child5_name}')
                                try:
                                    description_string = get_description(filename, child5.attrib['href'])
                                    if description_string != "" and with_description and level <= description_level:
                                        # entire_string5 = shift_string("\t\t\t\t\t\t", description_string)
                                        entire_string5 = shift_string("", description_string)
                                        file.write(f'\n<pre> \n{entire_string5}</pre>')
                                except KeyError:
                                    pass
                            # level 6
                            level = 6
                            for child6 in child5:
                                # level 7
                                level = 7
                                file.write(f'\n\t\t\t\t<ul>\n')
                                for child7 in child6:
                                    if child7.tag == href_reference_tag or child7.tag == href_reference_tag1:
                                        child7_name = child7.attrib['name']
                                        file.write(f'\t\t\t\t\t<li> {child7_name}')
                                        try:
                                            description_string = get_description(filename, child7.attrib['href'])
                                            if description_string != "" and with_description and \
                                                    level <= description_level:
                                                entire_string7 = shift_string("\t\t\t\t\t\t\t\t\t",
                                                                              description_string)
                                                file.writelines(entire_string7)
                                        except KeyError:
                                            pass
                                    # level 8
                                    level = 8
                                    for child8 in child7:
                                        # level 9
                                        level = 9
                                        file.write(f'\n\t\t\t\t\t<ul>\n')
                                        for child9 in child8:
                                            if child9.tag == href_reference_tag or child9.tag == href_reference_tag1:
                                                child9_name = child9.attrib['name']
                                                file.write(f'\t\t\t\t\t\t<li> {child9_name}')
                                                try:
                                                    description_string = get_description(filename,
                                                                                         child9.attrib['href'])
                                                    if description_string != "" and with_description and \
                                                            level <= description_level:
                                                        entire_string9 = shift_string("\t\t\t\t\t\t\t\t\t\t\t",
                                                                                      description_string)
                                                        file.writelines(entire_string9)
                                                except KeyError:
                                                    pass
                                            # level 10
                                            level = 10
                                            for child10 in child9:
                                                # level 11
                                                level = 11
                                                file.write(f'\n\t\t\t\t\t\t<ul>\n')
                                                for child11 in child10:
                                                    child11_name = child11.attrib['name']
                                                    file.write(f'\t\t\t\t\t\t<li> {child11_name}')
                                                    try:
                                                        description_string = get_description(filename,
                                                                                             child11.attrib['href'])
                                                        if description_string != "" and with_description and \
                                                                level <= description_level:
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
    print("Success!!!")


# with headers
def parse_lib1(filepath_, file, description_level_, with_description_):
    with_description = with_description_
    description_level = description_level_
    filename = filepath_
    tree = ET.parse(filename)
    root = tree.getroot()
    level_ = depth(root, -1)
    print(f'Depth level is: {level_}')

    s1 = ""
    for attrib in root.attrib:
        pass
        s1 += f' {attrib}: {root.attrib[attrib]}\n'

    lib_info = f"""
┌───────────────────────────────────────┐\n
{s1}
└───────────────────────────────────────┘
"""

    file.writelines(f'<pre>{lib_info}</pre>\n\n')
    href_reference_tag = "blkx-reference"
    href_reference_tag1 = "Standard.LibraryFolder"
    root_name = root.attrib['name']
    file.write(f'<pre> {root_name}</pre>\n\n')

    # file.write(f'<ul>\n')
    for child in root:
        # level 1
        level = 1
        for child1 in child:
            if child1.tag == href_reference_tag:
                pass
            child1_name = child1.attrib['name']
            # file.write(f'\t<li> {child1_name}')
            file.write(f'<h1> {child1_name}</h1>\n')
            # level 2
            level = 2
            for child2 in child1:
                # level 3
                level = 3
                # file.write(f'\n\t\t<ul>\n')
                for child3 in child2:
                    if child3.tag == href_reference_tag or href_reference_tag1:
                        child3_name = child3.attrib['name']
                        # file.write(f'\t\t\t<li> {child3_name}')
                        file.write(f'\t<h2> {child3_name}</h2>\n')
                        try:
                            description_string = get_description(filename, child3.attrib['href'])
                            if description_string != "" and with_description and level <= description_level:
                                entire_string3 = shift_string("", description_string)
                                # file.write(f'\n\t\t\t\t<pre> \n{entire_string3}</pre>')
                                file.write(f'\t<pre> {entire_string3}</pre>\n')

                        except KeyError:
                            pass
                    # level 4
                    level = 4
                    for child4 in child3:
                        # level 5
                        level = 5
                        # file.write(f'\n\t\t\t<ul>\n')
                        for child5 in child4:
                            if child5.tag == href_reference_tag or href_reference_tag1:
                                child5_name = child5.attrib['name']
                                # file.write(f'\t\t\t\t<li> {child5_name}')
                                file.write(f'\t\t<h3> {child5_name}</h3>\n')
                                try:
                                    description_string = get_description(filename, child5.attrib['href'])
                                    if description_string != "" and with_description and level <= description_level:
                                        # entire_string5 = shift_string("\t\t\t\t\t\t", description_string)
                                        entire_string5 = shift_string("", description_string)
                                        # file.write(f'\n<pre> \n{entire_string5}</pre>')
                                except KeyError:
                                    pass
                            # level 6
                            level = 6
                            for child6 in child5:
                                # level 7
                                level = 7
                                # file.write(f'\n\t\t\t\t<ul>\n')
                                for child7 in child6:
                                    if child7.tag == href_reference_tag or child7.tag == href_reference_tag1:
                                        child7_name = child7.attrib['name']
                                        # file.write(f'\t\t\t\t\t<li> {child7_name}')
                                        file.write(f'\t\t\t<h4> {child7_name}</h4>\n')
                                        try:
                                            description_string = get_description(filename, child7.attrib['href'])
                                            if description_string != "" and with_description and \
                                                    level <= description_level:
                                                entire_string7 = shift_string("\t\t\t\t\t\t\t\t\t",
                                                                              description_string)
                                                # file.writelines(entire_string7)
                                        except KeyError:
                                            pass
                                    # level 8
                                    level = 8
                                    for child8 in child7:
                                        # level 9
                                        level = 9
                                        # file.write(f'\n\t\t\t\t\t<ul>\n')
                                        for child9 in child8:
                                            if child9.tag == href_reference_tag or child9.tag == href_reference_tag1:
                                                child9_name = child9.attrib['name']
                                                # file.write(f'\t\t\t\t\t\t<li> {child9_name}')
                                                file.write(f'\t\t\t\t<h5> {child9_name}</h5>\n')
                                                try:
                                                    description_string = get_description(filename,
                                                                                         child9.attrib['href'])
                                                    if description_string != "" and with_description and \
                                                            level <= description_level:
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
                                                # file.write(f'\n\t\t\t\t\t\t<ul>\n')
                                                for child11 in child10:
                                                    child11_name = child11.attrib['name']
                                                    # file.write(f'\t\t\t\t\t\t<li> {child11_name}')
                                                    file.write(f'\t\t\t\t\t<h6> {child11_name}</h6>\n')
                                                    try:
                                                        description_string = get_description(filename,
                                                                                             child11.attrib['href'])
                                                        if description_string != "" and with_description and \
                                                                level <= description_level:
                                                            shift_string("\t\t\t\t\t\t\t\t\t\t\t\t\t",
                                                                         description_string)
                                                    except KeyError:
                                                        pass
    #                                                 file.write(f'</li>\n')
    #                                             file.write(f'\t\t\t\t\t</ul>\n')
    #                                         file.write(f'</li>\n')
    #                                     file.write(f'\t\t\t\t\t</ul>\n')
    #                                 file.write(f'</li>\n')
    #                             file.write(f'\t\t\t\t</ul>\n')
    #                         file.write(f'</li>\n')
    #                     file.write(f'\t\t\t</ul>\n')
    #                 file.write(f'</li>\n')
    #             file.write(f'\t\t</ul>\n')
    #         file.write(f'\t</li>\n')
    # file.write(f'</ul>\n')
    print("Success!!!")


def parse_xml(filename_xml_path, path_saved_file, with_description, desc_level):
    with open(path_saved_file, 'w', encoding="utf-8") as file_:
        parse_lib(filename_xml_path, file_, desc_level, with_description)
    file_.close()


def parse_xml1(filename_xml_path, path_saved_file, with_description, desc_level):
    with open(path_saved_file, 'w', encoding="utf-8") as file_:
        parse_lib1(filename_xml_path, file_, desc_level, with_description)
    file_.close()


def create_path_to_save(filepath_):
    global path_saved_file_
    p1 = Path(filepath_)
    lib_folder = str(p1.parent)
    path_saved_file_ = f'{lib_folder}\\{p1.stem}_Parsed.html'


def start_parse():
    update_values()
    print(f'Description:[ {boolDecription} ] and level:[ {intDescriptionLevel} ]')
    if 'filepath' not in globals():
        messagebox.showinfo('Path not found', 'Path to file is missing, please browse the file!')
    else:
        try:
            parse_xml(filepath, path_saved_file_, boolDecription, intDescriptionLevel)
        except:
            messagebox.showinfo('Parsing Problems', 'The file was not parsed')


def str_to_bool_new(s):
    if s == '1':
        return True
    elif s == '0':
        return False


def str_to_int(inputvalue):
    if inputvalue == "":
        messagebox.showinfo('Description Level', 'Please use only integers eg: [0],[7],[10]')
    else:
        try:
            return int(inputvalue)
        except:
            messagebox.showinfo('Description Level', 'Please use only integers eg: [0],[7],[10]')


def update_values():
    global boolDecription
    global intDescriptionLevel
    boolDecription = str_to_bool_new(str(radiobutton_var.get()))
    intDescriptionLevel = int(vardescLevel.get())


def file_path():
    global filepath
    filepath = tk.StringVar()
    if filepath == "":
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="select a file",
                                              filetypes=[("adlx files", "*.adlx"), ("html files", "*.html"),
                                                         ("All files", "*.*")])
    else:
        filepath = filedialog.askopenfilename(initialdir=filepath,
                                              title="select a file",
                                              filetypes=[("adlx files", "*.adlx"), ("html files", "*.html"),
                                                         ("All files", "*.*")])
    generate()


def generate():
    # Validation of entry fields, if left empty.
    if filepath == "":
        messagebox.showinfo('Information', 'Please select the file')
    else:
        pathEntry.delete(0, 'end')
        pathEntry.insert(0, filepath)
        create_path_to_save(filepath)


def true_or_false_btn():
    boolDecription = str_to_bool_new(str(radiobutton_var.get()))


def grab_and_assign(event):
    intDescriptionLevel = int(vardescLevel.get())


def sel():
    boolDecription = true_or_false_btn()


form = tk.Tk()
form.title("Parse .adlx")
bg_color_default = 'ghost white'
# bg_color_default = 'light yellow'
form.configure(background=bg_color_default)

radiobutton_var = tk.StringVar()
vardescLevel = tk.StringVar()

descLabel = tk.Label(form, text="With Description:", bg=bg_color_default)
descLabel.grid(row=16, column=0)

descradiobtn1 = tk.Radiobutton(form, text="True", variable=radiobutton_var, value=1, bg=bg_color_default, command=sel)
descradiobtn1.grid(row=16, column=1, padx=10, pady=2, sticky="W")
descradiobtn2 = tk.Radiobutton(form, text="False", variable=radiobutton_var, value=0, bg=bg_color_default, command=sel)
descradiobtn2.grid(row=16, column=1, padx=70, pady=2, sticky="W")
radiobutton_var.set(1)

descLevelLabel = tk.Label(form, text="Description Level:", bg=bg_color_default)
descLevelLabel.grid(row=18, column=0, padx=0, pady=1)

drop_menu = tk.OptionMenu(form, vardescLevel, *list_depth_levels, command=grab_and_assign)
drop_menu.config(bg=bg_color_default)
drop_menu.grid(row=18, column=1, padx=5, pady=1, sticky="W")
vardescLevel.set(10)

btnbrowse = tk.Button(form, width=25, text="Select file", bg='pale green', command=file_path)
btnbrowse.grid(columnspan=2, padx=0, pady=10)

pathLabel = tk.Label(form, text="Path:", bg=bg_color_default)
pathLabel.grid(row=25, column=0, padx=0, pady=1, sticky="E")

pathEntry = tk.Entry(form, width=80)
pathEntry.grid(row=25, column=1, padx=5, pady=1, sticky="W")

btngenerate = tk.Button(form, width=25, text="Parse the file", bg='pale green', command=start_parse)
btngenerate.grid(columnspan=2, padx=0, pady=10)

form.mainloop()
