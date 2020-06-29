import numpy as np
import pandas as pd

class Thread():

    def __init__(self, thread):
        self._thread = thread.copy()
        self._offers = self._thread.sort_values('src_cre_date', ascending = True)[['anon_thread_id','anon_byr_id', 'anon_slr_id', 'offr_type_id','status_id','offr_price', 'src_cre_date']]

    def get_thread(self):
        return self._thread.copy()


    def get_offers(self):
        return self._offers.copy()

    def sold(self):
        return len(np.array(self._thread[self._thread['status_id'] == 1]['anon_byr_id'])) > 0

    def get_winning_offer(self):
        return np.array(self._thread[self._thread['status_id'] == 1]['offr_price'])[0]