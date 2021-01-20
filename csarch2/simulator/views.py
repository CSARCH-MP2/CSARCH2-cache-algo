from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  #download
  if request.method == "GET":
    file_data = "some text"
    response = HttpResponse(file_data, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="foo.txt"'
    return response
  #compute
  elif request.method == "POST":
    cacheAccessTime = request.POST.get('cache_access_time')
    memoryAccessTime = request.POST.get('memory_access_time')
    sets = request.POST.get('blocks_per_set')
    wordPerBlock = request.POST.get('words_per_block')
    numbers = request.POST.get('input')
    print(request.POST)
  return render(request, 'pages/home.html')
