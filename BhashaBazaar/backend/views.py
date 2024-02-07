from django.http import JsonResponse
from django.shortcuts import render
from google.cloud import translate_v2 as translate
# Create your views here.

def text_translator(request):
    translator = translate()
    if request.method == 'GET':
        input_text = request.GET['input_text']
        target_language = request.GET['target_language']
        detected_language = translator.detect(input_text).lang
        if detected_language == target_language:
            return JsonResponse({'translated_text': input_text})
        translate_client = translate.Client()
        translation = translate_client.translate(input_text, target_language=target_language)
        translated_text = translation['translatedText']
        return JsonResponse({'translated_text': translated_text})



def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')