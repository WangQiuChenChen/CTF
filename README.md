# CTP Blog


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
            <form action="" method="GET"><span id="exp">5160526 + 811146 * 44008 - 158998 = </span>
            <input name="answer" type="text" autofocus class="line_input" /><input type="submit" /></form>
        </center>
    </body>
</html>
```

可以得到要计算的式子为：`5160526 + 811146 * 44008 - 158998`，计算结果为`35701914696`

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

输出内容为新的HTML文件源码，新的表达式变为：`7553124 + 675371 * 42361 - 198070 = `，计算结果为：`28616745985`

尝试使用相同的方法发送POST请求，得到新的表达式：`9015527 + 957316 * 79168 - 101603 =`，计算结果为：`75797707012`

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