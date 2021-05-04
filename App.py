from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image
import pprint
from Ciphers import Cipher
import os


def changeTextboxText(textbox, text):
    textbox.config(state=NORMAL)
    textbox.delete(1.0, "end")
    textbox.insert(1.0, text)
    textbox.config(state=DISABLED)


def myCaesar(textbox):
    description = "Cipher description: " + "\n" + "A Caesar Cipher is a mono-alphabetic cipher in which shifts the " \
                                                  "letters a certain amount using an additive key. "
    changeTextboxText(textbox, description)

    Canvas(root, background="white", bd=0, relief='ridge', highlightthickness=3,
           highlightbackground="black", height=root_height() * .50,
           width=root_width() * .3375).place(x=915, y=400)

    labelShift = Label(root, text="Shift of cipher: ", font=("Times New Roman", 16))
    labelShift.place(x=930, y=420)
    shift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                 font=("Times New Roman", 12))
    shift.place(x=1075, y=420)
    Button(root, command=lambda: encrypt_caesar(), text="Encrypt Image", font=("Times New Roman", 16), padx=10).place(
        x=935, y=775)
    Button(root, command=lambda: decrypt_caesar(), text="Decrypt Image", font=("Times New Roman", 16), padx=10).place(
        x=1215, y=775)

    def encrypt_caesar():
        global cipher
        cipher.encode_caesar(int(shift.get("1.0", END)))

        global current_image_filename
        temp = os.path.basename(current_image_filename)

        current_image_filename = os.getcwd() + "\\Encoded_Images\\" + temp
        cipher = Cipher(in_url=current_image_filename)
        show_img(cipher.in_url)

    def decrypt_caesar():
        print(os.path.isfile(cipher.in_url))
        print(int(shift.get("1.0", END)))
        cipher.decode_caesar(int(shift.get("1.0", END)))
        show_img(os.getcwd() + "\\Decoded_Images\\" + os.path.basename(cipher.in_url))


def myMultiplicative(textbox):
    description = "Cipher description: " + "\n" + "A Multiplicative Cipher uses a key multiple of the alphabet to " \
                                                  "shift the letters.It is evident from the relative ease with which " \
                                                  "the Caesar Cipher – or its generalization to an arbitrary number " \
                                                  "of positions of shift – has been solved, that such a system offers " \
                                                  "very little security.  Let us think up a different method of " \
                                                  "enciphering a message.  Instead of adding a key number to the " \
                                                  "equivalents of the plain text letters, we shall multiply by the " \
                                                  "key number.  Abraham Sinkov, Elementary Cryptanalysis. "
    changeTextboxText(textbox, description)

    Canvas(root, background="white", bd=0, relief='ridge', highlightthickness=3,
           highlightbackground="black", height=root_height() * .50,
           width=root_width() * .3375).place(x=915, y=400)

    labelXShift = Label(root, text="X Shift of cipher: ", font=("Times New Roman", 16))
    labelXShift.place(x=930, y=420)
    xShift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                  font=("Times New Roman", 12))
    xShift.place(x=1080, y=420)

    labelYShift = Label(root, text="Y Shift of cipher: ", font=("Times New Roman", 16))
    labelYShift.place(x=930, y=460)
    yShift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                  font=("Times New Roman", 12))
    yShift.place(x=1080, y=460)
    Button(root, command=lambda: encrypt_multiplicative(), text="Encrypt Image", font=("Times New Roman", 16),
           padx=10).place(x=935, y=775)
    Button(root, command=lambda: decrypt_multiplicative(), text="Decrypt Image", font=("Times New Roman", 16),
           padx=10).place(x=1215, y=775)
    Button(root, command=lambda: show_possible_keys(), text="Show Possible Inverse Values",
           font=("Times New Roman", 16),
           padx=10).place(x=930, y=495)

    def show_possible_keys():
        global cipher
        xmult_table = Cipher.calculate_multiplicative_keys(cipher.xres)
        ymult_table = Cipher.calculate_multiplicative_keys(cipher.yres)
        x_values = "Possible X Values:"
        x_counter = 0
        for key in xmult_table:
            if x_counter < 20:
                x_values += (" " + str(key))
                x_counter = x_counter + 1

        y_values = "Possible Y Values:"
        y_counter = 0
        for key in ymult_table:
            if y_counter < 20:
                y_values += (" " + str(key))
                y_counter = y_counter + 1

        pprint.pprint(x_values)
        pprint.pprint(y_values)

        possibleXTextbox = Text(root, height=int(root_height() * .0035), width=int(root_width() * .0275), wrap=WORD,
                                font=("Times New Roman", 16))
        possibleYTextbox = Text(root, height=int(root_height() * .0035), width=int(root_width() * .0275), wrap=WORD,
                                font=("Times New Roman", 16))
        possibleXTextbox.place(x=930, y=530)
        possibleYTextbox.place(x=930, y=600)

        possibleXTextbox.config(state=NORMAL)
        possibleXTextbox.delete(1.0, "end")
        possibleXTextbox.insert(1.0, x_values)
        possibleXTextbox.config(state=DISABLED)

        possibleYTextbox.config(state=NORMAL)
        possibleYTextbox.delete(1.0, "end")
        possibleYTextbox.insert(1.0, y_values)
        possibleYTextbox.config(state=DISABLED)

    def encrypt_multiplicative():
        global cipher
        cipher.encode_multiplicative(int(xShift.get("1.0", END)), int(yShift.get("1.0", END)))

        global current_image_filename
        temp = os.path.basename(current_image_filename)

        current_image_filename = os.getcwd() + "\\Encoded_Images\\" + temp
        cipher = Cipher(in_url=current_image_filename)
        show_img(cipher.in_url)

    def decrypt_multiplicative():
        cipher.decode_multiplicative(int(xShift.get("1.0", END)), int(yShift.get("1.0", END)))
        show_img(os.getcwd() + "\\Decoded_Images\\" + os.path.basename(cipher.in_url))

    if current_image_filename is not "":
        pass


def myAffine(textbox):
    description = "Cipher description: " + "\n" + "The affine cipher is a type of monoalphabetic substitution cipher, " \
                                                  "where each letter in an alphabet is mapped to its numeric " \
                                                  "equivalent, encrypted using a simple mathematical function, " \
                                                  "and converted back to a letter. The formula used means that each " \
                                                  "letter encrypts to one other letter, and back again, meaning the " \
                                                  "cipher is essentially a standard substitution cipher with a rule " \
                                                  "governing which letter goes to which. As such, it has the " \
                                                  "weaknesses of all substitution ciphers. Each letter is enciphered " \
                                                  "with the function (ax + b) mod 26, where b is the magnitude of the " \
                                                  "shift. "
    changeTextboxText(textbox, description)

    Canvas(root, background="white", bd=0, relief='ridge', highlightthickness=3,
           highlightbackground="black", height=root_height() * .50,
           width=root_width() * .3375).place(x=915, y=400)

    labelXShift = Label(root, text="X Shift of cipher: ", font=("Times New Roman", 16))
    labelXShift.place(x=930, y=420)
    xShift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                  font=("Times New Roman", 12))
    xShift.place(x=1080, y=420)

    labelYShift = Label(root, text="Y Shift of cipher: ", font=("Times New Roman", 16))
    labelYShift.place(x=930, y=460)
    yShift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                  font=("Times New Roman", 12))
    yShift.place(x=1080, y=460)

    # todo: additive and multiplicative shift label
    labelAffineShift = Label(root, text="Caesar Shift of cipher", font=("Times New Roman", 16))
    labelAffineShift.place(x=930, y=650)
    affineShift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                  font=("Times New Roman", 12))
    affineShift.place(x=1115, y=650)

    Button(root, command=lambda: encrypt_multiplicative(), text="Encrypt Image", font=("Times New Roman", 16),
           padx=10).place(x=935, y=775)
    Button(root, command=lambda: decrypt_multiplicative(), text="Decrypt Image", font=("Times New Roman", 16),
           padx=10).place(x=1215, y=775)
    Button(root, command=lambda: show_possible_keys(), text="Show Possible Inverse Values",
           font=("Times New Roman", 16),
           padx=10).place(x=930, y=495)


    def show_possible_keys():
        global cipher
        xmult_table = Cipher.calculate_multiplicative_keys(cipher.xres)
        ymult_table = Cipher.calculate_multiplicative_keys(cipher.yres)
        x_values = "Possible X Values:"
        x_counter = 0
        for key in xmult_table:
            if x_counter < 20:
                x_values += (" " + str(key))
                x_counter = x_counter + 1

        y_values = "Possible Y Values:"
        y_counter = 0
        for key in ymult_table:
            if y_counter < 20:
                y_values += (" " + str(key))
                y_counter = y_counter + 1

        pprint.pprint(x_values)
        pprint.pprint(y_values)

        possibleXTextbox = Text(root, height=int(root_height() * .0035), width=int(root_width() * .0275), wrap=WORD,
                                font=("Times New Roman", 16))
        possibleYTextbox = Text(root, height=int(root_height() * .0035), width=int(root_width() * .0275), wrap=WORD,
                                font=("Times New Roman", 16))
        possibleXTextbox.place(x=930, y=530)
        possibleYTextbox.place(x=930, y=600)

        possibleXTextbox.config(state=NORMAL)
        possibleXTextbox.delete(1.0, "end")
        possibleXTextbox.insert(1.0, x_values)
        possibleXTextbox.config(state=DISABLED)

        possibleYTextbox.config(state=NORMAL)
        possibleYTextbox.delete(1.0, "end")
        possibleYTextbox.insert(1.0, y_values)
        possibleYTextbox.config(state=DISABLED)

    def encrypt_multiplicative():
        global cipher
        cipher.encode_affine(int(xShift.get("1.0", END)), int(yShift.get("1.0", END)), int(affineShift.get("1.0", END)))

        global current_image_filename
        temp = os.path.basename(current_image_filename)

        current_image_filename = os.getcwd() + "\\Encoded_Images\\" + temp
        cipher = Cipher(in_url=current_image_filename)
        show_img(cipher.in_url)

    def decrypt_multiplicative():
        cipher.decode_affine(int(xShift.get("1.0", END)), int(yShift.get("1.0", END)), int(affineShift.get("1.0", END)))
        show_img(os.getcwd() + "\\Decoded_Images\\" + os.path.basename(cipher.in_url))

    if current_image_filename is not "":
        pass


