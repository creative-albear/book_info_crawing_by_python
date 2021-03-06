from strategy.parse_strategy import ParseStrategy
from book.book_info import BookInfo
from bs4 import BeautifulSoup
from type.rank_type import RankType
from type.site_type import SiteType

class KyoboDetailParseStrategy(ParseStrategy):
    def __init__(self):
        self.site_type = SiteType.KYOBO
        self.rank_type = RankType.NONE

    def parse(self, dom: BeautifulSoup):
        title_item = dom.select('div.box_detail_point')
        body_item = dom.select('ul.list_detail_price')
        book_info = BookInfo()

        # 판매지수
        book_info.selling_score = "-"
        # 세일가
        book_info.sale_price = body_item[0].select_one('li:nth-child(1) > span.sell_price > strong').text
        print(book_info.sale_price)

        return book_info