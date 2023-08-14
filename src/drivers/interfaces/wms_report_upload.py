from abc import ABC, abstractmethod

class WmsReportUploadInterface(ABC):

    @abstractmethod
    def upload_sheet(self,filename:str):
        pass