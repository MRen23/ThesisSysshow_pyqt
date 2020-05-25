__author__ = 'TF'
# -*- coding:utf-8-*-
#　导入必要的包
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
import pickle
from sklearn.metrics.pairwise import rbf_kernel,laplacian_kernel
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



# 读数据face
def loadjson_face(path):
    with open (path,'rb') as json_data:
        data = json.load(json_data)
    data_with_face = []
    for i in data:
        if len(i)!=1:
            data_with_face.append(i)
    rate = len(data_with_face)/len(data)
#     print ("识别出来脸总共：",len(data_with_face))
#     print ("总数据：",len(data))
    return data,data_with_face,rate




# 读数据color
def loadjson_color(path):
    with open (path,'rb') as json_data:
        data = json.load(json_data)
    labels = []
    # #打印所有的了labels
    for i in data:
        labels.append(i[:-1])
    temp = []
    for i in labels:
        temp_t = []
        for j in i:
            temp_t.append(j[:4])
        temp.append(temp_t)

    urls = []
    for i in data:
        urls.append(i[-1])

    datasets = []
    for i in range(0,len(temp)):
        datasets.append(list(temp[i])+list(urls[i].values()))

    return datasets

# # # 读label
# # print('====================================官方数据集label识别结果=======================================')
# official_labelset_five,official_score_five, official_urls_five = loadjson_label('dataset\official\google\label\\five.json')
# # print('五星级酒店图片总共:',len(official_labelset_five))
# official_labelset_four,official_score_four, official_urls_four = loadjson_label('dataset\official\google\label\\four.json')
# # print ('四星级酒店图片总共:',len(official_labelset_four))
# official_labelset_three,official_score_three, official_urls_three = loadjson_label('dataset\official\google\label\\three.json')
# # print ('三星级酒店图片总共:',len(official_labelset_three))
# official_labelset_two,official_score_two, official_urls_two = loadjson_label('dataset\official\google\label\\two.json')
# # print ('二星级酒店图片总共:',len(official_labelset_two))
# # print('总数据量：',len(official_labelset_five)+len(official_labelset_four)+len(official_labelset_three)+len(official_labelset_two))
#
# # # 读color
# # print('=====================================官方数据集color识别结果========================================')
# official_colorset_five = loadjson_color('dataset\official\google\color\\five.json')
# # print('五星级酒店可识别颜色图片总数：',len(official_colorset_five))
# official_colorset_four = loadjson_color('dataset\official\google\color\\four.json')
# # print('四星级酒店可识别颜色图片总数：',len(official_colorset_four))
# official_colorset_three= loadjson_color('dataset\official\google\color\\three.json')
# # print('三星级酒店可识别颜色图片总数：',len(official_colorset_three))
# official_colorset_two= loadjson_color('dataset\official\google\color\\two.json')
# # print('二星级酒店可识别颜色图片总数：',len(official_colorset_two))
# # print ('总数据量：',len(official_colorset_five)+len(official_colorset_four)+len(official_colorset_three)+len(official_colorset_two))
#
# # # 读face
# # print ('======================================官方数据集face识别结果=======================================')
# # #其中faceset_five表示五星级酒店总数据，face_five表示识别出来脸的图片集，rate_five表示评分
# official_faceset_five,official_face_five,official_rate_five = loadjson_face('dataset\official\google\\face\\five.json')
# # print('五星级酒店识别出来脸的图片：',len(official_face_five))
# official_faceset_four,official_face_four,official_rate_four = loadjson_face('dataset\official\google\\face\\four.json')
# # print('四星级酒店识别出来脸的图片：',len(official_face_four))
# official_faceset_three,official_face_three,official_rate_three = loadjson_face('dataset\official\google\\face\\three.json')
# # print('三星级酒店识别出来脸的图片：',len(official_face_three))
# official_faceset_two,official_face_two,official_rate_two = loadjson_face('dataset\official\google\\face\\two.json')
# # print('二星级酒店识别出来脸的图片：',len(official_face_two))
# # print ('总共识别出来脸的图片数据量：',len(official_face_five)+len(official_face_four)+len(official_face_three)+len(official_face_two))
# #
#
#
#
# # 读label
# # print('====================================游客数据集label识别结果=======================================')
# traveler_labelset_five,traveler_score_five, traveler_urls_five = loadjson_label('dataset\\travelers\google\label\\five.json')
# # print('五星级酒店图片总共:',len(traveler_labelset_five))
# traveler_labelset_four,traveler_score_four, traveler_urls_four = loadjson_label('dataset\\travelers\google\label\\four.json')
# # print ('四星级酒店图片总共:',len(traveler_labelset_four))
# traveler_labelset_three,traveler_score_three, traveler_urls_three = loadjson_label('dataset\\travelers\google\label\\three.json')
# # print ('三星级酒店图片总共:',len(traveler_labelset_three))
# traveler_labelset_two,traveler_score_two, traveler_urls_two = loadjson_label('dataset\\travelers\google\label\\two.json')
# # print ('二星级酒店图片总共:',len(traveler_labelset_two))
# # print('总数据量：',len(traveler_labelset_five)+len(traveler_labelset_four)+len(traveler_labelset_three)+len(traveler_labelset_two))
#
# # 读color
# # print('=====================================游客数据集color识别结果========================================')
# traveler_colorset_five = loadjson_color('dataset\\travelers\google\color\\five.json')
# # print('五星级酒店可识别颜色图片总数：',len(traveler_colorset_five))
# traveler_colorset_four = loadjson_color('dataset\\travelers\google\color\\four.json')
# # print('四星级酒店可识别颜色图片总数：',len(traveler_colorset_four))
# traveler_colorset_three= loadjson_color('dataset\\travelers\google\color\\three.json')
# # print('三星级酒店可识别颜色图片总数：',len(traveler_colorset_three))
# traveler_colorset_two= loadjson_color('dataset\\travelers\google\color\\two.json')
# # print('二星级酒店可识别颜色图片总数：',len(traveler_colorset_two))
# # print ('总数据量：',len(traveler_colorset_five)+len(traveler_colorset_four)+len(traveler_colorset_three)+len(traveler_colorset_two))
#
# # 读face
# # print ('======================================游客数据集face识别结果=======================================')
# #其中faceset_five表示五星级酒店总数据，face_five表示识别出来脸的图片集，rate_five表示评分
# traveler_faceset_five,traveler_face_five,traveler_rate_five = loadjson_face('dataset\\travelers\google\\face\\five.json')
# # print('五星级酒店识别出来脸的图片：',len(traveler_face_five))
# traveler_faceset_four,traveler_face_four,traveler_rate_four = loadjson_face('dataset\\travelers\google\\face\\four.json')
# # print('四星级酒店识别出来脸的图片：',len(traveler_face_four))
# traveler_faceset_three,traveler_face_three,traveler_rate_three = loadjson_face('dataset\\travelers\google\\face\\three.json')
# # print('三星级酒店识别出来脸的图片：',len(traveler_face_three))
# traveler_faceset_two,traveler_face_two,traveler_rate_two = loadjson_face('dataset\\travelers\google\\face\\two.json')
# # print('二星级酒店识别出来脸的图片：',len(traveler_face_two))
# # print ('总共识别出来脸的图片数据量：',len(traveler_face_five)+len(traveler_face_four)+len(traveler_face_three)+len(traveler_face_two))
#
#
#


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



