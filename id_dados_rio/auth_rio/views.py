# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render

from .utils import (
    get_redirect_uri,
    is_authenticated,
    store_access,
    validate_recaptcha_token,
)


def auth(request: HttpRequest) -> HttpResponse:
    """
    This returns either 200 or 401. For either case, we store the
    access log in the database.

    How it works:

    - First, it tries to extract the desired domain from the request.
    - If it fails, it returns a 401.

    - Then, if there's an user logged in, it iterates over its tokens,
        looking for a token with the desired domain.
    - If it finds one, it returns a 200.
    - If it doesn't, it returns a 401.

    - Finally, if no user is logged in, tries to extract the token from
        the request headers.
    - If it finds one, it checks if it's valid for the domain.
    - If it is, it returns a 200.
    - If it isn't, it returns a 401.

    - If no token is found, it returns a 401.
    """
    _, token, domain, user, success = is_authenticated(request)
    if not success:
        store_access(token=token, domain=domain, user=user, success=success)
    if success:
        return HttpResponse(status=200)
    return HttpResponse(status=401)


def signin(request: HttpRequest) -> HttpResponse:
    """
    Sign in page.
    """
    redirect_uri, _, _, user, success = is_authenticated(request)
    if success:
        if redirect_uri:
            return redirect(redirect_uri)
        return HttpResponse(
            "You are already signed in. <a href='/auth/logout/'>Sign out</a>."
        )
    if request.user and request.user.is_authenticated:
        if redirect_uri:
            return HttpResponse("You do not have access to this page.", status=401)
        return HttpResponse(
            "You are already signed in. <a href='/auth/logout/'>Sign out</a>."
        )
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        recaptcha_response = request.POST.get("g-recaptcha-response", None)
        if (not recaptcha_response) or (
            not validate_recaptcha_token(recaptcha_response)
        ):
            return HttpResponse(
                "Captcha is invalid. <a href='/auth/login/'>Try again</a>.", status=401
            )
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if redirect_uri:
                    return redirect(redirect_uri)
                return HttpResponse(
                    "You are now signed in. <a href='/auth/logout/'>Sign out</a>."
                )
        return HttpResponse("Invalid username or password.", status=401)
    return render(
        request,
        "signin.html",
        context={"recaptcha_site_key": settings.RECAPTCHA_SITE_KEY},
    )


def signout(request: HttpRequest) -> HttpResponse:
    """
    Sign out page.
    """
    if request.user.is_authenticated:
        logout(request)
        redirect_url = get_redirect_uri(request, default=None)
        if redirect_url:
            return redirect(redirect_url)
        return HttpResponse(
            "You are now signed out. <a href='/auth/login/'>Sign in</a>."
        )
    return HttpResponse(
        "You are not signed in. <a href='/auth/login/'>Sign in</a>.", status=401
    )
