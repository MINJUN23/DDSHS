from django.core.management.base import BaseCommand, CommandError
from address.models import Address
from order.models import Order, Shipment
from item.models import Item, SubscribeItem
from payment.models import Payment
from product.models import Curtain
from users.models import User
from dateutil.relativedelta import relativedelta
import datetime

email = "pollo1999@naver.com"


class Command(BaseCommand):
    help = 'create order of all curtains that had paid'

    def handle(self, *args, **options):
        shopper = User.objects.get(username=email)
        address = Address.objects.create(user=shopper, address_name="test", customer_name="test",
                                         postalcode="00000", main_address="test_main_address", detail_address="test_detail_address",
                                         phone_number="0000000000")
        shipment = Shipment.objects.create(
            message="test", address=address)
        order = Order.objects.create(status="paid", shipment=shipment)

        deposit = 0
        price = 0
        for curtain in Curtain.objects.all():
            subscribe_item = SubscribeItem.objects.create(
                curtain=curtain, size="S", height=230, style="rail", build="No", period="3")

            item = Item.objects.create(
                shopper=shopper, order=order, on_cart=False, subscribe_item=subscribe_item)
            deposit += item.get_deposit()
            price += item.get_price()

        payment = Payment.objects.create(
            payment_way="naverpay", amount=deposit+price, deposit=deposit, payment_id="test")
        order.payment = payment
        order.save()
        order.start_shipment()
        order.complete_shipment()
