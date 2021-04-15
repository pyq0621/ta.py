def median(data, l=0):
    l = (l) if l > 0 else len(data); pl = []; med = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l:
            tmp = pl.copy();
            tmp.sort(reverse=True);
            med.append(tmp[round((len(tmp)-1) / 2)]);
            pl = pl[1:];
    return med;
def rsi(data, l=0):
    l = (l) if l > 0 else len(data); pl = []; rs = [];
    for i in range(1, len(data)):
        pl.append(data[i] - data[i - 1]);
        if (len(pl)) >= l:
            gain = 0; loss = 0;
            for a in range(len(pl)):
                if pl[a] > 0: gain += pl[a];
                if pl[a] < 0: loss += abs(pl[a]);
            gain /= l; loss /= l; f = 100 - 100 / (1 + (gain / loss)) if loss != 0 else 100;
            rs.append(f);
            pl = pl[1:];
    return rs;
def sma(data, l=0):
    l = (l) if l > 0 else len(data) - 1; pl = []; sm = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l:
            sm.append(sum(pl) / l);
            pl = pl[1:];
    return sm;
def smma(data, l=0):
    l = (l) if l > 0 else len(data) - 1; pl = []; sm = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l:
            average = 0;
            for a in range(len(pl)): average += pl[a];
            f = average / l if len(sm) <= 0 else (average - sm[len(sm) - 1]) / l;
            sm.append(f);
            pl = pl[1:];
    sm = sm[1:];
    return sm;
def wma(data, l=0):
    l = (l) if l > 0 else len(data) - 1; pl = []; wm = []; weight = [];
    for i in range(1, l+1):
        weight.append(i);
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l:
            average = 0;
            for q in range(1, len(pl)+1):
                average += pl[q-1] * q / sum(weight);
            wm.append(average);
            pl = pl[1:];
    return wm;
def ema(data, l=0):
    l = (l) if l > 0 else len(data) - 1; pl = []; em = []; weight = 2 / (l + 1);
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l:
            f = sum(pl) / l if len(em) <= 0 else (data[i] - em[len(em) - 1]) * weight + em[len(em) - 1]
            em.append(f);
            pl = pl[1:];
    return em;
def tsi(data, long=25, short=13, sig=13):
    mo = []; ab = []; ts = []; tsi = [];
    for i in range(1, len(data)):
        mo.append(data[i] - data[i - 1]);
        ab.append(abs(data[i] - data[i - 1]));
    sma1 = ema(mo, long); sma2 = ema(ab, long);
    ema1 = ema(sma1, short); ema2 = ema(sma2, short);
    for i in range(len(ema1)):
        ts.append(ema1[i] / ema2[i]);
    tma = ema(ts, sig);
    ts = ts[(len(ts)-len(tma)):];
    for i in range(len(tma)):
        tsi.append([tma[i], ts[i]]);
    return tsi;
def vwma(data, l=0):
    l = (l) if l > 0 else len(data) - 1; pl = []; wm = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l:
            weight = 0; sum = 0;
            for a in range(len(pl)):
                sum += (pl[a][0] * pl[a][1]);
                weight += pl[a][1];
            wm.append(sum/weight);
            pl = pl[1:];
    return wm;
def hull(data, l=0):
    l = (l) if l > 0 else len(data) - 1; pl = []; hma = []; ewma = wma(data.copy(), l); sqn = round(l**(1/2));
    first = wma(data.copy(), round(l / 2));
    first = first[-(len(ewma)-len(first)):];
    for i in range(len(ewma)):
        pl.append((first[i] * 2) - ewma[i]);
        if (len(pl)) >= sqn:
            h = wma(pl.copy(), sqn);
            hma.append(h[len(h) - 1]);
    return hma;
def kama(data, l1=0, l2=0, l3=0):
    l1 = l1 if l1 > 0 else 10; l2 = l2 if l2 > 0 else 2; l3 = l3 if l3 > 0 else 30;
    ka = sma(data.copy(), l1); ka = [ka[len(ka)-1]];
    for i in range(l1 + 1, len(data)):
        vola = 0; change = abs(data[i] - data[i - l1]);
        for a in range(1, l1):
            vola += abs(data[i-a] - data[(i-a)-1]);
        sc = (change/vola * (2/(l2+1) - 2/(l3+1) + 2/(l3+1))) ** 2;
        ka.append(ka[len(ka)-1] + sc * (data[i] - ka[len(ka)-1]));
    return ka;
