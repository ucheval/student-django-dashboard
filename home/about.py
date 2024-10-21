from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


def About_us(request):
    return render(request, "blog/about.html")


# def Contact_us(request):
#     return render(request, "blog/contact.html")



def Contact_us(request):
    if request.method == 'POST':
        # Get form data from the request
        name = request.POST['name']
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'my name is {name}')

        # Send welcome email to the user
        send_mail(
            subject='Welcome Onboard!',
            message=f'Hello {name},\n\nThank you for reaching out to us. We have received your message and will get back to you shortly.\n\nBest regards,\nYour Company',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        # Send email to the admin with form details
        send_mail(
            subject='New Contact Form Submission',
            message=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],  # Add the admin's email here
            fail_silently=False,
        )

        # Redirect or render a thank-you page
        return redirect('home')

    return render(request, "blog/contact.html")








