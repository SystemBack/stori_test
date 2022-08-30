from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from transactions.models import Update

from transactions.service.transactions_service import TransactionsService

def index(request):
    updates = Update.objects.all()

    return render(request, "transactions/index.html", {"updates": updates})

def save(request):
    csv_file = request.FILES["file"]
    name = csv_file.name
    if not name.endswith(".csv"):
        messages.error(request, "This is not a csv file!")
        return redirect("index")

    email = request.POST.get("email", "")

    details = TransactionsService().save_transactions(csv_file, email)

    html_template = get_template("./email/transactions_details.html")

    ctx = Context(details)

    html_content = html_template.render(details)

    msg = EmailMultiAlternatives("Transactions details", html_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")

    if (msg.send() == False ):
        messages.error(request, "We can not send the email!")
        return redirect("index")

    messages.info(request, "The transactions was sent successfully!")

    return redirect("index")