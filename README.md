# CTF Blog

## 2月24日 更新

### 机试试题 Part 3(约4小时)

#### Huffman编码

Huffman编码根据字符出现的次数来构造平均长度最短的码字，是二叉树的一种应用

压缩过程（以ABCDEABCDABCABA为例）：

第一步，统计字符及其出现次数，并计算出出现概率

字符|A|B|C|D|E
:-:|:-:|:-:|:-:|:-:|:-:
出现次数|5|4|3|2|1
出现频率|0.33|0.27|0.2|0.13|0.07

取概率最低的D、E为二叉树最高层的叶子，分别设为0、1，D+E的概率为0.2，加入到表格中，取代原来的D和E，并重新排序

字符|A|B|C|D+E
:-:|:-:|:-:|:-:|:-:
出现频率|0.33|0.27|0.2|0.2

字符|A|B|C|D|E
:-:|:-:|:-:|:-:|:-:|:-:
当前编码||||0|1

重复上述方法，取概率最低的C和D+E为次高层叶子，分别设为0、1，C+D+E的概率为0.4，加入到表格中，取代原来的C和D+E，并重新排序

字符|C+D+E|A|B
:-:|:-:|:-:|:-:
出现频率|0.4|0.33|0.27

字符|A|B|C|D|E
:-:|:-:|:-:|:-:|:-:|:-:
当前编码|||0|10|11

重复上述方法，取A、B为次高层叶子，分别设为0、1，A+B的概率为0.6，加入到表格中

字符|A+B|C+D+E
:-:|:-:|:-:
出现频率|0.6|0.4

字符|A|B|C|D|E
:-:|:-:|:-:|:-:|:-:|:-:
当前编码|0|1|0|10|11

最后，将剩余的两个结点合并，设高概率的A+B为0，低概率的C+D+E为1，最终编码

字符|A|B|C|D|E
:-:|:-:|:-:|:-:|:-:|:-:
当前编码|00|01|10|110|111

将字符串转换为Huffman编码：

000110110111000110110000110000100

#### 保险箱类

题目要求：

建立一个用数字作为密码，存放一个字符串的保险箱类，它具有以下成员函数：

1）一个构造函数，接受一个数字作为初始密码

2）另一个构造函数，没有指定初始密码，此时初始密码默认为0，不允许使用默认参数

3）一个开箱门函数，给定一个密码，如果密码正确，则保险箱开箱，否则保持状态不变

4）一个锁箱门函数，没有参数，将保险箱锁定

5）一个更新内容函数，在开箱的情况下，更新保险箱内存放的字符串

6）一个取出内容函数，在开箱的情况下，在屏幕上输出存放的字符串

7）一个更改密码函数，在开箱的情况下，更新保险箱的密码

根据题目要求，建立类的框架：

```cpp
class Safe {
  private:
    int password;
    string str;
    bool is_open;

  public:
    Safe(string str);
    Safe(int password, string str);
    bool Open(int password);
    void Close();
    bool Update(string str);
    void Show();
    bool ChangePassword(int password);
};
```

构造函数

如果题目不要求不允许使用默认参数，构造函数可以写成
```cpp
Safe(int password = 0, string str) {
    this->password = password;
    this->str = str;
    this->is_open = false;
}
```

根据题意，构造函数应当重载
```cpp
Safe(string str) : password(0), str(str), is_open(false) {}
Safe(int password, string str) : password(password), str(str), is_open(false) {}
```

开门函数，将实参密码与对象的密码进行比较，相同则打开，不同则关上
```cpp
bool Open(int password) {
    if (password == this->password)
        is_open = true;
    else
        is_open = false;
    return is_open;
}
```

关门函数相对简单，无论保险箱是否开启，将其关闭即可。可以将其设为内联函数

```cpp
inline void Close() {
    is_open = false;
}
```

更新内容与修改密码相似
```cpp
bool Update(string str) {
    if (is_open)
        this->str = str;
    return is_open;
}

bool ChangePassword(int password) {
    if (is_open)
        this->password = password;
    return is_open;
}
```

取出内容
```cpp
void Show() {
    if (is_open)
        cout << str << endl;
    else
        cout << "Safe Closed.\n";
}
```

#### 输出从2开始的前500个质数

题目的关键在于质数的判断，判断从2到sqrt(n)即可，这样可以减少运算次数，提高程序性能

```cpp
bool is_prime(int n) {
    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}
```

#### 顺序线性表

题目要求：

N个人围成一圈，1，2，3循环报数，报到3的人退出

并将退出的序号一次存到数组p中，包括最后一个人的序号

到最后剩余一人，输出最后留下的是第几号（最初的以1起始）及退出的顺序

如N=6，输出1，3 6 4 2 5 1

N=10，输出4， 3 6 9 2 7 8 5 10 4

函数int fun(int n, int *p);实现上述功能，返回N个人中最后余的1人的起始序号，并将退出的序号顺序写入p指向的数组中

此题是顺序线性表的应用，简易的顺序线性表的实现
```cpp
class Sequence {
    private:
        int *p;
        int length;
        int size;
    public:
        Sequence(int size) {
            this->size = size > 0 ? size : 10;
            p = new int[size];
            length = 0;
        }

        bool Insert(int index, int data) {
            if(index < 0 || index > length)
                return false;
            for(int i = length; i > index; --i)
                p[i] = p[i - 1];
            p[index] = data;
            length++;
            return true;
        }

        bool Delete(int index) {
            if(index < 0 || index >= length)
                return false;
            for(int i = index; i < length; ++i)
                p[i] = p[i + 1];
            return true;
        }

        bool GetData(int index, int &data) {
            if(index < 0 || index >= length)
                return false;
            data = p[index];
            return true;
        }
};
```

根据题目要求，可以每次取出第3、6、9...(int)(length/3)个数，一次存到p中，直到length==1

