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
    t_o, n_o = OFFSET[filename[-3:]]
    textures = []
    with open(filename, 'rb') as binary_file:
        binary_data = binary_file.read()
    c_endianness = ENDIANNESS
    endian_check = int.from_bytes(binary_data[0x04:0x06], ENDIANNESS)
    #If endianness check is 8448 (Dragon Engine) or 0 (Kenzan), it's little endian.
    if endian_check == 8448 or 0:
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
def copy_textures(n_textures, texpath, textures, output):
    for p in range (0, n_textures):
        original = texpath + "/" + textures[p] + ".dds"
        if os.path.exists(original):
            shutil.copy(original, output)
        else:
            print("Failed to find a texture.")    
            continue
#saves settings
def save(model, texpath, output, stfile):
        settings = [model, texpath, output]
        with open(stfile, 'w') as f:
            f.write(json.dumps(settings))
#does stuff
def dostuff(n_models, modelpath, texpath, output, stfile):
    for o in range (0, n_models):
        mp1, mp2 = os.path.split(modelpath[o])
        textures = list(get_textures(modelpath[o]))
        output2 = os.path.join(output, mp2[:-4])
        name = output + "/" + mp2[:-4] + "-textures.txt"
        print("Saving texture list to " + name)
        if not os.path.exists(output2):
            os.makedirs(output2)
        with open(name, 'w') as f:
            for texture in textures:
                f.write(texture + '\n')
        copy_textures(len(textures), texpath, textures, output2)
    save(mp1, texpath, output, stfile)
#picking texture/output paths
def findpath(): #paths
    global texpath
    global output
    texpath = filedialog.askdirectory(initialdir=settings[1],title = "Select the DDS folder")
    if texpath == "":
        quit()
    output = filedialog.askdirectory(initialdir=settings[2],title = "Select the output folder")
    if output == "":
        quit()
if os.name == 'nt':
    stfol = os.path.join(os.getenv('LOCALAPPDATA'), 'Texcop') #settings folder
else: stfol = os.path.join(os.environ['HOME'], '.config', 'Texcop')
stfile = os.path.join(stfol, 'settings.txt') #settings file
#making a settings file
if not os.path.exists(stfol):
    os.makedirs(stfol)
settings = []
if path.exists(stfile):
    with open(stfile, 'r') as f:
        settings = json.loads(f.read())
else: settings = ['/', '/', '/']

root = tk.Tk()
#tkinter icon
img = tk.PhotoImage(data=icon)
root.tk.call('wm', 'iconphoto', root._w, img)
root.withdraw()
#selecting gmds
models = [] 
if len(sys.argv) == 1:
    pickmodels = filedialog.askopenfilenames(initialdir=settings[0],title = "Select the Model",filetypes=(("Model files", "*.gmd"), ("All Files", "*.*")))
    if pickmodels == "":
        quit()
    models = list(pickmodels)
else:        
    models = sys.argv[1:]
#selecting paths for textures and output
if os.path.exists(stfile):
    MsgBox = tk.messagebox.askquestion ('Select paths','Do you want to load previously used paths?',icon = 'question')
    if MsgBox == 'yes':
        texpath = settings[1]
        output = settings[2]
    if MsgBox == 'no':
        findpath()
else:
    findpath()
#going through models and copying textures
dostuff(len(models), models, texpath, output, stfile)
input("Textures copied successfully.\nPress Enter to continue...")