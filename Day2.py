movies = ['The Lost Bus (2025)','The Gorge (2025)','Highest 2 Lowest (2025)','The Monkey (2025)','No Other Choice (2025)']
movies.append('ANACONDA')
movies.append("The Conjuring")
movies.pop(2)
print(movies[::-1])
print(movies)

numbers = list(range(1,21))
a = numbers[:5]
b = numbers[-5:]
c = numbers[5:15]
d =  numbers[::3]

print(a,b,c,d)


num = list(range(1,101))
even_num = [x ** 2 for x in num if x %2 == 0]
divisible_7 = [x for x in num if x %7 == 0]
a = [(x,'even' if x % 2 == 0 else "odd" )for x in num]
   
print("Squares of even numbers:", even_num)
print("Numbers divisible by 7:", divisible_7)
print("List of tuples (number, even/odd):", a)