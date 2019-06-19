from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "login_reg_app/index.html")
# ======================================================================================================================
def new(request):
    return render(request, "login_reg_app/new.html")