def myVigenere(textbox):
    description = "Cipher description: " + "\n" + "The Vigenère cipher (French pronunciation: ​[viʒnɛːʁ]) is a method " \
                                                  "of encrypting alphabetic text by using a series of interwoven " \
                                                  "Caesar ciphers, based on the letters of a keyword. It employs a " \
                                                  "form of polyalphabetic substitution. "
    changeTextboxText(textbox, description)

    Canvas(root, background="white", bd=0, relief='ridge', highlightthickness=3,
           highlightbackground="black", height=root_height() * .50,
           width=root_width() * .3375).place(x=915, y=400)

    labelShift = Label(root, text="Cipher Keyword: ", font=("Times New Roman", 16))
    labelShift.place(x=930, y=420)
    keyword = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                 font=("Times New Roman", 12))
    keyword.place(x=1075, y=420)
    Button(root, command=lambda: encrypt_vigenere(), text="Encrypt Image", font=("Times New Roman", 16), padx=10).place(
        x=935, y=775)
    # Button(root, command=lambda: decrypt_vigenere(), text="Decrypt Image", font=("Times New Roman", 16),
    # padx=10).place( x=1215, y=775)

    def encrypt_vigenere():
        global cipher
        cipher.encode_vigenere(keyword.get("1.0", END))

        global current_image_filename
        temp = os.path.basename(current_image_filename)

        current_image_filename = os.getcwd() + "\\Encoded_Images\\" + temp
        cipher = Cipher(in_url=current_image_filename)
        show_img(cipher.in_url)

    """
    def decrypt_vigenere():
        print(os.path.isfile(cipher.in_url))
        print(int(shift.get("1.0", END)))
        cipher.decode_vigenere(keyword.get("1.0", END))
        show_img(os.getcwd() + "\\Decoded_Images\\" + os.path.basename(cipher.in_url))
    """


def root_width():
    root.update()
    return root.winfo_width()


