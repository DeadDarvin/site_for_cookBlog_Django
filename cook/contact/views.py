from django.views import View
from .forms import ContactForm
from django.views.generic import DetailView, CreateView, TemplateView
from .models import ContactLink
from django.urls import reverse_lazy
from blog.utils import DataMixin
from .models import ContactLink, AboutModel

#class ContactView(View):
    #def get(self, request):
        #contacts = ContactLink.objects.all()
        #form =
        #return


#class CreateContact(CreateView):
    #form_class = ContactForm # Связываем форму
    #success_url = '/'

class ContactFormView(DataMixin, CreateView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = ContactLink.objects.all()
        c_def = super().get_user_context(
            title='Контакты',
            page_selected='contact',
            contact_list=contacts
        )
        return dict(list(context.items()) + list(c_def.items()))


class AboutView(DataMixin, TemplateView):
    template_name = 'contact/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = ContactLink.objects.all()
        gen_model = AboutModel.objects.last()
        c_def = super().get_user_context(
            title='Обо мне',
            page_selected='about',
            contact_list=contacts,
            gen_model=gen_model
        )
        return dict(list(context.items()) + list(c_def.items()))