## 2月23日 更新

### Base64 编码解码(约30分)

Base64是网络上最常见的用于传输8Bit字节码的编码方式之一，Base64就是一种基于64个可打印字符来表示二进制数据的方法。定义Base64的RFC文档同样定义了MIME的详细规范

MISC Email题目中WireShark捕获到了以Base64为编码的邮件附件

Base64编码是从二进制到字符的过程，可用于在HTTP环境下传递较长的标识信息，采用Base64编码具有不可读性，需要解码后才能阅读

简单来说，Base64编码就是将3个字节的信息拆分为4个6位，最高两位补0，形成4个字节的信息

如：
```
        abc
ASCII:  97 98 99
Bin:    01100001 01100010 01100011
分组：   011000 010110 001001 100011
补0：    00011000 00010110 00001001 00100011
Oct:    30 26 11 43
查表：   e a L r
```

Java、Python、Go等编程语言都有对Base64编码的实现，C++实现Base64涉及位运算符`>>`和`<<`

### 机试试题 Part 2(约4小时)

#### 行程编码

行程编码是数据压缩的一种编码方式

其基本原理是：用一个符号值和串长代替具有相同值的连续符号

如：

输入：AAAADDEEEEEEGGFFFFFFF

输出：A4,D2,E6,G2,F7

编写程序实现上述功能，输入为连续字母，输出按上述格式

1.字母计数

可以申请一个长为128的int数组，数组元素下标为字母的ASCII值

```c
int value[128] = {0};
for (...) {
    value[s[i] - '\0']++;
}
```

2.字符串去重

从题目给出的输入输出样例中可以看到，输出时不是按照字母的顺序输出的，需要对源字符串进行去重操作，按照去重后的字符串进行输出。

STL Vector的去重：
```c++
#include <algorithm>
#include <vector>
using namespace std;

vector<char> key;
vector<char>::iterator it;

it = unique(key.begin(), key.end());
key.erase(it, key.end());
```

#### 字符串匹配定位

题目要求：

编写函数int locStr(char* str1, char* str2)实现字符串匹配的定位功能，若字符串str1中含有字符串str2，则返回字符串str2在字符串str1中的位置，否则返回-1

题目可以使用二层for循环实现，时间复杂度为O(mn)，m、n分别为两个字符串的长度

KMP算法是一种改进的字符串匹配算法，KMP算法的关键是利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的。具体实现就是实现一个next()函数，函数本身包含了模式串的局部匹配信息。时间复杂度O(m+n)。

在KMP算法中，对于每一个模式串我们会事先计算出模式串的内部匹配信息，在匹配失败时最大的移动模式串，以减少匹配次数。

右移的距离在KMP算法中是如此计算的：在已经匹配的模式串子串中，找出最长的相同的前缀和后缀，然后移动使它们重叠。

如果每次计算右移的距离，会耗费很长的时间，可以使用辅助数组来存放一些信息供后面使用

#### MD5计算

1.MD5简介

MD5，消息摘要算法第五版，为计算机安全领域广泛使用的一种散列函数，能够将数据运算为固定长度的一个值。具有压缩性、容易计算、抗修改性、强抗碰撞的特点

MD5可以用于信息一致性验证，比如网上下载文件时可以提供一个文件的MD5值，用于验证下载的文件是否正确完整。

MD5也可用于数字签名，以防止被篡改

现如今MD5算法已不安全，被更先进的SHA1等算法替代

2.MD5算法原理

MD5以512位分组来处理输入的信息，且每一分组又被划分为16个32位子分组，经过了一系列的处理后，算法的输出由四个32位分组组成，将这四个32位分组级联后将生成一个128位散列值。

第一步：填充

对信息进行填充，使其位长对512求余的结果等于448，并且填充必须进行，即使其位长对512求余的结果等于448。因此，信息的位长（Bits Length）将被扩展至N*512+448，N为一个非负整数，N可以是零。

填充方法：在信息的后面填充一个1和无数个0，直到满足上面的条件时才停止用0对信息的填充。在这个结果后面附加一个以64位二进制表示的填充前信息长度（单位为Bit），如果二进制表示的填充前信息长度超过64位，则取低64位。

经过这两步的处理，信息的位长=N
512+448+64=(N+1)
512，即长度恰好是512的整数倍。这样做的原因是为满足后面处理中对信息长度的要求。

第二步：初始化变量

初始的128位值为初试链接变量，这些参数用于第一轮的运算，以大端字节序来表示，他们分别为： A=0x01234567，B=0x89ABCDEF，C=0xFEDCBA98，D=0x76543210。

（大端字节序：高字节存于内存低地址，低字节存于内存高地址）

第三步：处理分组数据

第一分组需要将上面四个链接变量复制到另外四个变量中：A到a，B到b，C到c，D到d。从第二分组开始的变量为上一分组的运算结果，即A = a， B = b， C = c， D = d

主循环有四轮，每轮循环都很相似。第一轮进行16次操作。每次操作对a、b、c和d中的其中三个作一次非线性函数运算，然后将所得结果加上第四个变量、文本的一个子分组和一个常数。再将所得结果向左环移一个不定的数，并加上a、b、c或d中之一。最后用该结果取代a、b、c或d中之一。

每轮使用的非线性函数（每轮一个）

F(X, Y, Z) = ( X & Y) | ( (~X) & Z)

G(X, Y, Z) = ( X & Z) | ( Y & (~Z))

H(X, Y, Z) = X ^ Y ^ Z

I(X, Y, Z) = Y ^ ( X | (~Z))

