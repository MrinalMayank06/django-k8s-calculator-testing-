from django.shortcuts import render

def calculator(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST["num1"])
        num2 = float(request.POST["num2"])
        op = request.POST["op"]

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result = "Error: Division by zero not allowed"
            else:
                result = num1 / num2

    return render(request, "index.html", {"result": result})