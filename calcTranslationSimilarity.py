import sys
import csv
import MeCab
import numpy as np


class CalcSim_MeCab:

    def __init__(self):
        pass

    def cos_sim(self, x, y):
        val = np.sqrt(np.sum(x**2)) * np.sqrt(np.sum(y**2))
        return np.dot(x, y) / val if val != 0 else 0

    def WordFrequencyCount(self, word, wordFreq_dict):
        if word in wordFreq_dict:
            wordFreq_dict[word] +=1
        else:
            wordFreq_dict.setdefault(word, 1)
        return wordFreq_dict

    """
    @fn calcTranslationSimilarity_normal()
    @brief calculate a similarity between two sentences
    @param original_translation first sentence for reference (string)
    @param other_translations second, third,... sentences for similarity calculation (string array)
    @retval similarity array (float array)
    @details "Wakati"で分けた形態素をそのまま使用して類似度を計算
    @warning 
    @note https://www.creativevillage.ne.jp/84849
    """
    def calcTranslationSimilarity_normal(self, original_translation, other_translations):

        sentence_list = []
        sentence_wakati_list = []

        # words separation with "wakati"
        # wakati = MeCab.Tagger('-Owakati')
        wakati = MeCab.Tagger(r'-O wakati -d D:\\MeCab\\dic\\ipadic')
        sentence_list.append(original_translation)
        for i in other_translations:
            if i != "":
                sentence_list.append(i)
        sentence_wakati_list = [wakati.parse(i).split() for i in sentence_list]
        # print(sentence_wakati_list)

        # create Bag of Words table
        word_to_index = {}
        index_to_word = {}
        for s in sentence_wakati_list:
            for w in s:
                if w not in word_to_index:
                        new_index = len(word_to_index)
                        word_to_index[w] = new_index
                        index_to_word[new_index] = w

        corpus = np.zeros((len(sentence_wakati_list), len(word_to_index)))

        for i, s in enumerate(sentence_wakati_list):
            for w in s:
                corpus[i, word_to_index[w]] = 1

        sentence_wakati_list_2 = sentence_wakati_list
        sentence_wakati_list_2.pop(0)

        # calculate sentence similarity
        similarity_score = []
        for i, v in enumerate(sentence_wakati_list_2):
            per = self.cos_sim(corpus[0], corpus[i + 1])
            print(str(v) + ": " + str(per))
            similarity_score.append(per)

        return similarity_score

    """
    @fn calcTranslationSimilarity_important()
    @brief calculate a similarity between two sentences
    @param original_translation first sentence for reference (string)
    @param other_translations second, third,... sentences for similarity calculation (string array)
    @retval similarity array (float array)
    @details "名詞"や"動詞"などの重要な形態素のみを抽出して類似度を計算
    @warning 
    @note https://your-3d.com/pytho-mecab-frequencywords/
    """
    def calcTranslationSimilarity_important(self, original_translation, other_translations):

        sentence_list = []
        sentence_wakati_list = []

        wakati = MeCab.Tagger(r'-O chasen -d D:\\MeCab\\dic\\ipadic')
        sentence_list.append(original_translation)
        for i in other_translations:
            if i != "":
                sentence_list.append(i)
        
        wordFreq_dict = {}
        for i in sentence_list:
            node = wakati.parseToNode(i)
            temp_list = []
            while node:
                if node.feature.split(",")[0] == "名詞" or node.feature.split(",")[0] == "動詞" or node.feature.split(",")[0] == "形容詞" or node.feature.split(",")[0] == "形容動詞":
                    word = node.surface
                    # print(word)
                    self.WordFrequencyCount(word, wordFreq_dict)
                    temp_list.append(word)
                node = node.next
            sentence_wakati_list.append(temp_list)
        
        # print(sentence_wakati_list)

        # create Bag of Words table
        word_to_index = {}
        index_to_word = {}
        for s in sentence_wakati_list:
            for w in s:
                   if w not in word_to_index:
                        new_index = len(word_to_index)
                        word_to_index[w] = new_index
                        index_to_word[new_index] = w

        corpus = np.zeros((len(sentence_wakati_list), len(word_to_index)))

        for i, s in enumerate(sentence_wakati_list):
            for w in s:
                corpus[i, word_to_index[w]] = 1

        sentence_wakati_list_2 = sentence_wakati_list
        sentence_wakati_list_2.pop(0)

        similarity_score = []
        for i, v in enumerate(sentence_wakati_list_2):
            per = self.cos_sim(corpus[0], corpus[i + 1])
            print(str(v) + ": " + str(per))
            similarity_score.append(per)

        return similarity_score


if __name__ == '__main__':

    args = sys.argv
 
    # 引数チェック
    if len(args) != 3:
        print('使い方が間違っています。引数の個数: ' + str(len(args)))
        print('usage: python <*.py> <input_filename> <output_filename>')
        print('yours: ')  
        for i in range(len(args)):
            print('args[' + i + ']= ' + str(args[i]))
        exit()

    # 必要なファイルを開く
    try:
        f_in  = open(args[1], mode='r')
        f_out = open(args[2], mode='w')
    except FileNotFoundError as err:
        print("ファイルが存在しないため、読み込めませんでした。")
        exit()
    except Exception as other:
        print("ファイルが読み込めませんでした。")
        exit()

    
    print("Input File: " + args[1])
    reader = csv.reader(f_in, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    # object for calculating sentence similarity
    o_mecab = CalcSim_MeCab()  # MeCab Lib

    count = 0
    for line in reader:

        original_translation = line.pop(0)
        f_out.write(original_translation + ",")

        other_translations = line
        for ot in other_translations:
            f_out.write(ot + ",")

        if count == 0:  # CSVのヘッダー定義
            f_out.write("\n")
        else:           # 文章の類似度計算
            ####################################################
            # similarity_score = o_mecab.calcTranslationSimilarity_normal(original_translation, other_translations)
            similarity_score = o_mecab.calcTranslationSimilarity_important(original_translation, other_translations)          
            ####################################################
            for i in similarity_score:
                f_out.write(str(i) + ",") 
            f_out.write("\n")   
            print('===========================\n')  
        
        count += 1

    f_in.close()
    f_out.close()