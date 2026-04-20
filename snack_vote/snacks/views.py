from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Snack, Vote
from .forms import SnackForm


def index(request):
    snacks = Snack.objects.all().order_by("-created_at")
    form = SnackForm()
    return render(request, "snacks/index.html", {"snacks": snacks, "form": form})


@require_POST
def add_snack(request):
    form = SnackForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("index")


@require_POST
def vote(request, snack_id):
    snack = get_object_or_404(Snack, id=snack_id)
    vote_type = request.POST.get("vote_type")

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    existing = Vote.objects.filter(snack=snack, session_key=session_key).first()

    if existing:
        if existing.vote_type == vote_type:
            existing.delete()
            user_vote = None
        else:
            existing.vote_type = vote_type
            existing.save()
            user_vote = vote_type
    else:
        Vote.objects.create(snack=snack, vote_type=vote_type, session_key=session_key)
        user_vote = vote_type

    return JsonResponse({
        "agree": snack.agree_count(),
        "disagree": snack.disagree_count(),
        "agree_percent": snack.agree_percent(),
        "user_vote": user_vote,
    })
