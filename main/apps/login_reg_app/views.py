from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return redirect("/users")
# ======================================================================================================================
def users(request):
    return render(request, "login_reg_app/index.html")
# ======================================================================================================================
def users_new(request):
    return render(request, "login_reg_app/new.html")