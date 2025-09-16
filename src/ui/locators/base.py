from typing import NamedTuple, Self


class UILocator(NamedTuple):
    """
    Класс для хранения локатора элемента на странице и его описания.

    Attributes:
    selector (str): Селектор для поиска элемента на странице.
    description (str): Описание элемента на странице.
    """

    selector: str
    description: str

    def format(self, **kwargs) -> Self:
        """
        Форматирует локатор с учетом переданных параметров.

        Args:
        **kwargs: Параметры для форматирования локатора.
        """
        return UILocator(
            selector=self.selector.format(**kwargs),
            description=self.description.format(**kwargs),
        )
