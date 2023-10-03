from typing import *

from core.exceptions import WrongMinifierProviderException
from minifier.minificator.base import BaseMinifierProviderClass
from minifier.minificator.css_minifier import CSSMinifier
from minifier.minificator.enums import MinifierEnum
from minifier.minificator.terser import TerserMinifier


class MinifierProviderFactory:
    def get(self, minifier: MinifierEnum, *args, **kwargs) -> Union[BaseMinifierProviderClass,
                                                                    WrongMinifierProviderException]:

        minifier_mappings = {
            MinifierEnum.CSS: CSSMinifier,
            MinifierEnum.TERSER: TerserMinifier
        }

        if minifier in minifier_mappings:
            minifier_class = minifier_mappings[minifier]
            return minifier_class(*args, **kwargs)
        else:
            raise WrongMinifierProviderException("Invalid provider.")

    @classmethod
    def get_all_provider_keys(cls) -> List:
        """
            Returns:
                a list of all minifier enum available
        """
        return [
            MinifierEnum.CSS,
            MinifierEnum.TERSER
        ]