def macd(data, l1=0, l2=0):
    l1 = l1 if l1 > 0 else 12; l2 = l2 if l2 > 0 else 26;
    if l1 > l2: [l1, l2] = [l2, l1];
    em1 = ema(data.copy(), l1); em2 = ema(data.copy(), l2);
    em1 = em1[-(len(em2) - len(em1)):]; emf = [];
    for i in range(len(em1)):
        emf.append(em1[i] - em2[i]);
    return emf;
def variance(data, l1=0):
    mean = sma(data.copy(), l1);
    return sum((x - mean[len(mean)-1]) ** 2 for x in data) / len(data);
def std(data, l1=0):
    l1 = (l1) if l1 > 0 else len(data);
    std = variance(data.copy(), l1) ** (1/2)
    return std;
def bands(data, l1=0, l2=0):
    l1 = l1 if l1 > 0 else 14; l2 = l2 if l2 > 0 else 1;
    pl = []; deviation = []; boll = [];
    sm = sma(data.copy(), l1);
    for i in range(len(data)):
        pl.append(data[i]);
        if (len(pl)) >= l1:
            devi = std(pl.copy(), l1);
            deviation.append(devi);
            pl = pl[1:];
    for i in range(len(sm)):
        boll.append([sm[i] + deviation[i] * l2, sm[i], sm[i] - deviation[i] * l2]);
    return boll;
def bandwidth(data, l1=0, l2=0):
    l1 = l1 if l1 > 0 else 14; l2 = l2 if l2 > 0 else 1;
    band = bands(data.copy(), l1, l2); boll = [];
    for i in range(len(band)): boll.append((band[i][0] - band[i][2]) / band[i][1]);
    return boll;
def atr(data, l1=0):
    l1 = l1 if l1 > 0 else 14; atr = [data[0][0] - data[0][2]];
    for i in range(1, len(data)):
        t0 = max((data[i][0] - data[i - 1][1]), (data[i][2] - data[i - 1][1]), (data[i][0] - data[i][2]));
        atr.append((atr[len(atr)-1] * (l1 - 1) + t0) / l1)
    return atr;
def keltner(data, l1=0, l2=0):
    l1 = l1 if l1 > 0 else 14; l2 = l2 if l2 > 0 else 1;
    closing = []; tr = atr(data.copy(), l1); kelt = [];
    for i in range(len(data)): closing.append(sum(data[i]) / 3);
    kma = sma(closing, l1);
    tr = tr[(len(tr) - len(kma)):];
    for i in range(len(kma)): kelt.append([kma[i] + tr[i] * l2, kma[i], kma[i] - tr[i] * l2]);
    return kelt
def cor(data1, data2):
    d1avg = sma(data1.copy(), len(data1)); d1avg = d1avg[len(d1avg)-1];
    d2avg = sma(data2.copy(), len(data2)); d2avg = d2avg[len(d2avg)-1]
    sumavg = 0; sx = 0; sy = 0;
    for i in range(len(data1)):
        x = data1[i]-d1avg;
        y = data2[i]-d2avg;
        sumavg += (x * y); sx += x**2; sy += y**2;
    n = len(data1)-1;
    sx/=n; sy/=n; sx = sx ** (1/2); sy = sy ** (1/2);
    return (sumavg / (n*sx*sy));
def dif(n, o): return (n-o)/o;
def aroon_up(data, l1=0):
    l1 = l1 if l1 > 0 else 10; pl = []; aroon = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) >= l1):
            hl = pl.copy();
            aroon.append((100 * (l1 - (hl.index(max(hl))+1)) / l1));
            pl = pl[1:];
    return aroon;
def aroon_down(data, l1=0):
    l1 = l1 if l1 > 0 else 10; pl = []; aroon = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) >= l1):
            hl = pl.copy();
            aroon.append((100 * (l1 - (hl.index(min(hl))+1)) / l1));
            pl = pl[1:];
    return aroon
def aroon_osc(data, l1=0):
    l1 = l1 if l1 > 0 else 10; pl = []; aroon = [];
    u = aroon_up(data.copy(), l1); d = aroon_down(data.copy(), l1);
    for i in range(len(u)): aroon.append(u[i] - d[i]);
    return aroon;
def mfi(data, l1=0):
    l1 = l1 if l1 > 0 else 14; mfi = []; n = []; p = [];
    for i in range(len(data)):
        p.append(data[i][0]); n.append(data[i][1]);
        if(len(p) >= l1):
            mfi.append((100 - 100 / (1 + sum(p) / sum(n))));
            p = p[1:]; n = n[1:];
    return mfi;
