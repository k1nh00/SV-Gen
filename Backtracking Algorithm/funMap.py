from slither.slither import Slither
from cName_stateVars_Funs import getStateVariables


# return a list of function name list which include the functions operate a certain state variable
def getStateVarWriteDic(path):
    stateWriteDic = {}
    stateVarList = getStateVariables(path)
    slither = Slither(path)
    for contract in slither.contracts:
        for var in stateVarList:
            varObj = contract.get_state_variable_from_name(var)
            functions_write_var = contract.get_functions_writing_to_variable(varObj)
            funNameList = []
            for fun in functions_write_var:
                funNameList.append(fun.name)
            stateWriteDic.update({var: funNameList})
    return stateWriteDic


# print(getStateVarWriteDic('file.sol'))