# #　对数据集进行预处理
# # print ('=======================================官方数据集预处理===============================')
# official_five_ini = preprocessing(official_labelset_five,official_urls_five)
# # print ("五星级酒店官方图片数据集个数 = ", len (official_five_ini))
# official_four_ini = preprocessing(official_labelset_four,official_urls_four)
# # print ("四星级酒店官方图片数据集个数 = ", len (official_four_ini))
# official_three_ini = preprocessing(official_labelset_three,official_urls_three)
# # print ("三星级酒店官方图片数据集个数 = ", len (official_three_ini))
# official_two_ini = preprocessing(official_labelset_two,official_urls_two)
# # print ("二星级酒店官方图片数据集个数 = ", len (official_two_ini))
#
# # print('========================================游客数据集预处理===============================')
# traveler_five_ini = preprocessing(traveler_labelset_five,traveler_urls_five)
# # print ("五星级酒店游客图片数据集个数 = ", len (traveler_five_ini))
# traveler_four_ini = preprocessing(traveler_labelset_four,traveler_urls_four)
# # print ("四星级酒店游客图片数据集个数 = ", len (traveler_four_ini))
# traveler_three_ini = preprocessing(traveler_labelset_three,traveler_urls_three)
# # print ("三星级酒店游客图片数据集个数 = ", len (traveler_three_ini))
# traveler_two_ini = preprocessing(traveler_labelset_two,traveler_urls_two)
# # print ("二星级酒店游客图片数据集个数 = ", len (traveler_two_ini))
#
#
#
# '''所有标签统计'''
#
# all_labels_set = official_five_ini + official_four_ini + official_three_ini + official_two_ini + traveler_five_ini + traveler_four_ini + traveler_three_ini + traveler_two_ini
# official_labels_set = official_five_ini + official_four_ini + official_three_ini + official_two_ini
# traveler_labels_set = traveler_five_ini + traveler_four_ini + traveler_three_ini + traveler_two_ini
#
#
#
# '''
# 将整个数据集分为四个部分：官方图片4,5星级，官方图片2,3星级。旅游者图片4,5星级，旅游者图片2,3星级。
# '''
# official_45_ini = official_five_ini + official_four_ini
# official_23_ini = official_three_ini + official_two_ini
#
# traveler_45_ini = traveler_five_ini + traveler_four_ini
# traveler_23_ini = traveler_three_ini + traveler_two_ini




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