def roc(data, l1=0):
    l1 = l1 if l1 > 0 else 14; pl = []; roc = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) >= l1):
            roc.append((pl[len(pl)-1] - pl[0]) / pl[0]);
            pl = pl[1:];
    return roc;
def cop(data, l1=0, l2=0, l3=0):
    l1 = l1 if l1 > 0 else 11; l2 = l2 if l2 > 0 else 14; l3 = l3 if l3 > 0 else 10; m = max(l1, l2); co = [];
    if l1 > l2: [l1, l2] = [l2, l1];
    for i in range(m + l3, len(data)):
        r1 = roc(data[i-(m+l3):i], l1); r2 = roc(data[i-(m+l3):i], l2); tmp = [];
        r1 = r1[(len(r1) - len(r2)):];
        for a in range(len(r1)):
            tmp.append(r1[a] + r2[a]);
        tmp = wma(tmp.copy(), l3);
        co.append(tmp[len(tmp)-1]);
    return co;
def kst(data, r1=10, s1=10, r2=15, s2=10, r3=20, s3=10, r4=30, s4=15, sig=9):
    ks = []; fs = []; ms = (max(r1, r2, r3, r4) + max(s1, s2, s3, s4));
    for i in range(ms, len(data)):
        rcma1 = roc(data[i-ms:i], r1); rcma2 = roc(data[i-ms:i], r2); rcma3 = roc(data[i-ms:i], r3); rcma4 = roc(data[i-ms:i], r4);
        rcma1 = sma(rcma1, s1); rcma2 = sma(rcma2, s2); rcma3 = sma(rcma3, s3); rcma4 = sma(rcma4, s4);
        ks.append(rcma1[len(rcma1)-1] + rcma2[len(rcma2)-1] + rcma3[len(rcma3)-1] + rcma4[len(rcma4)-1]);
    sl = sma(ks.copy(), sig);
    ks = ks[(len(ks) - len(sl)):];
    for i in range(len(ks)): fs.append([ks[i], sl[i]]);
    return fs;
def obv(data):
    obv = [0];
    for i in range(1, len(data)):
        if(data[i][1] > data[i-1][1]): obv.append(obv[len(obv)-1] + data[i][0]);
        if(data[i][1] < data[i-1][1]): obv.append(obv[len(obv)-1] - data[i][0]);
        if(data[i][1] == data[i-1][1]): obv.append(obv[len(obv)-1]);
    return obv;
def vwap(data, l1=0):
    l1 = l1 if l1 > 0 else len(data); pl = []; vwap = [];
    for i in range(len(data)):
        pl.append([(data[i][0] * data[i][1]), data[i][1]]);
        if(len(pl) >= l1):
            totalv = 0; totalp = 0;
            for a in range(len(pl)):
                totalv += pl[a][1];
                totalp += pl[a][0];
            vwap.append(totalp/totalv);
            pl = pl[1:];
    return vwap;
def mom(data, l1=10, p=False):
    mom = [];
    for i in range(l1-1, len(data)):
        mom.append(data[i] / data[i - (l1-1)] * 100) if p == True else mom.append(data[i] - data[i - (l1 - 1)]);
    return mom
def mom_osc(data, l1=9):
    pl = []; osc = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) > l1):
            sumh = 0; suml = 0;
            for a in range(1, l1):
                if(pl[a-1] < pl[a]): sumh = sumh+pl[a];
                else: suml = suml+pl[a];
            osc.append((sumh - suml) / (sumh + suml) * 100);
            pl = pl[1:];
    return osc;
def bop(data, l1=14):
    bo = [];
    for i in range(len(data)):
        bo.append((data[i][3] - data[i][0]) / (data[i][1] - data[i][2]));
    bo = sma(bo, l1);
    return bo;
def fi(data, l1=13):
    pl = []; ff = [];
    for i in range(1, len(data)):
        pl.append(data[i][0] - data[i-1][0]);
        if(len(pl) >= l1):
            vfi = ema(pl.copy(), l1);
            ff.append((data[i][0] - data[i-1][0]) * vfi[len(vfi)-1]);
            pl = pl[1:];
    return ff;
