﻿from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from repositories import ProductSelectRepository
from repositories.price_repository import PriceRepository

product_repositories = ProductSelectRepository()
price_repo = PriceRepository()


class ProductSearchView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponseRedirect(reverse("productsapp:catalog"))

    def post(self, request: HttpRequest) -> HttpResponse:
        text = request.POST.get("query")
        if text:
            products = product_repositories.\
                get_all_products_by_name_match(name=text)
            products = product_repositories.get_product_prices(products)

            return render(request, "productsapp/catalog.html", context={
                "page_obj": products,
            })
        else:
            return HttpResponseRedirect(reverse("productsapp:catalog"))