# #official_label_all_five表示五星级酒店出现的标签，official_stat_five表示五星级酒店每个词以及这个词出现的频率
# # print('===============================官方数据集label统计=======================================')
# official_label_all_five, official_stat_five = label_stat(official_five_ini)
# # print ("五星级酒店官方数据集label个数 = ",len(official_stat_five))
# official_label_all_four,official_stat_four = label_stat(official_four_ini)
# # print ("四星级酒店官方数据集label个数 = ",len(official_stat_four))
# official_label_all_three,official_stat_three = label_stat(official_three_ini)
# # print ("三星级酒店官方数据集label个数 = ",len(official_stat_three))
# official_label_all_two,official_stat_two = label_stat(official_two_ini)
# # print ("二星级酒店官方数据集label个数 = ",len(official_stat_two))
#
# # print('==============================游客数据集label统计=======================================')
# traveler_label_all_five, traveler_stat_five = label_stat(traveler_five_ini)
# # print ("五星级酒店游客数据集label个数 = ",len(traveler_stat_five))
# traveler_label_all_four,traveler_stat_four = label_stat(traveler_four_ini)
# # print ("四星级酒店游客数据集label个数 = ",len(traveler_stat_four))
# traveler_label_all_three,traveler_stat_three = label_stat(traveler_three_ini)
# # print ("三星级酒店游客数据集label个数 = ",len(traveler_stat_three))
# traveler_label_all_two,traveler_stat_two = label_stat(traveler_two_ini)
# # print ("二星级酒店游客数据集label个数 = ",len(traveler_stat_two))
# #
# #
# # print ('===============================四部分数据集统计==========================================')
# official_label_all_45, official_stat_45 = label_stat(official_45_ini)
# # print ('官方4,5星级酒店图片数据集label个数 = ', len(official_stat_45))
# official_label_all_23, official_stat_23 = label_stat(official_23_ini)
# # print ('官方2,3星级酒店图片数据集label个数 = ', len(official_stat_23))
# traveler_label_all_45, traveler_stat_45 = label_stat(traveler_45_ini)
# # print ('旅游者4,5星级酒店图片数据集label个数 = ', len(traveler_stat_45))
# traveler_label_all_23, traveler_stat_23 = label_stat(traveler_23_ini)
# # print ('旅游者2,3星级酒店图片数据集label个数 = ', len(traveler_stat_23))
#
#
# # print ('================================所有标签统计============================================')
# official_all_labels, official_stat_all = label_stat(official_labels_set)
# # print ('官方数据集label个数 = ', len(official_stat_all))
# traveler_all_labels, traveler_stat_all = label_stat(traveler_labels_set)
# # print ('旅游者数据集label个数 = ', len(traveler_stat_all))
# all_labels,all_labels_stat = label_stat(all_labels_set)
# # print ('所有label个数 = ', len(all_labels_stat))




