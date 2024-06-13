from django.shortcuts import render
import gpiod
from gpiozero import AngularServo

def set_gpio_value(chip_name, line_number, value):
    chip = gpiod.Chip(chip_name)
    line = chip.get_line(line_number)
    line.request(consumer="gpioset", type=gpiod.LINE_REQ_DIR_OUT)
    line.set_value(value)
    line.release()

def index(request):
    return render(request, 'index.html')

def turn_on(request):
    try:
        set_gpio_value('gpiochip4', 17, 1)
        message = "LED off"
    except Exception as e:
        message = f"Hiba: {e}"
    
    return render(request, 'index.html', {'message': message})

def turn_off(request):
    try:
        set_gpio_value('gpiochip4', 17, 0)
        message = "LED on"
    except Exception as e:
        message = f"Hiba: {e}"
    
    return render(request, 'index.html', {'message': message})

servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)

def motor(request):
    template='index.html'
    context={}
    
    
    
    if request.method == 'POST':
        angle = request.POST.get('angle')
        try:
            angle = int(angle)
            servo.angle = angle
            context['message'] = f'Servo moved to {angle} degrees.'
        except ValueError:
            context['message'] = 'Invalid angle. Please enter a number.'

    return render(request, template, context)