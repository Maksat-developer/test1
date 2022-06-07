from django.shortcuts import render


def index(requests):
    return render(requests, "shopkg/index.html")
