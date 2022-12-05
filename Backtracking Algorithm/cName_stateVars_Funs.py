from slither.slither import Slither


# get contract name
def getContractName(path):
    slither = Slither(path)
    contract = slither.contracts[len(slither.contracts) - 1]
    return contract.name


# get state variables of a contract, return a str list
def getStateVariables(path):
    slither = Slither(path)
    stateVariableList = []
    contract = slither.contracts[len(slither.contracts) - 1]
    for var in contract.state_variables:
        stateVariableList.append(var.name)
    return stateVariableList


# get function names
def getFunctionNames(path):
    slither = Slither(path)
    funNameList = []
    contract = slither.contracts[len(slither.contracts) - 1]
    for fun in contract.functions:
        funNameList.append(fun.name)

    return funNameList


# print(getStateVariables('file.sol'))
