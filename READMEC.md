# [京剧](https://zh.wikipedia.org/wiki/%E4%BA%AC%E5%89%A7)音素标注

[English](https://github.com/ronggong/jingjuPhonemeAnnotation/blob/master/README.md)

作者: 龚嵘, 贵云飞（Rafael Caro Repetto）, 杨弋乐, MTG-UPF, rong.gong@upf.edu, rafael.caro@upf.edu

2017年1月16日

分级式标注 - 京剧清唱数据库的上下句, 音节和音素标注。

格式： 	Praat TextGrid

标注层数:	5

[行当](http://baike.baidu.com/view/15254.htm): 旦，老生

##标注层数描述：

*1-line:         上下句边界。

*2-pinyin:       音节边界，不包含垫字，休止标注。  

*3-dian:         音节边界，包含垫子，休止标注。

*4-dianSilence:  音节边界，包含电子，休止未标注，连接于前一音节。  

*5-details:      音素标注

##用法：

解析代码位于pycode目录。

##授权：
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
