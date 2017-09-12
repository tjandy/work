#coding:utf-8

import glob

from xml.etree import ElementTree

def getCsvFileName(str):
    return str.split("\\")[-1].split(".")[0]

def getClassName(str):
    return str+ "Info"

def RBC(str):
    return str.replace("${N}", '\n').replace("${L}", '<').replace("${R}", '>').replace("${C}", '&')

def getTempleteStr(templete):
    code = ""
    for node in templete:
        code = code + node.text
    return code

#初始化模板
root = ElementTree.fromstring(open("JavaCodeTemplate.xml").read())
javaCodeTemplete_Import = getTempleteStr(root.getiterator("import"))
javaCodeTemplete_Namespace=getTempleteStr(root.getiterator("namespace"))
javaCodeTemplete_ClassHead=getTempleteStr(root.getiterator("classhead"))
javaCodeTemplete_Single=getTempleteStr(root.getiterator("single"))
javaCodeTemplete_Repeat=getTempleteStr(root.getiterator("repeat"))
javaCodeTemplete_InitTable=getTempleteStr(root.getiterator("inittable"))
javaCodeTemplete_Tail=getTempleteStr(root.getiterator("tail"))
javaCodeTemplete_Enum=getTempleteStr(root.getiterator("enum"))
javaCodeTemplete_ReadInt=getTempleteStr(root.getiterator("readint"))
javaCodeTemplete_ReadString=getTempleteStr(root.getiterator("readstring"))

def buildCode(csvFile):
    javaCodeStr_Import = ""
    javaCodeStr_Namespace = ""
    javaCodeStr_ClassHead = ""
    javaCodeStr_Single = ""
    javaCodeStr_Repeat = ""
    javaCodeStr_InitTable = ""
    javaCodeStr_Tail = ""
    javaCodeStr_Enum=""
    javaCodeStr_Read=""

    csvFileName = getCsvFileName(csvFile)
    className = getClassName(csvFileName)
    fileName = className + ".java"

    #import
    #namespace
    javaCodeStr_Namespace = javaCodeTemplete_Namespace

    javaCodeStr_ClassHead = ""
    try:
        with open(csvFile) as dataFile:
            notes = dataFile.readline().strip('\n').split("\t")
            params = dataFile.readline().strip('\n').split("\t")
            for i, paramName in enumerate(notes):
                try:
                    paramNote = params[i]
                    # 默认类型string
                    paramType = "string"
                    # 查找和判断类型
                    findIndex = 0
                    findIndex = paramNote.rfind("INT")
                    if (findIndex != -1):
                        paramType = "int"
                        paramNote = paramNote[0:findIndex]
                        javaCodeStr_Read += javaCodeTemplete_ReadInt.replace("${name}",paramName.capitalize()).\
                            replace("${enumname}", paramName.upper())

                    findIndex = paramNote.rfind("STRING")
                    if (findIndex != -1):
                        paramType = "string"
                        paramNote = paramNote[0:findIndex]
                        javaCodeStr_Read += javaCodeTemplete_ReadString.replace("${name}",paramName.capitalize()).\
                            replace("${enumname}", paramName.upper())
                        # 生成属性
                    javaCodeStr_Single += javaCodeTemplete_Single.replace("${type}", paramType).replace("${Variable}", paramName.capitalize()).\
                            replace("${N}", '\n').replace("${L}", '<').replace("${R}", '>').replace("${C}", '&')
                    javaCodeStr_Enum += javaCodeTemplete_Enum.replace("${idx}",str(i)).replace("${name}", paramName.upper())


                except ValueError:
                    pass

        javaCodeStr_ClassHead = javaCodeTemplete_ClassHead. \
            replace("${CodeName}", className). \
            replace("${FileName}", csvFileName + ".csv"). \
            replace("${FULLENUM}", javaCodeStr_Enum). \
            replace("${N}", '\n').replace("${L}", '<').replace("${R}", '>').replace("${C}", '&')

    except IOError as err:
        print("The data file is missing:" + str(err))

    javaCodeStr_InitTable = javaCodeTemplete_InitTable. \
        replace("${CodeName}", className). \
        replace("${FULLREADER}", javaCodeStr_Read). \
        replace("${N}", '\n').replace("${L}", '<').replace("${R}", '>').replace("${C}", '&')

    javaCodeStr_Tail = javaCodeTemplete_Tail.\
            replace("${N}", '\n').replace("${L}", '<').replace("${R}", '>').replace("${C}", '&')
    try:
        with open("csv\\" + fileName, "w") as outFile:
            outFile.write(javaCodeStr_Import)
            outFile.write(javaCodeStr_Namespace)
            outFile.write(javaCodeStr_ClassHead)
            outFile.write(javaCodeStr_Single)
            outFile.write(javaCodeStr_Repeat)
            outFile.write(javaCodeStr_InitTable)
            outFile.write(javaCodeStr_Tail)
    except IOError:
        print("write file error")

