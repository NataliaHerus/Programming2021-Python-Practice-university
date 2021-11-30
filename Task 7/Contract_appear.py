from Validation import *


class Contract(object):
    def __init__(self, **kwargs):
        for (prop, default) in kwargs.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def name(self):
        return self._name

    @name.setter
    @Validation.check_name
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    @Validation.check_email
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    @Validation.check_phone
    def phone(self, value):
        self._phone = value

    @property
    def iban(self):
        return self._iban

    @iban.setter
    @Validation.check_iban
    def iban(self, value):
        self._iban = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    @Validation.check_date
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    @Validation.check_date
    @Validation.compare_dates
    def end_date(self, value):
        self._end_date = value

    ''''@Validation.check_a_contract
    def validate_contract(self, v1, v2, v3, v4, v5, v6):
        self._name = v1
        Validation.check_name(v1)
        self._email = v2
        Validation.check_email(v2)
        self._phone = v3
        Validation.check_phone(self._phone)
        self._iban = v4
        Validation.check_iban(self._iban)
        self._start_date = v5
        Validation.check_date(self._start_date)
        self._end_date = v6
        Validation.check_date(self._end_date)'''

    def __get_dictionary__(self):
        return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
                    and not name.startswith('_') and name != "input_product")

    @staticmethod
    def input_product(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d

    def __str__(self):
        return "Contract:\n" + '\n'.join("%s : %r" % (key2, str(val2)) for (key2, val2)
                                         in self.__get_dictionary__().items()) + "\n"
