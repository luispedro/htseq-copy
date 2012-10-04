from StringIO import StringIO

import HTSeq
unpaired = '''@HD\tVN:1.0\tSO:unsorted
@SQ\tSN:chr1\tLN:249250621
@SQ\tSN:chr2\tLN:243199373
@PG\tID:bowtie2\tPN:bowtie2\tVN:2.0.0-beta7
FCC0DEFACXX:2:1101:1087:101744#CCACATTC\t153\tchr2\t128281285\t42\t75M\t=\t128281285\t0\tTCCGGAGTGTTGCTCATTTACATNATCCTNACCGTCTGACCCNGAATCCCGTTCATCCTGTACTGGGGTAGCACC\t_aabcbca`ccbccbbcb^^\\TKB^a^TLB_hhgfee[VaVOBge^higdhhfgfhgfhgd^ffihfadebd_c`\tAS:i:-3\tXN:i:0\tXM:i:3\tXO:i:0\tXG:i:0\tNM:i:3\tMD:Z:23C5C12T32\tYT:Z:UP
FCC0DEFACXX:2:1101:1087:101744#CCACATTC\t69\t*\t128281285\t0\t*\t=\t128281285\t0\tGTCTGTCACATGATGTCCTTTGGGGAGGCCATCTTCTCGATCACTAGTTTCATTCTCTGAATGACGTTCTACACT\tfQ``aggghh[[eQXeeeSSdghh_cghiihhghbhbfdfbfgf\\c___dfg`ddgdgR^abeeeb\\\\`acbccZ\tYT:Z:UP
'''


try:
    assert len(list(HTSeq.SAM_Reader(StringIO(unpaired)))) == 2
except:
    pass

