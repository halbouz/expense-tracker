from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CategoryForm


@login_required
@require_POST
def category_create_view(request):
    form = CategoryForm(request.POST)

    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()

    return redirect("expenses:list")