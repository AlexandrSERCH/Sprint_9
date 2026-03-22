import allure
import pytest


def mark_tag(*tags):
    """Одновременно добавляется allure.tag и pytest.mark"""

    def decorator(func):
        func = allure.tag(*tags)(func)
        for tag in tags:
            func = getattr(pytest.mark, tag)(func)
        return func

    return decorator
