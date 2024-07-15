class Solution:
    def num_to_str_arr(self, number):
        if number < 1000:
            return [str(number)]
        num = str(number)[::-1]
        arr = []
        for i in range(0,len(num)-3,3):
            arr.append(num[i:i+3][::-1])
        if len(num) == 6 or len(num) == 9:
            arr.append(num[len(num) - 3:][::-1])
        else:
            arr.append(num[len(num) - len(num)%3:][::-1])  
        arr = arr[::-1]
        return arr

    dct = {
        1: 'One ',
        2: 'Two ',
        3: 'Three ',
        4: 'Four ',
        5: 'Five ',
        6: 'Six ',
        7: 'Seven ',
        8: 'Eight ',
        9: 'Nine '
    }

    teens_dct = {
        10: 'Ten ',
        11: 'Eleven ',
        12: 'Twelve ',
        13: 'Thirteen ',
        14: 'Fourteen ',
        15: 'Fifteen ',
        16: 'Sixteen ',
        17: 'Seventeen ',
        18: 'Eighteen ',
        19: 'Nineteen '
    }

    tens_dct = {
        2: 'Twenty ',
        3: 'Thirty ',
        4: 'Forty ',
        5: 'Fifty ',
        8: 'Eighty '
    }


    def to_words_3_dig(self, number):
        hundreds = int(number) // 100
        tens = int(number) % 100 // 10
        units = int(number) % 10
        if tens == 1:
            last_two = int(str(tens) + str(units))
            tens = self.teens_dct[last_two]
            units = ''
        elif tens > 1 and tens < 6 or tens == 8:
            tens = self.tens_dct[tens]
            units = '' if units == 0 else self.dct[units]
        else:
            tens = self.dct[tens].strip() + 'ty ' if tens != 0 else ''
            units = '' if units == 0 else self.dct[units]
        if hundreds == 1:
            hundreds = 'One Hundred '
        else:
            hundreds = self.dct[hundreds] + 'Hundred ' if hundreds != 0 else ''
        return hundreds + tens + units        
        

    def numberToWords(self, num: int) -> str: 
        if num == 0:
            return 'Zero'
        lst = self.num_to_str_arr(num)
        words = ''
        if len(lst) == 4:
            words += (self.to_words_3_dig(lst[0]) + 'Billion ')
            if int(lst[1]) != 0:
                words += (self.to_words_3_dig(lst[1]) + 'Million ')
            if int(lst[2]) != 0:
                words += (self.to_words_3_dig(lst[2]) + 'Thousand ')
            if int(lst[3]) != 0:
                words += self.to_words_3_dig(lst[3])

        elif len(lst) == 3:
            words += (self.to_words_3_dig(lst[0]) + 'Million ')
            if int(lst[1]) != 0:
                words += (self.to_words_3_dig(lst[1]) + 'Thousand ')
            if int(lst[2]) != 0:
                words += self.to_words_3_dig(lst[2])

        elif len(lst) == 2:
            words += (self.to_words_3_dig(lst[0]) + 'Thousand ')
            if int(lst[1]) != 0:
                words += self.to_words_3_dig(lst[1])

        elif len(lst) == 1:
            words += self.to_words_3_dig(lst[0])

        return words.strip()
    

print(Solution().numberToWords(18934528))