假设Mj表示消息的第j个子分组（从0到15），常数ti是2<sup>32</sup>*abs(sin(i)）的整数部分，i 取值从1到64，单位是弧度。

现定义：

FF(a ,b ,c ,d ,Mj ,s ,ti) 操作为 a = b + ((a + F(b,c,d) + Mj + ti) << s)

GG(a ,b ,c ,d ,Mj ,s ,ti) 操作为 a = b + ((a + G(b,c,d) + Mj + ti) << s)

HH(a ,b ,c ,d ,Mj ,s ,ti) 操作为 a = b + ((a + H(b,c,d) + Mj + ti) << s)

II(a ,b ,c ,d ,Mj ,s ,ti) 操作为 a = b + ((a + I(b,c,d) + Mj + ti) << s)

则四轮64步操作为：

第一轮

FF(a ,b ,c ,d ,M0 ,7 ,0xd76aa478)；FF(d ,a ,b ,c ,M1 ,12 ,0xe8c7b756)；FF(c ,d ,a ,b ,M2 ,17 ,0x242070db)；FF(b ,c ,d ,a ,M3 ,22 ,0xc1bdceee)

FF(a ,b ,c ,d ,M4 ,7 ,0xf57c0faf)；FF(d ,a ,b ,c ,M5 ,12 ,0x4787c62a)；FF(c ,d ,a ,b ,M6 ,17 ,0xa8304613)；FF(b ,c ,d ,a ,M7 ,22 ,0xfd469501)

FF(a ,b ,c ,d ,M8 ,7 ,0x698098d8)；FF(d ,a ,b ,c ,M9 ,12 ,0x8b44f7af)；FF(c ,d ,a ,b ,M10 ,17 ,0xffff5bb1)；FF(b ,c ,d ,a ,M11 ,22 ,0x895cd7be)

FF(a ,b ,c ,d ,M12 ,7 ,0x6b901122)；FF(d ,a ,b ,c ,M13 ,12 ,0xfd987193)；FF(c ,d ,a ,b ,M14 ,17 ,0xa679438e)；FF(b ,c ,d ,a ,M15 ,22 ,0x49b40821)

第二轮

GG(a ,b ,c ,d ,M1 ,5 ,0xf61e2562)；GG(d ,a ,b ,c ,M6 ,9 ,0xc040b340)；GG(c ,d ,a ,b ,M11 ,14 ,0x265e5a51)；GG(b ,c ,d ,a ,M0 ,20 ,0xe9b6c7aa)

GG(a ,b ,c ,d ,M5 ,5 ,0xd62f105d)；GG(d ,a ,b ,c ,M10 ,9 ,0x02441453)；GG(c ,d ,a ,b ,M15 ,14 ,0xd8a1e681)；GG(b ,c ,d ,a ,M4 ,20 ,0xe7d3fbc8)

GG(a ,b ,c ,d ,M9 ,5 ,0x21e1cde6)；GG(d ,a ,b ,c ,M14 ,9 ,0xc33707d6)；GG(c ,d ,a ,b ,M3 ,14 ,0xf4d50d87)；GG(b ,c ,d ,a ,M8 ,20 ,0x455a14ed)

GG(a ,b ,c ,d ,M13 ,5 ,0xa9e3e905)；GG(d ,a ,b ,c ,M2 ,9 ,0xfcefa3f8)；GG(c ,d ,a ,b ,M7 ,14 ,0x676f02d9)；GG(b ,c ,d ,a ,M12 ,20 ,0x8d2a4c8a)

第三轮

HH(a ,b ,c ,d ,M5 ,4 ,0xfffa3942)；HH(d ,a ,b ,c ,M8 ,11 ,0x8771f681)；HH(c ,d ,a ,b ,M11 ,16 ,0x6d9d6122)；HH(b ,c ,d ,a ,M14 ,23 ,0xfde5380c)

HH(a ,b ,c ,d ,M1 ,4 ,0xa4beea44)；HH(d ,a ,b ,c ,M4 ,11 ,0x4bdecfa9)；HH(c ,d ,a ,b ,M7 ,16 ,0xf6bb4b60)；HH(b ,c ,d ,a ,M10 ,23 ,0xbebfbc70)

HH(a ,b ,c ,d ,M13 ,4 ,0x289b7ec6)；HH(d ,a ,b ,c ,M0 ,11 ,0xeaa127fa)；HH(c ,d ,a ,b ,M3 ,16 ,0xd4ef3085)；HH(b ,c ,d ,a ,M6 ,23 ,0x04881d05)

HH(a ,b ,c ,d ,M9 ,4 ,0xd9d4d039)；HH(d ,a ,b ,c ,M12 ,11 ,0xe6db99e5)；HH(c ,d ,a ,b ,M15 ,16 ,0x1fa27cf8)；HH(b ,c ,d ,a ,M2 ,23 ,0xc4ac5665)

第四轮

II(a ,b ,c ,d ,M0 ,6 ,0xf4292244)；II(d ,a ,b ,c ,M7 ,10 ,0x432aff97)；II(c ,d ,a ,b ,M14 ,15 ,0xab9423a7)；II(b ,c ,d ,a ,M5 ,21 ,0xfc93a039)

II(a ,b ,c ,d ,M12 ,6 ,0x655b59c3)；II(d ,a ,b ,c ,M3 ,10 ,0x8f0ccc92)；II(c ,d ,a ,b ,M10 ,15 ,0xffeff47d)；II(b ,c ,d ,a ,M1 ,21 ,0x85845dd1)

II(a ,b ,c ,d ,M8 ,6 ,0x6fa87e4f)；II(d ,a ,b ,c ,M15 ,10 ,0xfe2ce6e0)；II(c ,d ,a ,b ,M6 ,15 ,0xa3014314)；II(b ,c ,d ,a ,M13 ,21 ,0x4e0811a1)

II(a ,b ,c ,d ,M4 ,6 ,0xf7537e82)；II(d ,a ,b ,c ,M11 ,10 ,0xbd3af235)；II(c ,d ,a ,b ,M2 ,15 ,0x2ad7d2bb)；II(b ,c ,d ,a ,M9 ,21 ,0xeb86d391)

所有这些完成之后，将a、b、c、d分别在原来基础上再加上A、B、C、D。即a = a + A，b = b + B，c = c + C，d = d + D

然后用下一分组数据继续运行以上算法。

第四步：输出

最后输出的时a、b、c、d的级联

## 2月22日 更新

### Python Requests Part 5 (约1小时)

#### 重定向与请求历史

默认情况下，除了HEAD请求，Requests会自动处理所有重定向。可以使用相应对象的history方法来追踪重定向

```python
r = requests.get('http://github.com/')
print(r.url)            # 'https://github.com/'
print(r.status_code)    # 200
print(r.history)        # [<Response [301]>]
```

可以看到，发生了重定向

使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE可以通过allow_redirects参数禁用重定向处理

```python
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)    # 301
print(r.history)        # []
```

可以看到，此时重定向被禁用

使用了 HEAD，你也可以启用重定向

```python
r = requests.head('http://github.com/')
print(r.url)    # 'https://github.com/'
print(r.history)        # [<Response [301]>]
```

#### HTTP 常用状态码

HTTP状态码用来表示网页服务器HTTP响应状态。遇到的最多的就是404 NOT FOUND。

1XX：信息，临时响应

2XX：成功，表示请求已经被服务器接收、理解并接受

3XX：重定向，代表客户端需要采取进一步的操作才能完成请求

4XX：客户端错误

5XX：服务器错误

#### 超时

可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应：
```python
>>> requests.get('http://github.com', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```
timeout 仅对连接过程有效，与响应体的下载无关。 timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）


### 机试试题 Part 1 (约3小时)

#### 素数

题目要求：统计素数的个数，求出2到m之间（含m，m<=1000）所有素数并放在数组a中。

输入：正整数m，要求支持命令行输入参数

输出：从小到大的所有素数及个数（素数输出的时候用%4d来控制）

（如：your-program 10，则输出：2 3 5 7	4）

分析：

1.题目输入格式类似于常用的Shell命令，如：
```shell
apt upgrade -y
```

可以使用argc和argv实现
```c
int main(int argc, char **argv) {
    // ...
    return 0;
}
```

argc为参数个数，argv[]为参数内容。其中argv[0]为可执行程序的路径，argv[1]到argv[argc - 1]为每一个参数

2.字符串与数字之间的转换

题目输入的信息为字符串，程序中需要将其转换为int类型的数字

```c
#include <string.h>

int i, m = 0;
for (i = 0; i < strlen(argv[1]); i++) {
    m *= 10;
    m += argv[1][i] - '0';
}
```

3.获取2到m之间的所有素数

可以定义一个长度为1010的bool型数组，数组中元素为true表示该下标为合数，false为素数

然后从头扫描，遇到一个为false的元素，将数组中下标为该元素下标的整数倍设为false

这样可以将所有合数全部排除

#### 数组最小元素

题目要求：编写一个函数void fun(int *s, int t, int *result),用来求出数组的最小元素在数组中的下标，并存放在result所指的存储单元中。

例如，输入如下整数：

564，165，567，121，948，324，329，454，5345，783，434，124，561，985，118

则输出结果为：14，118

题目给出了函数的定义
```c
void fun (int *s, int t, int *result);
```

此题考查数组、指针的操作和参数传递

1.数组的表示

一维数组的表示形式
```c
int a[];
int *a;
```

题目中的`int *s`表示要操作的数组，`int t`表示数组的长度

2.指针的操作

简单来说，指针就是地址，通过指针可以找到变量

```c
int *p; // 指针定义
int a;
p = &a; // p中存放a的地址
*p = 1; // a = 1
```

3.函数参数传递

参数传递总的来说有两种形式：传值、传地址。如果需要修改实参的内容，需要传地址，如果只是借用实参的值，传值即可。

传地址又有两种形式：传指针、传引用。指针和引用都是存放的变量的地址，二者的区别：
```c++
void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

void swap(int &a, int &b) {
    int t = a;
    a = b;
    b = t;
}
```

4.C++ STL 获得数组最小元素
```c++
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    int a[] = {1, 2, 3}; 
    int *m = min_element(a, a + 3);
    cout << *m << endl;
    return 0;
}
```

#### Class IPv4

题目要求：写一个IPv4的地址如“202.112.17.33”，“192.168.1.1”等，设计一个IPv4地址分析类，功能包括

1)构造函数：参数包含IPv4地址字符串

