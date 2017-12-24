from django.shortcuts import render, HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, "index.html")


def down(request):
    response = []
    response['Content-Disposition'] = 'attachment; filename="happy.jpg"'
    return response


def slide1(request):
    return render(request, "slide1.html")


def nope(request):
    return render(request, "nope.html")


def slide2(request):
    return render(request, "slide2.html")


def code2(request):
    if request.POST['code'] == 'bayes':
        return HttpResponseRedirect('/bproject/macube/')
    else:
        return HttpResponseRedirect('/bproject/me/')


def slide3(request):
    return render(request, "slide3.html")


def code3(request):
    if request.POST['code'] == 'youandme':
        return HttpResponseRedirect('/bproject/hero/')
    else:
        return HttpResponseRedirect('/bproject/macube/')


def slide4(request):
    return render(request, "slide4.html")


def code4(request):
    if request.POST['code'] == 'secretbase':
        response = HttpResponse(request)
        response['Content-Disposition'] = 'attachment; filename="happy.jpg"'
        return response
    else:
        return HttpResponseRedirect('/bproject/damnwerehot/')


def slide5(request):
    return render(request, "slide5.html")


def code5(request):
    if request.POST['code'] == 'sniper':
        return HttpResponseRedirect('/bproject/almost/')
    else:
        return HttpResponseRedirect('/bproject/hero/')


def slide6(request):
    return render(request, "slide6.html")


def code6(request):
    if request.POST['code'] == 'smile':
        return HttpResponseRedirect('/bproject/damnwerehot/')
    else:
        return HttpResponseRedirect('/bproject/almost/')


