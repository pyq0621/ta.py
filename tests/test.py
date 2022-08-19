import ta_py as ta
median = ta.median([4, 6, 3, 1, 2, 5], 4);
assert median == [3, 2, 2];
kmeans = ta.kmeans([2, 3, 4, 5, 3, 5, 7, 8, 6, 8, 6, 4, 2, 6], 4);
assert kmeans == [[ 4, 5, 5, 4 ], [ 7, 6, 6, 6 ], [ 8, 8 ], [ 2, 3, 3, 2 ]];
normal = ta.normalize([5,4,9,4], 0.1);
assert normal == [0.2222222222222222, 0.06349206349206349, 0.8571428571428571, 0.06349206349206349];
denormal = ta.denormalize([5,4,9,4], [0.2222222222222222, 0.06349206349206349, 0.8571428571428571, 0.06349206349206349, 0.4444444444444444], 0.1);
assert denormal == [5.0, 4.0, 9.0, 4.0, 6.4];
mad = ta.mad([3, 7, 5, 4, 3, 8, 9], 6);
assert mad == [1.0, 2.0];
aad = ta.aad([4, 6, 8, 6, 8, 9, 10, 11], 7);
assert aad == [1.6734693877551021, 1.469387755102041];
ssd = ta.ssd([7, 6, 5, 7, 9, 8, 3, 5, 4], 7);
assert ssd == [4.869731585445518, 4.9856938190329, 5.3718844791323335];
er = ta.er([0.02, -0.01, 0.03, 0.05, -0.03]);
assert er == 0.011934565489708282;
rsi = ta.rsi([1,2,3,4,5,6,7,5], 6);
assert rsi == [100.0, 100.0, 66.66666666666666];
wrsi = ta.wrsi([1, 2, 3, 4, 5, 6, 7, 5, 6], 6);
assert wrsi == [100, 71.42857142857143, 75.60975609756098];
sma = ta.sma([1, 2, 3, 4, 5, 6, 10], 6);
assert sma == [3.5, 5];
smma = ta.smma([1, 2, 3, 4, 5, 6, 10], 5);
assert smma == [3.4, 4.92];
wma = ta.wma([69, 68, 66, 70, 68], 4);
assert wma == [68.3, 68.2];
pwma = ta.pwma([17, 26, 23, 29, 20], 4);
assert pwma == [24.09090909090909, 25.18181818181818];
hwma = ta.hwma([54, 51, 86, 42, 47], 4);
assert hwma == [56.199999999999996, 55.0];
ema = ta.ema([1, 2, 3, 4, 5, 6, 10], 6);
assert ema == [3.5, 5.357142857142857];
wsma = ta.wsma([1, 2, 3, 4, 5, 6, 10], 6);
assert wsma == [3.5, 4.583333333333333];
tsi = ta.tsi([1.32, 1.27, 1.42, 1.47, 1.42, 1.45, 1.59], 3, 2, 2);
assert tsi == [[0.3268608414239478, 0.32038834951456274], [0.5795418491021003, 0.7058823529411765]];
vwma = ta.vwma([[1, 59], [1.1, 82], [1.21, 27], [1.42, 73], [1.32, 42]], 4);
assert vwma == [1.184771784232365, 1.258794642857143];
hull = ta.hull([6, 7, 5, 6, 7, 4, 5, 7], 6);
assert hull == [4.761904761904762, 5.476190476190476];
kama = ta.kama([8, 7, 8, 9, 7, 9], 2, 4, 8);
assert kama == [8, 8.64, 8.377600000000001, 8.377600000000001];
macd = ta.macd([1, 2, 3, 4, 5, 6, 14], 3, 6);
assert macd == [1.5, 3];
variance = ta.variance([6, 7, 2, 3, 5, 8, 6, 2], 7);
assert variance == [3.918367346938776, 5.061224489795919];
std = ta.std([1, 2, 3], 3);
assert std <= 0.816496580928;
normsinv = ta.normsinv(0.4732);
assert normsinv == -0.06722824471054376;
bands = ta.bands([1, 2, 3, 4, 5, 6], 5, 2);
assert bands == [[5.82842712474619, 3.0, 0.1715728752538097], [6.82842712474619, 4.0, 1.1715728752538097]];
bandwidth = ta.bandwidth([1, 2, 3, 4, 5, 6], 5, 2);
assert bandwidth == [1.8856180831641265, 1.414213562373095];
atr = ta.atr([[3,2,1], [2,2,1], [4,3,1], [2,2,1]], 3);
assert atr == [2.0, 1.6666666666666667, 2.111111111111111, 1.7407407407407407];
keltner = ta.keltner([[3,2,1], [2,2,1], [4,3,1], [2,2,1], [3,3,1]], 5, 1);
assert keltner == [[3.932266666666667, 2.066666666666667, 0.20106666666666695]];
cor = ta.cor([1, 2, 3, 4, 5, 2], [1, 3, 2, 4, 6, 3]);
assert cor >= 0.8808929232684737
dif = ta.dif(0.75, 0.5);
assert dif == 0.5;
draw = ta.drawdown([1,2,3,4,2,3]);
assert draw == -0.5;
aroon_up = ta.aroon_up([5, 4, 5, 2], 3);
assert aroon_up == [100.0, 50.0];
aroon_down = ta.aroon_down([2, 5, 4, 5], 3);
assert aroon_down == [0.0, 50.0];
aroon_osc = ta.aroon_osc([2, 5, 4, 5], 3);
assert aroon_osc == [50, 50];
mfi = ta.mfi([[19, 13], [14, 38], [21, 25], [32, 17]], 3);
assert mfi == [41.53846153846154, 45.578231292517];
roc = ta.roc([1, 2, 3, 4], 3);
assert roc == [2, 1];
cop = ta.cop([3, 4, 5, 3, 4, 5, 6, 4, 7, 5, 4, 7, 5], 4, 6, 5);
assert cop == [0.3755555555555556, 0.23666666666666666];
kst = ta.kst([8, 6, 7, 6, 8, 9, 7, 5, 6, 7, 6, 8, 6, 7, 6, 8, 9, 9, 8, 6, 4, 6, 5, 6, 7, 8, 9], 5, 5, 7, 5, 10, 5, 15, 7, 4);
assert kst == [[-0.6828231292517006, -0.5174886621315192], [-0.2939342403628118, -0.5786281179138322], [0.3517800453514739, -0.35968820861678]];
obv = ta.obv([[25200, 10], [30000, 10.15], [25600, 10.17], [32000, 10.13]]);
assert obv == [0, 30000, 55600, 23600];
vwap = ta.vwap([[127.21, 89329], [127.17, 16137], [127.16, 23945]], 2);
assert vwap == [127.20387973375304, 127.16402599670675];
mom = ta.mom([1, 1.1, 1.2, 1.24, 1.34], 4);
assert mom == [0.24, 0.24];
mom_osc = ta.mom_osc([1, 1.2, 1.3, 1.3, 1.2, 1.4], 4);
assert mom_osc == [0.0, 3.8461538461538494];
bop = ta.bop([[4, 5, 4, 5], [5, 6, 5, 6], [6, 8, 5, 6]], 2);
assert bop == [1, 0.5];
fi = ta.fi([[1.4, 200], [1.5, 240], [1.1, 300], [1.2, 240], [1.5, 400]], 4);
assert fi == [12.00000000000001];
asi = ta.asi([[7, 6, 4], [9, 7, 5], [9, 8, 6]]);
assert asi == [0, -12.5];
ao = ta.ao([[6, 5], [8, 6], [7, 4], [6, 5], [7, 6], [9, 8]], 2, 5);
assert ao == [0.0, 0.9000000000000004];
pr = ta.pr([2, 1, 3, 1, 2], 3);
assert pr == [0, -100, -50];
lsma = ta.lsma([5, 6, 6, 3, 4, 6, 7], 6);
assert lsma == [4.714285714285714, 5.761904761904762];
don = ta.don([[6, 2], [5, 2], [5, 3], [6, 3], [7, 4], [6, 3]], 5);
assert don == [[7, 4.5, 2], [7, 4.5, 2]];
percentile = ta.percentile([[6,4,7],[5,3,6],[7,5,8]], 0.5);
assert percentile == [6,4,7];
ichimoku = ta.ichimoku([[6,3,2], [5,4,2], [5,4,3], [6,4,3], [7,6,4], [6,5,3], [7,6,5], [7,5,3], [8,6,5], [9,7,6], [8,7,6], [7,5,5],[6,5,4],[6,5,3],[6,3,2], [5,4,2]], 2, 4, 6, 4);
assert ichimoku == [[7, 6, 10.5, 6, 5], [7.5, 6, 7.5, 5.5, 6], [6.5, 7, 8, 5, 5]];
stoch = ta.stoch([[3,2,1], [2,2,1], [4,3,1], [2,2,1]], 2, 1, 1);
assert stoch == [[66.66666666666667, 66.66666666666667], [33.333333333333336, 33.333333333333336]];
ha = ta.ha([[3, 4, 2, 3], [3, 6, 3, 5], [5, 5, 2, 3]]);
assert ha == [[3.0, 4.0, 2.0, 3.0], [3.0, 4.0, 2.0, 3.0], [3.0, 6.0, 3.0, 4.25], [3.625, 5.0, 2.0, 3.75]];
ren = ta.ren([[8, 6], [9, 7], [9, 8], [13, 10]], 2);
assert ren == [[8.0, 10.0, 8.0, 10.0], [10.0, 12.0, 10.0, 12.0]];
chaikin = ta.chaikin_osc([[2,3,4,6],[5,5,5,4],[5,4,3,7],[4,3,3,4],[6,5,4,6],[7,4,3,6]],2,4);
assert chaikin == [-1.6666666666666665, -0.28888888888888886, -0.7362962962962962];
enve = ta.envelope([6,7,8,7,6,7,8,7,8,7,8,7,8], 11, 0.05);
assert enve == [[7.540909090909091, 7.181818181818182, 6.822727272727272], [7.636363636363637, 7.2727272727272725, 6.909090909090908]];
frac = ta.fractals([[7,6],[8,6],[9,6],[8,5],[7,4],[6,3],[7,4],[8,5]]);
assert frac == [[False, False], [False, False], [True, False], [False, False], [False, False], [False, True], [False, False], [False, False]];
hi = ta.recent_high([4,5,6,7,8,9,8,7,8,9,10,3,2,1], 3);
assert hi == {'index': 10, 'value': 10};
lo = ta.recent_low([1,4,5,6,4,3,2,3,4,3,5,7,8,8,5], 4);
assert lo == {'index': 6, 'value': 2};
sup = ta.support([4,3,2,5,7,6,5,4,7,8,5,4,6,7,5]);
sup = sup['calculate'](9);
assert sup == 4.0;
res = ta.resistance([5,7,5,5,4,6,5,4,6,5,4,3,2,4,3,2,1]);
res = res['calculate'](4);
assert res == 6.428571428571429;
ac = ta.ac([[6, 5], [8, 6], [7, 4], [6, 5], [7, 6], [9, 8]], 2, 4);
assert ac == [0.125, 0.5625];
fib = ta.fib(1, 2);
assert fib == [1,1.236,1.3820000000000001,1.5,1.6179999999999999,1.786,2,2.6180000000000003,3.618,4.618,5.236];
alli = ta.alligator([8,7,8,9,7,8,9,6,7,8,6,8,10,8,7,9,8,7,9,6,7,9]);
assert alli == [[7.217569412835686, 6.985078985569999, 6.456171046541722], [7.171597633136094, 7.119368115440011, 6.719144767291392]];
gato = ta.gator([8,7,8,9,7,8,9,6,7,8,6,8,10,8,7,9,8,7,9,6,7,9]);
assert gato == [[0.23249042726568714, -0.5289079390282767], [0.05222951769608297, -0.4002233481486188]];
standard = ta.standardize([6,4,6,8,6]);
assert standard == [0, -1.5811388300841895, 0, 1.5811388300841895, 0];
fisher = ta.fisher([8,6,8,9,7,8,9,8,7,8,6,7], 9);
assert fisher == [[-0.018907501228583555, -0.1104469157900972], [-0.32522580129662043, -0.018907501228583555],[-0.4884829106274281, -0.32522580129662043]];
kelly = ta.kelly([0.01,0.02,-0.01,-0.03,-0.015,0.045,0.005]);
assert kelly == 0.14434748152632182;
se = ta.se([34,54,45,43,57,38,49], 10);
assert se == 2.4243661069253055
zscore = ta.zscore([34,54,45,43,57,38,49], 5);
assert zscore == [1.2664106627730554, -1.3314928442246727, 0.4078462733398033];
ar = ta.ar([0.02, -0.01, 0.03, 0.05, -0.03], 3);
assert ar == [0.03667479679633267, -0.053301281310417566];
winratio = ta.winratio([0.01,0.02,-0.01,-0.03,-0.015,0.005]);
assert winratio == 0.5;
avgwin = ta.avgwin([0.01,0.02,-0.01,-0.03,-0.015,0.005]);
assert avgwin == 0.011666666666666665;
avgloss = ta.avgloss([0.01,0.02,-0.01,-0.03,-0.015,0.005]);
assert avgloss == -0.018333333333333333;
normal_pair = ta.normalize_pair([10,12,11,13],[100,130,100,140]);
assert normal_pair == [[55,55],[66,71.5],[60.5,54.99999999999999],[71.5,76.99999999999999]];
normal_from = ta.normalize_from([8,12,10,11], 100);
assert normal_from == [100,150,125,137.5];
fisher = ta.fisher([8,6,8,9,7,8,9,8,7,8,6,7], 9);
assert fisher == [[-0.018907501228583555, -0.1104469157900972], [-0.32522580129662043, -0.018907501228583555],[-0.4884829106274281, -0.32522580129662043]];
cross = ta.cross([3,4,5,4,3], [4,3,2,3,4]);
assert cross == [{'index': 1, 'cross': True}, {'index': 4, 'cross': False}];
half = ta.halftrend([[100,97,90],[101,98,94],[103,96,92],[106,100,95],[110,101,100],[112,110,105],[110,100,90],[103,100,97],[95,90,85],[94,80,80],[90,82,81],[85,80,70]], 6, 3, 2);
assert half == [[110.13773148148148, 100, 89.86226851851852, 'long'], [115.77674897119341, 105, 94.22325102880659, 'long'], [111.32021604938272, 100, 88.67978395061728, 'long'], [116.10018004115227, 105, 93.89981995884773, 'long'], [111.2485853909465, 100, 88.7514146090535, 'long'], [114.76787551440329, 105, 95.23212448559671, 'long'], [114.99356995884773, 100, 85.00643004115227, 'long']]
log = ta.log([5, 14, 18, 28, 68, 103]);
assert log == [1.6094379124341003, 2.6390573296152584, 2.8903717578961645, 3.332204510175204, 4.219507705176107, 4.634728988229636];
# test result different on python versions
# exp = ta.exp([1.6, 2.63, 2.89, 3.33, 4.22, 4.63]);
# assert exp == [4.953032424395115, 13.873769902129904, 17.99330960155032, 27.938341703236507, 68.03348428941966, 102.51406411049346];
covariance = ta.covariance([12,13,25,39],[67,45,32,21],4);
assert covariance == [-165.8125];
ncdf = ta.ncdf(13,10,2);
assert ncdf == 0.9331737996110652;
zig = ta.zigzag([[10,9], [12,10], [14,12], [15,13], [16,15], [11,10], [18,15]]);
assert zig == [9, 10.75, 12.5, 14.25, 16, 10, 18];
zc = ta.zigzag([6,7,8,9,10,12,9,8,5,3,3,3,5,7,8,9,11]);
assert zc == [6, 7.2, 8.4, 9.6, 10.8, 12.0, 10.5, 9.0, 7.5, 6.0, 4.5, 3.0, 4.6, 6.2, 7.800000000000001, 9.4, 11.0]
psar = ta.psar([[82.15,81.29],[81.89,80.64],[83.03,81.31],[83.30,82.65],[83.85,83.07],[83.90,83.11],[83.33,82.49],[84.30,82.3],[84.84,84.15],[85,84.11],[75.9,74.03],[76.58,75.39],[76.98,75.76],[78,77.17],[70.87,70.01]], 0.02, 0.2);
assert psar == [81.29,82.15,80.64,80.64,80.7464,80.932616,81.17000672,81.3884061824,81.67956556416,82.0588176964608,85,85,84.7806,84.565588,84.35487624000001];
fibbands = ta.fibbands([[1,59],[1.1,82],[1.21,27],[1.42,73],[1.32,42]], 4, 3);
assert fibbands == [[1.6526058894448858,1.542197040614731,1.4738932612537028,1.4186888368386255,1.363484412423548,1.29518063306252,1.184771784232365,1.0743629354022102,1.0060591560411822,0.9508547316261047,0.8956503072110273,0.8273465278499992,0.7169376790198443],[1.6177775811703725,1.5330576077284503,1.4806460987347188,1.4382861120137578,1.3959261252927968,1.3435146162990652,1.258794642857143,1.1740746694152209,1.1216631604214893,1.0793031737005283,1.0369431869795673,0.9845316779858357,0.8998117045439136]];
supertrend = ta.supertrend([[3,2,1], [2,2,1], [4,3,1], [2,2,1]], 3, 0.5);
assert supertrend == [[3.5555555555555554, 1.4444444444444444],[2.3703703703703702, 0.6296296296296297]];
cwma = ta.cwma([69,68,66,70,68,69], [1,2,3,5,8]);
assert cwma == [68.26315789473684, 68.52631578947368];
perm = ta.permutations([10,10,10]);
assert perm == 1000;
mse = ta.mse([7,8,7,8,6,9],[6,8,8,9,6,8]);
assert mse == 0.6666666666666666;
cum = ta.cum([3,5,7,5,10], 4);
assert cum == [20,27];
vwwma = ta.vwwma([[1,59],[1.1,82],[1.21,27],[1.42,73],[1.32,42]],4);
assert vwwma == [1.2618288590604028, 1.3160229445506693];
elder = ta.elderray([6,5,4,7,8,9,6,8], 7);
assert elder == [[2.571428571428571,-2.428571428571429],[2.2857142857142856,-2.7142857142857144]];
hv = ta.hv([7,6,5,7,8,9,7,6,5], 8);
assert hv == [0.6420403501307599,0.6823595190987881];
print('Test Passed');
