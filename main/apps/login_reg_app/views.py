from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return redirect("/users")
# ======================================================================================================================
def users(request):
    return render(request, "login_reg_app/index.html")
# ======================================================================================================================
def reg_login(request):
    return render(request, "login_reg_app/reg_login.html")
# ======================================================================================================================
def reg_login_reg(request):
    debug = 0
# TODO: Press register button on new.html
#  (following strategy from the Flask version)
#  (specifically the POST version)
# TODO: -Step 1: Link to "/users/new"
# TODO: -Step 2: From urls.py jump to users() in views.py
# TODO: -Step 3: FUTURE-TODO: Apply validation
# TODO: -Step 4: Query into the db to create new user
#       -Follow the pattern used in past few Django projects
#       -Follow Django patter from here on.
    return redirect("/users")