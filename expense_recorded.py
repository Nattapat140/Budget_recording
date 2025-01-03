import sys
import matplotlib.pyplot as plt
"""Class template from weekly checkpoint 10"""
class Record:
    '''Represent a record.'''
    def __init__(self, C, D, A):
        self._Category = C
        self._Description = D
        self._Amount = A
        
    @property
    def get_Category(self):
        """return self._Category"""
        return self._Category
    
    @property
    def get_Description(self):
        """return self._Description"""
        return self._Description
    
    @property
    def get_Amount(self):
        """return self._Amount"""
        return self._Amount
        
class Records:
    '''Maintain a list of all the 'Record's and the initial amount of money.'''
    def __init__(self):
        """Read total balance from the file"""
        self._new = 0
        try:
            with open('Balance.txt', 'r') as fh:
                self._balance = fh.read()
                if self._balance == 'q':
                    self._new = 1
        except OSError:
            sys.stderr.write('File not found TT')
            
            """Read records from the file"""
        try:
            with open('Records.txt') as fh:
                self._records_book = fh.read()
        except OSError:
            sys.stderr.write('File not found TT')
        if self._new == 1:
            try:
                self._balance = int(input('Hi, welcome to pymoney, How much money do you have? '))
            except ValueError:
                sys.stderr.write('Wrong input')
                self._balance = 0
            try:
                with open('Balance.txt', 'w') as fh:
                    fh.write(str(self._balance))
            except OSError:
                sys.stderr.write('File not found TT')
            self._new = 0
        elif self._new == 0:
            print('Welcome back!')
    
    def show_graph(self, choice):
        '''show graph(records)'''
        try:
            tmp = self._records_book.split(',')
            tmp.pop()
            if choice in 'Cc':
                d= {}
                data = {}
                for i in tmp:
                    i = i.split()
                    if i[0] in d.keys():
                        num = int(d[i[0]])
                        num += int(i[2])
                        d[i[0]] = num
                    else:
                        d[i[0]] = int(i[2])
                    data.update(d)
                description = list(data.keys())
                values = list(data.values())
                fig = plt.figure(figsize = (10, 10))
                # creating the bar plot
                plt.bar(description, values, color ='gold',width = 0.1)
                plt.xlabel("Categories")
                plt.ylabel("Amount")
                plt.title("Here's your expense and income records")
                plt.show()
                print(f'Now you have {self._balance} dollars.\n')
                return
            elif choice in 'Dd':
                d= {}
                data = {}
                for i in tmp:
                    i = i.split()
                    if i[0] in d.keys():
                        num = int(d[i[1]])
                        num += int(i[2])
                        d[i[1]] = num
                    else:
                        d[i[1]] = int(i[2])
                    data.update(d)
                description = list(data.keys())
                values = list(data.values())
                fig = plt.figure(figsize = (10, 10))
                # creating the bar plot
                plt.bar(description, values, color ='lightskyblue',width = 0.1)
                plt.xlabel("Descriptions")
                plt.ylabel("Amount")
                plt.title("Here's your expense and income records")
                plt.show()
                print(f'Now you have {self._balance} dollars.\n')
                return
            else:
                sys.stderr.write('Wrong Input')
        except (ValueError, IndexError):
            sys.stderr.write('Wrong Input')
       
    def add(self, lists):
        '''add records'''
        for i in lists:
            try:
                tmp = i.split()
                record = Record(tmp[0],tmp[1],tmp[2])
                Category = record.get_Category
                Description = record.get_Description
                Amount = record.get_Amount
                if categories.is_category_valid(Category, categories._categories) == True:
                    self._balance = int(self._balance) + int(Amount)
                    self._records_book = self._records_book + ''.join(str(i)) + ','
                    self.save
                else:
                    sys.stderr.write('The specified category is not in the category list. \
                    \nYou can check the category list by command "view categories". \
                    \nFail to add a record.')
            except (ValueError, IndexError):
                sys.stderr.write('Wrong Input')
        return

    @property
    def view(self):
        '''view records'''
        tmp = self._records_book.split(',')
        tmp.pop()
        print("\nHere's your expense and income records:")
        print('Category        Description          Amount')
        print('=============== ==================== ======')
        for i in tmp:
            i = i.split()
            spaces = 15 - int(len(i[0]))
            print(i[0], ' '*spaces, end='')
            spaces = 20 - int(len(i[1]))
            print(i[1], ' '*spaces, end='')
            spaces = 6 - int(len(i[1]))
            print(i[2], ' '*spaces)
        print('===========================================')
        print(f'Now you have {self._balance} dollars.\n')
        return

    def delete(self, Del):
        '''delete records'''
        tmp = self._records_book.split(',')
        tmp.pop()
        if Del not in tmp:
            sys.stderr.write('Sorry we cannot find the given input in the list')
            return
        cnt = 0
        tmp_list = []
        for i in tmp:
            if Del in i:
                tmp_list.append(i)
                cnt+=1
        if cnt == 1:
            des = tmp_list[0]+','
            del_balance = tmp_list[0].split()
            self._balance = int(self._balance) - int(del_balance[2])
            self._records_book = self._records_book.replace(des, '')
            self.save
        elif cnt > 1:
            print('There are more than 1 description with same as the input')
            pos = 1
            for j in tmp_list:
                print(f'{pos}-> {j}')
                pos+=1
            try:
                choose = int(input('Please input a number: '))
                if choose <= 0 or choose > pos:
                    sys.stderr.write('Wrong input!')
                    return
                choose-=1
                des = tmp_list[choose]
                del_balance = tmp_list[choose].split()
                self._balance = int(self._balance)-int(del_balance[2])
                self._records_book = self._records_book.split(',')
                tmp_cnt = 0
                tmp_cntt = 0
                for k in self._records_book:
                    if des in k:
                        tmp_cnt+=1
                    if tmp_cnt == choose+1:
                        self._records_book.pop(tmp_cntt)
                        break
                    tmp_cntt+=1
                self._records_book = ','.join(self._records_book)
                self.save
            except ValueError:
                sys.stderr.write('Wrong input!')
        return

    def find(self, lists, check):
        '''find categories'''
        tmp = self._records_book.split(',')
        tmp.pop()
        cnt=0
        for i in tmp:
            tmp[cnt]=i.split()
            cnt+=1
        if check == True:
            result = list(filter(lambda x: x[0] in lists, tmp))
            cnt=0
            balance = 0
            for i in result:
                balance += int(i[2])
                result[cnt] = ' '.join(i)
                cnt+=1
            print(f"\nHere's your expense and income records under category '{category}':")
            print('Category        Description          Amount')
            print('=============== ==================== ======')
            for i in result:
                i = i.split()
                spaces = 15 - int(len(i[0]))
                print(i[0], ' '*spaces, end='')
                spaces = 20 - int(len(i[1]))
                print(i[1], ' '*spaces, end='')
                spaces = 6 - int(len(i[1]))
                print(i[2], ' '*spaces)
            print('===========================================')
            print(f'The total amount above is {balance}.\n')
            return
        else:
            sys.stderr.write('The specified category is not in the category list. \
            \nYou can check the category list by command "view categories"')
        
    @property
    def save(self):
        '''save balance and records to files'''
        try:
            with open('Balance.txt', 'w') as fh:
                fh.write(str(self._balance))
            with open('Records.txt', 'w') as fh:
                fh.writelines(list(self._records_book))
            return
        except OSError:
            sys.stderr.write('File not found TT')
        
