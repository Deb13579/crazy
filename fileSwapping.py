Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open(crazy, "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
        print("The file says", data_a)

        
fileSwapper()
Name the file which you want to get data from: Crazy
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'Crazy'
fileSwapper()
Name the file which you want to get data from: craazy
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'craazy'
fileSwapper()
Name the file which you want to get data from: crazy
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'crazy'
fileSwapper()
Name the file which you want to get data from: crazy
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'crazy'
fileSwapper()
Name the file which you want to get data from: 
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: ''
fileSwapper()
Name the file which you want to get data from: crazy.txt
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'crazy.txt'
fileSwapper()
Name the file which you want to get data from: crazy
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'crazy'
fileSwapper()
Name the file which you want to get data from: crazy.txt
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'crazy.txt'
fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/crazy.txt
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fileSwapper()
  File "<pyshell#1>", line 5, in fileSwapper
    with open(crazy, "r") as b:
NameError: name 'crazy' is not defined
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open(C:/Users/dbrp2/Downloads/crazy.txt, "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
        print("The file says", data_a)
        
SyntaxError: expected ':'
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open(C:/Users/dbrp2/Downloads/crazy.txt, "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
        print("The file says", data_a)
        
SyntaxError: expected ':'
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
        print("The file says", data_a)

        
fileSwapper():
    
SyntaxError: invalid syntax
fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/crazy.txt
The file says 
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "w") as b:
        b.write(data_a)
        print("This random file says", data_a)
        print("The file you actually wanted said", data_b)

        
fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/loremipsum.text
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fileSwapper()
  File "<pyshell#19>", line 3, in fileSwapper
    with open(fileName, "r") as a:
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/dbrp2/Downloads/loremipsum.text'
fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/loremipsum.txt
This random file says Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla rutrum ornare hendrerit. In lacinia facilisis pharetra. Ut pulvinar iaculis purus at tempor. Proin euismod sem metus, nec laoreet elit imperdiet id. Nullam sit amet lorem luctus augue luctus dignissim. In hac habitasse platea dictumst. Ut semper feugiat orci eu faucibus. Suspendisse risus lacus, finibus condimentum orci sit amet, tincidunt tempus nulla. Proin felis erat, imperdiet ut nulla sed, consequat tristique tellus. Cras mauris lorem, molestie sit amet auctor sit amet, venenatis et neque. Donec quis elit faucibus, dignissim ante quis, aliquam mi. Vestibulum nisi mi, placerat vitae metus eget, volutpat accumsan purus. Proin vitae tellus ullamcorper, aliquam metus quis, egestas erat.

Sed massa nulla, ullamcorper vel volutpat dapibus, auctor at velit. Donec orci velit, luctus eu nibh sed, lobortis mattis ante. Nulla placerat tristique scelerisque. Etiam sed mi lobortis, fermentum lacus et, fringilla nibh. Maecenas sit amet nisl nulla. Nam non auctor justo. Donec vel consectetur risus.

Quisque sollicitudin aliquam purus ultrices sodales. Suspendisse potenti. Mauris eu suscipit felis, vel mattis libero. Nulla facilisi. Donec eleifend vulputate elit sed mollis. Vestibulum turpis ex, malesuada dictum dignissim ac, finibus et nunc. Nunc scelerisque nibh ac consectetur mollis. Sed consequat nulla ut ligula aliquet, non ultricies orci cursus. Nullam viverra nisi elit, ac consequat felis consequat ac. Phasellus ultrices hendrerit odio sed finibus. Cras tincidunt in nisl sit amet pulvinar. Cras efficitur ullamcorper euismod. Nullam mollis porta mauris vel suscipit.

Pellentesque sollicitudin ullamcorper elit id hendrerit. Curabitur accumsan cursus felis quis egestas. Quisque ante sem, auctor posuere placerat ac, blandit at erat. Aenean feugiat semper enim non finibus. Nam ornare egestas tortor, eget blandit felis auctor in. Curabitur ligula leo, facilisis sed nulla nec, ornare efficitur ligula. Donec a sagittis enim, rutrum gravida lacus. Donec imperdiet, nisl nec blandit tempor, elit risus efficitur felis, non finibus urna nisl a mauris. Praesent tempus velit et aliquet vulputate.

Donec commodo volutpat tincidunt. Suspendisse non tempus dui. Aliquam orci arcu, venenatis vel eros vel, maximus tempor ligula. Donec eu tortor nisl. Ut congue, nunc id euismod volutpat, justo neque suscipit quam, ultricies fermentum velit tortor sit amet tellus. Fusce convallis magna sagittis tellus semper, a laoreet justo fermentum. Maecenas porttitor mi turpis, sed porta risus fringilla sed. Nulla ex lacus, condimentum eget sapien sed, pellentesque vehicula lectus. Vivamus vitae orci pellentesque, laoreet mauris et, scelerisque odio. Ut vel ipsum metus. Vivamus rutrum, justo venenatis hendrerit tristique, nulla ex placerat justo, quis eleifend ante nunc eget orci.


The file you actually wanted said 
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "w") as b:
        b.write(data_a)
        print("This random file says", data_b)
        print("The file you actually wanted said", data_a)

        
fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/loremipsum.txt
This random file says Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla rutrum ornare hendrerit. In lacinia facilisis pharetra. Ut pulvinar iaculis purus at tempor. Proin euismod sem metus, nec laoreet elit imperdiet id. Nullam sit amet lorem luctus augue luctus dignissim. In hac habitasse platea dictumst. Ut semper feugiat orci eu faucibus. Suspendisse risus lacus, finibus condimentum orci sit amet, tincidunt tempus nulla. Proin felis erat, imperdiet ut nulla sed, consequat tristique tellus. Cras mauris lorem, molestie sit amet auctor sit amet, venenatis et neque. Donec quis elit faucibus, dignissim ante quis, aliquam mi. Vestibulum nisi mi, placerat vitae metus eget, volutpat accumsan purus. Proin vitae tellus ullamcorper, aliquam metus quis, egestas erat.

Sed massa nulla, ullamcorper vel volutpat dapibus, auctor at velit. Donec orci velit, luctus eu nibh sed, lobortis mattis ante. Nulla placerat tristique scelerisque. Etiam sed mi lobortis, fermentum lacus et, fringilla nibh. Maecenas sit amet nisl nulla. Nam non auctor justo. Donec vel consectetur risus.

Quisque sollicitudin aliquam purus ultrices sodales. Suspendisse potenti. Mauris eu suscipit felis, vel mattis libero. Nulla facilisi. Donec eleifend vulputate elit sed mollis. Vestibulum turpis ex, malesuada dictum dignissim ac, finibus et nunc. Nunc scelerisque nibh ac consectetur mollis. Sed consequat nulla ut ligula aliquet, non ultricies orci cursus. Nullam viverra nisi elit, ac consequat felis consequat ac. Phasellus ultrices hendrerit odio sed finibus. Cras tincidunt in nisl sit amet pulvinar. Cras efficitur ullamcorper euismod. Nullam mollis porta mauris vel suscipit.

Pellentesque sollicitudin ullamcorper elit id hendrerit. Curabitur accumsan cursus felis quis egestas. Quisque ante sem, auctor posuere placerat ac, blandit at erat. Aenean feugiat semper enim non finibus. Nam ornare egestas tortor, eget blandit felis auctor in. Curabitur ligula leo, facilisis sed nulla nec, ornare efficitur ligula. Donec a sagittis enim, rutrum gravida lacus. Donec imperdiet, nisl nec blandit tempor, elit risus efficitur felis, non finibus urna nisl a mauris. Praesent tempus velit et aliquet vulputate.

Donec commodo volutpat tincidunt. Suspendisse non tempus dui. Aliquam orci arcu, venenatis vel eros vel, maximus tempor ligula. Donec eu tortor nisl. Ut congue, nunc id euismod volutpat, justo neque suscipit quam, ultricies fermentum velit tortor sit amet tellus. Fusce convallis magna sagittis tellus semper, a laoreet justo fermentum. Maecenas porttitor mi turpis, sed porta risus fringilla sed. Nulla ex lacus, condimentum eget sapien sed, pellentesque vehicula lectus. Vivamus vitae orci pellentesque, laoreet mauris et, scelerisque odio. Ut vel ipsum metus. Vivamus rutrum, justo venenatis hendrerit tristique, nulla ex placerat justo, quis eleifend ante nunc eget orci.


The file you actually wanted said 
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "w") as b:
        b.write(data_a)
        print("This random file says", data_b)
        print("The file you actually wanted said", data_a)

        

