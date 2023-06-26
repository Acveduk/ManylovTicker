from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render

from tickerVideo.forms import TextField
from tickerVideo.models import Ticker

from moviepy.editor import *
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


# Create your views here.

def index(request):
    if request.method == 'GET':
        if request.GET.get('text') is not None:
            p = Ticker(text_ticker=request.GET.get('text'))
            p.save()
            screensize = (100, 100)
            img = ImageClip("img/background.jpg").set_duration(3)
            txt = TextClip(txt=request.GET.get('text'), color=request.GET.get('color'), font=request.GET.get('font'), fontsize=70).set_duration(3)
            size = txt.size[0] if txt.size[0] >= 100 else 100

            video = CompositeVideoClip([img, txt.set_pos(lambda t: (0 - t * ((size-99)/3), 'center'))],
                                       size=screensize)
            video.write_videofile(f'video/{p.id}.mp4', fps=60, codec='mpeg4')
            p.link_to_video = f"video/{p.id}.mp4"
            p.save()
            file = FileWrapper(open(f'video/{p.id}.mp4', 'rb'))
            response = HttpResponse(file, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
            return response

    form = TextField()
    context = {'form': form}
    return render(request, 'tickerVideo/index.html', context)
