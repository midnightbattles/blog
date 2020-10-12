from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # enviar e-mail
        nome = request.POST.get("nome", "")
        email = request.POST.get("email", "")
        assunto = request.POST.get("mensagem", "")
        email = EmailMessage(
            "Mensagem do Blog Django",
            "De {} <{}> Escreveu: \n\n{}".format(nome, email, assunto),
            "nao-responder@inbox.mailtrap.io",
            ["midnight_battles@protonmail.com"],
            reply_to=[email],
        )
        try:
            email.send()
            send = True
        except Exception:
            send = False

    context = {"form": form, "success": send}
    return render(request, "contact/contact.html", context)
