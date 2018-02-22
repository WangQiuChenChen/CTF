# CTF Blog

## 2月22日 更新

### Python Requests Part 5 (约1小时)

#### 重定向与请求历史

默认情况下，除了HEAD请求，Requests会自动处理所有重定向。可以使用相应对象的history方法来追踪重定向

```python
r = requests.get('http://github.com/')
print(r.url)    # 'https://github.com/'
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