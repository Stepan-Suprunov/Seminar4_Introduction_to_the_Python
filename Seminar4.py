#  Наепишите программу, которая на вход принимает стрку, и отслеживаает, сколько раз каждый символ уже встречался.
#  Количество повторов добавляется к символамс помощью плстфикса формата _n.

string = 'd g h t r g r h t j n b v f d s d f'
my_list = string.split(' ')
my_dict = {}

new_list = []

for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)

print(' '.join(new_list))


#  Пользователь вводит текст (строка).
#  Словом считается последовательность непробельных символов идущих подряд,
#  слова разделены одним или большим числом пробелов.
#  Определите, сколько различных слов сожержится в этом тексте.

string = 'сегодня мама мыла раму  раму мыла без отца'
collection = string.split(' ')
collection = set(collection)
collection.discard('')

print(len(collection))


#  Дана последовательность чисел, получить список уникальных элементов заданной последовательности.
#  [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_dict = {}
my_collection = []

for number in my_list:
    my_dict[number] = my_dict.get(number, 0) + 1

for i in my_dict:
    if my_dict[i] == 1:
        my_collection.append(i)

print(my_collection)
