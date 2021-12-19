from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import Github

# Create your views here.


def index(request):
    if request.method == "POST":
        keywords = request.POST["keywords"]
        language = request.POST["language"]
        query_amount = request.POST["query_amount"]
        for i in range(1, int(query_amount) // 10 + 1):
            github_url = (
                "https://github.com/search?l="
                + language
                + "&p="
                + str(i)
                + "&q="
                + keywords
                + "&type=Users"
            )
            r = requests.get(github_url)
            soup = BeautifulSoup(r.content, "html.parser")
            profile_image_url_list = soup.find_all(
                "img", {"class": "avatar-user"}, limit=15
            )  # [src]

            for url in profile_image_url_list:
                new_github = Github(
                    image_url=url["src"],
                    github_url="https://github.com/" + url["alt"].strip("@"),
                )
                new_github.save()
                print(new_github, new_github.image_url, new_github.github_url)

        # messages.info(request, "Github profile added")
        return redirect("/")

    return render(request, "index.html")


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         password2 = request.POST["password2"]

#         if password == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "Username taken")
#                 return redirect("register")
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "Email taken")
#                 return redirect("register")
#             else:
#                 user = User.objects.create_user(
#                     username=username, password=password, email=email
#                 )
#                 user.save()
#                 messages.success(request, "User created")
#                 return redirect("login")
#         else:
#             messages.info(request, "Passwords do not match")
#             return redirect("register")
#     else:
#         return render(request, "signup.html")


# def login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect("/")
#         else:
#             messages.info(request, "Invalid credentials")
#             return redirect("login")
#     return render(request, "login.html")


# def logout(request):
#     auth.logout(request)
#     return redirect("login")


def images(request):
    username = request.user.username
    github = Github.objects.filter(username=username)
    return render(request, "images.html", {"github": github})
