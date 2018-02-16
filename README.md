# CTP Writeup

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

<!--
### Misc LSB

LSB也就是最低有效位 (Least Significant Bit)。原理就是图片中的像数一般是由三种颜色组成，即三原色，由这三种原色可以组成其他各种颜色，例如在PNG图片的储存中，每个颜色会有8bit，LSB隐写就是修改了像数中的最低的1bit，在人眼看来是看不出来区别的，也把信息隐藏起来了。

使用Python写了一个程序，以二进制形式读取图片文件，将每8位的最后一位读出来，然后连起来

也可以使用工具软件Stegsolve等
-->