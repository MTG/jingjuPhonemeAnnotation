'''
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

Author: Rong Gong, MTG-UPF, rong.gong@upf.edu
17 January 2016
'''

import textgridParser

groundtruth_textgrid_file   = '../laosheng/lsxp-Wo_zheng_zai-Kong_cheng_ji01-upf.TextGrid'

# parse the phrase boundary, and its content
lineList            		= textgridParser.textGrid2WordList(groundtruth_textgrid_file, whichTier='line')

# parse the dian Tier
dianList 	                = textgridParser.textGrid2WordList(groundtruth_textgrid_file, whichTier='dian')

print lineList
print dianSilenceList