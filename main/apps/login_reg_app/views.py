from django.shortcuts import render, HttpResponse, redirect
from .models import Users
# ======================================================================================================================
def get_user_info(user_id):
  return {'user': Users.objects.get(id=user_id)}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_all_users_info():
  return {'users': Users.objects.all()}
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
def index(request):
  return redirect("/users")
# ======================================================================================================================
def users(request):
  users = get_all_users_info()
  return render(request, "login_reg_app/index.html", users)
# ======================================================================================================================
def reg_login(request):
  return render(request, "login_reg_app/reg_login.html")
# ======================================================================================================================
# ======================================================================================================================
def register(request):
  debug = 0
  # TODO: Press register button on reg_login.html
  #  (following strategy from the Flask version)
  #  (specifically the POST version)
  # TODO: -Step 1: Link to "/users/new"
  # TODO: -Step 2: From urls.py jump to users() in views.py
  # TODO: -Step 3: FUTURE-TODO: Apply validation
  # TODO: -Step 4: Query into the db to create new user
  #       -Follow the pattern used in past few Django projects
  #       -Follow Django patter from here on.

  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  # email = request.POST['email']

  user = Users.objects.create(
    first_name=first_name,
    last_name=last_name)

  return redirect("/users")
# ======================================================================================================================
def users_showUser(request, user_id):
  return render(request, "login_reg_app/show_user.html", get_user_info(user_id))
# ======================================================================================================================
import bcrypt
def login(request):

  password_orig = 'test'
  password_hash = bcrypt.hashpw(password_orig.encode(), bcrypt.gensalt())
  password_test = 'test'
  is_valid = bcrypt.checkpw(password_test.encode(), password_hash)
  return 0
# ======================================================================================================================
