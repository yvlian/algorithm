
'''
1.判断一个字符串需要改变多少个字母才能成为回文串
2.N*M的方格图进行染色：
  每种颜色染色的格子数目相同
  相邻格子染色不同，所有格子必须染色
  至少需要多少种颜色
3.给定正整数n，将其拆成k个数字，这k个数字的部分和可以表示1~n中的所有数字，求最小的k.
e.g.n=6, 1 2 3  k为3
4.对一个n*m的矩阵操作k次，每次选取和最大的行或列，加入到sum中，并将对应的元素均减去d，求最大的sum。1<=k<<10**5
'''



'''
1.直接首尾对比
2.寻找N*M的除了1以外的最小因子
3.找规律。若2**x<=n<2**(x+1),则k=x+1
4.???  40%

'''