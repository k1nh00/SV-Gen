from slither.slither import Slither

# DIY packages
from cName_stateVars_Funs import getStateVariables


# return a list of function name list which include the functions operate a certain state variable
def getStateVarReadInFunConDic(path):
    stateVarList = getStateVariables(path)
    slither = Slither(path)
    varReadFunctionDic = {}
    for contract in slither.contracts:
        for function in contract.functions:
            varsReadInCondition = []
            for var in stateVarList:
                varObj = contract.get_state_variable_from_name(var)
                if function.is_reading_in_conditional_node(varObj) or \
                        function.is_reading_in_require_or_assert(varObj):
                    varsReadInCondition.append(var)
            varReadFunctionDic.update({function.name: varsReadInCondition})
    return varReadFunctionDic


# print(getStateVarReadInFunConDic('file.sol'))