# with open('official_stat_45_hotel.pickle', 'wb') as f:
#     pickle.dump(official_stat_45, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('official_stat_23_hotel.pickle', 'wb') as f:
#     pickle.dump(official_stat_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('traveler_stat_45_hotel.pickle', 'wb') as f:
#     pickle.dump(traveler_stat_45, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('traveler_stat_23_hotel.pickle', 'wb') as f:
#     pickle.dump(traveler_stat_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open('official_stat_all_hotel.pickle', 'wb') as f:
#     pickle.dump(official_stat_all, f, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open('traveler_stat_all_hotel.pickle', 'wb') as f:
#     pickle.dump(traveler_stat_all, f, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open('all_labels_stat_hotel.pickle', 'wb') as f:
#     pickle.dump(all_labels_stat, f, protocol=pickle.HIGHEST_PROTOCOL)





with open('official_stat_45_hotel.pickle', 'rb') as f:
    official_stat_45 = pickle.load(f)

with open('official_stat_23_hotel.pickle', 'rb') as f:
    official_stat_23 = pickle.load(f)

with open('traveler_stat_45_hotel.pickle', 'rb') as f:
    traveler_stat_45 = pickle.load(f)


with open('traveler_stat_23_hotel.pickle', 'rb') as f:
    traveler_stat_23 = pickle.load(f)

with open('official_stat_all_hotel.pickle', 'rb') as f:
    official_stat_all = pickle.load(f)


with open('traveler_stat_all_hotel.pickle', 'rb') as f:
    traveler_stat_all = pickle.load(f)


with open('all_labels_stat_hotel.pickle', 'rb') as f:
    all_labels_stat = pickle.load(f)


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


# hist_bar(official_stat_45,'官方图像数据集A')
# hist_bar(official_stat_23,'官方图像数据集B')
# hist_bar(traveler_stat_45,'旅游图像者数据集A')
# hist_bar(traveler_stat_23,'旅游者图像数据集B')
#
# hist_bar(official_stat_all,'官方图像数据集')
# hist_bar(traveler_stat_all,'旅游者图像数据集')
# hist_bar(all_labels_stat,'所有图像数据集')



# print('start......')
with open('all_embedding_hotel.pickle', 'rb') as f:
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
rbf =  rbf_kernel(arr,gamma=0.5)  #高斯核
Z = linkage(rbf, method ='ward')#,metric=rbf)#('euclidean')


# cluster = sch.fcluster(Z,t=5,criterion='maxclust')
# print (len(cluster))
# print (len(all_key))

# cluster_n = list(range(20))[2:]
cluster_n = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
silhouette_avg = []
for i in cluster_n:
    cluster = sch.fcluster(Z,t=i,criterion='maxclust')
    silhouette_avg.append(davies_bouldin_score(all_mat, cluster))
# print (silhouette_avg)




import matplotlib.pyplot as plt
from pylab import *

def bar_vis(cluster_n,silhouette_avg):#支持中文
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    # distances = [8,9,10,11,12,13,14,15,16]

    # dbi_list = [1622.4592050715905, 1502.149736283232, 1469.7160379962177, 1370.619858904026, 1246.7293342334567, 684.668871309834, 802.5160147681532, 1144.8552821387746, 1081.5971861525102]

    plt.plot(cluster_n, silhouette_avg, marker='o', mec='r', mfc='w',label=u'Davies-BouldinIndex曲线图')
    plt.legend()  # 让图例生效
    # plt.xticks(distance, names, rotation=45)
    # plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"聚类数") #X轴标签
    plt.ylabel("Davies Bouldin Index指数值") #Y轴标签
    plt.title("Davies Bouldin Index指数") #标题
    # plt.savefig(r'./导出的图片/DBI.pdf',dpi=300,bbox_inches = 'tight')
    # plt.savefig(r'./导出的图片/DBI.png',dpi=300,bbox_inches = 'tight')

    plt.show()




