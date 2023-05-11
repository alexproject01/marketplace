from productsapp.models import Product, Review
from profileapp.models import Profile
from repositories.reviews_select_repository import ReviewSelectRepository
from repositories.reviews_update_repository import ReviewUpdateRepository


class AddProductReview:
    """
    Сервис добавления отзыва к товару
    """
    select_repository = ReviewSelectRepository()
    update_repository = ReviewUpdateRepository()

    def add_product_review(self,
                           user: Profile,
                           product: Product,
                           text: str):
        """
        Добавление отзыва к товару

        :param user: объект User, который дает отзыв
        :param product: объект Product, которому адресован отзыв
        :param text: текст отзыва
        :return: bool
        """
        if user.user.is_anonymous:
            return False

        review = Review(user=user,
                        product=product,
                        text=text)
        self.update_repository.update_review(review=review)
        return True

    def product_reviews_list(self, product: Product):
        """
        Получение списка отзывов к товару

        :param product: объект Product, у которого берем отзывы
        :return: QuerySet
        """
        return self.select_repository.get_all_reviews(product=product)

    def product_reviews_amount(self, product: Product) -> int:
        """
        Получение количества отзывов для товара

        :param product: объект Product, у которого находим кол-во отзывов.

        :return: int
        """

        return self.select_repository.get_amount_reviews(product=product)
