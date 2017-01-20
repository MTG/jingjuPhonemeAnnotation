# [Jingju (Beijing opera)](https://en.wikipedia.org/wiki/Peking_opera) Phoneme Annotation

[中文版](https://github.com/ronggong/jingjuPhonemeAnnotation/blob/master/READMEC.md)

Authors: Rong Gong, Rafael Caro Repetto, Yile Yang, MTG-UPF, rong.gong@upf.edu, rafael.caro@upf.edu

## Description
This dataset is a collection of boundary annotations of a cappella singing performed by Beijing Opera (Jingju, 京剧) professional and amateur singers. This dataset was used as the experimental dataset in the following work:

>Rong Gong, Nicolas Obin, Georgi Dzhambazov and Xavier Serra, “Score-Informed Segmentation of Jingju Singing Phrases into Syllabic Units by Syllable Onset Detection" in ISMIR 2017 [submitted]

The boundries have been annotated in a hierarchical way. Line (phrase), syllable, phoneme singing units have been annotated to a jingju (Beijing opera) a-cappella singing audio dataset.

The corresponding audio files are the a-cappella singing arias recordings, which are stereo or mono, sampled at 44.1 kHz, and stored as wav files. Due to its large size, we can’t upload the audio files here, please write to us if you wish to use the audios. The wav files are recorded by two institutes: those file names ending with ‘qm’ are recorded by C4DM Queen Mary University of London; others file names ending with ‘upf’ or ‘lon’ are recorded by MTG-UPF. If you use the dataset in your work, please cite the following publication.
 
>D. A. A. Black, M. Li, and M. Tian, “Automatic Identification of Emotional Cues in Chinese Opera Singing,” in 13th Int. Conf. on Music Perception and Cognition (ICMPC-2014), 2014, pp. 250–255.

## Details

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

The textgrid file parsing code is in pycode folder, see `demo.py` for some examples.

##License:
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
