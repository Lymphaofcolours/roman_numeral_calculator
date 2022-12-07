if __name__ == '__main__':
# -*- coding: utf-8 -*-


    def input_number():
        '''
        :return: str: Input number from user. Detect invalid inputs and ask for number again.
        '''
        input_x: int = input('Input Your Number [<= 10e6]:')
        try:
            input_x = int(input_x)
            if input_x > 1e6:
                print('Wrong Value [> 10e6]. Please, Try Again:')
                return input_number()
            else:
                return str(input_x)
        except ValueError:
            print('Wrong Input. Please, Try Again:')
            return input_number()


    reference_dict: dict = {'0': '',
                            '1': 'I',
                            '5': 'V',
                            '10': 'X',
                            '50': 'L',
                            '100': 'C',
                            '500': 'D',
                            '1000': 'M',
                            '5000': str(u'V\u0304'),
                            '10000': str(u'X\u0304'),
                            '50000': str(u'L\u0304'),
                            '100000': str(u'C\u0304'),
                            '500000': str(u'D\u0304'),
                            '1000000': str(u'M\u0304')
                            }

    def num_decomp(count: int = 1) -> list:
        '''
        Decompose each number in multiples of 10 starting with units and return it as an inverted list of tuples.
            :param: count: int
            :return: list(tuple(str, int)
        '''
        listnum: list = []
        listcount: list = []
        def nine_decomp() -> tuple:
            '''
            :return: str, int
            '''
            listnum.append(str(1))
            listcount.append(count*10)
            listnum.append(str(1))
            listcount.append(count)
        def five_plus_decomp() -> tuple:
            '''
            :return: str, int
            '''
            listnum.append(str(int(i) - 5))
            listcount.append(count)
            listnum.append(str(5))
            listcount.append(count)
        def five_decomp() -> tuple:
            '''
            :return: str, int
            '''
            listnum.append(str(5))
            listcount.append(count)
        def four_decomp() -> tuple:
            '''
            :return: str, int
            '''
            listnum.append(str(5))
            listcount.append(count)
            listnum.append(str(1))
            listcount.append(count)
        def four_less_decomp() -> tuple:
            '''
            :return: str, int
            '''
            listnum.append(i)
            listcount.append(count)
        for i in input_number()[::-1]:
            if int(i) == 9:
                nine_decomp()
            elif (int(i) - 5) > 0:
                five_plus_decomp()
            elif (int(i) - 5) == 0:
                five_decomp()
            elif (int(i) - 5) == -1:
                four_decomp()
            else:
                four_less_decomp()
            count *= 10
        # I chose a tuple because dictionaries don´t accept two entries with the same key
        ziptuple = zip(listnum, listcount)
        # Returns inverted list of tuples
        return list(ziptuple)[::-1]

    def sequencer(ziptuple) -> str:
        '''
        Take output list from num_decomp function, extract elements and compare with dictionary values.
        :param: ziptuple (list) : List of tuples with input number decomposed.
        :return: sequence (str) : Roman numeral sequence.
        '''
        listletter: list = []
        for i in ziptuple:
            # Searches for the count times first element(eg.5*100=500) and looks for its value in reference_dict.
            if i[0] == '5':
                listletter.append(reference_dict.get(str(int(i[0]) * int(i[1]))))
            # Writes [count] as many times as the first element value (eg: '3', 100 -> 100,100,100) and looks for their values in reference_dict.
            else:
                listletter.append(reference_dict.get(str(i[1])) * int(i[0]))
        letterseq = ''.join(listletter)
        print(letterseq)


    sequencer(num_decomp())

