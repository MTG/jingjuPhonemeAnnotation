# [Jingju (Beijing opera)](https://en.wikipedia.org/wiki/Peking_opera) Phoneme Annotation

[中文版](https://github.com/ronggong/jingjuPhonemeAnnotation/blob/master/READMEC.md)

Authors: Rong Gong, Rafael Caro Repetto, Yile Yang, MTG-UPF, rong.gong@upf.edu, rafael.caro@upf.edu

16 January 2017

Hierarchical annotation - line (phrase), syllable, phoneme annotations of the jingju (Beijing opera) a-cappella singing dataset

Format: 	Praat TextGrid

Tiers number:	5

[Role-types](https://en.wikipedia.org/wiki/Peking_opera#Classification_of_performers_and_roles): dan, laosheng

##Tier descriptions:

*1-line:         line boundary

*2-pinyin:       written character (syllable) boundary not including padding characters. Silence is annotated.  

*3-dian:         written character boundary including padding characters. Silence is annotated.

*4-dianSilence:  written character boundary. Silence is not annotated explicitly, it follows the previous dian syllable.  

*5-details:      phoneme boundary

##Usage:

The parsing code is in pycode folder

##License:
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
