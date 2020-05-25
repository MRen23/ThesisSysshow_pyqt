# -*- coding:utf-8-*-

'''
时间：2020年4月22日
本文的主要用来实现进行数据分析的一些方法函数
'''

from tkinter import *
from sklearn.metrics.pairwise import rbf_kernel

import csv
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster,cut_tree,cophenet,inconsistent
import scipy.cluster.hierarchy as sch
from matplotlib import pyplot as plt
from matplotlib.pyplot import xticks
import pandas as pd
from scipy.spatial import distance
from itertools import groupby #itertool还包含有其他很多函数，比如将多个list联合起来
import json
from sklearn.metrics.pairwise import euclidean_distances
import re
from orangecontrib.associate.fpgrowth import *
from collections import Counter
from gensim.models import KeyedVectors
from sklearn.metrics import silhouette_samples, silhouette_score, davies_bouldin_score
import pickle


'''
函数名：读数据
输入：json数据的路径
输出：每张图片用list数据存储的label集，每个图片label的评分集，以及每个图片的url
描述：该函数实现从文件中读取json数据文件，并分别解析出label集，评分集，以及url集
'''
def loadjson_label(path):
    with open (path,'rb') as json_data:
        data = json.load(json_data)
    labels = []

    #打印所有的labels
    for i in data:
        labels.append(i[:-1])
    classes = []
    for i in labels:
        temp = []
        for j in i:
            c = list(j[0].values())
            temp.append(c[0])
        classes.append(temp)

    # 打印所有的score
    score = []
    for i in labels:
        temp = []
        for j in i:
            c = list(j[1].values())
            temp.append(c[0])
        score.append(temp)


    #打印所有的urls
    urls = []
    for i in data:
        urls.append(list(i[-1].values())[0])
    return classes, score, urls



'''
函数名：数据预处理
输入：label集，url
输出：经过处理的label集，并将url并进去
描述：通过该函数将获取到的数据集进行预处理。1.去掉空格，2.去掉括号，3.将url添加上。
'''
def preprocessing(labelset,urls):
#     i=0
#     for labels in labelset:
#         labels.append(urls[i])
#         i+=1
    sets_ini = []
    for i in labelset:
        inter_sets = []
        for j in i:
#             j = j.replace(' ','')                          # 去掉空格
            j = j.split(' ')[-1]
            inter_sets.append(re.sub('\((.*?\))', '', j))  # 去掉括号
        sets_ini.append(inter_sets)
    return sets_ini


# 取出所有的label
'''
函数名：取出所有label并进行统计
输入：每个图片的label list
输出：每个数据集中的label集合，数据集label统计并排序之后的结果
描述：对之前的图片的label list中的label先取出来，然后进行统计每个label在整个数据集中出现的百分比
'''
def label_stat(sets_ini):
#     all_sets = [] # 存放c不带url的数据集
#     for i in sets_ini:
#         all_sets.append(i[:-1])
#     label_all = [] # 存放所有label
#     for i in all_sets:
#         for j in i:
#             label_all.append(j)
    label_all = [] # 存放所有label
    for i in sets_ini:
        for j in i:
            label_all.append(j)
    #数据集长度定义
    length = len(sets_ini)
    #数据集每个label计数
    c = Counter(label_all)
    stat_sets = []
    for i in c.items():
        stat_sets.append([i[0],round(i[1]/length,5)])
    # 数据集label 频率排序
    n = len(stat_sets)
    for i in range(n-1):
        for j in range(n-i-1):
            if stat_sets[j][1]<stat_sets[j+1][1]:
                stat_sets[j],stat_sets[j+1] = stat_sets[j+1],stat_sets[j]
    return label_all, stat_sets




#读label
coshared_labelset, coshared_score, coshared_urls = loadjson_label('dataset\office\label\coshared.json')
open_labelset, open_score, open_urls = loadjson_label('dataset\office\label\open.json')

coshared_ini = preprocessing(coshared_labelset,coshared_urls)
open_ini = preprocessing(open_labelset,open_urls)

'''所有标签统计'''
all_labels_set = coshared_ini + open_ini
coshared_label_all, coshared_stat = label_stat(coshared_ini)
open_label_all,open_stat = label_stat(open_ini)
all_labels,all_labels_stat = label_stat(all_labels_set)


coshared_stat_df = pd.DataFrame(np.array(coshared_stat[:50]).T)
# print (coshared_stat_df)
# 开放型办公室图像标签出现前50
# print (open_stat[:50])
open_stat_df = pd.DataFrame(np.array(open_stat[:50]).T)
# print(open_stat_df)
# print ('所有图片出现频率前50：') # print (all_labels_stat[:50])
all_stat_df = pd.DataFrame(np.array(all_labels_stat[:50]).T)
# print(all_stat_df)


