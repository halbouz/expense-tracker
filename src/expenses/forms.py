# expenses/forms.py
from django import forms
from .models import Expense
from categories.models import Category


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["date", "amount", "category", "description"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is None:
            raise ValueError("ExpenseForm requires a user.")

        self.user = user

        # Restrict categories to this user only
        self.fields["category"].queryset = Category.objects.filter(user=user)

    def save(self, commit=True):
        expense = super().save(commit=False)
        expense.user = self.user

        if expense.pk is None:
            expense.currency = self.user.profile.default_currency

        if commit:
            expense.save()
            self.save_m2m()

        return expense