2)判断是否是合法主机IP地址的接口

3)判断IP地址是A类、B类、C类或者其他的接口

1.类的构造函数

构造函数的函数名与类名相同，没有返回值，可以没有形参，可以重载。

```c++
class IPv4 {
    public:
        IPv4(string ip);
        IPv4(const IPv4 &ip);   // 拷贝构造函数
}
```

2.字符串分割

这个题目对字符串的分割要求相对简单，针对关键字符`.`进行分割即可。使用到STL String中的`find()`和`substr()`函数

find函数用来找到第一个关键字符在字符串中的位置，substr函数用来获得字符串的子串，二者配合使用可以分割IP地址的每一部分

3.IPv4的分类

A：0.0.0.0~127.255.255.255

B：128.0.0.0~191.255.255.255

C：192.0.0.0~223.255.255.255

D：224.0.0.0~239.255.255.255

E：240.0.0.0~247.255.255.255

#### Class FTP

题目要求：访问一个FTP服务器的完整链接字符串为

ftp://test:12345@192.168.1.1:2121

设计一个字符串分析类，功能包括

1）构造函数：参数包含ftp链接字符串

2）获取ftp服务器IP的接口

3）获取登陆ftp服务器的用户名及密码的接口

4）获取ftp服务器的服务端口

编写主程序测试类的有效性

