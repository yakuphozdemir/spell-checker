import ttkbootstrap as tbs
from autocorrect import Speller
import re

root = tbs.Window()
root.title("Tetveket")   # TElaffuz Tashihi VE KElime Tadâtı
root.geometry("900x800")
root.minsize(600,500)
#root.iconbitmap("arabic.ico")

a = tbs.Style().theme_names()
b=13
style = tbs.Style(a[b])

langDict =    {
                "English" : "en",
                "Turkish" : "tr",
                "Spanish" : "es",
                "French"  : "fr",
                "Portuguese":"pt",
                "Russian" : "ru",
                "Polish"  : "pl",
                "Italian" : "it",
                "Vietnamese":"vi",
                "Ukrainian": "uk",
                "Greek"   : "el",
                "Czech"   : "cs"
            }

keysList = []
valuesList = []

for key, value in langDict.items():
    keysList.append(key)
    valuesList.append(value)
    
#print(keysList)
#print(valuesList)
#print(type(valuesList[9]))

def spellerize():
    text2.delete(1.0, "end")
    getText = text1.get(1.0, "end")
    
    key = comboBox.get()
    index = keysList.index(key)
    lang = valuesList[index]
    #print(lang)
    
    spell = Speller(lang=lang)
    newText = spell(getText)
    text2.insert(1.0, newText)
    
    res = len(re.findall(r'\w+', newText))
    countLabel.configure(text="Word Number : " + str(res))

def deleteTemp(e):
    global text1
    text1.delete(0.0,"end")
    
def recallTemp(e):
    global text1
    a = text1.get(0.0, "end-1c")
    if a == "":
        text1.insert(0.0, "Please type your text...")

mainLabel = tbs.Label(root, text="Tetveket App", font=('Segoe UI',14))
mainLabel.place(relx=0, rely=0, x=20, y=5, anchor="nw")    
    
text1 = tbs.Text(root)
text1.place(relx=0.5, rely=0, y=70, relheight=0.35, relwidth=0.5 , anchor="n")
text1.insert(0.0, "Please type your text...")
text1.bind("<FocusIn>",deleteTemp)
text1.bind("<FocusOut>",recallTemp)

text2 = tbs.Text(root, width=60, height=15)
text2.place(relx=0.5, rely=0.5, y=70, relheight=0.35, relwidth=0.5 , anchor="n")

spellButton = tbs.Button(root, text="Fix Spelling Errors", command=spellerize)
spellButton.place(in_=text1,rely=1, relx=1, x=8, y=55, anchor="se")

originLabel = tbs.Label(root, text="Original Text", font=('Segoe UI',13))
originLabel.place(in_=text1, relx=0, rely=0, x=-10, y=-45, anchor="nw")

spelledLabel = tbs.Label(root, text="Spelled Text", font=('Segoe UI',13))
spelledLabel.place(in_=text2, relx=0, rely=0, x=-10, y=-45, anchor="nw")

countLabel = tbs.Label(root, text="Word Number : 0")
countLabel.place(in_= text2, relx = 1, rely = 1, anchor = "se")

comboBox = tbs.Combobox(root, bootstyle=a[b], state="readonly", width=10, values=keysList)
comboBox.place(relx=1, x=-18, y=30, anchor="ne")
comboBox.current(0)

root.mainloop()