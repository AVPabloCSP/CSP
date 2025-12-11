from django.shortcuts import render

def calculadora_view(request):
    resultado = None
    if request.method == "POST":
        numero1 = float(request.POST.get("numero1", 0))
        numero2 = float(request.POST.get("numero2", 0))
        operacion = request.POST.get("operacion")
        
        if operacion == "sumar":
            resultado = numero1 + numero2
        elif operacion == "restar":
            resultado = numero1 - numero2
    
    return render(request, "calculadora/index.html", {"resultado": resultado})