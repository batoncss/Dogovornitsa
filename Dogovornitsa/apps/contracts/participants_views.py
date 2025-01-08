from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from Dogovornitsa.apps.contracts.forms import ParticipantForm
from Dogovornitsa.apps.contracts.models import Participant


def participants(request):
    form_is_invalid = False
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новую запись
            return redirect('participants')  # Перезагрузка страницы
        else:
            form_is_invalid = True
    else:
        form = ParticipantForm()
    search_query = request.GET.get('search', '')
    order_by = request.GET.get('order_by', 'name')
    order_direction = request.GET.get('order_direction', '')
    per_page = request.GET.get('per_page', '') if request.GET.get('per_page', '').isdigit() else 5

    all_participants = Participant.objects.filter(name__contains=search_query).order_by(order_by if order_direction == 'asc' else "-" + order_by)
    paginator = Paginator(all_participants, per_page)

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, "contracts/participants.html", {
        "page_obj": page_obj,
        'form': form,
        "form_is_invalid": form_is_invalid,
        'current_get_params': request.GET.urlencode()
    })


def participants_delete(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    participant.delete()
    return redirect('participants')  # Перезагрузка страницы

def participant_detail(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    edit_mode = request.GET.get('edit_mode', 'false') == 'true'
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant-detail', participant_id=participant.id)  # Перезагрузка страницы
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'contracts/participant-detail.html', {
        'participant': participant,
        'edit_mode': edit_mode,
        'form': form
    })
