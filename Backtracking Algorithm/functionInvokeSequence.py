from slither.slither import Slither
# from slitherUse import *
from varMap import getStateVarReadInFunConDic
from cName_stateVars_Funs import getStateVariables
from funMap import getStateVarWriteDic
import random
import math


# randomly return an item in a list
def randomChoose(list):
    r = random.random() * len(list)
    v = math.floor(r)
    return list[v]


def funInvokSeq(path):
    varMap = getStateVarWriteDic(path)
    # print(varMap)

    funMap = getStateVarReadInFunConDic(path)
    # print(funMap)

    slither = Slither(path)
    max_seq_length = 10
    contractLen = len(slither.contracts)

    for contract in slither.contracts:
        if contract is slither.contracts[contractLen - 1]:
            seqMap = {}
            for function in contract.functions:
                seq = [function.name]
                i = 0
                # print(seq)
                while i <= len(seq) - 1:
                    if len(funMap[seq[i]]) == 0:
                        break
                    else:
                        for var in funMap[seq[i]]:
                            if len(varMap[var]) == 0:
                                break
                            else:
                                seq.append(randomChoose(varMap[var]))
                                if len(seq) >= max_seq_length:
                                    break
                                else:
                                    i += 1
                                    continue
                seq.reverse()
                seqMap.update({function.name: seq})
                # print('..............................')

    return seqMap


# print(funInvokSeq('file.sol'))