#聚类结果
cluster_result = sch.fcluster(Z,t=24,criterion='maxclust')
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

total = []
for i in range(0,len(keys_label)):
    total.append([keys_label[i],cluster_label[i]])

for i in total:
    for j in dict_keys.keys():
        if i[1] == j:
            dict_keys[j].append(i[0])
#
#
values_list = []
for i in dict_keys.values():
    values_list.append(i)
#



# '''
# 输入：原数据集list，经过聚类之后的字典
# 输出：通过处理之后，将原数据集转化为聚类之后的数据集。该函数结果返回将聚类标签替换为原数据集中的值。
# '''
def transform_into_datasets(dataset_list,clustering_result_dict):
    key_list = list(clustering_result_dict.keys())
    values_list = list(clustering_result_dict.values())
    clustering_in_dataset = []
    for i in dataset_list:
        tmp = []
        for j in i:
            for k in range(0,len(values_list)):
                if j in values_list[k]:
                    tmp.append(key_list[k])
        clustering_in_dataset.append(tmp)
    delete_redis = []
    for i in clustering_in_dataset:
        i = set(i)
        i = list(i)
        delete_redis.append(i)
    return delete_redis

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


# cluster_list_official_45 = list_revert_into_clustering(dict_keys,official_45_ini)
# print (cluster_list_official_45)
# cluster_list_official_23 = list_revert_into_clustering(dict_keys,official_23_ini)
# cluster_list_traveler_45 = list_revert_into_clustering(dict_keys,traveler_45_ini)
# cluster_list_traveler_23 = list_revert_into_clustering(dict_keys,traveler_23_ini)
# cluster_list_all_45 = list_revert_into_clustering(dict_keys,all_labels_set)
#
# # 将所有数据集进行聚类标签的对应
# clustering_result_list_official_45 = transform_into_datasets(official_45_ini,dict_keys)
# # print (clustering_result_list_official_45)
# clustering_result_list_official_23 = transform_into_datasets(official_23_ini,dict_keys)
# clustering_result_list_traveler_45 = transform_into_datasets(traveler_45_ini,dict_keys)
# clustering_result_list_traveler_23 = transform_into_datasets(traveler_23_ini,dict_keys)
# clustering_result_list_official_all = transform_into_datasets(official_labels_set,dict_keys)
# clustering_result_list_traveler_all = transform_into_datasets(traveler_labels_set,dict_keys)
# clustering_result_list_all = transform_into_datasets(all_labels_set,dict_keys)
#
#
#
# with open('clustering_result_list_official_45_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_official_45, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('clustering_result_list_official_23_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_official_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('clustering_result_list_traveler_45_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_traveler_45, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
#
# with open('clustering_result_list_traveler_23_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_traveler_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
#
# with open('clustering_result_list_official_all_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_official_all, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
#
# with open('clustering_result_list_traveler_all_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_traveler_all, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('clustering_result_list_all_hotel.pickle', 'wb') as f:
#     pickle.dump(clustering_result_list_all, f, protocol=pickle.HIGHEST_PROTOCOL)



with open('clustering_result_list_official_45_hotel.pickle', 'rb') as f:
    clustering_result_list_official_45 = pickle.load(f)

with open('clustering_result_list_official_23_hotel.pickle', 'rb') as f:
    clustering_result_list_official_23 = pickle.load(f)

with open('clustering_result_list_traveler_45_hotel.pickle', 'rb') as f:
    clustering_result_list_traveler_45 = pickle.load(f)

with open('clustering_result_list_traveler_23_hotel.pickle', 'rb') as f:
    clustering_result_list_traveler_23 = pickle.load(f)

with open('clustering_result_list_official_all_hotel.pickle', 'rb') as f:
    clustering_result_list_official_all = pickle.load(f)

with open('clustering_result_list_traveler_all_hotel.pickle', 'rb') as f:
    clustering_result_list_traveler_all = pickle.load(f)

with open('clustering_result_list_all_hotel.pickle', 'rb') as f:
    clustering_result_list_all = pickle.load(f)


