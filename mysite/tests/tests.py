import datetime
import time
from uuid import uuid4
from django.test import TestCase
from django.urls import reverse

from mysite.forms import DateHistoryForm
from mysite.models import Note


class NewestNotesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_notes = 5

        # create 5 notes
        for note_id in range(number_of_notes):
            Note.objects.create(
                title=f'Title {note_id}',
                content=f'text {note_id}',
                note_uuid=uuid4()
            ).save()

        # modified 1st note, count newest version of notes = 5
        test_note_1 = Note.objects.get(id=1)

        note_6 = Note.objects.create(
            title=test_note_1.title,
            content=test_note_1.content,
            created=test_note_1.created,
            modified=datetime.datetime.now(),
            version=test_note_1.version + 1,
            note_uuid=test_note_1.note_uuid,
        )
        note_6.save()
        test_note_1.newest_version = False
        test_note_1.save(update_fields=['newest_version'])

        # modified 6th note, count newest version of notes is still = 5
        note_7 = Note.objects.create(
            title=note_6.title,
            content=note_6.content,
            created=note_6.created,
            modified=datetime.datetime.now(),
            version=note_6.version + 1,
            note_uuid=note_6.note_uuid,
        )
        note_7.save()
        note_6.newest_version = False
        note_6.save(update_fields=['newest_version'])

        # delete 3 note, count newest version of notes = 4
        test_note_3 = Note.objects.get(id=3)
        test_note_3.deleted = True
        test_note_3.save(update_fields=['deleted'])

    def test_display_all_newest_notes(self):
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 4)

    def test_add_note(self):
        response = self.client.get('/notes/add/')
        self.assertEqual(response.status_code, 200)

    def test_edit_note(self):
        note_uuid = Note.objects.get(id=2).note_uuid
        edit_url = '/notes/edit/{}/'.format(note_uuid)
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        bad_note_uuid = note_uuid+'5'
        bad_edit_url = '/notes/edit/{}/'.format(bad_note_uuid)
        response = self.client.get(bad_edit_url)
        self.assertEqual(response.status_code, 404)

    def test_delete_notes(self):
        note_uuid = Note.objects.get(id=1).note_uuid
        delete_url = '/notes/delete/{}/'.format(note_uuid)
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        note_deleted_uuid = Note.objects.get(id=3).note_uuid
        delete_notes_deleted_url = '/notes/delete/{}/'.format(note_deleted_uuid)
        response = self.client.get(delete_notes_deleted_url)
        self.assertEqual(response.status_code, 404)

        note_bad_uuid = '12345'
        bad_deleted_url = '/notes/delete/{}/'.format(note_bad_uuid)
        response = self.client.get(bad_deleted_url)
        self.assertEqual(response.status_code, 404)

    def test_note_history(self):
        note_uuid = Note.objects.get(id=1).note_uuid
        history_url = '/notes/history/{}/'.format(note_uuid)
        response = self.client.get(history_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 3)

        note_bad_uuid = '12345'
        history_bad_url = '/notes/history/{}/'.format(note_bad_uuid)
        response = self.client.get(history_bad_url)
        self.assertEqual(response.status_code, 404)

    def test_history(self):
        future_date = datetime.datetime.today() + datetime.timedelta(days=1)
        form = DateHistoryForm(data={'history_date': future_date})
        self.assertTrue(form.is_valid())
        response = self.client.get(reverse('history'), kwargs={'history_date': future_date})
        self.assertEqual(response.status_code, 200)

        last_date = datetime.datetime.today() + datetime.timedelta(days=1)
        form_2 = DateHistoryForm(data={'history_date': last_date})
        self.assertTrue(form_2.is_valid())
        response = self.client.get(reverse('history'), kwargs={'history_date': future_date})
        self.assertEqual(response.status_code, 200)

        form_3 = DateHistoryForm(data={'history_date': None})
        self.assertFalse(form_3.is_valid())
