from typing import List, Dict
from bs4 import BeautifulSoup
from .interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    
    @classmethod
    def collect_essential_information(cls, html:str) -> List[Dict[str,str]]:
        soup = BeautifulSoup(html, 'html.parser')
        
        login_page = soup.find(class_= 'src-component-login-__header-3-Iu6')
        
        essential_information = []
        chinese_title = login_page
        links = 'https://ulp.sheincorp.cn/#/login'
        essential_information.append({
            "chinese_title": chinese_title,
            "link": links
        })
            
        assert isinstance(essential_information, list)
        assert isinstance(essential_information[0], dict)
        assert 'chinese_title' in  essential_information[0]
        assert 'link' in  essential_information[0]
        
        
        return essential_information