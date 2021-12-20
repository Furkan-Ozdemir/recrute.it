from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import Github
from datetime import datetime
from django.utils import timezone


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
                    title=keywords,
                    language=language,
                    added_date=datetime.now(tz=timezone.utc),
                    alt=url["alt"],
                )
                new_github.save()
                print(new_github, new_github.image_url, new_github.github_url)

        # messages.info(request, "Github profile added")
        return redirect("/results")

    return render(request, "index.html")


def results(request):
    people = Github.objects.all()
    return render(request, "results.html", {"people": people})