def asi(data):
    pl = []; a = [];
    for i in range(1, len(data)):
        c = data[i][1]; y = data[i-1][1]; h = data[i][0]; hy = data[i-1][0]; cy = data[i-1][1]
        l = data[i][2]; ly = data[i-1][2]; o = data[i][0]; oy = data[i-1][0]; t = max(data[i][0], data[i-1][0]) - min(data[i][2], data[i-1][2]);
        if(hy-c > ly-c): k = hy-c;
        else: k = ly-c;
        if(h - cy > l - cy & h - cy > h - l): r = h - cy - (l - cy) / 2 + (cy - oy) / 4;
        if(l - cy > h - cy & l - cy > h - l): r = l - cy - (h - cy) / 2 + (cy - oy) / 4;
        if(h - l > h - cy & h - l > l - cy): r = h - l + (cy - oy) / 4;
        a.append(50 * ((cy - c + (cy - oy) / 2 + (c - o) / 2) / r) * k / t);
    return a;
def ao(data, l1=5, l2=35):
    pl = []; a = [];
    for i in range(len(data)):
        pl.append((data[i][0] + data[i][1]) / 2);
        if(len(pl) >= l2):
            f = sma(pl.copy(), l1);
            s = sma(pl.copy(), l2);
            a.append(f[len(f)-1] - s[len(s)-1]);
            pl = pl[1:];
    return a;
def pr(data, l1=14):
    n = []; pl = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) >= l1):
            highd = max(pl.copy()); lowd = min(pl.copy());
            n.append((highd - data[i]) / (highd - lowd) * -100);
            pl = pl[1:];
    return n;
def lsma(data, l1=25):
    pl = []; lr = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) >= l1):
            sum_x = 0; sum_y = 0; sum_xy = 0; sum_xx = 0; sum_yy = 0;
            for a in range(1, len(pl)+1):
                sum_x += a;
                sum_y += pl[a-1];
                sum_xy += (pl[a-1] * a);
                sum_xx += (a*a);
                sum_yy += (pl[a-1] * pl[a-1]);
            m = ((sum_xy - sum_x * sum_y / l1) / (sum_xx - sum_x * sum_x / l1));
            b = sum_y / l1 - m * sum_x / l1;
            lr.append(m * l1 + b);
            pl = pl[1:];
    return lr;
def don(data, l1=20):
    pl = []; channel = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) >= l1):
            highs = []; lows = [];
            for h in range(len(pl)):
                highs.append(pl[h][0]);
                lows.append(pl[h][1]);
            m = max(highs); l = min(lows);
            channel.append([m, (m+l) / 2, l]);
            pl = pl[1:];
    return channel;
def ichimoku(data, l1=9, l2=26, l3=52, l4=26):
    cloud = []; place = []; pl = [];
    for i in range(len(data)):
        pl.append(data[i]);
        if(len(pl) > l3):
            highs = []; lows = [];
            for a in range(len(pl)):
                highs.append(pl[a][0]);
                lows.append(pl[a][2]);
            tsen = (max(highs[len(highs)-1-l1:len(highs)-1]) + (min(lows[len(lows)-1-l1:len(lows)-1]))) / 2;
            ksen = (max(highs[len(highs)-1-l2:len(highs)-1]) + (min(lows[len(lows)-1-l2:len(lows)-1]))) / 2;
            senka = data[i][1] + ksen;
            senkb = (max(highs[len(highs)-1-l3:len(highs)-1]) + (min(lows[len(lows)-1-l2:len(lows)-1]))) / 2;
            chik = data[i][1];
            place.append([tsen, ksen, senka, senkb, chik]);
            pl = pl[1:];
    for i in range(l4, len(place)-l4):
        if(place[i+l4-1]): cloud.append([place[i][0], place[i][1], place[i+l4-1][2], place[i+l4-1][3], place[i+l4-1][4]]);
    return cloud;
def stoch(data, l1=14, sd=3, sk=3):
    stoch = []; high = []; low = []; ka = [];
    for i in range(len(data)):
        high.append(data[i][0]);
        low.append(data[i][2]);
        if(len(high) >= l1):
            highd = max(high); lowd = min(low);
            k = 100 * (data[i][1] - lowd) / (highd - lowd);
            ka.append(k);
        if(sk > 0 & len(ka) > sk):
            smoothedk = sma(ka.copy(), sk);
            ka.push(smoothedk[len(smoothedk)-1]);
        if(len(ka) - sk >= sd):
            d = sma(ka.copy(), sd);
            stoch.append([k, d[len(d)-1]]);
            high = high[1:];
            low = low[1:];
            ka = ka[1:];
    return stoch;
