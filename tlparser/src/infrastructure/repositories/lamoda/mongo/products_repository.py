"""
products_repository.py: File, containing lamoda products mongo repository implementation.
"""


from domain.entities.lamoda.product_entity import LamodaProductEntity
from domain.repositories.lamoda.products_repository import LamodaProductsRepository
from infrastructure.connections.mongo.database import MongoDatabase
from infrastructure.mappers.lamoda.mongo.product_mapper import LamodaProductMapper
from infrastructure.models.lamoda.mongo.product_model import LamodaProduct


class LamodaProductsMongoRepository(LamodaProductsRepository):
    """
    LamodaProductsMongoRepository: Mongo implementation of LamodaProductsRepository.

    Args:
        LamodaProductsRepository (_type_): Repository abstract class.
    """

    def __init__(self, db: MongoDatabase) -> None:
        """
        __init__: Initialize repository.

        Args:
            db (MongoDatabase): MongoDatabase instance, containing mongo connection.
        """

        self.db = db

    def create_or_update(self, product_entity: LamodaProductEntity) -> LamodaProductEntity:
        """
        create_or_update: Create or update lamoda product.

        Args:
            product_entity (LamodaProductEntity): Lamoda product entity.

        Returns:
            LamodaProductEntity: Created/updated lamoda product entity.
        """

        product_persistence = LamodaProductMapper.to_persistence(product_entity)
        product_persistence.save()

        return LamodaProductMapper.to_domain(product_persistence)

    def all(self) -> list[LamodaProductEntity]:
        """
        all: Return list of lamoda products.

        Returns:
            list[LamodaProductEntity]: List of lamoda products.
        """

        return [
            LamodaProductMapper.to_domain(product_persistence)
            for product_persistence in LamodaProduct.objects
        ]

    def delete_products_by_category(self, category: str) -> None:
        """
        delete_products_by_category: Delete lamoda products by category.

        Args:
            category (str): Category of the products.
        """

        for product_persistence in LamodaProduct.objects(category=category):
            product_persistence.delete()

        return

    def get_products_by_category(self, category: str) -> list[LamodaProductEntity]:
        """
        get_products_by_category: Return lamoda products with the same category.

        Args:
            category (str): Category of the products.

        Returns:
            list[LamodaProductEntity]: Lamoda product instance.
        """

        return [
            LamodaProductMapper.to_domain(product_persistence)
            for product_persistence in LamodaProduct.objects(category=category)
        ]