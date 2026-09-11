from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class SupplierProduct:
    """Товар, как его отдаёт поставщик. Сырые данные, ничего не теряем."""

    supplier: str
    supplier_sku: str
    raw_name: str
    purchase_price: Decimal
    stock: Optional[int] = None


@dataclass
class NormalizedProduct:
    """Товар после разбора названия и нормализации."""

    supplier: str
    supplier_sku: str
    raw_name: str
    purchase_price: Decimal
    stock: Optional[int]

    brand: Optional[str] = None
    model: Optional[str] = None
    codes: List[str] = field(default_factory=list)
    region: Optional[str] = None
    color: Optional[str] = None
    product_type: Optional[str] = None
    category: Optional[str] = None