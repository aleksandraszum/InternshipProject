from datetime import datetime

from django.http import Http404, HttpResponse
from django.shortcuts import render
from uuid import uuid4
from mysite.forms import NoteForm, DateHistoryForm
from mysite.models import Note


def index(request):
    # display all newest and not-deleted notes
    notes = Note.objects.filter(deleted=False, newest_version=True)
    return render(request, 'mysite/index.html', {'notes': notes})


def add(request):
    # add a new note
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = str(form['title'].value())
            content = str(form['content'].value())
            note_uuid = uuid4()
            note = Note(title=title, content=content, note_uuid=note_uuid)
            note.save()
            return render(request, 'mysite/add.html', {'communicate': 'Successfully add new note!'})
        else:
            return HttpResponse(status=406)

    form = NoteForm()
    return render(request, 'mysite/add.html', {'form': form})


def edit(request, note_uuid):
    # edit an existed note
    try:
        note = Note.objects.get(note_uuid=note_uuid, newest_version=True, deleted=False)
    except Note.DoesNotExist:
        raise Http404
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
        else:
            return HttpResponse(status=406)

        return render(request, 'mysite/edit.html',
                      {'communicate': 'Successfully edit!'})
    form = NoteForm(instance=note)

    return render(request, 'mysite/edit.html', {'form': form})


def delete(request, note_uuid):
    # delete an existed note
    try:
        note = Note.objects.get(note_uuid=note_uuid, deleted=False, newest_version=True)
    except Note.DoesNotExist:
        raise Http404
    notes = list(Note.objects.filter(note_uuid=note_uuid, deleted=False))
    for note in notes:
        note.deleted = True
        note.save(update_fields=['deleted'])
    return render(request, 'mysite/delete.html', {'communicate': 'Successfully deleted the note!'})


def note_history(request, note_uuid):
    # display a note's history
    try:
        note = Note.objects.get(note_uuid=note_uuid, newest_version=True)
    except Note.DoesNotExist:
        raise Http404
    notes = Note.objects.filter(note_uuid=note_uuid)
    return render(request, 'mysite/notes_history.html', {'notes': notes})


def history(request):
    # display an app's history
    if request.method == 'POST':
        form = DateHistoryForm(request.POST)
        if form.is_valid():
            history_date = str(form['history_data'].value())
            notes = Note.objects.exclude(modified__gt=history_date)
            return render(request, 'mysite/history.html', {'history_date': history_date, 'notes': notes})
        else:
            return HttpResponse(status=406)
    form = DateHistoryForm()
    return render(request, 'mysite/history.html', {'form': form})
