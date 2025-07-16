from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

def home(request):
    return HttpResponse("จารุวิทย์ คำพันธ์ 66114540131 ครับ")
#get ออกเป็น json
def get_question(request):
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data)
#ประมวลผลผล POST
def test_post(request):
    if request.method == "POST":
        try:
            question_id = int(request.POST.get('id', 0))
            text = request.POST.get('text', '')
            choices_raw = request.POST.get('choices', '')
            choices = [c.strip() for c in choices_raw.split(',') if c.strip()]

            data = {
                "id": question_id,
                "text": text,
                "choices": choices
            }

            return render(request, "test_post.html", {"result": data})

        except Exception as e:
            return render(request, "test_post.html", {"error": str(e)})
    # สำหรับ GET ปกติ
    return render(request, "test_post.html")

@csrf_exempt
def create_question(request):
    if request.method == "POST":
            body = json.loads(request.body)

            return JsonResponse({
                "id": 9,
                "text": body.get("text"),
                "choices": body.get("choices"),
                "dsd":body.get("text")
            })
    
from .models import Question
from django.views.decorators.csrf import csrf_exempt
import json

