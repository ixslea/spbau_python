import itertools

first_6_fibs = [1, 1, 2, 3, 5, 8]
class Fib6:    
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _Fib6_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.fibs = first_6_fibs # они у нас выше были

        def add(self, a):
            self.fibs.append(a)
        
        def __next__(self):

            #if self.i >= 20:            # Если хочется остановиться на каком-то числе
                #raise StopIteration()
            if self.i >= 6:
                j = self.i
                self.i += 1
                p = self.fibs[j-2]
                l = self.fibs[j-1]
                p, l = l, p+l
                self.add(l)
                return self.fibs[j]
            else:
                j = self.i # Вывод первых 6 изначальных чисел из списка
                self.i += 1
                return self.fibs[j]

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib6._Fib6_iter()

f6 = Fib6()

# Вывод - бесконечный
for f in f6:
   print(f)




