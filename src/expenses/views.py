from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense

@login_required
def expenses_list_view(request):
    expenses = Expense.objects.filter(user=request.user).select_related("category")

    context = {
        "expenses": expenses,
        "currency": request.user.profile.default_currency,
    }

    return render(request, 'expenses/list.html', context)
