
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

# Create your views here.
from ecommerce.form import ContactForm
from ecommerce.views import write

#own models
from products.models import Behdashti, Tebi



class Eshop(ListView):

    queryset      = Behdashti.objects.all()
    template_name = 'shop.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Eshop, self).get_context_data(*args, **kwargs)

        print("%%%%%%%%%%%%%%%")
        print(context)
        print("%%%%%%%%%%%%%%%")

        return context




def shop(request):
    contactform = ContactForm
    behdashti_products = Behdashti.objects.all()
    tebi_products      = Tebi.objects.all()
    content  = {
        'form' : contactform,
        'behdashti' : behdashti_products,
        'tebi' : tebi_products,
    }
    return render(request, 'shop.html', content)




#######################################
###########  detail view  #############
#######################################


class ProductDetail(DetailView):

    queryset      = Behdashti.objects.all()
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(*args, **kwargs)

        print("%%%%%%%%%%%%%%%")
        print(context)
        print("%%%%%%%%%%%%%%%")

        return context




def product_detail_behdashti(request, productId):


#this bit is experimental and for fun, not practical
    try:
        products = Behdashti.objects.filter(id=productId)
        if products.count() == 1:
            products= products.first
        else:
            return redirect('/shop')
    except Behdashti.DoesNotExist:
        raise Http404(f'no such thing with primary key as : $$$  {productId}  $$$ were found')
#till here ^^^^^


    content  = {
        'queryset' : products,
        'id' : productId,
    }

    print('0'*10)
    print(products)
    print('0'*10)

    return render(request, 'detail.html', content)


def product_detail_tebi(request, productId=None, *args, **kwargs):
    try:
        products = Tebi.objects.get(id=productId)

    except Tebi.DoesNotExist:
        raise Http404(f'no such thing with primary key as : $$${productId}$$$ were found')
        

    content  = {
        'queryset' : products,
        'id' : productId,
    }
    return render(request, 'detail.html', content)
