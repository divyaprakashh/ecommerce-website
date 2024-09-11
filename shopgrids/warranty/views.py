# warranty/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Warranty
from .forms import WarrantyForm
from .services import create_warranty_from_order

def add_warranty(request):
    """View to add a new warranty."""
    if request.method == 'POST':
        form = WarrantyForm(request.POST)
        if form.is_valid():
            # Save form data directly; form handles ForeignKey relationships
            form.save()
            messages.success(request, 'Warranty successfully added!')
            return redirect('add_warranty')  # Redirect to avoid resubmission on refresh
    else:
        form = WarrantyForm()
    return render(request, 'admin/add_warranty.html', {'form': form})

def validate_warranty(request, pk):
    """View to validate a warranty by its primary key."""
    warranty = get_object_or_404(Warranty, pk=pk)
    status = 'Valid' if warranty.is_valid() else 'Expired'
    return render(request, 'user/validate_warranty.html', {'warranty': warranty, 'status': status})

def list_warranties(request):
    """View to list all warranties with optional search."""
    warranties = Warranty.objects.all()
    search_term = request.GET.get('search', '')
    
    if search_term:
        warranties = warranties.filter(product__name__icontains=search_term)
    
    return render(request, 'admin/view_warranty.html', {
        'warranties': warranties,
        'search_term': search_term
    })

def delete_warranty(request, pk):
    """View to delete a warranty by its primary key."""
    warranty = get_object_or_404(Warranty, pk=pk)
    if request.method == 'POST':
        warranty.delete()
        messages.success(request, 'Warranty successfully deleted!')
        return redirect('list_warranties')  # Redirect to the list view after deletion
    return render(request, 'admin/confirm_delete.html', {'warranty': warranty})