这个题目相比Class IPv4难度大一些，对字符串的分割不只是依靠单一的关键字符，但原理相通，使用`find()`和`substr()`函数即可达到题目要求


## 2月21日 更新

### Python Requests Part 4

#### 会话对象

会话对象能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持cookie。如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。

我在解答Web Calculator题目时先获取了一个Cookie，再用这个Cookie将计算结果发出。题目要求1.5秒解答，如果这个时间再短一点，原来的方法可能会超时。使用会话对象能够减小耗时。

会话对象具有主要的Requests API的所有方法。

```python
s = requests.Session()
# or
with requests.Session() as s:
    pass
```
第二种方法可以确保with区块推出后会话能被关闭，即使发生了异常也能够关闭


### 排序算法

#### 直接插入排序（时间：O(n)~O(n<sup>2</sup>)；空间：O(1)）

将序列第一个元素视为有序序列，从第二个元素开始，将其放入前面有序序列中合适的位置，至此前两个元素有序。以此类推，直到所有元素有序

```c
void InsertSort(int a[], int n) {
    int i, j, t;
    for (i = 1; i < n; i++) {
        if (a[i] < a[i - 1]) {
            t = a[i];
            a[i] = a[i - 1];
            for (j = i - 1; t < a[j] && j >= 0; j--)
                a[j + 1] = a[j];
            a[j + 1] = t;
        }
    }
}

/* 示例
(49) 38  65  97  76  13  27  49
(38  49) 65  ...
(38  49  65) 97  ...
(38  49  65  97) 76  ...
(38  49  65  76  97) 13  ...
(13  38  49  65  76  97) 27  ...
(13  27  38  49  65  76  97) 49
(13  27  38  49  49  65  76  97)
*/
```

#### 选择排序（时间：O(n<sup>2</sup>)；空间：O(1)）

从序列中找到最大元素，移到最后；找到次大元素，移到n-1位置；以此类推，直至有序

```c++
void SelectionSort(int a[], int n) {
    int size, m;
    for (size = n; size > 1; size--) {
        m = Max(a, size);
        swap(a[m], a[size - 1]);
    }    
}

// STL
void SelectionSort(int a[], int n) {
    int *m;
    while(n--) {
        m = max_element(a, a + n + 1);
        swap(a[m - a], a[n]);
    }
}
```

#### 冒泡排序（时间：O(n)~O(n<sup>2</sup>)；空间：O(1)）

从第二个元素开始，与前面的元素进行比较，大的元素交换到后面；每一轮都会将最大的元素移到最后。

```c
// 冒泡排序
void BubbleSort(int a[], int n) {
    int i, j;
    for (i = n - 1; i > 0; i--)
        for (j = 0; j < i; j++)
            if (a[j] > a[j + 1])
                swap(a[j], a[j + 1]);
}
```

#### 箱子排序（仅用于链表）（时间：O(n+r)；空间：O(n)）

具有相同分数的结点，放在同一个箱子中；把箱子按顺序连起来，成为一个有序链表
```c++
/* 举例
(A,2)->(B,4)->(C,5)->(D,4)->(E,3)
->(F,0)->(G,4)->(H,3)->(I,4)->(J,3)
        I
      J G
      H D
F   A E B C
0 1 2 3 4 5
排序后：
(F,0)->(A,2)->(E,3)->(H,3)->(J,3)
->(B,4)->(D,4)->(G,4)->(I,4)->(C,5)
*/
void BinSort(Chain<Node> &X, int range) {
    int len = X.length();
    Node x;
    Chain<Node> *bin = new Chain<Node>[range + 1];
    // 分配
    for (i = 1; i < len; i++) {
        X.Delete(1, x);
        bin[x.score].Insert(0, x);
    }
    // 收集
    for (i = range; i >= 0; i--) {
        while(!bin[i].IsEmpty()) {
            bin[j].Delete(1, x);
            X.Insert(0, x);
        }
    }
    delete[] bin;
}
```

#### 基数排序（箱子排序扩展；时间：O(d(n+rd)；空间：O(rd)）

把数按照某种基数分解为数字，对数字进行排序
举例：
278->109->063->930->589->184->505->269->008->083
range = 10

第一趟：对末位排序
```
                            269
        083             008 589 
930     063 184 505     278 109
 0  1 2  3   4   5  6 7  8   9
930->063->083->184->505->278->008->109->589->269
```

第二趟：对中间位排序
```
109                     589
008             269     148
505     930     063 278 083
 0  1 2  3  4 5  6   7   8  9
505->008->109->930->063->269->278->083->148->589
```
第三趟：对最高位排序
```
083
063 184 278     589
008 109 269     505       930
 0   1   2  3 4  5  6 7 8  9
008->063->083->109->184->269->278->505->589->930
```
已经有序

#### 堆排序（时间：O(nlogn)；空间：O(1)）

堆定义（数组存放）

小顶堆：k[i] <= k[2i], k[i] <= k[2i + 1]

大顶堆：k[i] >= k[2i], k[i] >= k[2i + 1]

特点：输出堆顶最大（小）值后，剩余n - 1个元素的序列又成一个堆

#### 归并排序（分治思想；时间：O(nlogn)；空间：O(n)）

举例：

 49 39   65 97   76 13   27

(38 49) (65 97) (76 13) (27)

 (38 49 65 97)   (13 27 76)

   (13 27 38 49 65 76 97)

```c
void MergeSort(int a[], int n) {
    int *b = new int[n];
    s = 1;
    while(s < n) {
        MergePass(a, b, s, n);
        s += s;
        MergePass(b, a, s, n);
        s += s;
    }
}

void MergePass(int x[], int y[], int s, int n) {
    int i = 0;
    while(i <= n - 2s) {
        Merge(x, y, i, i + s - 1, i + 2s - 1);
        i = i + 2s;
    }
}
```

