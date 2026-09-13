from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

my_notes = []


class Note(BaseModel):
    id: int
    title: str
    content: str


# GET - Get all notes
@app.get("/notes")
def get_all_notes():
    return {"notes": my_notes}


# POST - Add a new note
@app.post("/notes")
def create_note(new_note: Note):
    my_notes.append(new_note)
    return {"message": "Note added successfully!"}


# PUT - Update an existing note
@app.put("/notes/{id}")
def update_note(id: int, updated_note: Note):
    for i in range(len(my_notes)):
        if my_notes[i].id == id:
            my_notes[i] = updated_note
            return {"message": "Note updated successfully!"}

    return {"error": "Note not found"}


# DELETE - Delete a note
@app.delete("/notes/{id}")
def delete_note(id: int):
    for i in range(len(my_notes)):
        if my_notes[i].id == id:
            del my_notes[i]
            return {"message": "Note deleted successfully!"}

    return {"error": "Note not found"}