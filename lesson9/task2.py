# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class HuffmanTree:
    """ Класс дерева """

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def leaf(self):  # узел\лист
        return self.left, self.right

    def __str__(self):
        return f'{self.left}{self.right}'


def huffman_coding(node, code=""):
    """
        Кодирование строки алгоритмом Хаффман с помощью рекурсии.
        На выходе получаем словарь, где в качестве ключа является исходный символ, в качестве значения его
        закодированное значение.
    """
    if type(node) is str:
        return {node: code}
    (left, right) = node.leaf()
    coding = {}
    coding.update(huffman_coding(left, code + "0"))
    coding.update(huffman_coding(right, code + "1"))
    return coding


def hmc(str_line):
    """ Основная функция по кодированию иходной строки """
    encoded_str = ""

    # Подсчет частоты встречи символов
    count = Counter()
    for i in str_line:
        count[i] += 1
    freq = sorted(count.items(), key=lambda x: x[1], reverse=True)
    nodes = freq[:]

    # Цикл для построения дерева
    while len(nodes) > 1:
        # забираем два последних значения из списка
        s1, c1 = nodes.pop()
        s2, c2 = nodes.pop()
        # строим узел и добавляем его в список, после чего повторяем сортировку
        node = HuffmanTree(s1, s2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    # кодируем, используя построенное дерево
    huffman_code = huffman_coding(nodes[0][0])
    for key in str_line:
        encoded_str += huffman_code[key] + " "

    return encoded_str


string1 = 'bccabbddaeccbbaeddcc'
print(f'Исходное сообщение: {string1}')
print(f'Закодированное сообщение: {hmc(string1)}')

string2 = 'beep boop beer!'
print(f'Исходное сообщение: {string2}')
print(f'Закодированное сообщение: {hmc(string2)}')
