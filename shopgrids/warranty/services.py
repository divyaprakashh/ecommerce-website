# warranty/services.py
from cart.models import Order
from warranty.models import Warranty
from django.core.exceptions import ValidationError

def create_warranty_from_order(order_id, start_date, end_date):
    """Create a warranty from an order ID, start date, and end date."""
    try:
        order = Order.objects.get(id=order_id)
        # Create and save the warranty
        warranty = Warranty.objects.create(
            product=order.product,
            user=order.user,
            order=order,
            start_date=start_date,
            end_date=end_date
        )
        return warranty
    except Order.DoesNotExist:
        raise ValueError("Order not found")
    except ValidationError as e:
        raise ValueError(f"Invalid data: {e}")
