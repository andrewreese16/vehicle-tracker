from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Vehicle, MaintenanceWork
from .forms import VehicleForm, MaintenanceWorkForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Save the user and add a success message with session-based storage
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! You can now log in.', extra_tags='success', fail_silently=False)
        return response

    def form_invalid(self, form):
        # Add an error message if the form is invalid
        messages.error(self.request, 'There were errors in your submission. Please correct them and try again.')
        return super().form_invalid(form)
@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, "vehicles/vehicle_list.html", {"vehicles": vehicles})


@login_required
def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    maintenance_records = vehicle.maintenance_records.all()
    return render(
        request,
        "vehicles/vehicle_detail.html",
        {"vehicle": vehicle, "maintenance_records": maintenance_records},
    )


@login_required
def vehicle_create(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect("vehicle_list")
    else:
        form = VehicleForm()

    return render(request, "vehicles/vehicle_form.html", {"form": form})


@login_required
def vehicle_update(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect("vehicle_detail", vehicle_id=vehicle.id)
        else:
            form = VehicleForm(instance=vehicle)
        return render(request, "vehicles/vehicle_form.html", {"form": form})


@login_required
def vehicle_delete(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicle_list")
    return render(request, "vehicles/vehicle_confirm_delete.html", {"vehicle": vehicle})


@login_required
def maintenance_create(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    if request.method == "POST":
        form = MaintenanceWorkForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.vehicle = vehicle
            if not maintenance.date_of_service:
                maintenance.date_of_service = timezone.now()
            maintenance.save()
            return redirect("vehicle_detail", vehicle_id=vehicle.id)
    else:
        form = MaintenanceWorkForm()
    return render(
        request, "maintenance/maintenance_form.html", {"form": form, "vehicle": vehicle}
    )


@login_required
def maintenance_update(request, vehicle_id, maintenance_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    maintenance_record = get_object_or_404(
        MaintenanceWork, id=maintenance_id, vehicle=vehicle
    )

    if request.method == "POST":
        form = MaintenanceWorkForm(request.POST, instance=maintenance_record)
        if form.is_valid():
            form.save()
            return redirect("vehicle_detail", vehicle_id=vehicle.id)
    else:
        form = MaintenanceWorkForm(instance=maintenance_record)

    return render(
        request,
        "maintenance/maintenance_form.html",
        {"form": form, "vehicle": vehicle, "maintenance_record": maintenance_record},
    )


@login_required
def maintenance_delete(request, vehicle_id, maintenance_id):
    # Retrieve the vehicle and maintenance record
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    maintenance_record = get_object_or_404(
        MaintenanceWork, id=maintenance_id, vehicle=vehicle
    )

    # Check if the request is a POST (confirm deletion)
    if request.method == "POST":
        maintenance_record.delete()
        return redirect("vehicle_detail", vehicle_id=vehicle.id)

    # If it's a GET request, render a confirmation page
    return render(
        request,
        "maintenance/maintenance_confirm_delete.html",
        {"vehicle": vehicle, "record": maintenance_record},
    )
