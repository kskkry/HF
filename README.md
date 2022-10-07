### complile
- 必要ファイルを全てコンパイルする必要あり（C++に詳しくない）
    - エラー
        - collect2: error: ld returned 1 exit status
```bash
g++ main.cpp hf.cpp variables.cpp systemparam.cpp gto.cpp vec3.cpp matrix.cpp
```

### 実装
- 参考資料
    - 基底関数の処理
        - https://github.com/ifilot/hfcxx/tree/master
    - 行列クラス
        - https://qiita.com/ccam/items/75efe05edf815ea6734b