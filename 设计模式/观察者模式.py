class Subject(object):
    __observers = []

    def __init__(self,state='sunny'):#sunny rain
        self.__state = state

    def get_state(self):
        return self.__state

    def set_state(self,state):
        self.__state = state
        self.notify_observers()

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()

    def attach_observers(self,observer):
        self.__observers.append(observer)

class Observer(object):

    def __init__(self,subject):
        self._subject = subject
        subject.attach_observers(self)

    def update(self):
        pass


class Boy(Observer):
    def update(self):
        if self._subject.get_state() == 'sunny':
            print('boy will play football while sunny.')
        elif self._subject.get_state() == 'rain':
            print('boy will read while rain.')


class Girl(Observer):
    def update(self):
        if self._subject.get_state() == 'sunny':
            print('girl will go hiking while sunny.')
        elif self._subject.get_state() == 'rain':
            print('girl will read while rain.')


if __name__ == "__main__":
    subject = Subject()
    boy = Boy(subject)
    girl = Girl(subject)
    subject.set_state('rain')
    subject.set_state('sunny')
