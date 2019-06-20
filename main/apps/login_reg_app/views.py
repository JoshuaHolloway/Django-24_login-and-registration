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
def root(request):
  # Initialize session
  if 'user_logged_in' not in request.session:
    request.session['user_logged_in'] = {}
  return redirect("/users/reg_login")
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
  # logged_in = 0

  # Hash Password
  password_hash = bcrypt.hashpw(password_orig.encode(), bcrypt.gensalt())

  # Create row in database
  user = Users.objects.create(
    first_name=first_name,
    last_name=last_name,
    email=email,
    password_hash=password_hash)
    #logged_in=logged_in)

  return redirect("/users")
# ======================================================================================================================
# TODO: Show
def users_showUser(request, user_id):
  return render(request, "login_reg_app/show_user.html", get_user_info(user_id))
# ======================================================================================================================
import bcrypt
def login(request):

  # Grab email from form
  email = request.POST['email-login']

  # Grab row from database
  user = Users.objects.get(email=email)

  # Grab entered password and test against stored hash
  password_login = request.POST['password-login']
  if bcrypt.checkpw(password_login.encode(), user.password_hash.encode()):
    print("password match")

    # # Change logged_in field in database to True
    # user.logged_in = 1
    # user.save()

    # Set Session with logged-in users info
    request.session['user_logged_in'] = {
      'id': user.id,
      'first_name': user.first_name,
      'logged_in': True
    }

    return render(request, "login_reg_app/logged_in.html", {'user': user})
  else:
    print("failed password")
    return HttpResponse("You Loose!")

  return 0
# ======================================================================================================================
def logout(request):

  # # Set logged-in to false in database
  # user = get_user_info(id)
  # user.logged_in = 0
  # user.save()

  # Pop session['user_logged_in']
  request.session.pop('user_logged_in')
  return redirect("/")
# ======================================================================================================================