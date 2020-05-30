class WashingMachine:
    def __init__(self):
        pass

    def washing(self, temperature='hot'):
        self._fill_up(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_up(self, temperature):
        print('Fill up with {temperature}')

    def _add_soap(self):
        print('Add soap')

    def _wash(self):
        print('Wash')

    def _centrifuge(self):
        print('Centrifuge')


if __name__ == '__main__':
    wash_one = WashingMachine()
    wash_one.washing('cold')
