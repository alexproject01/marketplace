from repositories.cart_repository import RepCart
from repositories.price_repository import PriceRepository
from repositories.product_select_repository import ProductSelectRepository
from repositories.seller_select_repository import SellerSelectRepository
from coreapp.utils.select_cart import SelectCart
from coreapp.utils.product_discounts import ProductDiscounts
from productsapp.models import CartDiscount

rep_cart = RepCart()
rep_price = PriceRepository()
rep_prod = ProductSelectRepository()
rep_sell = SellerSelectRepository()


def cart_block(request):
    """
    Контекстный процессор для отображения
    количества товаров в корзине и общей цены товаров в корзине
    """
    if request.user.is_authenticated:
        # если пользователь авторизован
        user = request.user
        cart = rep_cart.get_cart(user=user)
        count = SelectCart.cart_all_products_amount(cart=cart)
        cart_price = SelectCart.cart_total_amount(cart=cart)
        discounted_prices_list, discount = ProductDiscounts. \
            get_prices_discount_on_cart(cart_price, count, cart=cart)
    else:
        session_products = request.session.get('products')
        count = SelectCart.cart_all_products_amount(
            session_products=session_products)
        cart_price = SelectCart.cart_total_amount(
            session_products=session_products)
        discounted_prices_list, discount = ProductDiscounts. \
            get_prices_discount_on_cart(cart_price, count,
                                        session_products=session_products)
        request.session['prices'] = discounted_prices_list
        request.session.modified = True

    if discount:
        if isinstance(discount, CartDiscount):
            type_discount = 'cart'
        else:
            type_discount = 'set'
    else:
        type_discount = ''
    context = {
        'cart_count': count,
        'cart_sum': round(sum(discounted_prices_list), 2),
        'discount': discount,
        'type_discount': type_discount
    }  # словарь с количеством и суммой товаров в корзине и
    # применённой скидкой
    return context