# histogram 对co shared 数据集进行统计
'''
函数名：画统计图
输入：统计后的数据集，图名
输出：统计图
描述：该函数用来画统计图
'''
def hist_bar(sets,title):
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    X = []
    for i in sets[:20]:
        X.append(i[0])
    # print (co_X)
    Y = []
    for i in sets[:20]:
        Y.append(i[1])

    fig = plt.figure()
    plt.bar(X,Y,0.6,color="green")
    plt.xlabel("标签名",family = 'FangSong',weight='bold',size=14)
    plt.xticks(rotation=90)

    plt.ylabel("频率",family = 'FangSong',size=14)
    plt.title(title+ "标签统计结果",fontsize=16,family = 'FangSong')
    plt.tick_params(axis='both',which='major',labelsize=14.5)
    # plt.savefig(r'./导出的图片/'+title+'20.png',dpi=200,bbox_inches = 'tight')
    plt.show()


# coshared_visual = hist_bar(coshared_stat,'共享办公室数据集')
# open_visual = hist_bar(open_stat,'开放式办公室数据集')
# all_visual = hist_bar(all_labels_stat,'办公室总数据集')

'''
词向量转化
'''
# # google news
# # GOOGLENEWS_FILE_GLOVE = 'C:\\Users\TF\Desktop\BunCode\GoogleNews-vectors-negative300.bin'
# GOOGLENEWS_FILE_GLOVE = 'E:\毕业论文\BunCode\GoogleNews-vectors-negative300.bin'
#
# def word_embedding_to_vector(path,word_set):
#     print('starting')
#     embeddings = {}
#     embeddings_process=KeyedVectors.load_word2vec_format(path, binary=True)
#
#     for word in word_set:
#         if word in embeddings_process.vocab:
#             embeddings[word]=embeddings_process.word_vec(word)
#         else:
#             pass
#     print ('ending')
#     return embeddings
#
# all_embedding = word_embedding_to_vector(GOOGLENEWS_FILE_GLOVE,all_labels)

# print('start......')
with open('all_embedding_office.pickle', 'rb') as f:
    all_embedding = pickle.load(f)

# print ('end......')

def divided (res_emb):
    # 对于可以得到词向量的元素
    mat = [] # 存词向量
    for val in res_emb.values():
        mat.append(val)
    mat_key = [] # 存key值
    for ke in res_emb.keys():
        mat_key.append(ke)
    return mat,mat_key

all_mat,all_key = divided(all_embedding)


arr = np.array(all_mat)
arr = pd.DataFrame(arr)
# 利用scipy包进行层次聚类

# lp = laplacian_kernel(arr,gamma=0.05)
rbf =  rbf_kernel(arr,gamma=0.5)
Z = linkage(rbf, method ='ward')#,metric=rbf)#('euclidean')

cluster_n = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
silhouette_avg = []
for i in cluster_n:
    cluster = sch.fcluster(Z,t=i,criterion='maxclust')
    silhouette_avg.append(davies_bouldin_score(all_mat, cluster))
# print (silhouette_avg)
'''
对聚类结果进行评估并可视化
'''
from pylab import *                                 #支持中文
def bar_vis(cluster_n,silhouette_avg):
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    # distances = [8,9,10,11,12,13,14,15,16]
    # cluster_n = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

    # dbi_list = [1622.4592050715905, 1502.149736283232, 1469.7160379962177, 1370.619858904026, 1246.7293342334567, 684.668871309834, 802.5160147681532, 1144.8552821387746, 1081.5971861525102]

    plt.plot(cluster_n, silhouette_avg, marker='o', mec='r', mfc='w',label=u'Davies-BouldinIndex曲线图')
    plt.legend()  # 让图例生效
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"聚类数") #X轴标签
    plt.ylabel("Davies Bouldin Index指数值") #Y轴标签
    plt.title("Davies Bouldin Index指数") #标题
    plt.show()


# dbi_vis=bar_vis(cluster_n,silhouette_avg)

'''
展示聚类结果
'''
cluster_result = sch.fcluster(Z,t=14,criterion='maxclust')
clustering_dict = dict(zip(all_key,cluster_result))

#构建字典
dict_keys = {}
for i in clustering_dict.values():
    dict_keys[i] = []


#将类别分门别类存入字典中
keys_label = []
cluster_label = []
for i in clustering_dict.keys():
    keys_label.append(i)
for i in clustering_dict.values():
    cluster_label.append(i)

# print (keys_label)
# print (cluster_label)

total = []
for i in range(0,len(keys_label)):
    total.append([keys_label[i],cluster_label[i]])

for i in total:
    for j in dict_keys.keys():
        if i[1] == j:
            dict_keys[j].append(i[0])

# print ('聚类字典：',dict_keys)#字典结果

values_list = []
for i in dict_keys.values():
    values_list.append(i)

# print ('values值',values_list[1])


'''
该函数主要将每个图片所打的标签转化为聚类中的每个类的类名
输入：聚类所得到的字典，需要转化的list
输出：转化结果
'''
def list_revert_into_clustering(dict_result,revert_list):
    cluster_id_list=[]
    for j in revert_list:
        temp = []
        for k in j:
            for i in dict_result.values():
                if k in i:
                    temp.append(list(dict_result.keys())[list(dict_result.values()).index(i)])
        if temp == []:
            continue
        temp = set(temp)
        cluster_id_list.append(list(temp))
    return cluster_id_list



