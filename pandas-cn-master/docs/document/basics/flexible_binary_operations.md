# 灵活的二进制操作

With binary operations between pandas data structures, there are two key points of interest:  
对于pandas数据类型的二元操作，有以下两点值得注意：

- Broadcasting behavior between higher- (e.g. DataFrame) and lower-dimensional (e.g. Series) objects.  
  在高维（如，数据表）与低维（如，序列）对象间的广播行为
- Missing data in computations.  
  缺失值对于计算的影响  
We will demonstrate how to manage these issues independently, though they can be handled simultaneously.  
尽管我们可以同时处理，这里，我们将仅展示如何单独地解决这两个问题。

## Matching / broadcasting behavior
## 匹配/广播 行为

DataFrame has the methods [add()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.add.html#pandas.DataFrame.add), [sub()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sub.html#pandas.DataFrame.sub), [mul()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.mul.html#pandas.DataFrame.mul), [div()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.div.html#pandas.DataFrame.div) and related functions [radd()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.radd.html#pandas.DataFrame.radd), [rsub()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rsub.html#pandas.DataFrame.rsub), … for carrying out binary operations. For broadcasting behavior, Series input is of primary interest. Using these functions, you can use to either match on the index or columns via the **axis** keyword:  
数据表拥有 [add()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.add.html#pandas.DataFrame.add), [sub()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sub.html#pandas.DataFrame.sub), [mul()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.mul.html#pandas.DataFrame.mul), [div()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.div.html#pandas.DataFrame.div) 方法，以及相关的[radd()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.radd.html#pandas.DataFrame.radd), [rsub()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rsub.html#pandas.DataFrame.rsub), …函数，用于执行二元操作。对于广播行为，序列输入是最重要的。使用这些函数，你可以通过关键字``axixs``在索引或着列上进行匹配:

```python
In [14]: df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
   ....:                    'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
   ....:                    'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
   ....: 

In [15]: df
Out[15]: 
        one       two     three
a -1.101558  1.124472       NaN
b -0.177289  2.487104 -0.634293
c  0.462215 -0.486066  1.931194
d       NaN -0.456288 -1.222918

In [16]: row = df.iloc[1]

In [17]: column = df['two']

In [18]: df.sub(row, axis='columns')
Out[18]: 
        one       two     three
a -0.924269 -1.362632       NaN
b  0.000000  0.000000  0.000000
c  0.639504 -2.973170  2.565487
d       NaN -2.943392 -0.588625

In [19]: df.sub(row, axis=1)
Out[19]: 
        one       two     three
a -0.924269 -1.362632       NaN
b  0.000000  0.000000  0.000000
c  0.639504 -2.973170  2.565487
d       NaN -2.943392 -0.588625

In [20]: df.sub(column, axis='index')
Out[20]: 
        one  two     three
a -2.226031  0.0       NaN
b -2.664393  0.0 -3.121397
c  0.948280  0.0  2.417260
d       NaN  0.0 -0.766631

In [21]: df.sub(column, axis=0)
Out[21]: 
        one  two     three
a -2.226031  0.0       NaN
b -2.664393  0.0 -3.121397
c  0.948280  0.0  2.417260
d       NaN  0.0 -0.766631
```

Furthermore you can align a level of a multi-indexed DataFrame with a Series.  
进一步，你可以将序列与数据表的多级索引中的一级对齐。

```python
In [22]: dfmi = df.copy()

In [23]: dfmi.index = pd.MultiIndex.from_tuples([(1,'a'),(1,'b'),(1,'c'),(2,'a')],
   ....:                                        names=['first','second'])
   ....: 

In [24]: dfmi.sub(column, axis=0, level='second')
Out[24]: 
                   one      two     three
first second                             
1     a      -2.226031  0.00000       NaN
      b      -2.664393  0.00000 -3.121397
      c       0.948280  0.00000  2.417260
2     a            NaN -1.58076 -2.347391
```

With Panel, describing the matching behavior is a bit more difficult, so the arithmetic methods instead (and perhaps confusingly?) give you the option to specify the broadcast axis. For example, suppose we wished to demean the data over a particular axis. This can be accomplished by taking the mean over an axis and broadcasting over the same axis:  
当使用面板时，描述匹配方法有些复杂，因此替代的数学方法讲给你选择广播的维度。例如，我们想要描述延某一特定维度的数据。这可以通过延某一维度广播并计算均值的方法达成：

```python
In [25]: major_mean = wp.mean(axis='major')

In [26]: major_mean
Out[26]: 
      Item1     Item2
A -0.878036 -0.092218
B -0.060128  0.529811
C  0.099453 -0.715139
D  0.248599 -0.186535

In [27]: wp.sub(major_mean, axis='major')
Out[27]: 
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 5 (major_axis) x 4 (minor_axis)
Items axis: Item1 to Item2
Major_axis axis: 2000-01-01 00:00:00 to 2000-01-05 00:00:00
Minor_axis axis: A to D
```

And similarly for ``axis="items"`` and ``axis="minor"``.  
对于``axis="items"``和``axis="minor"``也是类似的。

**Note**：I could be convinced to make the **axis** argument in the DataFrame methods match the broadcasting behavior of Panel. Though it would require a transition period so users can change their code…  
**注意**：尽管这样将需要为我们的用户提供一个过度期，来让他们改写他们的代码，我仍然决定在数据表方法中提供一个**axis**参数，用于匹配类似面板中的广播行为  

Series and Index also support the [divmod()](https://docs.python.org/3/library/functions.html#divmod) builtin. This function takes the floor division and modulo operation at the same time returning a two-tuple of the same type as the left hand side. For example:  
序列与索引也原生支持 [divmod()](https://docs.python.org/3/library/functions.html#divmod) 。这个函数同时计算商与余数，并返回一个二元元组

```python
In [28]: s = pd.Series(np.arange(10))

In [29]: s
Out[29]: 
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int64

In [30]: div, rem = divmod(s, 3)

In [31]: div
Out[31]: 
0    0
1    0
2    0
3    1
4    1
5    1
6    2
7    2
8    2
9    3
dtype: int64

In [32]: rem
Out[32]: 
0    0
1    1
2    2
3    0
4    1
5    2
6    0
7    1
8    2
9    0
dtype: int64

In [33]: idx = pd.Index(np.arange(10))

In [34]: idx
Out[34]: Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')

In [35]: div, rem = divmod(idx, 3)

In [36]: div
Out[36]: Int64Index([0, 0, 0, 1, 1, 1, 2, 2, 2, 3], dtype='int64')

In [37]: rem
Out[37]: Int64Index([0, 1, 2, 0, 1, 2, 0, 1, 2, 0], dtype='int64')
```

We can also do elementwise [divmod()](https://docs.python.org/3/library/functions.html#divmod):  
我们也可以在元素级别使用[divmod()](https://docs.python.org/3/library/functions.html#divmod): 

```python
In [38]: div, rem = divmod(s, [2, 2, 3, 3, 4, 4, 5, 5, 6, 6])

In [39]: div
Out[39]: 
0    0
1    0
2    0
3    1
4    1
5    1
6    1
7    1
8    1
9    1
dtype: int64

In [40]: rem
Out[40]: 
0    0
1    1
2    2
3    0
4    0
5    1
6    1
7    2
8    2
9    3
dtype: int64
```

## Missing data / operations with fill values
## 缺失值/补全计算

In Series and DataFrame, the arithmetic functions have the option of inputting a fill_value, namely a value to substitute when at most one of the values at a location are missing. For example, when adding two DataFrame objects, you may wish to treat NaN as 0 unless both DataFrames are missing that value, in which case the result will be NaN (you can later replace NaN with some other value using ``fillna`` if you wish).  
在序列与数据表中，运算函数包含一个fill_value参数，它可以在碰到至多1个缺失值的时候替换该缺失值。例如，当进行两个数据表相加时，你有可能希望所有的NaN被作为0处理，除非两个数据表同时缺失这个值时，结果才是NaN（你可以在之后使用``fillna``方法来将他们替换为其他值）

```python
In [41]: df
Out[41]: 
        one       two     three
a -1.101558  1.124472       NaN
b -0.177289  2.487104 -0.634293
c  0.462215 -0.486066  1.931194
d       NaN -0.456288 -1.222918

In [42]: df2
Out[42]: 
        one       two     three
a -1.101558  1.124472  1.000000
b -0.177289  2.487104 -0.634293
c  0.462215 -0.486066  1.931194
d       NaN -0.456288 -1.222918

In [43]: df + df2
Out[43]: 
        one       two     three
a -2.203116  2.248945       NaN
b -0.354579  4.974208 -1.268586
c  0.924429 -0.972131  3.862388
d       NaN -0.912575 -2.445837

In [44]: df.add(df2, fill_value=0)
Out[44]: 
        one       two     three
a -2.203116  2.248945  1.000000
b -0.354579  4.974208 -1.268586
c  0.924429 -0.972131  3.862388
d       NaN -0.912575 -2.445837
```

## Flexible Comparisons
## 灵活比较

Series and DataFrame have the binary comparison methods ``eq, ne, lt, gt, le``, and ``ge`` whose behavior is analogous to the binary arithmetic operations described above:  
序列和数据表都包含 ``eq, ne, lt, gt, le``, 和 ``ge`` 二元比较。他们的行为与算术的二元比较操作是类似的：

```python
In [45]: df.gt(df2)
Out[45]: 
     one    two  three
a  False  False  False
b  False  False  False
c  False  False  False
d  False  False  False

In [46]: df2.ne(df)
Out[46]: 
     one    two  three
a  False  False   True
b  False  False  False
c  False  False  False
d   True  False  False
```

These operations produce a pandas object of the same type as the left-hand-side input that is of dtype ``bool``. These ``boolean`` objects can be used in indexing operations, see the section on [Boolean indexing](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-boolean).  
这些操作返回一个具有与左操作数相同类型的pandas对象，即布尔型。这些布尔型对象可以在索引操作时使用，请参见： [Boolean indexing](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-boolean)。

## Boolean Reductions
## 布尔降维

You can apply the reductions: [empty](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.empty.html#pandas.DataFrame.empty), [any()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.any.html#pandas.DataFrame.any), [all()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.all.html#pandas.DataFrame.all), and [bool()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.bool.html#pandas.DataFrame.bool) to provide a way to summarize a boolean result.  
你可以使用[empty](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.empty.html#pandas.DataFrame.empty), [any()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.any.html#pandas.DataFrame.any), [all()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.all.html#pandas.DataFrame.all), 和 [bool()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.bool.html#pandas.DataFrame.bool) 函数来对你的数据进行布尔降为，并得到一个布尔型的结果

```python
In [47]: (df > 0).all()
Out[47]: 
one      False
two      False
three    False
dtype: bool

In [48]: (df > 0).any()
Out[48]: 
one      True
two      True
three    True
dtype: bool
```

You can reduce to a final boolean value.  
你可以对结果继续进行降维

```python
In [49]: (df > 0).any().any()
Out[49]: True
```

You can test if a pandas object is empty, via the empty property.  
你可以通过empty属性来测试是否一个pandas对象为空

```python
In [50]: df.empty
Out[50]: False

In [51]: pd.DataFrame(columns=list('ABC')).empty
Out[51]: True
```

To evaluate single-element pandas objects in a boolean context, use the method bool():  
使用``bool()``方法来计算一个单元素布尔型的pandas对象的布尔属性

```python
In [52]: pd.Series([True]).bool()
Out[52]: True

In [53]: pd.Series([False]).bool()
Out[53]: False

In [54]: pd.DataFrame([[True]]).bool()
Out[54]: True

In [55]: pd.DataFrame([[False]]).bool()
Out[55]: False
```

### !Warning
### ！警告

You might be tempted to do the following:  
你或许试图尝试以下的操作：

```python
>>> if df:
     ...
```

Or  
或者

```python
>>> df and df2
```

These will both raise errors, as you are trying to compare multiple values.  
这回触发一个错误，因为你再尝试比较多个值

```python
ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().
```

See [gotchas](http://pandas.pydata.org/pandas-docs/stable/gotchas.html#gotchas-truth) for a more detailed discussion.  
更多讨论，参见[gotchas](http://pandas.pydata.org/pandas-docs/stable/gotchas.html#gotchas-truth)

## Comparing if objects are equivalent
## 比较是否对象相等

Often you may find that there is more than one way to compute the same result. As a simple example, consider ``df+df`` and ``df*2``. To test that these two computations produce the same result, given the tools shown above, you might imagine using ``(df+df == df*2).all().`` But in fact, this expression is False:  
通常我们有多种方法来计算同一个结果。例如：``df+df`` 和 ``df*2``。为了比较两个对象是否相等，或许有些人希望使用``(df+df == df*2).all().``这样的语句，但事实上，这种语句是错误的

```python
In [56]: df+df == df*2
Out[56]: 
     one   two  three
a   True  True  False
b   True  True   True
c   True  True   True
d  False  True   True

In [57]: (df+df == df*2).all()
Out[57]: 
one      False
two       True
three    False
dtype: bool
```

Notice that the boolean DataFrame df+df == df*2 contains some False values! This is because NaNs do not compare as equals:  
注意，这两个布尔型的数据表 df+df == df*2 包含一些 False 值！这是因为NaN并不被人为是相等的。

```python
In [58]: np.nan == np.nan
Out[58]: False
```

So, NDFrames (such as Series, DataFrames, and Panels) have an equals() method for testing equality, with NaNs in corresponding locations treated as equal.  
因此，NDFrames（如，序列，数据表与面板）拥有一个``equal()``方法来进行“相等”的测试，此时两个位置相同的NaN被认为是相等的

```python
In [59]: (df+df).equals(df*2)
Out[59]: True
```

Note that the Series or DataFrame index needs to be in the same order for equality to be True:  
注意，序列和数据表的所索引需要是相同的顺序，才能在“相等”测试中 获得True的返回

```python
In [60]: df1 = pd.DataFrame({'col':['foo', 0, np.nan]})

In [61]: df2 = pd.DataFrame({'col':[np.nan, 0, 'foo']}, index=[2,1,0])

In [62]: df1.equals(df2)
Out[62]: False

In [63]: df1.equals(df2.sort_index())
Out[63]: True
```

## Comparing array-like objects  
## 比较数组型的对象

You can conveniently perform element-wise comparisons when comparing a pandas data structure with a scalar value:  
当使用标量类型的pandas数据结构时，你可以轻易地执行元素对元素的比较：

```python
In [64]: pd.Series(['foo', 'bar', 'baz']) == 'foo'
Out[64]: 
0     True
1    False
2    False
dtype: bool

In [65]: pd.Index(['foo', 'bar', 'baz']) == 'foo'
Out[65]: array([ True, False, False], dtype=bool)
```

Pandas also handles element-wise comparisons between different array-like objects of the same length:  
pandas可以处理不同类型，但长度相同的数组型对象

```python
In [66]: pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'qux'])
Out[66]: 
0     True
1     True
2    False
dtype: bool

In [67]: pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux'])
Out[67]: 
0     True
1     True
2    False
dtype: bool
```

Trying to compare ``Index`` or ``Series`` objects of different lengths will raise a ValueError:  
试图比较不同长度的``Index`` 或 ``Series``对象将会引发错误

```python
In [55]: pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo', 'bar'])
ValueError: Series lengths must match to compare

In [56]: pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo'])
ValueError: Series lengths must match to compare
```

Note that this is different from the NumPy behavior where a comparison can be broadcast:  
注意，Pandas中并不可以进行比较。这不同于NumPy中比较可以被广播，

```python
In [68]: np.array([1, 2, 3]) == np.array([2])
Out[68]: array([False,  True, False], dtype=bool)
```

or it can return False if broadcasting can not be done:  
或者在广播失败后返回False：

```python
In [69]: np.array([1, 2, 3]) == np.array([1, 2])
Out[69]: False
```

## Combining overlapping data sets  
## 合并带有重复数据的数据集

A problem occasionally arising is the combination of two similar data sets where values in one are preferred over the other. An example would be two data series representing a particular economic indicator where one is considered to be of “higher quality”. However, the lower quality series might extend further back in history or have more complete data coverage. As such, we would like to combine two DataFrame objects where missing values in one DataFrame are conditionally filled with like-labeled values from the other DataFrame. The function implementing this operation is [combine_first()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first), which we illustrate:  
再合并两个相似的数据集时，一个常见的问题是，我们希望保留其中一个数据集中的数据，而舍弃另一个。一个例子便是我们有两个序列来表达一个特定的经济指标，然而其中的一个被认为是更“好”的。然而相对“不好”的数据集则包含更远古的数据，或者有这更大的数据覆盖。因此，我们将希望能够将两个数据表合并起来，并且将其中一个数据表中的缺失值，有条件地用另外一个数据表中的“相似标签”的数据来填充。完成此类操作的函数是[combine_first()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first), 我们详述如下:

```python
In [70]: df1 = pd.DataFrame({'A' : [1., np.nan, 3., 5., np.nan],
   ....:                     'B' : [np.nan, 2., 3., np.nan, 6.]})
   ....: 

In [71]: df2 = pd.DataFrame({'A' : [5., 2., 4., np.nan, 3., 7.],
   ....:                     'B' : [np.nan, np.nan, 3., 4., 6., 8.]})
   ....: 

In [72]: df1
Out[72]: 
     A    B
0  1.0  NaN
1  NaN  2.0
2  3.0  3.0
3  5.0  NaN
4  NaN  6.0

In [73]: df2
Out[73]: 
     A    B
0  5.0  NaN
1  2.0  NaN
2  4.0  3.0
3  NaN  4.0
4  3.0  6.0
5  7.0  8.0

In [74]: df1.combine_first(df2)
Out[74]: 
     A    B
0  1.0  NaN
1  2.0  2.0
2  3.0  3.0
3  5.0  4.0
4  3.0  6.0
5  7.0  8.0
```

## General DataFrame Combine
## 一般性数据表合并

The [combine_first()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first) method above calls the more general [DataFrame.combine()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine.html#pandas.DataFrame.combine). This method takes another DataFrame and a combiner function, aligns the input DataFrame and then passes the combiner function pairs of Series (i.e., columns whose names are the same).  
[combine_first()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first) 方法，调用了更一般化的[DataFrame.combine()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine.html#pandas.DataFrame.combine). 这个方法使用另外一个数据表和一个合并函数，对齐输入数据表，然后传入合并函数的序列对（即，列名相同）。

So, for instance, to reproduce [combine_first()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first) as above:  
因此，例如，重现上述 [combine_first()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first) 函数:

```python
In [75]: combiner = lambda x, y: np.where(pd.isna(x), y, x)

In [76]: df1.combine(df2, combiner)
Out[76]: 
     A    B
0  1.0  NaN
1  2.0  2.0
2  3.0  3.0
3  5.0  4.0
4  3.0  6.0
5  7.0  8.0
```
