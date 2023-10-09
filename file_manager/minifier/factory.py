from typing import *

from core.exceptions import WrongMinifierProviderException
from file_manager.minifier.base import BaseMinifierProviderClass
from file_manager.minifier.css_minifier import CSSMinifier
from file_manager.minifier.enums import MinifierEnum
from file_manager.minifier.jsmin import JsminMinifier


class MinifierProviderFactory:
    def get(self, minifier: MinifierEnum, *args, **kwargs) -> Union[BaseMinifierProviderClass,
                                                                    WrongMinifierProviderException]:

        minifier_mappings = {
            MinifierEnum.CSS_HTML_JS: CSSMinifier,
            MinifierEnum.JSMIN: JsminMinifier  # TODO: IMPLEMENT JSMIN CLASS
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
                a list of all file_manager enum available
        """
        return [
            MinifierEnum.CSS_HTML_JS,
            MinifierEnum.JSMIN
        ]