class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self): ##Got reference from hint in weekly checkpoint
        '''initialize catgories'''
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation',
        ['bus', 'railway']], 'income', ['salary', 'bonus']]
        self._pos = 0
        self._white = " "

    def view(self, L):
        '''show categories'''
        if type(L) == list:
            self._pos+=2
            result = []
            for child in L:
                ans = categories.view(child)
                if ans == []:
                    self._pos-=2
                else:
                    print(f'{self._white*self._pos}- {ans}')
            return result
        else:
            return L

    def is_category_valid(self, category, cate):
        '''check categories whether it is valid or not'''
        if type(cate) != list:
            if cate == category:
                return True
            else:
                return False
        else:
            check = False
            for i in cate:
                check = self.is_category_valid(category,i)
                if check == True:
                    return check
            return check


    def find_subcategories(self, category, categories): ##Got reference from hint in weekly checkpoint 12
        '''find subcategories'''
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                    and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(category, categories[index + 1], found=True)
            else:
                if categories == category or found == True:
                    yield categories
                
        return list(find_subcategories_gen(category, categories, found=False))


    """def _flatten(self, L): ##Got reference from hint in weekly checkpoint
        '''turn nest lists into normal flat list'''
        if type(L) == list:
            result = []
            for child in L:
                result.extend(self._flatten(child))
            return result
        else:
            return [L]"""

categories = Categories()
records = Records()

while True:
    try:
        command = input('What do you want to do? \
        \n(a or A)add \
        \n(v or V)view \
        \n(d or D)delete \
        \n(g or G)graph \
        \n(vc or VC)view categories \
        \n(f or F)find \
        \n(e or E)exit\n')
        if command in 'eE':
            print('Bye~')
            records.save
            break
        if command in 'aA':
            lists = str(input('Add some expense or income records with categories, description and amount: ')).split(', ')
            records.add(lists)
            continue
        if command in 'vV':
            records.view
            continue
        if command in 'dD':
            Del = str(input('Type the category, description and amount: '))
            records.delete(Del)
            continue
        if command in 'gG':
            choice = str(input("What do want prefer? 'D'/'d' for Description/Amount or 'C'/'c' for Categories/Amount"))
            records.show_graph(choice)
            continue
        if command == 'vc' or command == 'VC':
            categories.view(categories._categories)
            continue
        if command in 'fF':
            category = input('Which category do you want to find? ')
            check = categories.is_category_valid(category, categories._categories)
            lists = categories.find_subcategories(category, categories._categories)
            records.find(lists, check)
            continue
        else:
            sys.stderr.write('Wrong input!')
    except (ValueError, IndexError):
        sys.stderr.write('Wrong input!')
