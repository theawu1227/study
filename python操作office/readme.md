# 东方学者.py
## 将doc文件转化成docx文件 -- doSaveAas()
使用库 -- `from win32com import client`
## 读取word
使用库 -- from docx import Document

1.读取文件段落内容:
```python
    doc = Document(file)  # 实例化
    for va in doc.paragraphs:  # 循环文本段落
       print(va.text)  # 打印每个段落的内容
        ...
```
2.读取文件中的表格
```python
    doc = Document(file)  # 实例化
    tables = doc.tables  # 得到所有的表格对象
    # 得到第一个表格  doc.tables[0]
    for table in tables:  # 遍历所有表格
        for row in table.rows:  # 遍历表格的行对象
           #  得到每一行第一列的值  row.cells[0].text
            for va in row.cells:  # 遍历行的每一个单元格
                print(va.text)  # 打印单元格的值
```

## excel追加sheet --create_sheet() ：
使用库 -- from openpyxl import load_workbook
`wb.create_sheet(sheet_name)  # 创建sheet`

`wb.sheetnames  # 获取表格中所有的sheetname`

## 给指定的sheet追加数据 -- in_datas()：
`wb.active  # 获取工作簿的活动表，默认为第一个`

`wb[指定sheet]  # 获取指定工作簿` 

# excel_table.py

## 判断表格文件是否存在
`my_file = os.path.exists(self.excel_file)  # return True/False`
如果True 则向指定表格追加数据 -- input_table()
False,则创建指定名称的表格 -- create_table()