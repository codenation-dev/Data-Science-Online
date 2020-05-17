from abc import ABC, abstractmethod
import pandas as pd

class FonteDados(ABC):
    
    @abstractmethod
    def obter_dados(self) -> pd.DataFrame:
        pass
         