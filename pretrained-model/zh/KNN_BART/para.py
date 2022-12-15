import torch

path = "/home/users/jiangjin/jiangjin_bupt/ASR_CORRECTION/Context_Correction/context_seq2seq/pretrained-model/zh/KNN_BART/pytorch_model.bin"
paras = torch.load(path)


list_new = ['decoder.layers.3.knn_attn.q_proj.bias', 'decoder.layers.3.knn_attn.k_proj.weight', 'decoder.layers.3.knn_attn.v_proj.bias', 'decoder.layers.3.knn_attn.v_proj.weight', 'decoder.layers.3.knn_attn.k_proj.bias', 'decoder.layers.3.knn_attn.out_proj.weight', 'decoder.layers.3.knn_attn.q_proj.weight', 'decoder.layers.3.knn_attn.out_proj.bias']

list_need = [item.replace('knn_attn','self_attn') for item in list_new]

for i in range(len(list_need)):
    item_new = list_new[i]
    item_need = list_need[i]
    paras[item_new] = paras[item_need]

torch.save(paras, path)
a = 1