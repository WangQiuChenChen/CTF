# CTP Writeup


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