# -*- encoding: utf-8 -*-
'''
Filename         :acc_recall_f1.py
Description      :
Time             :2025/03/28 12:25:03
Author           :CIAN
Email            :cian@foxmail.com
Version          :1.0
'''
import json
from loguru import logger
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


data_dir = "your/file/path"

data = json.load(open(data_dir, 'r', encoding='utf-8'))
standard_list = []
candidate_list = []
for d in data:
    standard_list.append(d['syndrome_standard'])
    candidate_list.append(d['syndrome_output'])

acc = accuracy_score(standard_list, candidate_list)
precision = precision_score(standard_list, candidate_list, average='macro')
recall = recall_score(standard_list, candidate_list, average='macro')
f1 = f1_score(standard_list, candidate_list, average='macro')
logger.info(f"acc: {acc:.3f}, precision: {precision:.3f}, recall: {recall:.3f}, f1: {f1:.3f}")