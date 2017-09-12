#coding:utf-8
import glob

from xml.etree import ElementTree

desc=""

def print_node(node):
    '''''打印结点基本信息'''
    print  node.text

def read_xml(text):
        '''''读xml文件'''
        # 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）
        # root = ElementTree.parse(r"D:/test.xml")
        root = ElementTree.fromstring(text)

        # 获取element的方法
        # 1 通过getiterator
        lst_node = root.getiterator("descript")
        for node in lst_node:
                print_node(node)
        lst_node = root.getiterator("import")
        for node in lst_node:
            print_node(node)

        lst_node = root.getiterator("classhead")
        for node in lst_node:
            print_node(node)
        # 2通过 getchildren
        # lst_node_child = lst_node[0].getchildren()[0]
        # print_node(lst_node_child)

        # # 3 .find方法
        # node_find = root.find('plist')
        # print_node(node_find)
        #
        # # 4. findall方法
        # node_findall = root.findall("plist")[1]
        # print_node(node_findall)

def buildCode(filePath):
        #类模版
        classTemplate = """
using System;

namespace Data
{
    /// <summary>
    /// 静态表数据类
    /// </summary>
    [Serializable]
    public class $className
    {
	$paramFied

    }
}
"""
        #属性模版
        paramTemplate = """
        /// <summary>
        /// $paramNote
        /// </summary>
        public $paramType $paramName;"""

        className = filePath.split("\\")[-1].split(".")[0] + "Info"
        code = "";
        try:
                with open(filePath) as dataFile:
                        notes = dataFile.readline().strip('\n').split(",")
                        params = dataFile.readline().strip('\n').split(",")
                        for i,paramName in enumerate(params):
                                try:
                                        paramNote = notes[i]
                                        #默认类型string
                                        paramType = "string"
                                        #查找和判断类型
                                        findIndex = 0;
                                        findIndex = paramNote.rfind("[int]")                                     
                                        if(findIndex != -1):
                                           paramType = "int"
                                           paramNote = paramNote[0:findIndex]
                                        findIndex = paramNote.rfind("[float]")
                                        if(findIndex != -1):
                                           paramType = "float"
                                           paramNote = paramNote[0:findIndex]               
                                        #生成属性
                                        code += paramTemplate.replace("$paramNote", paramNote).replace("$paramName", paramName).replace("$paramType",paramType)
                                except ValueError:
                                        pass
                        #生成类
                        code = classTemplate.replace("$className", className).replace("$paramFiedZ", code)
        except IOError as err:
                print("The data file is missing:" + str(err))
        try:
                with open("csv\\" + className + ".cs", "w") as outFile:
                        outFile.write(code)
        except IOError:
                print("write file error")

def build_tableManger():
    return

# 导出csv目录下所有文件
csvFiles = glob.glob("csv\\*.csv")
# for eachFile in csvFiles:
# 	buildCode(eachFile)
# print("csv_to_csharp ok.")

read_xml(open("CSharpCodeTemplate.xml").read())
#input()





