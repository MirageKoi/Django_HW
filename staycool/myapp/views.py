from django.http import HttpRequest, HttpResponse


def page_zero(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>This is page zero!<h1>")


def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>This is homepage<h1>")


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Welcome to home!")


def progression(request: HttpRequest, start: int, count: int, step: int) -> HttpResponse:
    return HttpResponse(f"{[(start + step * x) for x in range(count)]}")


def greeting(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hello {name}")


def fib(request: HttpRequest, n: int) -> HttpResponse:
    return HttpResponse(f"{fibonacci_of(n)} is {n} element in order")


def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)