#### 快速排序（冒泡改进，分治思想；时间：O(nlogn)~O(n<sup>2</sup>)；空间：O(logn)）

将第一个元素设为枢轴，从左边找一个大于枢轴的元素，从右边找一个小于枢轴的元素，进行交换；最终小于枢轴的元素都在枢轴左边，大于枢轴的元素都在枢轴右边；对分开的两部分再次使用快速排序算法排序。

```c
int Partition (int a[], int p, int r) {
    int i = p, j = r + 1;
    int x = a[p];
    while (true) {
        while(a[++i] < x && i < r);
        while(a[--j] > x && j > p);
        if (i >= j)
            break;
        swap(a[i], a[j]);
    }
    a[p] = a[j];
    a[j] = x;
    return j;
}

// 快速排序算法
void QuickSort(int a[], int p, int r) {
    if (p < r) {
        int q = Partition (a, p, r);
        QuickSort(a, p, q - 1);
        QuickSort(a, q + 1, r);
    }
}
```


### 《保密概论》第二章 保密法规

#### 一、保密法律、法规、规章

1.我国保密法律两类：根本法（宪法）、有关法律（专门法律+基本法律中的有关规定）

2.保密法规：行政法规（国务院制定）、地方性法规（地方人大制定）

3.保密规章：国务院部门规章、地方政府规章

总的来说，都由一个根本性文件和配套的基本性文件组成

4.三者关系：共同构成我国保密法律体系的框架，是我国保密法律体系的重要组成部分；法律是其他二者制定的依据，法规是法律体系的主要表现形式；地位和效力：法律>法规>规章

#### 二、保密法及其实施办法

1.立法背景

1951.6：政务院颁布《保守国家机密暂行条例》，我国政府制定的第一个全国性的保密工作行政法规，对加强我国保密工作的管理起了重大作用。

1988.9.5：《中华人民共和国保守国家秘密法》

2010.4.29：《中华人民共和国保守国家秘密法》修订草案

2.《实施办法》是《保密法》的具体化，它使《保密法》的若干内容更具备可操作性。


## 2月20日 更新

### Python Requests Part 3

#### Cookie

Cookie，有时也用其复数形式 Cookies，指某些网站为了辨别用户身份、进行 session 跟踪而储存在用户本地终端上的数据（通常经过加密）

如果某个响应中包含一些 cookie，可以快速访问它们：

```python
url = 'xxx.org'
r = requests.get(url)
print(r.cookies)
```

要想发送 cookies 到服务器，可以使用 cookies 参数：

```python
url = 'xxx.org'
# 自定义cookies
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
```

Web Calculator题目应该在发送答案的时候带上Cookies

```python
import requests

r = requests.get(url)
cookies = r.cookies
# 计算结果
r = requests.get(URL, params={'answer': ans}, cookies=c)
print(r.text)
```
在输出的信息中找到`flag{yes_you_are_calculat0r}`

理论上使用同样的方法可以解出Web RapidTyping题目。

在得到题目网页源码时发现网页中的图片使用base64编码的，将其解码后得到xml格式的svg图像，取出所有有效字符，组成字符串，发送答案时提示错误，原因在于没有根据字符的位置安排字符在答案中的位置


### 《保密概论》第一章 保密基础知识

#### 保密工作概要

1.保密：在一定时间和范围内加以保护和隐蔽

2.保密工作：与政党、国家的安全和利益密切相关的保守国家秘密的一切活动

3.保密工作的特征：政治性（法律保护）、群众性、防御性（防泄漏）、专业性（各行各业、各项工作都有）

4.指导思想：中特基本路线 + 《保守国家秘密法》

5.指导方针：积极防范、突出重点、依法管理

6.基本原则：

第一，党委统一领导保密工作的原则；
 
第二，保密工作归口管理，分级负责的原则；
 
第三，保密工作属地管理与系统管理相结合的原则；
 
第四，依法行政、依法管理保密工作的原则；
 
第五，保密管理与业务管理结合的原则；
 
第六，管理与服务相结合的原则。

#### 国家秘密

1.国家秘密：关系国家安全和利益，依照法定程序确定，在一定时间内只限一定范围的人员知悉的事项

2.国家秘密特征：关系国家安全和利益（关键性要素、本质特征、区分标准）、依照法定程序确定（程序特征）、在一定时间内只限一定范围的人员知悉（时空特征）

3.国家秘密的特征：绝密、机密、秘密

4.确定权限：

绝密级：省以上；县以下：不能确定秘密等级；地级市：机密级、秘密级

5.定密责任人制度

6.保密期限：绝密<=30年，机密<=20年，秘密<=10年；提前解密或延长保密期限；确定后做出标志

#### 商业秘密、工作秘密

1.商业秘密三要素：(1)技术信息、经营信息；(2)能为权利人带来经济利益；(3)采取了保密措施；泄露后根据情节给予民事或刑事处罚

2.工作秘密：“内部”、“内部文件”、“内部资料”、“内部刊物”；泄露后收到政纪处分



## 2月19日 更新

### 将Kali Linux安装到Bash on Windows记录

后面的题目只在Windows环境下不可完成，将Win10上的Linux子系统启动，并装上Kali Linux

