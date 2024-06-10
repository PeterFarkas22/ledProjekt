from django.shortcuts import render
from gpiozero import LED
from django.shortcuts import render

# Set up the GPIO pin for the LED
led = LED(17)

def toggle_led(request):
    if request.method == 'POST':
        if 'on' in request.POST:
            led.on()
        elif 'off' in request.POST:
            led.off()
    return render(request, 'control/led_control.html')