def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
    with open("C:/Users/dbrp2/Downloads/crazy.txt", "w") as b:
        b.write(data_a)
        print("This random file says", data_b)
        print("The file you actually wanted said", data_a)

        

fileswapper()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    fileswapper()
NameError: name 'fileswapper' is not defined. Did you mean: 'fileSwapper'?
fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/loremipsum.txt
This random file says 
The file you actually wanted said Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla rutrum ornare hendrerit. In lacinia facilisis pharetra. Ut pulvinar iaculis purus at tempor. Proin euismod sem metus, nec laoreet elit imperdiet id. Nullam sit amet lorem luctus augue luctus dignissim. In hac habitasse platea dictumst. Ut semper feugiat orci eu faucibus. Suspendisse risus lacus, finibus condimentum orci sit amet, tincidunt tempus nulla. Proin felis erat, imperdiet ut nulla sed, consequat tristique tellus. Cras mauris lorem, molestie sit amet auctor sit amet, venenatis et neque. Donec quis elit faucibus, dignissim ante quis, aliquam mi. Vestibulum nisi mi, placerat vitae metus eget, volutpat accumsan purus. Proin vitae tellus ullamcorper, aliquam metus quis, egestas erat.

Sed massa nulla, ullamcorper vel volutpat dapibus, auctor at velit. Donec orci velit, luctus eu nibh sed, lobortis mattis ante. Nulla placerat tristique scelerisque. Etiam sed mi lobortis, fermentum lacus et, fringilla nibh. Maecenas sit amet nisl nulla. Nam non auctor justo. Donec vel consectetur risus.

