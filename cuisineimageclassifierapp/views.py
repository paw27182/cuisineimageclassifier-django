from pathlib import Path
from datetime import datetime as dt
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import cuisineimageclassifierapp.command as cmd

mid = Path(__file__).name  # module id
ftime = "%Y/%m/%d %H:%M:%S"

# Create your views here.


class CuisineImageClassifierClass(TemplateView):
    template_name = 'topview.html'


@csrf_exempt
def appmain(request):
    command = request.POST.get('command')
    file_name = request.POST.get('file_name')

    msg = f'{dt.now().strftime(ftime)} [{mid}] -- appmain/ -- command: {command} -- file_name: {file_name} --'
    print(msg)

    if command in ["submit_an_image"]:
        file = request.FILES["data_file"]
        file_name = file.name

        if file_name[-4:] not in [".jpg", ".png"] and file_name[-5:] not in [".jpeg"]:
            return render(request,
                          'area4Result.html',
                          {'message': "NG. Unsupported file type",
                           'alert': "NG"},
                          )

        input_data = file.read()
        answer, images = cmd.predict_image(input_data)

        return render(request,
                      'area4Result.html',
                      {'message': f"OK. The answer is {answer}.",
                       'images': images,
                       'alert': 'OK'},
                      )
    else:
        pass
