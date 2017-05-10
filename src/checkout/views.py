from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == "POST":
		token = request.POST["stripeToken"]
		# Create a Charge:
		# Charge the user's card:
		customer = stripe.Customer.retrieve(customer_id)
		customer.sources.create(source=token)
		charge = stripe.Charge.create(
		  amount=1000,
		  currency="usd",
		  description="Example charge",
		  customer = customer,
		)
	context = {"publishKey":publishKey} #locals()
	template = "checkout.html"
	return render(request,template,context)