from datetime import datetime

from django.shortcuts import render
from uuid import uuid4
from mysite.forms import NoteForm
from mysite.models import Note


def index(request):
    notes = Note.objects.filter(deleted=False, newest_version=True)
    return render(request, 'mysite/index.html', {'notes': notes})


def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = str(form['title'].value())
            content = str(form['content'].value())
            note_uuid = uuid4()
            note = Note(title=title, content=content, note_uuid=note_uuid)
            note.save()
        return render(request, 'mysite/add.html', {'communicate': 'Successfully add new note!'})
    form = NoteForm()
    return render(request, 'mysite/add.html', {'form': form})


def edit(request, note_uuid):
    notes = list(Note.objects.filter(note_uuid=note_uuid))
    version = [note.version for note in notes]
    max_version = max(version)
    note = Note.objects.get(note_uuid=note_uuid, version=max_version)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            old_note = note
            old_note.newest_version = False
            old_note.save(update_fields=['newest_version'])
            title = str(form['title'].value())
            content = str(form['content'].value())
            note_uuid = note_uuid
            created = note.created
            modified = datetime.now()
            version = note.version + 1
            note = Note(title=title, content=content, note_uuid=note_uuid, modified=modified, version=version,
                        created=created)
            note.save()

        return render(request, 'mysite/edit.html',
                      {'communicate': 'Successfully edit!'})
    form = NoteForm(instance=note)

    return render(request, 'mysite/edit.html', {'form': form})


def history(request, note_uuid):
    notes = Note.objects.filter(deleted=False, newest_version=True)
    uuid = [set((note.note_uuid for note in notes))]
    return render(request, 'mysite/index.html', {'notes': notes})

