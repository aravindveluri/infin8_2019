from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponseRedirect

# Create your views here.
from stage.models import Stage

def create_team(request):
    if request.method == 'POST':
        form = Stage(request.POST or None)
        if form.is_valid():
            do_something_with(form.cleaned_data)
            return redirect("add_team")

        return render_to_response("templates/form.html", {'form': form})