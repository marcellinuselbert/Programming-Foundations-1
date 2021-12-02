# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt
import operator


# lengkapi fungsi berikut
def load_stop_words(filename):
    """
    Parameters
    ----------
    filename : string
        nama file yang menyimpan daftar stopwords.
        Di soal, nama default-nya adalah stopwords.txt

    Returns
    -------
    stop_words : set
        himpunan stopwords (unik)

    Fungsi menerima nama file yang berisi daftar stopwords,
    kemudian memuat semua stopwords ke dalam struktur data
    set. Perhatikan bahwa semua stopwords yang ada di dalam
    file sudah dalam bentuk huruf kecil semua.
    """
    # open the file, why errors ignore there is a character that cant be encoded
    stop = open(filename, "r", encoding="utf-8", errors="ignore")
    # lower all
    text_stop = stop.read().lower()
    # split per line
    list_text_stop = text_stop.split("\n")
    # get the unique text stop
    stop_words = set(list_text_stop)
    stop.close()
    return stop_words


# lengkapi fungsi berikut
def count_words(filepath, stop_words):
    """
    Parameters
    ----------
    filepath : string
        path atau lokasi dari file yang berisi sekumpulan
        kalimat-kalimat yang memiliki polaritas sentiment,
        yaitu rt-polarity.neg atau rt-polarity.pos

    stop_words : set
        himpunan stopwords

    Returns
    -------
    word_freq : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut.

    Fungsi ini akan scan semua baris (semua kalimat) yang
    ada di file dan kemudian mengakumulasikan frekuensi dari
    setiap kata yang muncul pada file tersebut.

    Contoh
    ------
    Jika isi dari file adalah:

        I just watched a good movie
        wow! a good movie
        a good one

    Fungsi akan mengembalikan dictionary:
        {'i':1, 'just':1, 'watched':1, 'a':3, 'good':3,
         'movie':2, 'wow!':1, 'one':1}

    Notes
    -----
    1. stopwords diabaikan
    2. karakter tanda baca seperti , . / dan sebagainya juga
       diabaikan (gunakan string.punctuation di library string)
    """
    # encode with utf-8
    input_text = open(filepath, "r", encoding="utf-8")
    # lower all
    input_opened_text = input_text.read().lower()
    # split based on whitespace so we get every words list of words
    list_text_splitted = input_opened_text.split()
    # for every word in list of words, please only add the word that isnt stop words and not punctuation
    list_filtered = [
        word for word in list_text_splitted if word not in stop_words
        if word not in string.punctuation
    ]
    # get unique word
    get_unique_word = set(list_filtered)

    word_freq = {}
    # for every unique word please count the unique word
    # key word and value is word appearance
    for word in get_unique_word:
        word_freq[word] = list_filtered.count(word)

    input_text.close()
    return word_freq


# lengkapi fungsi berikut
def compute_ndsi(word_freq_pos, word_freq_neg):
    """
    Parameters
    ----------
    word_freq_pos : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.pos
    word_freq_neg : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.neg

    Returns
    -------
    word_ndsi : dictionary
        sebuah dictionary, dimana key merupakan kata (string)
        dan value adalah NDSI score (float)

    Notes
    -----
    NDSI dari sebuah kata dihitung dengan:

              word_freq_pos[word] - word_freq_neg[word]
              -----------------------------------------
              word_freq_pos[word] + word_freq_neg[word]

    Jika kata tidak ditemukan pada salah satu dictionary,
    frekuensi kata tersebut adalah 0.

    Contoh
    ------
    Jika word_freq_neg = {'bad':10, 'worst':5, 'good':1} dan
         word_freq_pos = {'good':20, 'nice':5, 'bad':2},

    maka word_ndsi = {'bad':-0.67, 'worst':-1, 'good':0.90, 'nice':1}

    """
    word_ndsi = {}

    words_pos = set(word_freq_pos.keys())
    words_neg = set(word_freq_neg.keys())
    no_words_in_pos = words_neg - words_pos
    no_words_in_neg = words_pos - words_neg
    # get key unique, and get key neg unique
    # no words in pos is set words Neg - word Pos ex: {"hello","you"} word Neg ex: {"you","are","my best"}
    # so the word Neg - Word pos with - sign is difference sign in set, we get all the words that are not in word pos
    # wordsneg-wordspos = {"are","mybest"}

    # add the no words in pos/neg to the dictionary with value 0
    for word_pos in no_words_in_pos:
        word_freq_pos[word_pos] = 0
    for word_neg in no_words_in_neg:
        word_freq_neg[word_neg] = 0

    # union the words_neg and words_pos
    list_words = words_neg | words_pos

    # for every word then compute the the ndsi value
    for word in list_words:
        word_ndsi[word] = (word_freq_pos[word] - word_freq_neg[word]) / (
            word_freq_pos[word] + word_freq_neg[word])

    # sort based on the lowest to the highest
    sorted_ndsi = dict(sorted(word_ndsi.items(), key=operator.itemgetter(1)))

    return sorted_ndsi


# Fungsi berikut sudah selesai. Anda tidak perlu implementasikan
def show_ndsi_histogram(word_ndsi):
    """
    Parameters
    ----------
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.

    Returns
    -------
    None.

    Plot histogram dari semua NDSI scores yang dihasilkan

    """
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor='g', alpha=0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")


out = ""

if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos",
                                stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg",
                                stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi
    # word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # # urutkan pasangan kata dan skor ndsi yang ada
    # # di word_freq_ndsi berdasarkan nilai ndsi saja, dari terkecil
    # # ke yang terbesar

    for key, value in word_freq_ndsi.items():

        out += f"{key} {value}\n"

    # # simpan daftar kata-kata dan nilai ndsi yang sudah diurutkan tadi ke
    # # file ndsi.txt
    # ndsi_filename = "ndsi.txt"

    output_file = open("ndsi.txt", "w")
    output_file.write(out)
    output_file.close()
