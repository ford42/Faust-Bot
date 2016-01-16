import _thread

from Communication.Observable import Observable

class JoinObservable(Observable):

    def input(self, raw_data):
        data = {}
        data['raw'] = raw_data
        data['nick'] = raw_data.split('!')[0][1:]
        data['channel'] = raw_data.split('JOIN ')[1].split(' :')[0]
        data['raw_nick'] = raw_data.split(' JOIN')[0][1:]
        self.notifyObservers(data)

    def input_names(self, raw_data):
        data ={}
        data['raw_data'] = raw_data
        data['channel'] = raw_data.split(' = ')[1].split(' :')[0]
        nicks = raw_data.split('353')[1].split('\n')[0].split(' :')[1].split(' ')
        for nick in nicks:
            data['nick'] = nick
            self.notifyObservers(data)
            # TODO remove \r of last nick, remove +@ etc of all nicks


    def notifyObservers(self, data):
         for observer in self._observers:
            _thread.start_new_thread(observer.__class__.update_on_join, (observer, data))