Quisque sollicitudin aliquam purus ultrices sodales. Suspendisse potenti. Mauris eu suscipit felis, vel mattis libero. Nulla facilisi. Donec eleifend vulputate elit sed mollis. Vestibulum turpis ex, malesuada dictum dignissim ac, finibus et nunc. Nunc scelerisque nibh ac consectetur mollis. Sed consequat nulla ut ligula aliquet, non ultricies orci cursus. Nullam viverra nisi elit, ac consequat felis consequat ac. Phasellus ultrices hendrerit odio sed finibus. Cras tincidunt in nisl sit amet pulvinar. Cras efficitur ullamcorper euismod. Nullam mollis porta mauris vel suscipit.

Pellentesque sollicitudin ullamcorper elit id hendrerit. Curabitur accumsan cursus felis quis egestas. Quisque ante sem, auctor posuere placerat ac, blandit at erat. Aenean feugiat semper enim non finibus. Nam ornare egestas tortor, eget blandit felis auctor in. Curabitur ligula leo, facilisis sed nulla nec, ornare efficitur ligula. Donec a sagittis enim, rutrum gravida lacus. Donec imperdiet, nisl nec blandit tempor, elit risus efficitur felis, non finibus urna nisl a mauris. Praesent tempus velit et aliquet vulputate.