coshared_cluster_list_result = list_revert_into_clustering(dict_keys,coshared_ini)
open_cluster_list_result = list_revert_into_clustering(dict_keys,open_ini)
all_result = coshared_cluster_list_result + open_cluster_list_result



'''
进行频繁项集挖掘
'''

def fre_itemsets(a,b,c,delta):# co shared 频繁项集其中delta表示阈值
    co_length= len(a)
    co_itemsets = frequent_itemsets(a, delta)
    co_itemlist=list(co_itemsets)
    co_frequentItem = [(item[0],item[1]/co_length) for item in co_itemlist]
    # print (len (co_frequentItem))

    # open place 频繁项集
    open_length= len(b)
    open_itemsets = frequent_itemsets(b, delta)
    open_itemlist=list(open_itemsets)
    open_frequentItem = [(item[0],item[1]/open_length) for item in open_itemlist]
    # print (len (open_frequentItem))

    # open place 和 co shared 频繁项集
    length= len(c)
    itemsets = frequent_itemsets(c, delta)
    itemlist=list(itemsets)
    frequentItem = [(item[0],item[1]/length) for item in itemlist]
    # print (len (frequentItem))
    return co_frequentItem,open_frequentItem,frequentItem


coshared_fre_result, open_fre_result, all_fre_result = fre_itemsets(coshared_cluster_list_result,open_cluster_list_result,all_result,0.001)


#根据support值排序
def sortbysup(result):
    n = len(result)
    for i in range(n-1):
        for j in range(n-i-1):
            if result[j][1]<result[j+1][1]:
                result[j],result[j+1] = result[j+1],result[j]
#     print ("result = ",result)
    return result

def sortbysup_1(result):
    n = len(result)
    for i in range(n-1):
        for j in range(n-i-1):
            if result[j][3]<result[j+1][3]:
                result[j],result[j+1] = result[j+1],result[j]
#     print ("result = ",result)
    return result

# 按照频繁项集长度排序
def sortbylen(result):
    n = len(result)
    for i in range(n-1):
        for j in range(n-i-1):
            if len(result[j][0])>len(result[j+1][0]):
                result[j],result[j+1] = result[j+1],result[j]
#     print ("result = ",result)
    return result



co_fre_sort = sortbysup(coshared_fre_result)
open_fre_sort = sortbysup(open_fre_result)
all_fre_sort = sortbysup(all_fre_result)

co_processing = []
for i in range(0,len(co_fre_sort)):
    co_processing.append([co_fre_sort[i][0],round(co_fre_sort[i][1],5)])

open_processing = []
for i in range(0,len(open_fre_sort)):
    open_processing.append([open_fre_sort[i][0],round(open_fre_sort[i][1],5)])

# co_support = sortbysup(quchong(fre_item(preprocessing_A)))
# open_support = sortbysup(quchong(fre_item(preprocessing_B)))
# support = sortbysup(quchong(fre_item(preprocessing_A+preprocessing_B)))
co_support=co_fre_sort
open_support=open_fre_sort
support = all_fre_sort


fre_co = []
for i in co_support:
    fre_co.append(i[0])
# print (fre_co)

# print ("======================================================================")
fre_open = []
for i in open_support:
    fre_open.append(i[0])

# 找出两边都包含的itemsets
ppp = [l for l in fre_co if l in fre_open]

a = []
for i in ppp:
    for j in co_support:
        if i == j[0]:
            a.append([i,j[1]])

b = []
for i in ppp:
    for j in open_support:
        if i == j[0]:
            b.append([i,j[1]])

co_contrast_ratio = []
for i in range(0,len(ppp)):
    co_contrast_ratio.append([ppp[i],round(a[i][1],5),round(b[i][1],5),round(a[i][1]/b[i][1],5)])

# 第一个表示a里面的support值 (coshared)，第二个表示b里面的support值（open plan office），第三个表示a/b的contrast值。
# print ("排序1：  ",sortbysup_1(co_contrast_ratio))

open_contrast_ratio = []
for i in range(0,len(ppp)):
    open_contrast_ratio.append([ppp[i],round(b[i][1],5),round(a[i][1],5),round(b[i][1]/a[i][1],5)])#表示b/a的congtrast值
# print ("排序2：   ",sortbysup_1(open_contrast_ratio))

#将两个对比组整合到一起
list_contrast_ratio = []
for i in range(0,len(ppp)):
    list_contrast_ratio.append([ppp[i],round(a[i][1],5),round(b[i][1],5),
                                round(a[i][1]/b[i][1],5),round(b[i][1]/a[i][1],5)])

show_list = sortbysup_1(list_contrast_ratio)
# print (show_list)

contrast_diff = []
for i in range(0,len(ppp)):
    contrast_diff.append([ppp[i],abs(round(a[i][1]-b[i][1],16))])
# print ("contrast different = ", contrast_diff)



'''
第二个案例
'''

def second_case():
    return 0