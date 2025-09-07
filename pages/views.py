from django.shortcuts import render
from .models import Calculation


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def calculator(request):
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1", 0))
            num2 = float(request.POST.get("num2", 0))
            operation = request.POST.get("operation")

            symbol = ""
            if operation == "+":
                result = num1 + num2
                symbol = "+"
            elif operation == "-":
                result = num1 - num2
                symbol = "-"
            elif operation == "*":
                result = num1 * num2
                symbol = "×"
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                    symbol = "÷"
                else:
                    result = None   
                    symbol = "÷"

            
            if result is not None:
                Calculation.objects.create(
                    num1=num1,
                    num2=num2,
                    operation=symbol,
                    result=result
                )
        except Exception:
            result = "Error"


    history = Calculation.objects.all().order_by("-created_at")[:5]

    return render(request, "pages/calculator.html", {
        "result": result,
        "calculations": history   
    })