def root_height():
    root.update()
    return root.winfo_height()


'''
def upload():
    root.update()
    return Label(text="Upload").grid(row=20,column=25)
affine_button = Radiobutton(root,text="Affine",value="Affine",variable=StringVar().set(' '),command=lambda: myAffine(T))
vigenere_button = Radiobutton(root,text="Vigenere",value="Vigenere",
                              variable=StringVar().set(' '),command=lambda: myVigenere(T))
'''


def openfn():
    global current_image_filename
    global cipher
    filename = filedialog.askopenfilename(title='Upload')
    current_image_filename = filename
    cipher = Cipher(in_url=current_image_filename)
    return filename


def savefn():
    filename = filedialog.asksaveasfilename(title='Save', filetypes=[("all files", "*."), (".jpg", "*.jpg"),
                                                                     (".png", "*.png"), (".jpeg", "*.jpeg")])
    with Image.open(filename) as im:
        im.save(filename + "downloaded" + ".jpg")
    return filename


def open_img():
    x = openfn()
    show_img(x)


def show_img(x):
    img = Image.open(x)
    img = img.resize((int(root_width() * .6185), int(root_height() * .7410)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=30, y=32)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1400x850")
    root.title("Crymage - Image Cryptography Software")
    root.iconbitmap("crymage.ico")

    cipher = None
    current_image_filename = ""

    T = Text(root, height=int(root_height() * .0175), width=int(root_width() * .0225), wrap=WORD,
             font=("Times New Roman", 16))
    T.place(x=1050, y=25)

    caesar_button = Radiobutton(root, text="Caesar", value="Caesar", command=lambda: myCaesar(T))
    caesar_button.select()

    multiplicative_button = Radiobutton(root, text="Multiplicative", value="Multiplicative",
                                        variable=StringVar().set(' '), command=lambda: myMultiplicative(T))
    affine_button = Radiobutton(root, text="Affine", value="Affine",
                                        variable=StringVar().set(' '), command=lambda: myAffine(T))
    vigenere_button = Radiobutton(root, text="Vigenere", value="Vigenere",
                                variable=StringVar().set(' '), command=lambda: myVigenere(T))
    # These two are the buttons for the Caesar and Multiplicative Ciphers
    caesar_button.place(x=925, y=25)
    multiplicative_button.place(x=925, y=50)
    affine_button.place(x=925, y=75)
    vigenere_button.place(x=925, y=100)

    '''affine_button.place(x=425,y=75)
    vigenere_button.place(x=425,y=100)'''

    # This is creating canvas' in which but all of the buttons in the root and all of the boxes in the root as well.
    imageCanvas = Canvas(bg="White", bd=0, highlightthickness=3, highlightbackground="black", width=root_width() * .625,
                         height=root_height() * .75).place(x=25, y=25)

    '''uploadDownloadCanvas = Canvas(root,background="white",bd=0,relief='ridge',highlightthickness=3,
                       highlightbackground="black", height=root_height()*.10, width=root_width()*.50).place(x=0,y=410)'''

    # More buttons, this time upload and download buttons
    uploadButton = Button(root, text="Upload Image", font=("Times New Roman", 16), padx=20, command=open_img).place(
        x=225, y=750)
    downloadButton = Button(root, text="Download Image", font=("Times New Roman", 16), command=savefn, padx=10).place(
        x=450, y=750)

    cipherFrame = Canvas(root, background="white", bd=0, relief='ridge', highlightthickness=3,
                         highlightbackground="black", height=root_height() * .50,
                         width=root_width() * .3375).place(x=915, y=400)

    labelShift = Label(root, text="Shift of cipher: ", font=("Times New Roman", 16))
    labelShift.place(x=930, y=420)
    encryptButton = Button(root, text="Encrypt Image", font=("Times New Roman", 16), padx=10).place(x=935, y=775)
    decryptButton = Button(root, text="Decrypt Image", font=("Times New Roman", 16), padx=10).place(x=1215, y=775)
    Shift = Text(root, height=int(root_height() * .00125), width=int(root_width() * .02475),
                 font=("Times New Roman", 12))
    Shift.place(x=1075, y=420)

    root.mainloop()
