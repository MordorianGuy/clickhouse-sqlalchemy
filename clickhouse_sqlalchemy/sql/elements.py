from itertools import chain
from typing import Literal

from sqlalchemy import literal
from sqlalchemy.sql import ClauseElement, ColumnElement, FromClause


class Interval(ColumnElement):
    __visit_name__ = 'interval'

    def __init__(
        self,
        value: int,
        unit: Literal[
            'NANOSECOND',
            'MICROSECOND',
            'MILLISECOND',
            'SECOND',
            'MINUTE',
            'HOUR',
            'DAY',
            'WEEK',
            'MONTH'
            'QUARTER',
            'YEAR',
        ]
    ):
        self.value = value if isinstance(value, ClauseElement) else literal(value)
        self.unit = unit

    @property
    def _from_objects(self) -> list[FromClause]:
        return list(chain.from_iterable(x._from_objects for x in self.get_children()))