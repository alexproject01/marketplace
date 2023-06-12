from interfaces.discount_select_interface import DiscountInterface
from datetime import datetime
from productsapp.models import CartDiscount, Product, Category


class DiscountRepository(DiscountInterface):
    """
    Репозиторий для работы со скидками
    """

    def get_discount_by_product_or_category(self, product: Product,
                                            category: Category) -> float:
        """
        Метод получения скидки на товар и/или категорию
        возвращает значение скидки
        """
        date_now = datetime.now()
        product_discount = product.product_discounts.filter(
            start_date__lte=date_now, expiration_date__gte=date_now,
            is_active=True).order_by('-priority'). \
            only('value', 'priority')[:1]
        # наиболее приоритетная скидка на товар, если есть
        category_discount = category.category_discounts.filter(
            start_date__lte=date_now, expiration_date__gte=date_now,
            is_active=True).order_by('-priority'). \
            only('value', 'priority')[:1]
        # наиболее приоритетная скидка на категорию, если есть
        total = (category_discount | product_discount). \
            order_by('-priority').first()
        # наиболее приоритетная скидка среди категорий и товаров
        if total:
            return total
        else:
            return 0

    def get_discount_by_set_products(self, set_product):
        """
        Метод получения скидки на набор товаров
        """
        pass

    def get_discount_by_cart(self) -> CartDiscount:
        """
        Метод получения скидки на корзину
        возвращает экземпляр CartDiscount
        """
        date_now = datetime.now()
        cart_discount = CartDiscount.objects.filter(
            start_date__lte=date_now, expiration_date__gte=date_now,
            is_active=True).order_by('-priority') \
            .only('required_sum', 'required_quantity',
                  'value', 'priority').first()
        return cart_discount
