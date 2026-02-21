from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Expense
from .forms import ExpenseForm

@login_required
def expenses_list_view(request):
    expenses = Expense.objects.filter(user=request.user).select_related("category")
    form = ExpenseForm(user=request.user)

    context = {
        "expenses": expenses,
        "form": form,
    }

    return render(request, 'expenses/list.html', context)

@login_required
@require_POST
def expense_create_view(request):
    form = ExpenseForm(request.POST, user=request.user)
    if form.is_valid():
        form.save()
    return redirect("expenses:list")


@login_required
@require_POST
def expense_delete_view(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect("expenses:list")