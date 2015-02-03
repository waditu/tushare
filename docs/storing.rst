.. contents::
   :depth: 3.0
..

.. highlightlang:: python

数据存储
========

*数据存储*\ 模块主要是引导用户将数据保存在本地磁盘或数据库服务器上，便于后期做量化分析和回测使用，在以文件格式保存在电脑磁盘的方式上，主要是调用pandas本身自带的方法，此处会罗列常用的参数和说明，另外，也会通过实例，展示文件数据追加或保存的python代码。在存入DataBase方面，TuShare提供了简单的处理方式。

-  保存为csv格式
-  保存为Excel格式
-  保存为HDF5文件格式
-  保存为JSON格式
-  存入关系型数据库
-  存入NoSQL数据库

csv文件
-------

pandas的DataFrame和Series对象提供了直接保存csv文件格式的方法，通过参数设定，轻松将数据内容保存在本地磁盘。

常用参数说明：

-  **path\_or\_buf**: csv文件存放路径或者StringIO对象
-  **sep** : 文件内容分隔符，默认为,逗号
-  **na\_rep**: 在遇到NaN值时保存为某字符，默认为''空字符
-  **float\_format**: float类型的格式
-  **columns**: 需要保存的列，默认为None
-  **header**: 是否保存columns名，默认为True
-  **index**: 是否保存index，默认为True
-  **mode** : 创建新文件还是追加到现有文件，默认为新建
-  **encoding**: 文件编码格式
-  **date\_format**: 日期格式

注：在设定path时，如果目录不存在，程序会提示IOError，请先确保目录已经存在于磁盘中。

调用方法：

::

    import tushare as ts

    df = ts.get_hist_data('000875')
    #直接保存
    df.to_csv('c:/day/000875.csv')

    #选择保存
    df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])

追加数据的方式：

某些时候，可能需要将一些同类数据保存在一个大文件中，这时候就需要将数据追加在同一个文件里,简单举例如下：

::

    import tushare as ts
    import os

    filename = 'c:/day/bigfile.csv'
    for code in ['000875', '600848', '000981']:
        df = ts.get_hist_data(code)
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=None)
        else:
            df.to_csv(filename)  

【注：如果是不考虑header，直接df.to\_csv(filename,
mode='a'）即可，否则，每次循环都会把columns名称也append进去】

Excel文件
---------

pandas将数据保存为MicroSoft Excel文件格式。

常用参数说明：

-  **excel\_writer**: 文件路径或者ExcelWriter对象
-  **sheet\_name**:sheet名称，默认为Sheet1
-  **sep** : 文件内容分隔符，默认为,逗号
-  **na\_rep**: 在遇到NaN值时保存为某字符，默认为''空字符
-  **float\_format**: float类型的格式
-  **columns**: 需要保存的列，默认为None
-  **header**: 是否保存columns名，默认为True
-  **index**: 是否保存index，默认为True
-  **mode** : 创建新文件还是追加到现有文件，默认为新建
-  **encoding**: 文件编码格式
-  **startrow**: 在数据的头部留出startrow行空行
-  **startcol** :在数据的左边留出startcol列空列

调用方法：

::

    import tushare as ts

    df = ts.get_hist_data('000875')
    #直接保存
    df.to_excel('c:/day/000875.xlsx')

    #设定数据位置（从第3行，第6列开始插入数据）
    df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)

HDF5文件
--------

pandas利用PyTables包将数据保存为HDF5格式的文件。需要确认的是，运行时PyTables包的版本需要
>=3.0.0。

常用参数说明：

-  **path\_or\_buf**: 文件路径或者HDFStore对象
-  **key**:HDF5中的group标识
-  **mode** : 包括 {‘a’追加, ‘w’写入, ‘r’只读,
   ‘r+’等同于a但文件必须已经存在}, 默认是 ‘a’
-  **format**:‘fixed(f)\|table(t)’,默认‘fixed’，f适合快速读写，不能追加数据
   t适合从文件中查找和选择数据
-  **append**: 适用于table(t)模式追加数据，默认Flase
-  **complevel**: 压缩级别1-9, 默认0
-  **complib**: 压缩类型{‘zlib’, ‘bzip2’, ‘lzo’, ‘blosc’, None}默认None

调用方法：

::

    import tushare as ts

    df = ts.get_hist_data('000875')
    df.to_hdf('c:/day/hdf.h5','000875')

JSON文件
--------

pandas生成Json格式的文件或字符串。

常用参数说明：

-  **path\_or\_buf**: json文件存放路径
-  **orient**:json格式顺序，包括columns，records，index，split，values，默认为columns
-  **force\_ascii**: 将字符转ASCII，默认为True

调用方法：

::

    import tushare as ts

    df = ts.get_hist_data('000875')
    df.to_json('c:/day/000875.json',orient='records')

    #或者直接使用
    print df.to_json(orient='records')