#初始化管理器模板
root = ElementTree.fromstring(open("JavaTableManagerTemplate.xml").read())
javaTableMgrTemplete_Import=getTempleteStr(root.getiterator("import"))
javaTableMgrTemplete_Namespace=getTempleteStr(root.getiterator("namespace"))
javaTableMgrTemplete_ClassHead=getTempleteStr(root.getiterator("classhead"))
javaTableMgrTemplete_ManagerData=getTempleteStr(root.getiterator("managerdata"))
javaTableMgrTemplete_InitSingle=getTempleteStr(root.getiterator("initsingle"))
javaTableMgrTemplete_InitTable=getTempleteStr(root.getiterator("inittable"))
javaTableMgrTemplete_ManagerOpt=getTempleteStr(root.getiterator("manageropt"))
javaTableMgrTemplete_Tail=getTempleteStr(root.getiterator("tail"))


def bulidTableMgr():
    javaTableMgrCode_ManagerData =""
    javaTableMgrCode_InitSingle =""
    javaTableMgrCode_InitTable =""
    javaTableMgrCode_ManagerOpt =""

    javaTableMgrCode_Import = RBC(javaTableMgrTemplete_Import)
    javaTableMgrCode_Namespace = RBC(javaTableMgrTemplete_Namespace)
    javaTableMgrCode_ClassHead = RBC(javaTableMgrTemplete_ClassHead)
    csvFiles = glob.glob("csv\\*.csv")
    for eachFile in csvFiles:
        className = getClassName(getCsvFileName(eachFile))

        javaTableMgrCode_ManagerData += RBC(javaTableMgrTemplete_ManagerData.replace("${CodeName}",className))
        javaTableMgrCode_InitSingle += RBC(javaTableMgrTemplete_InitSingle.replace("${CodeName}",className))
        javaTableMgrCode_InitTable += RBC(javaTableMgrTemplete_InitTable.replace("${CodeName}",className))
        javaTableMgrCode_ManagerOpt +=RBC(javaTableMgrTemplete_ManagerOpt.replace("${CodeName}",className))

    javaTableMgrCode_Tail = RBC(javaTableMgrTemplete_Tail)
    try:
        with open("csv\\" + "TableManager.java", "w") as outFile:
            outFile.write(javaTableMgrCode_Import)
            outFile.write(javaTableMgrCode_Namespace)
            outFile.write(javaTableMgrCode_ClassHead)
            outFile.write(javaTableMgrCode_ManagerData)
            outFile.write(javaTableMgrCode_InitSingle)
            outFile.write(javaTableMgrCode_InitTable)
            outFile.write(javaTableMgrCode_ManagerOpt)
            outFile.write(javaTableMgrCode_Tail)
    except IOError:
        print("write file error")
# 导出csv目录下所有文件
csvFiles = glob.glob("csv\\*.csv")
for eachFile in csvFiles:
         buildCode(eachFile)

bulidTableMgr()
print("csv_to_java ok.")