# # 对聚类之后的标签进行统计以方便后面的对比
# label_stat_official_45,label_fre_official_45 = label_stat(clustering_result_list_official_45)
# label_stat_official_23,label_fre_official_23 = label_stat(clustering_result_list_official_23)
# label_stat_traveler_45,label_fre_traveler_45 = label_stat(clustering_result_list_traveler_45)
# label_stat_traveler_23,label_fre_traveler_23 = label_stat(clustering_result_list_traveler_23)
# label_stat_official_all,label_fre_official_all = label_stat(clustering_result_list_traveler_45)
# label_stat_traveler_all,label_fre_traveler_all = label_stat(clustering_result_list_traveler_23)
# label_stat_all,label_fre_all = label_stat(clustering_result_list_all)





# '''
# 频繁项集挖掘
# '''
# 频繁项集
def fre_item(itemsets):
    lenth = len(itemsets)
    itemsets = frequent_itemsets(itemsets,0.00015)
    itemlist = list(itemsets)
    frequentItem = [(item[0],item[1]/lenth) for item in itemlist]
    return frequentItem
#
#
# frequent_result_official_45 = fre_item(clustering_result_list_official_45)
# frequent_result_official_23 = fre_item(clustering_result_list_official_23)
# frequent_result_traveler_45 = fre_item(clustering_result_list_traveler_45)
# frequent_result_traveler_23 = fre_item(clustering_result_list_traveler_23)
# frequent_result_official_all = fre_item(clustering_result_list_official_all)
# frequent_result_traveler_all = fre_item(clustering_result_list_traveler_all)
# frequent_result_all = fre_item(clustering_result_list_all)  # 得到二维数组


# with open('frequent_result_official_45_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_official_45, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('frequent_result_official_23_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_official_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('frequent_result_traveler_45_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_traveler_45, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('frequent_result_traveler_23_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_traveler_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('frequent_result_official_all_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_official_all, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
# with open('frequent_result_traveler_all_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_traveler_all, f, protocol=pickle.HIGHEST_PROTOCOL)
#
# with open('frequent_result_all_hotel.pickle', 'wb') as f:
#     pickle.dump(frequent_result_all, f, protocol=pickle.HIGHEST_PROTOCOL)



with open('frequent_result_official_45_hotel.pickle', 'rb') as f:
    frequent_result_official_45 = pickle.load(f)

with open('frequent_result_official_23_hotel.pickle', 'rb') as f:
    frequent_result_official_23 = pickle.load(f)

with open('frequent_result_traveler_45_hotel.pickle', 'rb') as f:
    frequent_result_traveler_45 = pickle.load(f)

with open('frequent_result_traveler_23_hotel.pickle', 'rb') as f:
    frequent_result_traveler_23 = pickle.load(f)

with open('frequent_result_official_all_hotel.pickle', 'rb') as f:
    frequent_result_official_all = pickle.load(f)

with open('frequent_result_traveler_all_hotel.pickle', 'rb') as f:
    frequent_result_traveler_all = pickle.load(f)

with open('frequent_result_all_hotel.pickle', 'rb') as f:
    frequent_result_all = pickle.load(f)



# 去掉重复包含项
def quchong(frequentItem):
    result=[]   # 存放官方图片的频繁项集
    for i in range(0,len(frequentItem)):
        for j in range(i,len(frequentItem)):
            if (set(frequentItem[i][0]).issubset(frequentItem[j][0])== True):
                if (frequentItem[i][1] == frequentItem[j][1]):
                    if ((len(frequentItem[i][0])) < (len(frequentItem[j][0]))):
                        frequentItem[i] = "redundancy"
    for i in range(0,len(frequentItem)):
        if frequentItem[i] != "redundancy":
            result.append(frequentItem[i])
#     print (result)
    return result

# 按照频繁项集support排序[label:support]按照support值排序
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


gfA_fre_sort = sortbysup(frequent_result_official_45)
gfB_fre_sort = sortbysup(frequent_result_official_23)
lyA_fre_sort = sortbysup(frequent_result_traveler_45)
lyB_fre_sort = sortbysup(frequent_result_traveler_23)
all_fre_sort = sortbysup(frequent_result_all)


