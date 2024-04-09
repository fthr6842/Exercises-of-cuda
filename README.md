# test-of-cuda
### 1. GPU
#### GPU為圖形處理器用於數據運算(大量、重複性的計算任務)，相對地，CPU適合複雜的邏輯運算
### 2.GPU性能指標
#### a. 核心數
#### b. 顯存容量 (相當於內存)
#### c. 計算峰值
#### d. 顯存帶寬 (通信速率)
### 3. GPU+CPU架構
#### 首先，GPU無法單獨運算
#### CPU做為控制，稱為主機(host)
#### GPU作為CPU的協助處理器，稱為設備(device)
#### 主機和設備間的內存放間通過PCIe總線連接(較慢)
### 4. CUDA
#### Nvidia於2006年發布
#### 建立在Nvidia之GPU上的一個通用計算平台和編程模型
#### 支援C、C++、python、fortran
### 5. API
#### CUDA提供兩層API接口 (運行Runtime、驅動Driver)
#### 兩者調用性能無異
### 6. 編譯
#### C++編譯: gcc ...cpp -o ...
#### CUDA編譯: nvcc ...cu -o ...
### 7.核函數(Kernel function)
#### 在GPU上並行執行
#### 以限定詞__global__修飾
#### 返回值必須是void
#### __global__與void的位置可互換
#### 注意事項:
#### a. 核函數只能訪問GPU的內存空間(設備內存)
#### b. 核函數不能使用變長參數
#### c. 核函數不能使用靜態變數
#### d. 核函數不能使用函數指針
#### e. 核函數具有異步性
#### CUDA程式中的核函數執行與主機程式碼執行是異步的。在CUDA程式設計中，通常使用異步操作來最大程度地利用GPU的並行計算能力。
### 8. CUDA編寫程序
#### a. 主機程式碼
#### b.核函數調用
#### c. 主機程式碼(將GPU運算結果回傳給CPU主機)
#### Note: 核函數不支持CPP的iostream
### 9. 線程模型結構
#### a. grid: 網格
#### b. block: 線程塊
#### 邏輯上的劃分、並非物理意義
#### 配置: <<<grid_size, block_size>>>
#### 最大線程塊: 1024
#### 最大網格大小: 2^31 - 1 (針對一維網格)
### 10. 一維線程模型
#### 每個線程在核函數中有唯一標示
#### 每個線程的維一表示由<<<grod_size, block_size>>>確定，二者為內建變數(built-in variable)
#### a. gridDim.x: 
#### b. blockDim.x: 
#### 線程索引保存成內建變數
#### a. blockIdx.x: 變數指定一個線程在一個網格中的線程塊索引值，0 ~ gridDim.x - 1
#### b. threadIdx.x: 變數指定一個線程在一個線程塊中的線程索引值，0 ~ blockDim - 1
#### ex. <<<2, 4>>>: 網格中有2個線程塊(0 1)，每個線程塊有4個線程(0 1 2 3)
#### =>gridDim.x == 2； blockDim.x == 4； blockIdx.x == 0~1； threadIdx.x == 0~3
#### 線程唯一標示: Idx = threadIdx.x + blockIdx.x * blockDim.x
### 11. 多維線程
#### CUDA可以組織三維的網格、線程塊
#### blockIdx、threadIdx是類型維uint3的變數，具有x、y、z三個無符號成員
#### 定義多維網格和線程塊
#### dim3 grid_size(Gx, Gy, Gz)
#### dim3 block_size(Bx, By, Bz)
### 12. 一維網格、一維線程塊
#### int id = blockIdx.x + blockDim.x * threadIdx.x;
#### (線程塊索引 + 線程數量 * 線程索引)
### 13. 二維網格、二維線程塊
#### int blockId = blockIdx.x + blockId.y * gridDim.x
#### int threadId = threadIdx.x + threadIdx.y * blockDim.x
#### int id = blockId * (blockDim.x * blockDim.y) + threadId
### 14. 三維網格、三維線程塊
#### int blockId = blockIdx.x + blockIdx.y * gridDim.x
#### int threadId = threadIdx.x + (threadx.y * blockDim.x) + (threadIdx.z * (blockDim.x * blockDim.y))
#### int id = threadId + blockId * (blockDim.x * blockDim.y * blockDim.z)
### 15. nvcc編譯流程
#### nvcc分離程式為主機程式、設備程式
#### 主機程式為C/C++語法、設備程式為C/C++擴展語言邊寫
#### nvcc先將設備程式編譯為PTX偽匯編程式，再將PTX編譯為二進制cubin目標程式
#### 將源程式編譯為PTX程式時，需要使用-arch=compute_XY指定一個虛擬架構的計算能力，用來確定程式能夠使用cuda功能
#### 將PTX程式編譯為cubin程式時，需要使用-code=sm_ZW指定一個真實架構的計算能力，用來確定可執行文件能夠調用GPU
### 16. PTX
#### PTX是cuda基於GPU計算而定義的虛擬機和指令集
#### nvcc編譯命令使用兩個體系結構: 虛擬的中間體系結構、實際GPU
#### 虛擬架構如同對應用所需的GPU的聲明
#### 虛擬架構應盡可能選擇較低、真實架構應盡可能選擇較高
### 17. GPU架構與計算能力
#### 每款GPU都有用於標示計算能力的版本編號
#### 形式為X.Y
#### X為主版本號、Y表示次版本號
#### 並非GPU計算能力越高、性能就越高
### 18. 指定虛擬架構計算能力
#### C/C++編譯為PTX時，可以指定虛擬架構的計算能力，用來確定程式能夠使用CUDA功能
#### C/C++轉化為PTX與GPU硬體無關
### 19. 編譯指令
#### -arch=compute_XY -- XY分別代表主、次版本號
#### a. PTX指令只能在更高的計算能力的GPU使用(向下兼容)
#### b. PTX指令轉化為cubin與具體的GPU架構有關
### 20. 編譯指令
#### -code=sm_XY -- XY分別代表主、次版本號
#### a. cubin程式在大版本之間不兼容
#### b. 指定真實架構計算能力時需指定虛擬架構計算能力
#### c. 指定真實架構能力必須大於或等於虛擬架構能力(後大於前)
#### d. 真實架構可以實現低小版本號到高小版本號的兼容





















