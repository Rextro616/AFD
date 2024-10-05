import unittest
from afd import AFD
from afdController import main
import tkinter as tk
from loopApp import LoopApp
from readFileUtils import readFile 


class TestAFD(unittest.TestCase): 
    def test(self):
        file = readFile("./test/ciclo_control.docx", "docx")
        print(file)
        ocurrences = main(file, "docx")
        print(ocurrences)
        self.assertEqual(ocurrences, [{'lineas': '10 a la 12',
            'text': 'for(int i=0; i < arreglo.length; i++) {\n\tsumar(i);\n}'},
            {'lineas': '14 a la 19',
            'text': 'for( ; ; ){\n\n\taaaa\nbbbb\nvvvvcxxxsdakjdlk\n}'},
            {'lineas': '21 a la 26', 'text': 'while(true)\n{\n\nhola();\n\n}'},
            {'lineas': '34 a la 37', 'text': 'while(false) {\n\nadios()\n}'}
            ])


if __name__ == '__main__':
    unittest.main()