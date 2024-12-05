from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import TodoItem, ServiceItem, BarberItem, Appointment
from django.http import JsonResponse
from django import forms

# Create your views here.

# HTML Views
def home(request):
    services = ServiceItem.objects.all()
    return render(request, 'home.html', {'services': services})

def booking(request): 
    services = ServiceItem.objects.all()  # Get all service items
    barbers = BarberItem.objects.all()  # Get all barbers
    return render(request, 'booking.html', {'services': services, 'barbers': barbers})

def appointment(request):
    query = request.GET.get('q')  # Get the search query from the request
    appointments = Appointment.objects.all().order_by('date', 'time')

    if query:
        appointments = appointments.filter(
            barber__name__icontains=query
        ) | appointments.filter(
            service__name__icontains=query
        )

    return render(request, 'appointment.html', {'appointments': appointments, 'query': query})

def barber(request):
    barbers = BarberItem.objects.all()  # Fetch all barbers from the database
    return render(request, 'barber.html', {'barbers': barbers})  # Pass the barbers to the template

def barber_list(request):
    barbers = BarberItem.objects.all()  # Fetch all barbers from the database
    return render(request, 'barber.html', {'barbers': barbers})  # Pass the barbers to the template

# Model Objects
def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items })

def service_list(request):
    services = ServiceItem.objects.all()  # Fetch all service records
    return render(request, 'home.html', {'services': services})

def book_appointment(request):
    if request.method == 'POST':
        booking_date = request.POST.get('date')  # Updated to match the form field name
        booking_time = request.POST.get('time')  # Updated to match the form field name
        service_id = request.POST.get('service')
        barber_id = request.POST.get('barber')
        client_name = request.POST.get('client_name')  # Updated to match the form field name
        client_phone = request.POST.get('client_phone')  # Updated to match the form field name

        # Validate data
        if not (booking_date and booking_time and service_id and barber_id and client_name and client_phone):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Fetch related objects
        try:
            service = ServiceItem.objects.get(id=service_id)
            barber = BarberItem.objects.get(id=barber_id)
        except (ServiceItem.DoesNotExist, BarberItem.DoesNotExist):
            return JsonResponse({'error': 'Invalid service or barber'}, status=404)

        # Create the appointment
        appointment = Appointment.objects.create(
            barber=barber,
            service=service,
            client_name=client_name,  # Save the client name
            client_phone=client_phone,  # Save the client phone
            date=booking_date,
            time=booking_time
        )

        # Return the response with service and barber names
        return JsonResponse({
            'message': 'Appointment booked successfully',
            'client_name': client_name,  # Return the client name
            'service_name': service.name,  # Return the service name
            'barber_name': barber.name,  # Return the barber name
            'date': booking_date,
            'time': booking_time
        }, status=200)

    # Render the booking form with services and barbers
    services = ServiceItem.objects.all()
    barbers = BarberItem.objects.all()
    return render(request, 'booking.html', {'services': services, 'barbers': barbers})

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['barber', 'service', 'client_name', 'client_phone', 'date', 'time']

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment')  # Redirect to the appointment list after saving
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'edit_appointment.html', {'form': form, 'appointment': appointment})


def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment')  # Redirect to the appointment list after deletion
    return render(request, 'confirm_delete.html', {'appointment': appointment})