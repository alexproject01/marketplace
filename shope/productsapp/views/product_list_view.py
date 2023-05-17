from django.views.generic import ListView
from productsapp.forms.catalog_filter_form import CatalogFilterForm
from repositories.product_select_repository import ProductSelectRepository

select_repo = ProductSelectRepository()


class ProductListView(ListView):
    """ Класс-view для каталога """
    template_name = 'productsapp/catalog.html'
    paginate_by = 3
    extra_context = {'tags_list': select_repo.get_all_tags()}

    def get_queryset(self):
        queryset = select_repo.get_all_products()

        form = CatalogFilterForm(self.request.GET)
        if form.is_valid():

            price_min = form.cleaned_data.get('price_min')
            price_max = form.cleaned_data.get('price_max')
            tag = form.cleaned_data.get('tag')
            sort = form.cleaned_data.get('sort')
            name = form.cleaned_data.get('name')
            free_delivery = form.cleaned_data.get('free_delivery')
            in_stock = form.cleaned_data.get('in_stock')

            if tag:  # поиск по тегу
                queryset = select_repo.get_products_with_tag(tag=tag)

            else:  # поиск по имени и доп. параметрам
                queryset = select_repo.get_products_with_filter(
                    name=name,
                    free_delivery=free_delivery,
                    in_stock=in_stock)

            queryset = select_repo.get_product_prices(queryset)

            if price_min:  # ограничение выборки по цене, если диапазон задан
                queryset = select_repo.set_price_range(products=queryset,
                                                       price_min=price_min,
                                                       price_max=price_max)
            queryset = select_repo.get_sorted(products=queryset, sort=sort)

        return queryset
