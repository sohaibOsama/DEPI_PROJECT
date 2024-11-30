from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .sentiment_model import classify
# Create your views here.
def index(request):
    # vars = {'response': classify('Hello, this is the best')}
    return render(request, 'chatbot/index.html')


# Simulating a chat model response (you can replace this with your actual model)
async def get_chat_response(message):
    # Simulating a delay to mimic asynchronous behavior (like calling an external AI API)
    import asyncio
    await asyncio.sleep(.25)  # Simulate time taken by the model to respond
    return f"That's {classify(message)[0]} Opinion!"

@csrf_exempt
async def chat_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the JSON body
            message = data.get('message', '')  # Get the 'message' from the body
            
            # Get the chat response from your chat model (async function)
            ai_response = await get_chat_response(message)
            
            # Return the response as JSON
            return JsonResponse({"response": ai_response})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        except Exception as e:
            # Return any other exceptions as a 500 internal error
            return JsonResponse({"error": str(e)}, status=500)
    
    # Handle non-POST requests
    return JsonResponse({"error": "Invalid request method"}, status=405)