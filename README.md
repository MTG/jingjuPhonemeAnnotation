# Jingju (Beijing opera) Phoneme Annotation

[中文版](https://github.com/ronggong/jingjuPhonemeAnnotation/blob/master/READMEC.md)

Authors: Rong Gong, Rafael Caro Repetto, Yile Yang, MTG-UPF, rong.gong@upf.edu, rafael.caro@upf.edu

## Description
This dataset is a collection of boundary annotations of a cappella singing performed by Beijing Opera (Jingju, 京剧, [wiki page](https://en.wikipedia.org/wiki/Peking_opera)) professional and amateur singers. This dataset was used as the experimental dataset in the following work:

>Rong Gong, Nicolas Obin, Georgi Dzhambazov and Xavier Serra, “Score-Informed Segmentation of Jingju Singing Phrases into Syllabic Units by Syllable Onset Detection" in ISMIR 2017 [submitted]

The boundries have been annotated in a hierarchical way. Line (phrase), syllable, phoneme singing units have been annotated to a jingju (Beijing opera) a-cappella singing audio dataset.

The corresponding audio files are the a-cappella singing arias recordings, which are stereo or mono, sampled at 44.1 kHz, and stored as wav files. Due to its large size, we can’t upload the audio files here, please write to us if you wish to use the audios. The wav files are recorded by two institutes: those file names ending with ‘qm’ are recorded by C4DM Queen Mary University of London; others file names ending with ‘upf’ or ‘lon’ are recorded by MTG-UPF. If you use this audio dataset in your work, please cite as well the following publication:
 
>D. A. A. Black, M. Li, and M. Tian, “Automatic Identification of Emotional Cues in Chinese Opera Singing,” in 13th Int. Conf. on Music Perception and Cognition (ICMPC-2014), 2014, pp. 250–255.

## Details

Format: 	Praat TextGrid, [Praat official page of the textgrid annotation](http://www.fon.hum.uva.nl/praat/manual/Intro_7__Annotation.html)

Tiers number:	5

Role-types [wiki page](https://en.wikipedia.org/wiki/Peking_opera#Classification_of_performers_and_roles): dan, laosheng

### Annotation units for phoneme-level

1.This table shows the annotation units used in 'pinyin' and 'details' tiers of each .\dataset\textgrid\\*.TextGrid  

2.Chinese pinyin and X-SAMPA format are given. 

3.b,p,d,t,k,j,q,x,zh,ch,sh,z,c,s initials are grouped into one representation (not X-SAMPA): c  

4.v,N,J (X-SAMPA) are three special pronunciations which do not exist in pinyin.  

<dl>
<table>
  <tr>
    <th></th>
    <th>Structure</th>
    <th>Pinyin[X-SAMPA]</th>
  </tr>
  <tr>
    <td rowspan="2">head</td>
    <td>initials</td>
    <td>m[m], f[f], n[n], l[l], g[k], h[x], r[r\'], y[j], w[w],<br>{b, p, d, t, k, j, q, x, zh, ch, sh, z, c, s} - group [c]<br>[v], [N], [J] - special pronunciations</td>
  </tr>
  <tr>
    <td>medial vowels</td>
    <td>i[i], u[u], ü[y]</td>
  </tr>
  <tr>
    <td rowspan="4">belly</td>
    <td>simple finals</td>
    <td>a[a"], o[O], e[7], ê[E], i[i], u[u], ü[y],<br>i (zhi,chi,shi) [1], i (ci,ci,si) [M],</td>
  </tr>
  <tr>
    <td>compound finals</td>
    <td>ai[aI^], ei[eI^], ao[AU^], ou[oU^]</td>
  </tr>
  <tr>
    <td>nasal finals</td>
    <td>an[an], en[@n], in[in],<br>ang[AN], eng[7N], ing[iN], ong[UN]</td>
  </tr>
  <tr>
    <td>retroflexed finals</td>
    <td>er [@][r\']</td>
  </tr>
  <tr>
    <td>tail</td>
    <td></td>
    <td>i[i], u[u], n[n], ng[N]</td>
  </tr>
</table>
</dl>

##Tier descriptions:

*1-line:         line boundary, lyrics in Chinese characters

*2-pinyin:       written character (syllable, in pinyin) boundary not including padding characters. Silence is annotated.  

*3-dian:         written character (in pinyin) boundary including padding characters. Silence is annotated.

*4-dianSilence:  written character (in pinyin) boundary. Silence is not annotated explicitly, it follows the previous dian syllable.  

*5-details:      phoneme (in X-SAMPA) boundary

##Usage:
The annotation textgrid files can be opened by Praat or by our parsing code, see this [jupyter notebook](https://github.com/ronggong/jingjuPhonemeAnnotation/blob/master/pycode/demo.ipynb) for some parsing examples.

##License:
This textgrid annotation work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