Donec commodo volutpat tincidunt. Suspendisse non tempus dui. Aliquam orci arcu, venenatis vel eros vel, maximus tempor ligula. Donec eu tortor nisl. Ut congue, nunc id euismod volutpat, justo neque suscipit quam, ultricies fermentum velit tortor sit amet tellus. Fusce convallis magna sagittis tellus semper, a laoreet justo fermentum. Maecenas porttitor mi turpis, sed porta risus fringilla sed. Nulla ex lacus, condimentum eget sapien sed, pellentesque vehicula lectus. Vivamus vitae orci pellentesque, laoreet mauris et, scelerisque odio. Ut vel ipsum metus. Vivamus rutrum, justo venenatis hendrerit tristique, nulla ex placerat justo, quis eleifend ante nunc eget orci.


fileSwapper()
Name the file which you want to get data from: C:/Users/dbrp2/Downloads/loremipsum.txt
This random file says Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla rutrum ornare hendrerit. In lacinia facilisis pharetra. Ut pulvinar iaculis purus at tempor. Proin euismod sem metus, nec laoreet elit imperdiet id. Nullam sit amet lorem luctus augue luctus dignissim. In hac habitasse platea dictumst. Ut semper feugiat orci eu faucibus. Suspendisse risus lacus, finibus condimentum orci sit amet, tincidunt tempus nulla. Proin felis erat, imperdiet ut nulla sed, consequat tristique tellus. Cras mauris lorem, molestie sit amet auctor sit amet, venenatis et neque. Donec quis elit faucibus, dignissim ante quis, aliquam mi. Vestibulum nisi mi, placerat vitae metus eget, volutpat accumsan purus. Proin vitae tellus ullamcorper, aliquam metus quis, egestas erat.

Sed massa nulla, ullamcorper vel volutpat dapibus, auctor at velit. Donec orci velit, luctus eu nibh sed, lobortis mattis ante. Nulla placerat tristique scelerisque. Etiam sed mi lobortis, fermentum lacus et, fringilla nibh. Maecenas sit amet nisl nulla. Nam non auctor justo. Donec vel consectetur risus.

Quisque sollicitudin aliquam purus ultrices sodales. Suspendisse potenti. Mauris eu suscipit felis, vel mattis libero. Nulla facilisi. Donec eleifend vulputate elit sed mollis. Vestibulum turpis ex, malesuada dictum dignissim ac, finibus et nunc. Nunc scelerisque nibh ac consectetur mollis. Sed consequat nulla ut ligula aliquet, non ultricies orci cursus. Nullam viverra nisi elit, ac consequat felis consequat ac. Phasellus ultrices hendrerit odio sed finibus. Cras tincidunt in nisl sit amet pulvinar. Cras efficitur ullamcorper euismod. Nullam mollis porta mauris vel suscipit.

Pellentesque sollicitudin ullamcorper elit id hendrerit. Curabitur accumsan cursus felis quis egestas. Quisque ante sem, auctor posuere placerat ac, blandit at erat. Aenean feugiat semper enim non finibus. Nam ornare egestas tortor, eget blandit felis auctor in. Curabitur ligula leo, facilisis sed nulla nec, ornare efficitur ligula. Donec a sagittis enim, rutrum gravida lacus. Donec imperdiet, nisl nec blandit tempor, elit risus efficitur felis, non finibus urna nisl a mauris. Praesent tempus velit et aliquet vulputate.

Donec commodo volutpat tincidunt. Suspendisse non tempus dui. Aliquam orci arcu, venenatis vel eros vel, maximus tempor ligula. Donec eu tortor nisl. Ut congue, nunc id euismod volutpat, justo neque suscipit quam, ultricies fermentum velit tortor sit amet tellus. Fusce convallis magna sagittis tellus semper, a laoreet justo fermentum. Maecenas porttitor mi turpis, sed porta risus fringilla sed. Nulla ex lacus, condimentum eget sapien sed, pellentesque vehicula lectus. Vivamus vitae orci pellentesque, laoreet mauris et, scelerisque odio. Ut vel ipsum metus. Vivamus rutrum, justo venenatis hendrerit tristique, nulla ex placerat justo, quis eleifend ante nunc eget orci.


The file you actually wanted said 
