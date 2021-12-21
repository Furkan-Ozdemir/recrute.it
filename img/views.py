from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import Github
from datetime import datetime
from django.utils import timezone
from random import randint
from decouple import config


# Create your views here.


def index(request):
    TOKEN = config("TOKEN")

    if request.method == "POST":
        keywords = request.POST["keywords"]
        language = request.POST["language"]
        query_amount = request.POST["query_amount"]
        # query_amount = "13"  # hard coded due to search api limit

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
                headers = {"Authorization": "token " + TOKEN}
                r = requests.get(
                    "https://api.github.com/search/repositories?q=language:"
                    + language
                    + "+user:"
                    + url["alt"].strip("@"),
                    headers=headers,
                )
                repos = r.json()
                print(repos["total_count"])
                if not Github.objects.filter(alt=url["alt"]).exists():
                    new_github = Github(
                        image_url=url["src"].replace("s=40", "s=200"),
                        github_url="https://github.com/" + url["alt"].strip("@"),
                        title=keywords,
                        language=language,
                        added_date=datetime.now(tz=timezone.utc),
                        alt=url["alt"],
                        repo_count=int(repos["total_count"]),
                    )
                    new_github.save()

        return redirect(
            reverse("results")
            + "?keywords="
            + keywords
            + "&language="
            + language
            + "&query_amount="
            + query_amount
        )

    return render(request, "index.html")


def results(request):
    keywords = request.GET.get("keywords", "")
    language = request.GET.get("language", "")
    query_amount = request.GET.get("query_amount", "")
    people = Github.objects.filter(title=keywords, language=language)

    return render(
        request,
        "results.html",
        {
            "people": people[: int(query_amount)],
        },
    )
