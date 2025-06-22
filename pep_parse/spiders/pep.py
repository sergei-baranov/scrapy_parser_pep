import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        pep_name = response.meta.get('pep_name')
        pep_number = response.meta.get('pep_number')

        pep_status = response.xpath(
            '//dt[contains(text(), "Status")]'
            '/following-sibling::dd[1]/abbr/text()'
        ).get().strip()

        yield PepParseItem({
            'number': pep_number,
            'name': pep_name,
            'status': pep_status,
        })

    def parse(self, response, **kwargs):
        all_pep_rows = response.xpath(
            '//section[@id="index-by-category"]'
            '//table[contains(@class, "pep-zero-table")]/tbody/tr')

        for pep_row in all_pep_rows:
            pep_number = int(
                pep_row.xpath('td[2]/descendant-or-self::*/text()')
                .get().strip()
            )
            pep_anchor = pep_row.xpath('td[3]/a')[0]
            pep_name = pep_anchor.css('::text').get().strip()

            yield response.follow(
                pep_anchor,
                callback=self.parse_pep,
                meta={
                    'pep_number': pep_number,
                    'pep_name': pep_name,
                },
            )
