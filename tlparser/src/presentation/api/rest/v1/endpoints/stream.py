"""
stream.py: File, containing endpoinds for a twich stream.
"""


from typing import Annotated
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from application.dtos.fastapi_schemas.twich.stream_schema import TwichStreamSchema
from container import Container
from presentation.api.rest.v1.metadata.twich.stream_metadata import TwichStreamMetadata
from presentation.controllers.twich.stream_controller import TwichStreamController


router: APIRouter = APIRouter(
    prefix='/twich',
    tags=['twich'],
)


@router.post(
    path='/stream/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.parse_stream,
)
@inject
async def parse_stream(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_w_controller]),
) -> Response:
    """
    parse_stream: Produce message to kafka to parse stream.

    Args:
        user_login (str): Login of the user.

    Returns:
        Response: HTTP status code 200.
    """

    await controller.parse_stream(user_login)

    return JSONResponse(content={}, status_code=status.HTTP_200_OK)


@router.get(
    path='/private/stream/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.private_parse_stream,
)
# @cache(60)
@inject
async def private_parse_stream(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_w_controller]),
) -> TwichStreamSchema:
    """
    private_parse_stream: Parse twich stream and return result as TwichStreamSchema.

    Args:
        user_login (str): Login of the user.
        controller (TwichStreamController): Twich stream controller.

    Returns:
        TwichStreamSchema: Response as TwichStreamSchema instance.
    """

    return await controller.private_parse_stream(user_login)


@router.delete(
    path='/stream/{user_login}',
    status_code=status.HTTP_204_NO_CONTENT,
    **TwichStreamMetadata.delete_stream_by_user_login,
)
@inject
async def delete_stream_by_user_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_w_controller]),
) -> Response:
    """
    delete_stream_by_user_login: Delete twich stream.

    Args:
        user_login (str): Login of the user.
        controller (TwichStreamController): Twich stream controller.

    Returns:
        Response: HTTP status code 204.
    """

    await controller.delete_stream_by_user_login(user_login)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    path='/streams',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.get_all_streams,
)
# @cache(expire=60)
@inject
async def get_all_streams(
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_r_controller]),
) -> list[TwichStreamSchema]:
    """
    get_all_streams: Return all streams.

    Args:
        controller (TwichStreamController): Twich stream controller.

    Returns:
        list[TwichStreamSchema]: List of twich streams.
    """

    return await controller.get_all_streams()


@router.get(
    path='/stream/{user_login}',
    status_code=status.HTTP_200_OK,
    **TwichStreamMetadata.get_stream_by_user_login,
)
# @cache(expire=60)
@inject
async def get_stream_by_user_login(
    user_login: Annotated[str, Path(min_length=1, max_length=128)],
    controller: TwichStreamController = Depends(Provide[Container.twich_stream_r_controller]),
) -> TwichStreamSchema:
    """
    get_stream_by_user_login: Return twich stream by user login.

    Args:
        user_login (str): Login of the user.
        controller (TwichStreamController): Twich stream controller.

    Returns:
        TwichStreamSchema: TwichStreamSchema instance.
    """

    return await controller.get_stream_by_user_login(user_login)