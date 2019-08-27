# 窗口函数扩展

A common alternative to rolling statistics is to use an expanding window, which yields the value of the statistic with all the data available up to that point in time.

These follow a similar interface to ``.rolling``, with the ``.expanding`` method returning an **Expanding** object.

As these calculations are a special case of rolling statistics, they are implemented in pandas such that the following two calls are equivalent:

```python
In [96]: df.rolling(window=len(df), min_periods=1).mean()[:5]
Out[96]: 
                   A         B         C         D
2000-01-01  0.314226 -0.001675  0.071823  0.892566
2000-01-02  0.654522 -0.171495  0.179278  0.853361
2000-01-03  0.708733 -0.064489 -0.238271  1.371111
2000-01-04  0.987613  0.163472 -0.919693  1.566485
2000-01-05  1.426971  0.288267 -1.358877  1.808650

In [97]: df.expanding(min_periods=1).mean()[:5]
Out[97]: 
                   A         B         C         D
2000-01-01  0.314226 -0.001675  0.071823  0.892566
2000-01-02  0.654522 -0.171495  0.179278  0.853361
2000-01-03  0.708733 -0.064489 -0.238271  1.371111
2000-01-04  0.987613  0.163472 -0.919693  1.566485
2000-01-05  1.426971  0.288267 -1.358877  1.808650
```

These have a similar set of methods to .rolling methods.

## Method Summary

Function | Description
---|---
[count()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.count.html#pandas.core.window.Expanding.count) | Number of non-null observations
[sum()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.sum.html#pandas.core.window.Expanding.sum) | Sum of values
[mean()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.mean.html#pandas.core.window.Expanding.mean) | Mean of values
[median()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.median.html#pandas.core.window.Expanding.median) | Arithmetic median of values
[min()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.min.html#pandas.core.window.Expanding.min) | Minimum
[max()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.max.html#pandas.core.window.Expanding.max) | Maximum
[std()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.std.html#pandas.core.window.Expanding.std) | Unbiased standard deviation
[var()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.var.html#pandas.core.window.Expanding.var) | Unbiased variance
[skew()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.skew.html#pandas.core.window.Expanding.skew) | Unbiased skewness (3rd moment)
[kurt()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.kurt.html#pandas.core.window.Expanding.kurt) | Unbiased kurtosis (4th moment)
[quantile()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.quantile.html#pandas.core.window.Expanding.quantile) | Sample quantile (value at %)
[apply()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.apply.html#pandas.core.window.Expanding.apply) | Generic apply
[cov()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.cov.html#pandas.core.window.Expanding.cov) | Unbiased covariance (binary)
[corr()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.corr.html#pandas.core.window.Expanding.corr) | Correlation (binary)

Aside from not having a ``window`` parameter, these functions have the same interfaces as their ``.rolling`` counterparts. Like above, the parameters they all accept are:

- ``min_periods``: threshold of non-null data points to require. Defaults to minimum needed to compute statistic. No ``NaNs`` will be output once ``min_periods`` non-null data points have been seen.
- ``center``: boolean, whether to set the labels at the center (default is False).

**Note**: The output of the ``.rolling`` and ``.expanding`` methods do not return a ``NaN`` if there are at least ``min_periods`` non-null values in the current window. For example:

```python
In [98]: sn = pd.Series([1, 2, np.nan, 3, np.nan, 4])

In [99]: sn
Out[99]: 
0    1.0
1    2.0
2    NaN
3    3.0
4    NaN
5    4.0
dtype: float64

In [100]: sn.rolling(2).max()
Out[100]: 
0    NaN
1    2.0
2    NaN
3    NaN
4    NaN
5    NaN
dtype: float64

In [101]: sn.rolling(2, min_periods=1).max()
Out[101]: 
0    1.0
1    2.0
2    2.0
3    3.0
4    3.0
5    4.0
dtype: float64
```

In case of expanding functions, this differs from [cumsum()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.cumsum.html#pandas.DataFrame.cumsum), [cumprod()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.cumprod.html#pandas.DataFrame.cumprod), [cummax()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.cummax.html#pandas.DataFrame.cummax), and [cummin()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.cummin.html#pandas.DataFrame.cummin), which return NaN in the output wherever a NaN is encountered in the input. In order to match the output of cumsum with expanding, use [fillna()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna):

```python
In [102]: sn.expanding().sum()
Out[102]: 
0     1.0
1     3.0
2     3.0
3     6.0
4     6.0
5    10.0
dtype: float64

In [103]: sn.cumsum()
Out[103]: 
0     1.0
1     3.0
2     NaN
3     6.0
4     NaN
5    10.0
dtype: float64

In [104]: sn.cumsum().fillna(method='ffill')
Out[104]: 
0     1.0
1     3.0
2     3.0
3     6.0
4     6.0
5    10.0
dtype: float64
```

An expanding window statistic will be more stable (and less responsive) than its rolling window counterpart as the increasing window size decreases the relative impact of an individual data point. As an example, here is the [mean()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.window.Expanding.mean.html#pandas.core.window.Expanding.mean) output for the previous time series dataset:

```python
In [105]: s.plot(style='k--')
Out[105]: <matplotlib.axes._subplots.AxesSubplot at 0x7f210fc68518>

In [106]: s.expanding().mean().plot(style='k')
Out[106]: <matplotlib.axes._subplots.AxesSubplot at 0x7f210fc68518>
```

![扩展窗口示例](/static/images/expanding_mean_frame.png)