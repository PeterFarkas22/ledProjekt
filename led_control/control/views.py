import gpiod
from django.shortcuts import render
from gpiozero import AngularServo

# Állíts be különböző GPIO pineket a LED és a szervo számára
LED_GPIO_PIN = 17
SERVO_GPIO_PIN = 18

def set_gpio_value(chip_name, line_number, value):
    chip = gpiod.Chip(chip_name)
    line = chip.get_line(line_number)
    try:
        line.request(consumer="gpioset", type=gpiod.LINE_REQ_DIR_OUT)
        line.set_value(value)
    finally:
        line.release()

def index(request):
    return render(request, 'index.html')

def turn_on(request):
    try:
        set_gpio_value('gpiochip4', LED_GPIO_PIN, 1)
        message = "LED bekapcsolva"
    except Exception as e:
        message = f"Hiba: {e}"
    
    return render(request, 'index.html', {'message': message})

def turn_off(request):
    try:
        set_gpio_value('gpiochip4', LED_GPIO_PIN, 0)
        message = "LED kikapcsolva"
    except Exception as e:
        message = f"Hiba: {e}"
    
    return render(request, 'index.html', {'message': message})

servo = AngularServo(SERVO_GPIO_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)

def motor(request):
    template = 'index.html'
    context = {}
    
    if request.method == 'POST':
        angle = request.POST.get('angle')
        try:
            angle = int(angle)
            servo.angle = angle
            context['message'] = f'Servo moved to {angle} degrees.'
        except ValueError:
            context['message'] = 'Invalid angle. Please enter a number.'

    return render(request, template, context)