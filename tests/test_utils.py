import datetime

import pytest

from src.utils import get_data


def test_get_data():
    assert get_data('14.09.2024') == datetime.datetime(2024, 9, 14, 0, 0)
    with pytest.raises(ValueError) as exc_info:
        assert get_data('14.09') == ValueError

    # with pytest.raises(SystemExit, match="Нет транзакций") as exc_info: