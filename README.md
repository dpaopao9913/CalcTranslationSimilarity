<!-- screenshot -->
<img src="https://d-paopao.com/wp-content/uploads/2021/08/overview.webp" alt="" />

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#calcTranslationSimilarity">GoogleTranslationAuto</a>
    </li>
    <li>
      <a href="#package">Package</a>
    </li>
    <li>
      <a href="#prerequisite">Prerequisite</a>
    </li>
    <li>
      <a href="#setup">Setup</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#further-options">Further options</a></li>
      </ul>
    </li>
    <li>
      <a href="#license">License</a>
    </li>
    <li>
      <a href="#contributor">Contributor</a>
    </li>
    <li>
      <a href="#reference">Reference</a>
    </li>
  </ol>
</details>


# calcTranslationSimilarity

calculate a sentence similarity between japanese sentence pairs, this program can be used for inspecting whether the sentence is machine translated or not.



# Package

- calcTranslationSimilarity.bat <br>
  batch file for demo
  
- calcTranslationSimilarity.py <br>
  main program
  
- sentences.csv <br>
  input file for the batch file
  
- sentences_out.csv <br>
  output file with sentence similarity.
  

# Prerequisite

- Windows 10 x64

- Anaconda 5.2.0 (conda 4.9.2)

- Python 3.8.5


# Setup

You need to install MeCab library first. For installation on Anaconda on windows 10, plz refer to: https://emotionexplorer.blog.fc2.com/blog-entry-349.html

```sh
$ conda install -c mzh mecab-python3
```

```sh
$ conda install -c conda-forge unidic-lite 
```


# Usage

Run `calcTranslationSimilarity.bat` for demo.


## Further options

- You can change between Normal mode and Important mode. Normal mode is based on normal 'wakati' sentence separation, while Important mode is based on the important components (i.e. verb, noun, adjective, etc). default is Important mode. <br>
  
  ```python
  # similarity_score = o_mecab.calcTranslationSimilarity_normal(original_translation, other_translations)
  similarity_score = o_mecab.calcTranslationSimilarity_important(original_translation, other_translations)          
  ```
    
- You can change the interest of components in the Important mode below. <br>
  
  ```python
  if node.feature.split(",")[0] == "名詞" or node.feature.split(",")[0] == "動詞" or node.feature.split(",")[0] == "形容詞" or node.feature.split(",")[0] == "形容動詞":
  ```


# License

This software is released under the MIT License, see LICENSE.


# Contributor

[d_paopao9913](https://twitter.com/d_paopao9913)


# Reference

- https://d-paopao.com/calculation_sentense_similarity/
