import pywhatkit
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@xframe_options_sameorigin
def staffhomeview(request):
    if request.method == 'POST':
        button_clicked = request.POST.get('buttonClicked', None)
        if button_clicked == 'button1':
            data = {}
            api_url = "http://127.0.0.1:8000/page/student/"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
            # Render the template and set the header
            return render(request, 'Staffview.html', {'data': data})
        elif button_clicked == 'button2':
            return render(request, 'Staffview.html')
        elif button_clicked == 'button3':
            return render(request, 'Staffview.html')
    return render(request, 'staffview.html')


@xframe_options_sameorigin
def dynamiccontentview(request):
    return render(request, 'DynamicContentView.html')


@csrf_exempt
@xframe_options_sameorigin
def send_whatsapp_message(request):
    to_number = ""
    message_body = ""
    if request.method == 'POST':
        try:
            to_number = request.POST.get('StudentReference')  # Get recipient's number from POST data
            message_body = request.POST.get('Sendmessage')
            pywhatkit.sendwhatmsg_instantly(to_number, message_body)
            return render(request, 'Staffview.html')  # Return response_data in all cases
        # Too broad exception clause
        except ValueError:
            if not to_number or not message_body:
                return HttpResponse(request, "Enter a correct number")
