from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from feedbacks.models import Feedback
from django.core.mail import send_mail

class FeedbackView(CreateView):
    template_name = 'feedbacks/feedback.html'
    model = Feedback
    success_url = reverse_lazy('feedback')
        
        
    def form_valid(self, form):
        feedback = form.save()
        messages.success(self.request, u'Thank you for your feedback! We will keep in touch with you very soon!')
        send_mail('Subject', 'Hello!', 'vaschenko.margarita44@gmail.com', 'nikolay.borovenskiy@gmail.com', fail_silently=False)
        return super(FeedbackView, self).form_valid(form) 
