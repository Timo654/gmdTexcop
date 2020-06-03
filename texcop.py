#made by Timo654, thx to etra0 for his bones tool and thx to CapitanRetraso, julian20 and MnSXx for help
import json
import sys
import os.path
from os import path
import shutil
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
icon = """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
OS0wNzowMFs/TU8AAAAASUVORK5CYII=""" 
#gmd texture list and texture amount offset
OFFSET = {
    'gmd': (0x70, 0x74),
}

def resource_path(relative_path): #related to changing tkinter icon
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_textures(filename): #gets textures from gmd
    ENDIANNESS = 'big'
    t_o, n_o = OFFSET[filename[-3:]] #texture list offset and texture amount offset
    textures = []
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read()
    c_endianness = ENDIANNESS
    endian_check = int.from_bytes(binary_data[0x04:0x06], ENDIANNESS)
    #If endianness check is 8448 (Dragon Engine) or 0 (Kenzan), it's little endian.
    if endian_check in [8448, 0]:
        c_endianness = 'little'
    textures_offset = int.from_bytes(binary_data[t_o:t_o+4], c_endianness)
    n_textures = int.from_bytes(binary_data[n_o:n_o+4], c_endianness)
    print("Working...")
    for i in range(0, n_textures):
        texture = binary_data[textures_offset+2:textures_offset+0x20].decode().strip('\x00')
        textures.append(texture)
        textures_offset += 0x20
    return textures
#copies textures to folder
def copy_textures(n_textures, tex_path, textures, output):
    for p in range (0, n_textures):
        original = tex_path + '/' + textures[p] + '.dds'
        if os.path.exists(compare_tex + '/' + textures[p] + '.dds') and separate_common == True:
                if os.path.exists(original):
                    common_output = os.path.join(output, 'common')
                    shutil.copy(original, common_output)
        elif os.path.exists(original):
                shutil.copy(original, output)
        else:
            print("Failed to find a texture.")    
            continue
#saves settings
def save(model, tex_path, output, settings_file):
        settings = [model, tex_path, output, compare_tex]
        with open(settings_file, 'w') as f:
            f.write(json.dumps(settings))
#saves model texture list and gets info to copy textures 
def main(n_models, model_path, tex_path, output, settings_file):
    for o in range (0, n_models):
        model_folder, model_name = os.path.split(model_path[o])
        textures = list(get_textures(model_path[o]))
        output_model = os.path.join(output, model_name[:-4]) #gets path to save model to a separate folder
        name = output + "/" + model_name[:-4] + "-textures.txt"
        print("Saving texture list to " + name)
        if not os.path.exists(output_model):
            os.makedirs(output_model)
            if separate_common == True: 
                os.makedirs(output_model + '\\common') #creates a folder for textures that are in common
        with open(name, 'w') as f:
            for texture in textures:
                f.write(texture + '\n')
        copy_textures(len(textures), tex_path, textures, output_model)
    save(model_folder, tex_path, output, settings_file)
#picking texture/output paths
def find_path(): #paths
    global tex_path
    global output
    tex_path = filedialog.askdirectory(initialdir=settings[1],title = "Select the DDS folder")
    if tex_path == "":
        quit()
    output = filedialog.askdirectory(initialdir=settings[2],title = "Select the output folder")
    if output == "":
        quit()
    separate_textures()
#asks for paths to separate the common textures to a separate folder
def separate_textures():
    global separate_common
    global compare_tex
    ask_about_common = tk.messagebox.askquestion ('Common textures','Do you want to separate common textures?',icon = 'question')
    if ask_about_common == 'yes':
        separate_common = True
        compare_tex = filedialog.askdirectory(initialdir=settings[3],title = "Select the DDS folder to compare it to to find common textures")
    else:
        separate_common = False
        compare_tex = settings[3]
if os.name == 'nt':
    settings_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'Texcop') #settings folder
else: settings_folder = os.path.join(os.environ['HOME'], '.config', 'Texcop') 
settings_file = os.path.join(settings_folder, 'settings.json') #settings file
#making a settings file
if not os.path.exists(settings_folder):
    os.makedirs(settings_folder)
settings = []
if path.exists(settings_file):
    with open(settings_file, 'r') as f:
        settings = json.loads(f.read())
else: settings = ['/', '/', '/', '/']

root = tk.Tk()
#tkinter icon
img = tk.PhotoImage(data=icon)
root.tk.call('wm', 'iconphoto', root._w, img)
root.withdraw()
#selecting gmds
models = [] 
if len(sys.argv) == 1:
    pick_models = filedialog.askopenfilenames(initialdir=settings[0],title = "Select the Model",filetypes=(("Model files", "*.gmd"), ("All Files", "*.*")))
    if pick_models == "":
        quit()
    models = list(pick_models)
else:        
    models = sys.argv[1:]
#selecting paths for textures and output
if os.path.exists(settings_file):
    MsgBox = tk.messagebox.askquestion ('Select paths','Do you want to load previously used paths?',icon = 'question')
    if MsgBox == 'yes':
        tex_path = settings[1]
        output = settings[2]
        compare_tex = settings[3]
        ask_about_common = tk.messagebox.askquestion ('Common textures','Do you want to separate common textures?',icon = 'question')
        if ask_about_common == 'yes':
            separate_common = True
        else:
            separate_common = False
    if MsgBox == 'no':
        find_path()
else:
    find_path()
#going through models and copying textures
main(len(models), models, tex_path, output, settings_file)
input("Textures copied successfully.\nPress Enter to continue...")