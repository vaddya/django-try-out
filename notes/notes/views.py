from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from notes.models import Note


def index(request):
    latest_note_list = Note.objects.order_by('-is_pinned', '-pub_date')[:10]
    context = {
        'latest_note_list': latest_note_list,
    }
    return render(request, 'notes/index.html', context)


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    context = {
        'note': note,
    }
    return render(request, 'notes/detail.html', context)


def save(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.note_text = request.POST['note_text']
    note.mod_date = timezone.now()
    note.save()
    return HttpResponseRedirect(reverse('notes:detail', args=(note_id)))


def remove(request, note_id):
    get_object_or_404(Note, pk=note_id).delete()
    return HttpResponseRedirect(reverse('notes:index'))


def create(request, note_title, note_text, author, is_pinned):
    Note.objects.create(Note(
        note_title=note_title,
        note_text=note_text,
        author=author,
        is_pinned=is_pinned)
    )
    return HttpResponseRedirect(reverse('notes:index'))