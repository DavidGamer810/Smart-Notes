from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout
import json


try:
    with open("notes.json", "r") as file:
        notes = json.load(file)
except:
    notes = {
        "welcoming": {
            "text": "Welcome to the smart notes app",
            "tags": ["begin", "welcome"]
        },
        "note1": {
            "text": "Salut. Scrie ceva",
            "tags": ["scris", "salut"]
        }
    }


app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle("Smart notes")


list_notes = QListWidget()
list_notes_label = QLabel("List of notes")

button_note_create = QPushButton("Create note")
button_note_del = QPushButton("Delete note")
button_note_save = QPushButton("Save note")

field_tag = QLineEdit()
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

def save_to_file():
    with open("notes.json", "w") as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name")
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_notes.addItem(note_name)
        save_to_file()

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tag.clear()
        field_text.clear()
        list_notes.addItems(notes.keys())
        save_to_file()
    else:
        print("Note to delete is not selected!")

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        save_to_file()
    else:
        print("Note to save is not selected!")


list_notes.itemClicked.connect(show_notes)
list_notes.addItems(notes.keys())

button_note_create.clicked.connect(add_note)
button_note_del.clicked.connect(del_note)
button_note_save.clicked.connect(save_note)


notes_win.show()
app.exec()
