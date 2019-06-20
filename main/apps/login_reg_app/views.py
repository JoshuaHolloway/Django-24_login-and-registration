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

  # TODO: Apply validation
  #  -Do passwords match?
  #  -Does name contain numbers?
  #  -Is name at least one char?
  #  -Does email have proper form?

  # Grab values from form
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password_orig = request.POST['password']
  logged_in = 0

  # Hash Password
  password_hash = bcrypt.hashpw(password_orig.encode(), bcrypt.gensalt())

  # Create row in database
  user = Users.objects.create(
    first_name=first_name,
    last_name=last_name,
    email=email,
    password_hash=password_hash,
    logged_in=logged_in)

  return redirect("/users")
# ======================================================================================================================
def users_showUser(request, user_id):
  return render(request, "login_reg_app/show_user.html", get_user_info(user_id))
# ======================================================================================================================
import bcrypt
def validate_login(request):
  user = Users.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here?
  if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
    print("password match")
  else:
    print("failed password")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def login(request):
  password_orig = 'test'
  password_hash = bcrypt.hashpw(password_orig.encode(), bcrypt.gensalt())
  password_test = 'test'
  is_valid = bcrypt.checkpw(password_test.encode(), password_hash)
  return 0
# ======================================================================================================================
