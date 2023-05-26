from typing import List, Dict

from interfaces.product_select_interface import ProductSelectInterface
from productsapp.models import Discount
from productsapp.models.product import Product
from productsapp.models.price import SlicePrice
from productsapp.models.specific import Specific
from django.db.models import QuerySet, Sum, Count, Subquery, OuterRef
from coreapp.enums import SORT_TYPES


class ProductSelectRepository(ProductSelectInterface):

    def get_all_products(self) -> QuerySet[Product]:
        """Получить все продукты"""
        return Product.objects.all()

    def get_product_by_id(self, product_id: int) -> Product:
        """ Получить продукт по id """
        return Product.objects.get(id=product_id)

    def get_products_with_these_id(self, products_id: List[int])\
            -> QuerySet[Product]:
        return Product.objects.filter(id__in=products_id)

    def get_products_with_filter(self,
                                 name: str,
                                 category: str,
                                 free_delivery: bool,
                                 in_stock: bool) -> QuerySet[Product]:
        """Получить список продуктов на основании фильтра"""
        return Product.objects.filter(
            name__icontains=name,
            category__name__icontains=category,
            free_delivery__in=(True, free_delivery),
            is_active__in=(True, in_stock))

    def get_products_with_tag(self,
                              tag: str) -> QuerySet[Product]:
        """Получить список продуктов по тегу"""
        return Product.objects.filter(tags__name__in=[tag])

    def get_product_prices(self,
                           products: QuerySet) -> QuerySet[Product]:
        """Получить цены на список продуктов"""
        subquery = SlicePrice.objects.filter(
            product=OuterRef('pk')).order_by('value')

        prices = products.select_related('category').annotate(
            price=subquery.values('value')[:1],
            seller_id=subquery.values('seller_id')[:1])
        return prices

    def set_price_range(self,
                        products: QuerySet,
                        price_min: int,
                        price_max: int) -> QuerySet[Product]:
        """Выбрать диапазон цен"""
        return products.filter(price__gte=price_min, price__lte=price_max)

    def sort_by_popular(self,
                        products: QuerySet,
                        reverse: bool) -> QuerySet[Product]:
        """ Cортировка по количеству проданных """
        prefix = ''
        if reverse:
            prefix = '-'
        sorted_products = products.annotate(
            sold=Sum('ordered__count')).order_by(f'{prefix}sold')
        return sorted_products

    def sort_by_reviews(self,
                        products: QuerySet,
                        reverse: bool) -> QuerySet[Product]:
        """ Cортировка по количеству отзывов """
        prefix = ''
        if reverse:
            prefix = '-'
        sorted_products = products.annotate(
            reviews_amount=Count('reviews')).order_by(
            f'{prefix}reviews_amount')
        return sorted_products

    def sort_by_new(self,
                    products: QuerySet,
                    reverse: bool) -> QuerySet[Product]:
        """ Cортировка по году выпуска """
        prefix = ''
        if reverse:
            prefix = '-'
        sorted_products = products.annotate(
            year=Subquery(
                Specific.objects.filter(
                    type_spec__name='Год выпуска',
                    product=OuterRef('pk')
                ).values('description'))).order_by(f'{prefix}year')
        return sorted_products

    def sort_by_price(self,
                      products: QuerySet,
                      reverse: bool) -> QuerySet[Product]:
        """ Cортировка по цене """
        prefix = ''
        if reverse:
            prefix = '-'
        return products.order_by(f'{prefix}price')

    def get_sorted(self,
                   products: QuerySet,
                   sort: str) -> QuerySet[Product]:
        """ Выбор метода сортировки в зависимости от параметра """
        sort_methods = {
            'new': self.sort_by_new,
            'popular': self.sort_by_popular,
            'reviews': self.sort_by_reviews,
            'price': self.sort_by_price
        }
        if sort in SORT_TYPES:
            reverse = False
            if sort[0] == '-':
                reverse = True
                sort = sort[1:]
            return sort_methods[sort](products, reverse)
        else:  # при некорректном параметре сортировка не применяется
            return products

    def get_all_discounts(self, products_id: List[int]) -> \
            Dict[Product, QuerySet[Discount]]:
        products = Product.objects.filter(id__in=products_id)
        discounts = dict()
        for product in products:
            discounts[product] = product.discounted_products
        return discounts