gfA_processing = []
for i in range(0,len(gfA_fre_sort)):
    gfA_processing.append([gfA_fre_sort[i][0],round(gfA_fre_sort[i][1],5)])

gfB_processing = []
for i in range(0,len(gfB_fre_sort)):
    gfB_processing.append([gfB_fre_sort[i][0],round(gfB_fre_sort[i][1],5)])

lyA_processing = []
for i in range(0,len(lyA_fre_sort)):
    lyA_processing.append([lyA_fre_sort[i][0],round(lyA_fre_sort[i][1],5)])

lyB_processing = []
for i in range(0,len(lyB_fre_sort)):
    lyB_processing.append([lyB_fre_sort[i][0],round(lyB_fre_sort[i][1],5)])

all_processing = []
for i in range(0,len(all_fre_sort)):
    all_processing.append([all_fre_sort[i][0],round(all_fre_sort[i][1],5)])


#
# def sortbysup_1(result):
#     n = len(result)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if result[j][3]<result[j+1][3]:
#                 result[j],result[j+1] = result[j+1],result[j]
# #     print ("result = ",result)
#     return result



def contrast_result(A,B):
    co_support = sortbysup(quchong(fre_item(A)))
    open_support = sortbysup(quchong(fre_item(B)))
    support = sortbysup(quchong(fre_item(A+B)))

    fre_co = []
    for i in co_support:
        fre_co.append(i[0])
    # print (fre_co)

    # print ("======================================================================")
    fre_open = []
    for i in open_support:
        fre_open.append(i[0])
    # print (fre_open)

    # 找出两边都包含的itemsets
    ppp = [l for l in fre_co if l in fre_open]
    # print (ppp)

    a = []
    for i in ppp:
        for j in co_support:
            if i == j[0]:
                a.append([i,j[1]])
    # print (a)

    b = []
    for i in ppp:
        for j in open_support:
            if i == j[0]:
                b.append([i,j[1]])
    # print (b)

    co_contrast_ratio = []
    for i in range(0,len(ppp)):
        co_contrast_ratio.append([ppp[i],round(a[i][1],5),round(b[i][1],5),round(a[i][1]/b[i][1],5),round(b[i][1]/a[i][1],5)])
    # print ("contrast ratio A > B = ",co_contrast_ratio)


    show_list = sortbysup_1(co_contrast_ratio)

    return show_list

#
# # # print("官方总数据集 vs 旅游者总数据集")
# contrast_official_traveler = contrast_result(clustering_result_list_official_all,clustering_result_list_traveler_all)
# # print(len(contrast_official_traveler))
#
# # print("官方数据集A vs 官方数据集B")
# contrast_official_45_vs_23 = contrast_result(clustering_result_list_official_45,clustering_result_list_official_23)
# # print (len(contrast_official_45_vs_23))
#
# # # print("旅游者数据集A vs 旅游者数据集B")
# contrast_traveler_45_vs_23 = contrast_result(clustering_result_list_traveler_45,clustering_result_list_traveler_23)
# # print (len(contrast_traveler_45_vs_23))


# with open('contrast_official_traveler_hotel.pickle', 'wb') as f:
#     pickle.dump(contrast_official_traveler, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
#
# with open('contrast_official_45_vs_23_hotel.pickle', 'wb') as f:
#     pickle.dump(contrast_official_45_vs_23, f, protocol=pickle.HIGHEST_PROTOCOL)
#
#
#
# with open('contrast_traveler_45_vs_23_hotel.pickle', 'wb') as f:
#     pickle.dump(contrast_traveler_45_vs_23, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('contrast_official_traveler_hotel.pickle', 'rb') as f:
    contrast_official_traveler = pickle.load(f)


with open('contrast_official_45_vs_23_hotel.pickle', 'rb') as f:
    contrast_official_45_vs_23 = pickle.load(f)


with open('contrast_traveler_45_vs_23_hotel.pickle', 'rb') as f:
    contrast_traveler_45_vs_23 = pickle.load(f)
#


