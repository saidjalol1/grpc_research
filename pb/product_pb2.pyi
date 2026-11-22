from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductGetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("id", "name", "description", "price", "discount")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: float
    discount: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., discount: _Optional[float] = ...) -> None: ...

class ProductCreateRequest(_message.Message):
    __slots__ = ("name", "description", "price", "discount")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    price: float
    discount: float
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., discount: _Optional[float] = ...) -> None: ...

class ProductSearchRequest(_message.Message):
    __slots__ = ("name", "min_price", "max_price")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_FIELD_NUMBER: _ClassVar[int]
    MAX_PRICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    min_price: float
    max_price: float
    def __init__(self, name: _Optional[str] = ..., min_price: _Optional[float] = ..., max_price: _Optional[float] = ...) -> None: ...

class ProductSearchResponse(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...
