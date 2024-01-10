"""
products_controller.py: File, containing lamoda products controller.
"""


from fastapi import HTTPException
from pydantic import ValidationError
from requests import ConnectionError, RequestException, Timeout, TooManyRedirects
from application.interfaces.services.lamoda.products_service import ILamodaProductsService
from application.schemas.lamoda.product_schema import LamodaProductSchema
from domain.exceptions.lamoda.products_exceptions import WrongCategoryUrlException


class LamodaProductsController:
    """
    LamodaProductsController: Class, representing lamoda controller. It handles all http exceptions.
    """

    def __init__(self, service: ILamodaProductsService) -> None:
        """
        __init__: Initialize lamoda controller class.

        Args:
            service (ILamodaProductsService): Lamoda products service abstract class.
        """

        self.service: ILamodaProductsService = service

    async def parse_products(self, category_id: str) -> None:
        """
        parse_products: Called lamoda products service to send event about parsing.

        Args:
            category+id (str): Category lamoda identifier.
        """

        await self.service.parse_products(category_id)

    async def private_parse_products(self, category_id: str) -> list[LamodaProductSchema]:
        """
        private_parse_products: Delegate parsing to LamodaProductsService, handle all exceptions.

        Args:
            category_id (str): Category lamoda identifier.

        Raises:
            HTTPException: Raised when client passed wrong category url.
            HTTPException: Raised when ConnectionError exception is raised by requests.
            HTTPException: Raised when Timeout exception is raised by requests.
            HTTPException: Raised when TooManyRedirects exception is raised by requests.
            HTTPException: Raised when RequestException exception is raised by requests.
            HTTPException: Raised when ValidationError exception is raised by pydantic.
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[LamodaProductSchema]: List of LamodaProductSchema instances.
        """

        try:
            return await self.service.private_parse_products(category_id)
        except WrongCategoryUrlException:
            raise HTTPException(status_code=404, detail='Wrong category url')
        except ConnectionError:
            raise HTTPException(status_code=503, detail='Service unavaliable (connection issues)')
        except Timeout:
            raise HTTPException(status_code=503, detail='Service unavaliable (request timeout)')
        except TooManyRedirects:
            raise HTTPException(status_code=503, detail='Service unavaliable (too many redirects)')
        except RequestException:
            raise HTTPException(status_code=503, detail='Service unavaliable (requests error)')
        except ValidationError:
            raise HTTPException(status_code=400, detail='Validation error (parsing error)')
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def delete_products_by_category(self, category: str) -> None:
        """
        delete_products_by_category: Delegate deleting to LamodaProductsService, handle exceptions.

        Args:
            category (str): Lamoda products category.

        Raises:
            HTTPException: Raised when Any other exception is raised.
        """

        try:
            return await self.service.delete_products_by_category(category)
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_all_products(self) -> list[LamodaProductSchema]:
        """
        get_all_products: Delegate access to LamodaProductsService, catch and handle exceptions.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[LamodaProductSchema]: List of lamoda products.
        """

        try:
            return await self.service.get_all_products()
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')

    async def get_products_by_category(self, category: str) -> list[LamodaProductSchema]:
        """
        get_products_by_category: Delegate access to LamodaProductsService, handle exceptions.

        Args:
            category (str): Lamoda products category.

        Raises:
            HTTPException: Raised when Any other exception is raised.

        Returns:
            list[LamodaProductSchema]: List of lamoda products with the same category.
        """

        try:
            return await self.service.get_products_by_category(category)
        except Exception:
            raise HTTPException(status_code=503, detail='Service unavaliable (internal error)')
