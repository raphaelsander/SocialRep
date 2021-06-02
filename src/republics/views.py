from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from .forms import CreateForm
from .models import Rep


class RepListView(ListView):
    model = Rep


class RepDetailView(DetailView):
    model = Rep


def create_rep(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateForm(request.POST, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('/republics/detail/' + instance.slug)

        else:
            form = CreateForm()

        return render(request, "republics/rep_create.html", {'form': form})

    else:
        return redirect('/accounts/login/')