参考内容[WSL-Distribution-Switcher](https://github.com/RoliSoft/WSL-Distribution-Switcher)

1.启用Linux子系统功能

2.下载WSL-Distribution-Switcher

```shell
git clone git@github.com:RoliSoft/WSL-Distribution-Switcher.git
```

3.获取镜像文件

```shell
python get-prebuilt.py kalilinux/kali-linux-docker
```

4.安装

```shell
py install.py rootfs_kalilinux_kali-linux-docker_latest.tar.gz
```

5.配置
```shell
lxrun /setdefaultuser xxx
bash
export LANG=C && cd
```

6.系统更新

```shell
sudo apt update && sudo apt upgrade
```

### Python Requests Part 2

根据题目Web Calculator中提供的Requests官方文档，学习了如下内容，并以Web Calculator题目做练习

（摘自[Request 2.18.1文档](http://cn.python-requests.org/zh_CN/latest/)）

#### 1.发送请求
```python
import requests

r = requests.get(url)   
r = requests.post(url)
r = requests.put(url)
r = requests.delete(url)
r = requests.head(url)
r = requests.options(url)
```

```python
r = requests.get(url='http://121.42.176.204:23331/calculator/')
print(r.text)
```

输出网页HTML代码
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Calculator</title>
        <style type="text/css">
                .line_input{
                        border-width: 1px;
                        border-bottom: solid;
                        border-top: none;
                        border-left: none;
                        border-right: none;
                        border-width: 1px;
                        text-align: center;
                        outline: none;
                        margin: 0 1em;
                }
        </style>
    </head>
    <body>
        <center>
            <h1>Yet Another Calculator</h1>
            <p>Let's play a game. Please work on this math problem, and make it in 1.5 seconds.</p>
            <form action="" method="GET"><span id="exp">5160526 + 81114644008 - 158998 = </span>
            <input name="answer" type="text" autofocus class="line_input" /><input type="submit" /></form>
        </center>
    </body>
</html>
```

可以得到要计算的式子为：`5160526 + 81114644008 - 158998`，计算结果为`35701914696`

要在一个文本输入框中输入答案

#### 2.传递URL参数

手工构建的URL，例如，xxx.org/get?key=val，Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数。

```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://xxx.org/get", params=payload)
print(r.url)
```

```
http://httpbin.org/get?key2=value2&key1=value1
```

你还可以将一个列表作为值传入：
```python
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
```

```
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

尝试使用`answer=35701914696`作为payload向题目中传递参数

```python
payload = {'answer': '35701914696'}
r = requests.get('http://121.42.176.204:23331/calculator/', params=payload)
print(r.url)
print(r.text)
```

输出内容包含
```
Expression has not been generated.
```

此法无效

尝试使用POST请求
```python
payload = {'answer': '35701914696'}
r = requests.post('http://121.42.176.204:23331/calculator/', data=payload)
print(r.text)
```

输出内容为新的HTML文件源码，新的表达式变为：`7553124 + 67537142361 - 198070 = `，计算结果为：`28616745985`

尝试使用相同的方法发送POST请求，得到新的表达式：`9015527 + 95731679168 - 101603 =`，计算结果为：`75797707012`

再次使用相同的方法发送POST请求，依然得到新的表达式。也许此方法会如此循环下去，不能得到flag

在不计算表达式的情况下点击了以下按钮，网页跳转为
```url
http://121.42.176.204:23331/calculator/?answer=
```

上面使用POST请求的方法使用的URL没有后面的参数。这种方法有误。


### Misc Birthday

根据题目提示，编写了生成密码字典和暴力破解密码的Python脚本。解得压缩文件密码为`19950608`，解压缩后得到flag



## 2月18日 更新

### Misc Email

追踪IAMP数据包，可以看到发送了一个名为`20161008103416509320.7z`的邮件附件，文件以Base64格式编码：

```
N3q8ryccAAQ9AshlwFQFAAAAAAAqAAAAAAAAAOjuWeI83mZQMTuDbrw/ESKoLQCVZl4iDZ8FFWPWaFcXMf...
```

将其解码到文件，打开时提示文件已加密。

除了发送7z附件，还发送了其他的信息

找到一段字符
```
Fl5266q4PzYXSPdmgzrA
```

尝试将其作为压缩包的密码，可以打开压缩包，里面有`20161008103416509320.pdf`文件，打开后未发现所需要的flag

题目暂未解出


### HTML协议定义的8种方法

HTTP/1.1协议中共定义了八种方法（有时也叫“动作”）来表明Request-URI指定的资源的不同操作方式：

OPTIONS 

返回服务器针对特定资源所支持的HTTP请求方法。也可以利用向Web服务器发送'*'的请求来测试服务器的功能性。 

HEAD 

向服务器索要与GET请求相一致的响应，只不过响应体将不会被返回。这一方法可以在不必传输整个响应内容的情况下，就可以获取包含在响应消息头中的元信息。 

GET 

向特定的资源发出请求。注意：GET方法不应当被用于产生“副作用”的操作中。 

POST 

向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。 

PUT 

向指定资源位置上传其最新内容。 

DELETE 

请求服务器删除Request-URI所标识的资源。 

TRACE 

回显服务器收到的请求，主要用于测试或诊断。 

CONNECT 

HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。

### Python Request Part 1

以下内容部分摘自[CSDN博客：Python-第三方库requests详解](http://blog.csdn.net/shanzhizi/article/details/50903748)

```python
import python

r = requests.get(url='http://www.itwhy.org')    # 最基本的GET请求
print(r.status_code)    # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
print(r.url)
print(r.text)   #打印解码后的返回数据
```

其他方法是统一的接口样式
```python
requests.get(‘https://github.com/timeline.json’) #GET请求
requests.post(“http://httpbin.org/post”) #POST请求
requests.put(“http://httpbin.org/put”) #PUT请求
requests.delete(“http://httpbin.org/delete”) #DELETE请求
requests.head(“http://httpbin.org/get”) #HEAD请求
requests.options(“http://httpbin.org/get”) #OPTIONS请求
```

带参数的请求实例：
```python
import requests

requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})    #GET参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例
```

POST发送JSON数据：
```python
import requests
import json
 
r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())
```

### 其他

对lsb.py进行修改，使其成为命令行工具
```shell
py lsb.py <input file> <output file>
```


## 2月17日 更新

### Misc LSB

一开始根据网上有关LSB的介绍自己写了一段Python程序，将所有像素的R值的最低位提出，然后每8位个连在一起组成一个字节，将所有字节输出到新的图片中。得到的图片有二维码，但不清楚，无法被扫描。

原因在于自己写的程序在算法上有问题，后查资料找到知乎专栏的一篇文章。

以下部分内容摘自[知乎专栏：基于图像的 LSB 隐写术科普](https://zhuanlan.zhihu.com/p/32092460)

0x01 什么是隐写术？

维基百科对隐写术的定义：

隐写术是一门关于信息隐藏的技巧与科学，所谓信息隐藏指的是不让除预期的接收者之外的任何人知晓信息的传递事件或者信息的内容。
一般来说，隐写的信息看起来像一些其他的东西，例如一张购物清单，一篇文章，一篇图画或者其他“伪装”（cover）的消息。

换而言之，隐写不同于加密，加密是一段你看不懂的东西，隐写是一段你似乎能看懂的东西，但是实际上不是表面看上去那么简单。

而对应把隐藏的东西提取出来的技术称为隐写分析。

0x02 LSB算法

像素与RGB

计算机保存的图像是以数值保存每一个像素点。

数字图像有很多种，比如二值图像，每个像素点不是 0 ，就是 1 ；再比如灰度图像，每个像素取值从 0 到 255 。

通道：

通道，是数字图像中存储不同类型信息的灰度图像。一个图像最多可以有数十个个通道，常用的 RGB 和 Lab 图像默认有三个通道。（摘自维基百科）

RGB，这里指灰度图像里的以 RGB 模式存储数字图像的模型。其中，R 是 Red 的首字母，G 是 Green 的首字母，B 是 Blue 的首字母，它们分别代表一个通道，在每个通道上，保存一个代表该通道亮度的数字，取值范围从 0 到 255 。

用 Python 和第三方库 PIL(pillow) 读取它的第一个像素值：
```python
form PIL import Image

img = Image.open('a.png')
print(img.getpixel((0, 0)))
```

运行结果
```
(73, 158, 225)
```

Python 返回了一个元组，其中有三个元素，分别对应 RGB 三个通道的亮度值，R 通道的亮度值为 73 ，G 通道亮度值为 158 ，B 通道亮度值为 225 ，三个通道的颜色混合在一起，也就构成了第一个像素点所显示的颜色~

如果把像素的亮度值加一或减一，肉眼根本分辨不出来~那么，窝们就可以利用这个藏一点儿小秘密辣！

对应于把像素加一减一这样的操作，在用二进制表示像素亮度值的情况下，也就是改变这个二进制的最低位，也就是最低有效位 (Least Significant Bit, LSB) 算法。

根据文章中提供的示例代码改写了一个Python程序，对图片文件进行解码，得到`lsb.png`，打开后是一个二维码，扫描得`flag{least_significant_bitttt}`


### Misc Another01Game

根据题目要求，将TXT文件中的0和1组成一个正方形，用Python编程生成图片

首先根据01字符的个数判断为37x37的图像，然后将0视为黑色像素(0, 0, 0)，1视为白色像素(255, 255, 255)，生成二维码图片`01game.png`

扫描得到01字符串
```
110011011011001100001110011111110111111001011000010101011011111100101110011101001111101011110111111100001110001001100001110101111010010111111110001101001010000110110000110010001100111111101
```

将此字符串用ASCII解码得`flag{y0U_KNOW_ab0ut_qRC0d3}`


## 2月16日 更新

### Misc Shell

使用WireShark打开文件

在7号TCP报文的DATA字段发现
```shell
ls -la
```

在9号TCP报文的DATA字段发现
```shell
-rw-rw-r-- 1 user user 28 Feb 5 07:57 flag.txt
```

在15号TCP报文的DATA字段发现
```shell
cat ./flag.txt base64
```

在28号TCP报文的DATA字段发现
```
ZmxhZ3tyZXZlcnNlX3NoZWwxbDFsbGwxbH0KCg==
```

解码得
```
flag{reverse_shel1l1lll1l}
```

### Misc EXIF

题目提示找图片的EXIF信息，通过Python程序找到的信息
```
Image Orientation: Horizontal (normal)
Image XResolution: 72009/1000
Image YResolution: 72009/1000
Image ResolutionUnit: Pixels/Inch
Image Software: Adobe Photoshop CS6 (Windows)
Image DateTime: 2017:02:05 00:39:54
Image ExifOffset: 164
Thumbnail Compression: JPEG (old-style)
Thumbnail XResolution: 72
Thumbnail YResolution: 72
Thumbnail ResolutionUnit: Pixels/Inch
Thumbnail JPEGInterchangeFormat: 302
Thumbnail JPEGInterchangeFormatLength: 5530
EXIF ColorSpace: sRGB
EXIF ExifImageWidth: 451
EXIF ExifImageLength: 272
JPEGThumbnail ......
```

尝试将JPEGThumbnail导出到图片，未获得信息

读取信息不全，使用exiftool读取图片EXIF信息，未找到可用信息

此题未解出


## 2月15日 更新

### Misc SignIn

这个题目是用来介绍提交规则的，将`flag{welcome}`提交即可

### Misc DOCX

docx文件结构
```
_rels\
docProps\
word\
*.xml
```

将file.docx扩展名改为file.zip，用压缩软件打开后发现`Flag.xml`文件，用文本编辑器打开后发现`Flag{k42bP8khgqMZpCON}`

### Misc Forensics1

使用WireShark将pcap文件打开，找出http流量

在从192.168.245.136发往192.168.245.128的长度为454的包中发现如下html文件
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Secret Page</title>
    </head>
    <body>
        <h1>You have got the flag.</h1>
        <img src="./s3cret.png" />
    </body>
</html>
```
然后找到发送s3cret.png的数据包，从192.168.245.136发给192.168.245.128的png文件，将分组字节流导出，得到png图片

打开图片，得到`flag{simple_http_request}`