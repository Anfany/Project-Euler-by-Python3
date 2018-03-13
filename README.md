# Project Euler
>>>[欧拉计划](https://projecteuler.net/archives)(Project Euler)是一个解题网站，包括一系列有挑战性的数学与计算机编程题；要解开它们，需要的不止是数学知识：尽管数学能够帮助你找到一些优雅而有效的方法，大多数题目仍需要借助计算机和编程技巧来完成解答。本系列会持续按序更新对全部问题的基于Python3的解决方法。此外本项目仅提供问题的中文版以及code，英文题目请参见网站。

### 001. 3和5的倍数(Multiples of 3 and 5)

小于10的非零自然数中是3或者5的倍数有3、5、6、9，这四个数的和为23。计算小于1000的自然数中是3或者5的倍数的所有数的和。

### 002. 斐波那契数列中的偶数(Even Fibonacci numbers)

**斐波那契数列**中每一项均是由前两项的和组成，以1和2作为开始的两项，则前10项为1、2、3、5、8、13、21、34、59、89。请计算最后一项不超过400万的斐波那契数列中的所有偶数之和。

### 003. 最大素因数(Largest prime factor)

13195的素因数为5、17、13和29。求60051475143的最大素因数。

### 004. 最大的回文乘积数(Largest palindrome product)

所谓**回文数**就是从后往前和从前往后读是一样的数。由两个2位数相乘得到的最大回文乘积是 9009 = 91 × 99。找出由两个3位数相乘得到的最大回文乘积数。

### 005. 最小倍数(Smallest multiple)

能被1到10这10个数整除的最小的正数是2520。计算最小的能够被1到20整除的正数。

### 006. 平方的和与和的平方之差(Sum square difference)

前10个自然数平方的和是：1<sup>2</sup> + 2<sup>2</sup>+… + 10<sup>2</sup> = 385。前10个自然数和的平方是：(1 + 2 + … + 10)<sup>2</sup> = 55<sup>2</sup>=3025。因此前10个自然数的平方的和与和的平方之差是 3025−385=2640。求前100个自然数平方的和与和的平方之差

### 007. 第10001个素数(10001st prime)

如果要依次列出前6个素数的话，它们是：2、3、5、7、11和13。可以看出，第6个素数是13。求第10001个素数。

### 008. 连续数字最大乘积(Largest product in a series)

在下面的1000个正整数中，连续4个数字的最大乘积是 9 × 9 × 8 × 9 = 5832。

```
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
```

找出这个1000个正整数中乘积最大的连续的13个数字，求它们的乘积。

### 009. 特殊的毕达哥拉斯三元组(Special Pythagorean triplet)

**毕达哥拉斯三元组**是三个自然数a < b < c组成的集合，并满足a<sup>2</sup>+ b<sup>2</sup> = c<sup>2</sup>。 例如3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>。有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc。

### 010. 素数之和(Summation of primes)

所有小于10的素数的和为2 + 3 + 5 + 7 = 17。求小于两百万的所有素数之和。

### 011. 数字方阵中的最大乘积(Largest product in a grid)

在下面20×20的数字方阵中，以第7行第9列的数字26开始，右下对角线方向的3个数字分别是63,78,14。

```
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
```

这四个数的乘积是26 × 63 × 78 × 14 = 1788696。在这个20×20数字方阵中，计算4个在同一个方向（从下至上、从上至下、从右至左、从左至右或者对角线）上的紧邻的数的最大乘积。

### 012. 可约三角数(Highly divisible triangular number)

三角数数列是通过逐个加上自然数来生成的。例如，第7个三角形数是 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28。三角形数数列的前十项分别是：1, 3, 6, 10, 15, 21, 28, 36, 45, 55, … 下面是前七个三角数的所有约数：

&emsp;&emsp;__1: 1__

&emsp;&emsp;__3: 1、3__

&emsp;&emsp;__6: 1、2、3、6__

&emsp;&emsp;__10: 1、2、5、10__

&emsp;&emsp;__15: 1、3、5、15__

&emsp;&emsp;__21: 1、3、7、21__

&emsp;&emsp;__28: 1、2、4、7、14、28__

可以看出，28是第一个拥有超过5个约数的三角数。求第一个拥有超过500个约数的三角数。

### 013. 大数之和(Large sum)

计算出以下一百个50位数的和的前十位数字

```
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
```

### 014. 最长的考拉兹序列(Longest Collatz sequence)

在正整数集上定义如下的迭代序列：

&emsp;&emsp;&emsp;&emsp;__n ----> n/2 （若n为偶数）   n ----> 3n + 1 （若n为奇数）__

从13开始应用上述规则，我们可以生成如下的序列：13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1。可以看出这个序列（从13开始到1结束）共有10项。虽然还没有被证明，但普遍认为，从任何数开始最终都能迭代至1（这就是“考拉兹猜想”）。计算从小于一百万的哪个数开始，生成的序列最长。【注：序列开始生成后允许其中的项超过一百万】

### 015. 网格路径(Lattice paths)

从一个2×2方阵的左上角出发，只允许向右或向下移动，则恰好有6条通往右下角的路径。

![image](https://projecteuler.net/project/images/p015.gif)

对于20×20方阵来说，这样的路径有几条。

### 016. 幂的数字和(Power digit sum)

2<sup>15</sup>=32768，32768的各位数字之和为 3 + 2 + 7 + 6 + 8 = 26。计算2<sup>1000</sup>的各位数字之和。

### 017. 英文字母个数(Number letter counts)

把1到5写成英文单词，分别是：one, two, three, four, five，这些单词一共用了3 + 3 + 5 + 4 + 4 = 19个字母。把1到1000都写成英文单词，共用多少字母。【注： 不要算上空格和连字符。例如，342（three hundred and forty-two）包含23个字母，而115（one hundred and fifteen）包含20个字母。单词“and”的使用方式遵循英式英语的规则】。

### 018. 最大路径和(基础版)(Maximum path sum I)

从下图三角形的顶端出发，不断移动到在下一行与其相邻的元素(例如数字7只能移动到下一行的2或者4，而不能到达6)，得到的最大路径和是23。

```
   3
  7 4
 2 4 6
8 5 9 3
```

如上图，最大路径和为 3 + 7 + 4 + 9 = 23。求从下面的三角形顶端出发到达底部，所能够得到的最大路径和。

```
                         75
                        95 64
                      17 47 82
                    18 35 87 10
                  20 04 82 47 65
                19 01 23 75 03 34
               88 02 77 73 07 63 67
             99 65 04 28 06 16 70 92
           41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
       53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
```

【注：在上面这个问题中，由于只有16384条路径，通过尝试所有的路径来解决问题是可行的。但是如果三角形变大，暴力破解将不能解决，而需要一个更加聪明的办法】

### 019. 星期日个数(Counting Sundays)

1900年1月1日是星期一；天数是30天的月份有四、六、九、十一，剩下的月份除了二月，其他都是31天；闰年的二月有29天，平年的二月是28天；闰年指的是能够被4整除却不能被100整除的年份，或者能够被400整除的年份。

在二十世纪（1901年1月1日到2000年12月31日）中，有多少个月的1号是星期日。

### 020. 阶乘的数字之和(Factorial digit sum)

n! 表示的是 n × (n − 1) × … × 3 × 2 × 1。例如：10! = 10 × 9 × … × 3 × 2 × 1 = 3628800，所以10的阶乘的数字之和是 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27。

求出100!的各位数字和。

### 021. 亲和数(Amicable numbers)

记d(n)为n的所有真因数（小于n且整除n的正整数）之和。如果d(a) = b且d(b) = a，且a ≠ b，那么a和b构成一个亲和数对，a和b被称为亲和数。例如，220的真因数包括1、2、4、5、10、11、20、22、44、55和110，因此d(220) = 284。284的真因数包括1、2、4、71和142，因此d(284) = 220。说明284和220是亲和数。

求所有小于10000的亲和数的和。

### 022. 姓名之分(Names scores)

文本[names.txt](https://projecteuler.net/project/resources/p022_names.txt)中包含了五千多个姓名，首先将姓名按字母顺序排列，然后算出每个姓名字母的和值，最后乘以该姓名排列后的位置，以计算出__姓名之分__。例如，按照字母顺序排列后，姓名COLIN的位置是938，其字母的和值是3 + 15 + 12 + 9 + 14 = 53。因此COLIN的姓名之分是938 × 53 = 49714。

计算文件中所有姓名的姓名之分的和。

### 023. 非盈数之和的和(Non-abundant sums)

完全数是指真因数之和等于自身的那些数。例如，28的真因数之和为1 + 2 + 4 + 7 + 14 = 28，因此28是一个完全数。一个数n被称为亏数，如果它的真因数之和小于n；反之则被称为**盈数**。由于12是最小的盈数，它的真因数之和为1 + 2 + 3 + 4 + 6 = 16，所以最小的能够表示成两个盈数之和的数是24。

通过数学分析可以得出，所有大于28123的数都可以被写成两个盈数的和；因此28123是不能被分成两个盈数的和的最大的数的上界。

找出所有不能被写成两个盈数之和的正整数的和。

### 024. 字典序排列(Lexicographic permutations)

**排列**指的是将一组物体进行有顺序的放置。例如，3124是数字1、2、3、4的一个排列。如果把所有排列按照数字大小或字母先后进行排序，我们称之为字典序排列。0、1、2的字典序排列是：**012     021     102     120     201     210**。

数字0、1、2、3、4、5、6、7、8、9的字典序排列中第一百万位的排列是。

### 025. 1000位的斐波那契数(1000-digit Fibonacci number)

斐波那契数列是按如下递归关系定义的数列：

&emsp;&emsp;&emsp;__F1 = 1 F2 = 1__

&emsp;&emsp;&emsp;__Fn = Fn−1 + Fn−2__

因此斐波那契数列的前12项分别是：
>>F1 = 1
>>F2 = 1
>>F3 = 2
>>F4 = 3
>>F5 = 5
>>F6 = 8
>>F7 = 13
>>F8 = 21
>>F9 = 34
>>F10 = 55
>>F11 = 89
>>F12 = 144

不难看出，第一个有3位数字的是第12项F12。在斐波那契数列中，第一个有1000位数字的是第几项。

### 026. 最长的倒数循环节(Reciprocal cycles)

单位分数是指分子为1的分数。分母从2到10的单位分数的十进制表示如下所示：

>>&emsp;&emsp;&emsp;&emsp;__1/2= 0.5__
>>&emsp;&emsp;&emsp;&emsp;__1/3= 0.(3)__
>>&emsp;&emsp;&emsp;&emsp;__1/4= 0.25__
>>&emsp;&emsp;&emsp;&emsp;__1/5= 0.2__
>>&emsp;&emsp;&emsp;&emsp;__1/6= 0.1(6)__
>>&emsp;&emsp;&emsp;&emsp;__1/7= 0.(142857)__
>>&emsp;&emsp;&emsp;&emsp;__1/8= 0.125__
>>&emsp;&emsp;&emsp;&emsp;__1/9= 0.(1)__
>>&emsp;&emsp;&emsp;&emsp;__1/10= 0.1__

这里0.1(6)表示0.166666…，括号内表示有一位的循环节。可知，1/7有六位循环节。

找出小于1000的正整数d，其倒数的十进制表示的小数部分有最长的循环节。

### 027. 二次“素数生成”多项式(Quadratic primes)

欧拉发现了这个著名的二次多项式： __n<sup>2</sup> + n + 41__ 。n从0到39，这个二次多项式生成了40个素数。然而，当n = 40时，40<sup>2</sup> + 40 + 41 = 40(40 + 1) + 41能够被41整除，同时显然当n = 41时，41<sup>2</sup> + 41 + 41也能被41整除。

随后，另一个神奇的多项式 __n<sup>2</sup> − 79n + 1601__ 被发现了，对于n从0到79，它生成了80个素数。这个多项式的系数-79和1601的乘积为-126479。

考虑以下形式的二次多项式： __n<sup>2</sup> + an + b__ , 满足|a| < 1000且|b| < 1000。其中|n|表示n的绝对值，例如|11| = 11以及|−4| = 4。这其中存在某个二次多项式能够对从0开始尽可能多的连续整数n都生成素数，求其系数a和b的乘积。

### 028. 螺旋数阵对角线(Number spiral diagonals)

从1开始，按顺时针顺序向右铺开的5 × 5螺旋数阵如下所示：

![problem28.png](http://upload-images.jianshu.io/upload_images/4734220-c5162e3e4a4f99d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以验证，该数阵对角线上的数[红色数字]之和是101。

以同样方式构成的1001 × 1001螺旋数阵对角线上的数之和是。

### 029. 不同的幂(Distinct powers)

考虑所有满足2 ≤ a ≤ 5和2 ≤ b ≤ 5的整数组合生成的幂**a<sup>b</sup>** ：

>>&emsp;&emsp;&emsp;&emsp;__2<sup>2</sup>=4, 2<sup>3</sup>=8, 2<sup>4</sup>=16, 2<sup>5</sup>=32__
>>&emsp;&emsp;&emsp;&emsp;__3<sup>2</sup>=9, 3<sup>3</sup>=27, 3<sup>4</sup>=81, 3<sup>5</sup>=243__
>>&emsp;&emsp;&emsp;&emsp;__4<sup>2</sup>=16, 4<sup>3</sup>=64, 4<sup>4</sup>=256, 4<sup>5</sup>=1024__
>>&emsp;&emsp;&emsp;&emsp;__5<sup>2</sup>=25, 5<sup>3</sup>=125, 5<sup>4</sup>=625, 5<sup>5</sup>=3125__

如果把这些幂按照大小排列并去重，我们得到以下由15个不同的项组成的序列：

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

在所有满足2 ≤ a ≤ 100和2 ≤ b ≤ 100的整数生成的幂**a<sup>b</sup>** 排列并去重所得到的序列中，有多少项。


### 030. 姓名之分(Digit fifth powers)

数字的五次幂
&emsp;&emsp;令人惊讶的是，只有三个数可以写成它们各位数字的四次幂之和：

&emsp;&emsp;&emsp;&emsp; __1634 = 1<sup>4</sup> + 6<sup>4</sup> + 3<sup>4</sup> + 4<sup>4</sup>__
&emsp;&emsp;&emsp;&emsp; __8208 = 8<sup>4</sup> + 2<sup>4</sup> + 0<sup>4</sup> + 8<sup>4</sup>__
&emsp;&emsp;&emsp;&emsp; __9474 = 9<sup>4</sup> + 4<sup>4</sup> + 7<sup>4</sup> + 4<sup>4</sup>__

由于1 = 1<sup>4</sup不是一个和的形式，因此这里没列出。这些数的和是1634 + 8208 + 9474 = 19316。

找出所有可以写成它们各位数字的五次幂之和的数，并求这些数的和。










