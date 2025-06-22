from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.statuses_file_name = None
        self.statuses_counters = {}

    def open_spider(self, spider):
        time_mark = (datetime.utcnow().replace(microsecond=0)
                     .isoformat().replace(':', '-'))
        self.statuses_file_name = (
            BASE_DIR / f'results/status_summary_{time_mark}.csv'
        )

    def process_item(self, item, spider):
        status = item['status']
        self.statuses_counters[status] = (self.statuses_counters
                                          .get(status, 0) + 1)
        return item

    def close_spider(self, spider):
        statuses_counters_total = sum(self.statuses_counters.values())
        # 'Статус': 'Количество'
        # 'Total': statuses_counters_total
        with open(self.statuses_file_name, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.statuses_counters.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{statuses_counters_total}\n')
