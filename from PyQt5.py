from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json


app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle("Smart notes")
list_notes = QListWidget()
list_notes_label = QLabel("List of notes")

notes = {
    
    "welcoming": {
        "text" : "Welcome to the smart notes app",
        "tags" : ["begin", "welcome"]
    },
    "note1": {
        "text" : "Salut.Scrie ceva",
        "tags" : ["scris","salut"]
    }
}

with open("notes.json", "w") as file:
    json.dump(notes,file,ensure_ascii=False)


button_note_create = QPushButton("Create note")
button_note_del = QPushButton("Delete note")
button_note_save = QPushButton("Save note")

field_tag = QLineEdit(' ')
field_tag.setPlaceholderText("Enter tag...")
field_text = QTextEdit()

button_add = QPushButton("Add to note")
button_del = QPushButton("Untag from note")
button_search = QPushButton("Search notes by tag")
list_tag = QListWidget()
list_tags_label = QLabel("List of tags")

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)


def show_notes():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["text"])
    list_tag.clear()
    list_tag.addItems(notes[key]["tags"])

list_notes.itemClicked.connect(show_notes)
list_notes.addItems(notes)

def add_note():
    note_name,ok = QInputDialog.getText(notes_win, "Add note", "Note name")
    if ok and note_name != "":
        notes[note_name] = {"text" :"","tags" : []}
        list_notes.addItems(note_name)
        list_tag.addItems(notes[note_name]["tags"])
        print(notes)

def del_note():
    

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes.json", "w")as file:
            json.dump(notes,file,sort_keys = True, ensure_ascii= False)
        print(notes)
    else:
        print("Note to save is not selected!")

notes_win.show()
app.exec()
