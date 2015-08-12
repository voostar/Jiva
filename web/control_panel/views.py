from django.shortcuts import render
from control_panel.motor import motor

def panel(request):
    control = motor()
    action = request.GET.get('go')
    if action == 'up':
        control.right_forward()
        control.left_forward()
    elif action == 'back':
        control.right_backward()
        control.left_backward()
    elif action == 'left':
        control.right_forward()
    elif action == 'right':
        control.left_forward()
    elif action == 'stop':
        control.stop()

    return render(request, 'panel.html')