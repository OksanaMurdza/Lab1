import pickle

class database:
    def __init__(self):
        try:
            self.data = pickle.load(open('database.p', 'rb'))
        except:
            self.data = {}
            self.data['config'] = {
                'cid_current': 100,
                'sid_current': 200,
                'initMe': True
            }

            self.data['cinemas'] = []
            self.data['seances'] = []

            pickle.dump(self.data, open('database.p', 'wb'))
    def __del__(self):
        pickle.dump(self.data, open('database.p', 'wb'))
