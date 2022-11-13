### Note
    - This repo is created for my own learning...
    - This code doesn't guarantee the accuracy of the calculations.

### How to Complile
- 必要ファイルを全てコンパイルする必要あり（C++に詳しくない）
    - エラー
        - collect2: error: ld returned 1 exit status
```bash
$ g++ main.cpp hf.cpp variables.cpp systemparam.cpp gto.cpp vec3.cpp matrix.cpp functions.cpp overlap.cpp cgf.cpp
```

### Ref
- 参考資料
    - preprocessing basis-function
    - computing nuclear & repulsion matrix
        - https://github.com/ifilot/hfcxx/tree/master
    - 行列クラス
        - https://qiita.com/ccam/items/75efe05edf815ea6734b

### source is [here](https://github.com/kskkry/HF "Github")