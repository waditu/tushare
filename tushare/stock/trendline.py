# -*- coding:utf-8 -*-

"""
股票技术指标接口
Created on 2018/07/26
@author: Wangzili
@group : **
@contact: 446406177@qq.com

所有指标中参数df为通过get_k_data获取的股票数据
"""
import pandas as pd
import numpy as np
import itertools


def ma(df, n=10):
    """
    移动平均线 Moving Average
    MA（N）=（第1日收盘价+第2日收盘价—+……+第N日收盘价）/N
    """
    pv = pd.DataFrame()
    pv['date'] = df['date']
    pv['v'] = df.close.rolling(n).mean()
    return pv


def _ma(series, n):
    """
    移动平均
    """
    return series.rolling(n).mean()


def md(df, n=10):
    """
    移动标准差
    STD=S（CLOSE,N）=[∑（CLOSE-MA(CLOSE，N)）^2/N]^0.5
    """
    _md = pd.DataFrame()
    _md['date'] = df.date
    _md["md"] = df.close.rolling(n).std(ddof=0)
    return _md


def _md(series, n):
    """
    标准差MD
    """
    return series.rolling(n).std(ddof=0)  # 有时候会用ddof=1


def ema(df, n=12):
    """
    指数平均数指标 Exponential Moving Average
    今日EMA（N）=2/（N+1）×今日收盘价+(N-1)/（N+1）×昨日EMA（N）
    EMA(X,N)=[2×X+(N-1)×EMA(ref(X),N]/(N+1)
    """
    _ema = pd.DataFrame()
    _ema['date'] = df['date']
    _ema['ema'] = df.close.ewm(ignore_na=False, span=n, min_periods=0, adjust=False).mean()
    return _ema


def _ema(series, n):
    """
    指数平均数
    """
    return series.ewm(ignore_na=False, span=n, min_periods=0, adjust=False).mean()


def macd(df, n=12, m=26, k=9):
    """
    平滑异同移动平均线(Moving Average Convergence Divergence)
    今日EMA（N）=2/（N+1）×今日收盘价+(N-1)/（N+1）×昨日EMA（N）
    DIFF= EMA（N1）- EMA（N2）
    DEA(DIF,M)= 2/(M+1)×DIF +[1-2/(M+1)]×DEA(REF(DIF,1),M)
    MACD（BAR）=2×（DIF-DEA）
    return:
          osc: MACD bar / OSC 差值柱形图 DIFF - DEM
          diff: 差离值
          dea: 讯号线
    """
    _macd = pd.DataFrame()
    _macd['date'] = df['date']
    _macd['diff'] = _ema(df.close, n) - _ema(df.close, m)
    _macd['dea'] = _ema(_macd['diff'], k)
    _macd['macd'] = _macd['diff'] - _macd['dea']
    return _macd


def kdj(df, n=9):
    """
    随机指标KDJ
    N日RSV=（第N日收盘价-N日内最低价）/（N日内最高价-N日内最低价）×100%
    当日K值=2/3前1日K值+1/3×当日RSV=SMA（RSV,M1）
    当日D值=2/3前1日D值+1/3×当日K= SMA（K,M2）
    当日J值=3 ×当日K值-2×当日D值
    """
    _kdj = pd.DataFrame()
    _kdj['date'] = df['date']
    rsv = (df.close - df.low.rolling(n).min()) / (df.high.rolling(n).max() - df.low.rolling(n).min()) * 100
    _kdj['k'] = sma(rsv, 3)
    _kdj['d'] = sma(_kdj.k, 3)
    _kdj['j'] = 3 * _kdj.k - 2 * _kdj.d
    return _kdj


def rsi(df, n=6):
    """
    相对强弱指标（Relative Strength Index，简称RSI
    LC= REF(CLOSE,1)
    RSI=SMA(MAX(CLOSE-LC,0),N,1)/SMA(ABS(CLOSE-LC),N1,1)×100
    SMA（C,N,M）=M/N×今日收盘价+(N-M)/N×昨日SMA（N）
    """
    # pd.set_option('display.max_rows', 1000)
    _rsi = pd.DataFrame()
    _rsi['date'] = df['date']
    px = df.close - df.close.shift(1)
    px[px < 0] = 0
    _rsi['rsi'] = sma(px, n) / sma((df['close'] - df['close'].shift(1)).abs(), n) * 100
    # def tmax(x):
    #     if x < 0:
    #         x = 0
    #     return x
    # _rsi['rsi'] = sma((df['close'] - df['close'].shift(1)).apply(tmax), n) / sma((df['close'] - df['close'].shift(1)).abs(), n) * 100
    return _rsi


def vrsi(df, n=6):
    """
    量相对强弱指标
    VRSI=SMA（最大值（成交量-REF（成交量，1），0），N,1）/SMA（ABS（（成交量-REF（成交量，1），N，1）×100%
    """
    _vrsi = pd.DataFrame()
    _vrsi['date'] = df['date']
    px = df['volume'] - df['volume'].shift(1)
    px[px < 0] = 0
    _vrsi['vrsi'] = sma(px, n) / sma((df['volume'] - df['volume'].shift(1)).abs(), n) * 100
    return _vrsi


def boll(df, n=26, k=2):
    """
    布林线指标BOLL boll(26,2)	MID=MA(N)
    标准差MD=根号[∑（CLOSE-MA(CLOSE，N)）^2/N]
    UPPER=MID＋k×MD
    LOWER=MID－k×MD
    """
    _boll = pd.DataFrame()
    _boll['date'] = df.date
    _boll['mid'] = _ma(df.close, n)
    _mdd = _md(df.close, n)
    _boll['up'] = _boll.mid + k * _mdd
    _boll['low'] = _boll.mid - k * _mdd
    return _boll


def bbiboll(df, n=10, k=3):
    """
    BBI多空布林线	bbiboll(10,3)
    BBI={MA(3)+ MA(6)+ MA(12)+ MA(24)}/4
    标准差MD=根号[∑（BBI-MA(BBI，N)）^2/N]
    UPR= BBI＋k×MD
    DWN= BBI－k×MD
    """
    # pd.set_option('display.max_rows', 1000)
    _bbiboll = pd.DataFrame()
    _bbiboll['date'] = df.date
    _bbiboll['bbi'] = (_ma(df.close, 3) + _ma(df.close, 6) + _ma(df.close, 12) + _ma(df.close, 24)) / 4
    _bbiboll['md'] = _md(_bbiboll.bbi, n)
    _bbiboll['upr'] = _bbiboll.bbi + k * _bbiboll.md
    _bbiboll['dwn'] = _bbiboll.bbi - k * _bbiboll.md
    return _bbiboll


def wr(df, n=14):
    """
    威廉指标 w&r
    WR=[最高值（最高价，N）-收盘价]/[最高值（最高价，N）-最低值（最低价，N）]×100%
    """

    _wr = pd.DataFrame()
    _wr['date'] = df['date']
    higest = df.high.rolling(n).max()
    _wr['wr'] = (higest - df.close) / (higest - df.low.rolling(n).min()) * 100
    return _wr


def bias(df, n=12):
    """
    乖离率 bias
    bias=[(当日收盘价-12日平均价)/12日平均价]×100%
    """
    _bias = pd.DataFrame()
    _bias['date'] = df.date
    _mav = df.close.rolling(n).mean()
    _bias['bias'] = (np.true_divide((df.close - _mav), _mav)) * 100
    # _bias["bias"] = np.vectorize(lambda x: round(Decimal(x), 4))(BIAS)
    return _bias


def asi(df, n=5):
    """
    振动升降指标(累计震动升降因子) ASI  # 同花顺给出的公式不完整就不贴出来了
    """
    _asi = pd.DataFrame()
    _asi['date'] = df.date
    _m = pd.DataFrame()
    _m['a'] = (df.high - df.close.shift()).abs()
    _m['b'] = (df.low - df.close.shift()).abs()
    _m['c'] = (df.high - df.low.shift()).abs()
    _m['d'] = (df.close.shift() - df.open.shift()).abs()
    _m['r'] = _m.apply(lambda x: x.a + 0.5 * x.b + 0.25 * x.d if max(x.a, x.b, x.c) == x.a else (
        x.b + 0.5 * x.a + 0.25 * x.d if max(x.a, x.b, x.c) == x.b else x.c + 0.25 * x.d
    ), axis=1)
    _m['x'] = df.close - df.close.shift() + 0.5 * (df.close - df.open) + df.close.shift() - df.open.shift()
    _m['k'] = np.maximum(_m.a, _m.b)
    _asi['si'] = 16 * (_m.x / _m.r) * _m.k
    _asi["asi"] = _ma(_asi.si, n)
    return _asi


def vr_rate(df, n=26):
    """
    成交量变异率 vr or vr_rate
    VR=（AVS+1/2CVS）/（BVS+1/2CVS）×100
    其中：
    AVS：表示N日内股价上涨成交量之和
    BVS：表示N日内股价下跌成交量之和
    CVS：表示N日内股价不涨不跌成交量之和
    """
    _vr = pd.DataFrame()
    _vr['date'] = df['date']
    _m = pd.DataFrame()
    _m['volume'] = df.volume
    _m['cs'] = df.close - df.close.shift(1)
    _m['avs'] = _m.apply(lambda x: x.volume if x.cs > 0 else 0, axis=1)
    _m['bvs'] = _m.apply(lambda x: x.volume if x.cs < 0 else 0, axis=1)
    _m['cvs'] = _m.apply(lambda x: x.volume if x.cs == 0 else 0, axis=1)
    _vr["vr"] = (_m.avs.rolling(n).sum() + 1 / 2 * _m.cvs.rolling(n).sum()
                 ) / (_m.bvs.rolling(n).sum() + 1 / 2 * _m.cvs.rolling(n).sum()) * 100
    return _vr


def vr(df, n=5):
    """
    开市后平均每分钟的成交量与过去5个交易日平均每分钟成交量之比
    量比:=V/REF(MA(V,5),1);
    涨幅:=(C-REF(C,1))/REF(C,1)*100;
    1)量比大于1.8，涨幅小于2%，现价涨幅在0—2%之间，在盘中选股的
    选股:量比>1.8 AND 涨幅>0 AND 涨幅<2;
    """
    _vr = pd.DataFrame()
    _vr['date'] = df.date
    _vr['vr'] = df.volume / _ma(df.volume, n).shift(1)
    _vr['rr'] = (df.close - df.close.shift(1)) / df.close.shift(1) * 100
    return _vr


def arbr(df, n=26):
    """
    人气意愿指标	arbr(26)
    N日AR=N日内（H－O）之和除以N日内（O－L）之和
    其中，H为当日最高价，L为当日最低价，O为当日开盘价，N为设定的时间参数，一般原始参数日设定为26日
    N日BR=N日内（H－CY）之和除以N日内（CY－L）之和
    其中，H为当日最高价，L为当日最低价，CY为前一交易日的收盘价，N为设定的时间参数，一般原始参数日设定为26日。
    """
    _arbr = pd.DataFrame()
    _arbr['date'] = df.date
    _arbr['ar'] = (df.high - df.open).rolling(n).sum() / (df.open - df.low).rolling(n).sum() * 100
    _arbr['br'] = (df.high - df.close.shift(1)).rolling(n).sum() / (df.close.shift() - df.low).rolling(n).sum() * 100
    return _arbr


def dpo(df, n=20, m=6):
    """
    区间震荡线指标	dpo(20,6)
    DPO=CLOSE-MA（CLOSE, N/2+1）
    MADPO=MA（DPO,M）
    """
    _dpo = pd.DataFrame()
    _dpo['date'] = df['date']
    _dpo['dpo'] = df.close - _ma(df.close, int(n / 2 + 1))
    _dpo['dopma'] = _ma(_dpo.dpo, m)
    return _dpo


def trix(df, n=12, m=20):
    """
    三重指数平滑平均	TRIX(12)
    TR= EMA(EMA(EMA(CLOSE,N),N),N)，即进行三次平滑处理
    TRIX=(TR-昨日TR)/ 昨日TR×100
    TRMA=MA（TRIX，M）
    """
    _trix = pd.DataFrame()
    _trix['date'] = df.date
    tr = _ema(_ema(_ema(df.close, n), n), n)
    _trix['trix'] = (tr - tr.shift()) / tr.shift() * 100
    _trix['trma'] = _ma(_trix.trix, m)
    return _trix


def bbi(df):
    """
    多空指数	BBI(3,6,12,24)
    BBI=（3日均价+6日均价+12日均价+24日均价）/4
    """
    _bbi = pd.DataFrame()
    _bbi['date'] = df['date']
    _bbi['bbi'] = (_ma(df.close, 3) + _ma(df.close, 6) + _ma(df.close, 12) + _ma(df.close, 24)) / 4
    return _bbi


def mtm(df, n=6, m=5):
    """
    动力指标	MTM(6,5)
    MTM（N日）=C-REF(C,N)式中，C=当日的收盘价，REF(C,N)=N日前的收盘价；N日是只计算交易日期，剔除掉节假日。
    MTMMA（MTM，N1）= MA（MTM，N1）
    N表示间隔天数，N1表示天数
    """
    _mtm = pd.DataFrame()
    _mtm['date'] = df.date
    _mtm['mtm'] = df.close - df.close.shift(n)
    _mtm['mtmma'] = _ma(_mtm.mtm, m)
    return _mtm


def obv(df):
    """
    能量潮  On Balance Volume
    多空比率净额= [（收盘价－最低价）－（最高价-收盘价）] ÷（ 最高价－最低价）×V  # 同花顺貌似用的下面公式
    主公式：当日OBV=前一日OBV+今日成交量
    1.基期OBV值为0，即该股上市的第一天，OBV值为0
    2.若当日收盘价＞上日收盘价，则当日OBV=前一日OBV＋今日成交量
    3.若当日收盘价＜上日收盘价，则当日OBV=前一日OBV－今日成交量
    4.若当日收盘价＝上日收盘价，则当日OBV=前一日OBV
    """
    _obv = pd.DataFrame()
    _obv["date"] = df['date']
    # tmp = np.true_divide(((df.close - df.low) - (df.high - df.close)), (df.high - df.low))
    # _obv['obvv'] = tmp * df.volume
    # _obv["obv"] = _obv.obvv.expanding(1).sum() / 100
    _m = pd.DataFrame()
    _m['date'] = df.date
    _m['cs'] = df.close - df.close.shift()
    _m['v'] = df.volume
    _m['vv'] = _m.apply(lambda x: x.v if x.cs > 0 else (-x.v if x.cs < 0 else 0), axis=1)
    _obv['obv'] = _m.vv.expanding(1).sum()
    return _obv


def cci(df, n=14):
    """
    顺势指标
    TYP:=(HIGH+LOW+CLOSE)/3
    CCI:=(TYP-MA(TYP,N))/(0.015×AVEDEV(TYP,N))
    """
    _cci = pd.DataFrame()
    _cci["date"] = df['date']
    typ = (df.high + df.low + df.close) / 3
    _cci['cci'] = ((typ - typ.rolling(n).mean()) /
                   (0.015 * typ.rolling(min_periods=1, center=False, window=n).apply(
                    lambda x: np.fabs(x - x.mean()).mean())))
    return _cci


def priceosc(df, n=12, m=26):
    """
    价格振动指数
    PRICEOSC=(MA(C,12)-MA(C,26))/MA(C,12) * 100
    """
    _c = pd.DataFrame()
    _c['date'] = df['date']
    man = _ma(df.close, n)
    _c['osc'] = (man - _ma(df.close, m)) / man * 100
    return _c


def sma(a, n, m=1):
    """
    平滑移动指标 Smooth Moving Average
    """
    ''' # 方法一，此方法有缺陷
    _sma = []
    for index, value in enumerate(a):
        if index == 0 or pd.isna(value) or np.isnan(value):
            tsma = 0
        else:
            # Y=(M*X+(N-M)*Y')/N
            tsma = (m * value + (n - m) * tsma) / n
        _sma.append(tsma)
    return pd.Series(_sma)
    '''
    ''' # 方法二

    results = np.nan_to_num(a).copy()
    # FIXME this is very slow
    for i in range(1, len(a)):
        results[i] = (m * results[i] + (n - m) * results[i - 1]) / n
        # results[i] = ((n - 1) * results[i - 1] + results[i]) / n
    # return results
    '''
    # b = np.nan_to_num(a).copy()
    # return ((n - m) * a.shift(1) + m * a) / n

    a = a.fillna(0)
    b = a.ewm(min_periods=0, ignore_na=False, adjust=False, alpha=m/n).mean()
    return b


def dbcd(df, n=5, m=16, t=76):
    """
    异同离差乖离率	dbcd(5,16,76)
    BIAS=(C-MA(C,N))/MA(C,N)
    DIF=(BIAS-REF(BIAS,M))
    DBCD=SMA(DIF,T,1) =（1-1/T）×SMA(REF(DIF,1),T,1)+ 1/T×DIF
    MM=MA(DBCD,5)
    """
    _dbcd = pd.DataFrame()
    _dbcd['date'] = df.date
    man = _ma(df.close, n)
    _bias = (df.close - man) / man
    _dif = _bias - _bias.shift(m)
    _dbcd['dbcd'] = sma(_dif, t)
    _dbcd['mm'] = _ma(_dbcd.dbcd, n)
    return _dbcd


def roc(df, n=12, m=6):
    """
    变动速率	roc(12,6)
    ROC=(今日收盘价-N日前的收盘价)/ N日前的收盘价×100%
    ROCMA=MA（ROC，M）
    ROC:(CLOSE-REF(CLOSE,N))/REF(CLOSE,N)×100
    ROCMA:MA(ROC,M)
    """
    _roc = pd.DataFrame()
    _roc['date'] = df['date']
    _roc['roc'] = (df.close - df.close.shift(n))/df.close.shift(n) * 100
    _roc['rocma'] = _ma(_roc.roc, m)
    return _roc


def vroc(df, n=12):
    """
    量变动速率
    VROC=(当日成交量-N日前的成交量)/ N日前的成交量×100%
    """
    _vroc = pd.DataFrame()
    _vroc['date'] = df['date']
    _vroc['vroc'] = (df.volume - df.volume.shift(n)) / df.volume.shift(n) * 100
    return _vroc


def cr(df, n=26):
    """ 能量指标
    CR=∑（H-PM）/∑（PM-L）×100
    PM:上一交易日中价（(最高、最低、收盘价的均值)
    H：当天最高价
    L：当天最低价
    """
    _cr = pd.DataFrame()
    _cr['date'] = df.date
    # pm = ((df['high'] + df['low'] + df['close']) / 3).shift(1)
    pm = (df[['high', 'low', 'close']]).mean(axis=1).shift(1)
    _cr['cr'] = (df.high - pm).rolling(n).sum()/(pm - df.low).rolling(n).sum() * 100
    return _cr


def psy(df, n=12):
    """
    心理指标	PSY(12)
    PSY=N日内上涨天数/N×100
    PSY:COUNT(CLOSE>REF(CLOSE,1),N)/N×100
    MAPSY=PSY的M日简单移动平均
    """
    _psy = pd.DataFrame()
    _psy['date'] = df.date
    p = df.close - df.close.shift()
    p[p <= 0] = np.nan
    _psy['psy'] = p.rolling(n).count() / n * 100
    return _psy


def wad(df, n=30):
    """
    威廉聚散指标	WAD(30)
    TRL=昨日收盘价与今日最低价中价格最低者；TRH=昨日收盘价与今日最高价中价格最高者
    如果今日的收盘价>昨日的收盘价，则今日的A/D=今日的收盘价－今日的TRL
    如果今日的收盘价<昨日的收盘价，则今日的A/D=今日的收盘价－今日的TRH
    如果今日的收盘价=昨日的收盘价，则今日的A/D=0
    WAD=今日的A/D+昨日的WAD；MAWAD=WAD的M日简单移动平均
    """
    def dmd(x):
        if x.c > 0:
            y = x.close - x.trl
        elif x.c < 0:
            y = x.close - x.trh
        else:
            y = 0
        return y

    _wad = pd.DataFrame()
    _wad['date'] = df['date']
    _ad = pd.DataFrame()
    _ad['trl'] = np.minimum(df.low, df.close.shift(1))
    _ad['trh'] = np.maximum(df.high, df.close.shift(1))
    _ad['c'] = df.close - df.close.shift()
    _ad['close'] = df.close
    _ad['ad'] = _ad.apply(dmd, axis=1)
    _wad['wad'] = _ad.ad.expanding(1).sum()
    _wad['mawad'] = _ma(_wad.wad, n)
    return _wad


def mfi(df, n=14):
    """
    资金流向指标	mfi(14)
    MF＝TYP×成交量；TYP:当日中价（(最高、最低、收盘价的均值)
    如果当日TYP>昨日TYP，则将当日的MF值视为当日PMF值。而当日NMF值＝0
    如果当日TYP<=昨日TYP，则将当日的MF值视为当日NMF值。而当日PMF值=0
    MR=∑PMF/∑NMF
    MFI＝100-（100÷(1＋MR)）
    """
    _mfi = pd.DataFrame()
    _mfi['date'] = df.date
    _m = pd.DataFrame()
    _m['typ'] = df[['high', 'low', 'close']].mean(axis=1)
    _m['mf'] = _m.typ * df.volume
    _m['typ_shift'] = _m.typ - _m.typ.shift(1)
    _m['pmf'] = _m.apply(lambda x: x.mf if x.typ_shift > 0 else 0, axis=1)
    _m['nmf'] = _m.apply(lambda x: x.mf if x.typ_shift <= 0 else 0, axis=1)
    # _mfi['mfi'] = 100 - (100 / (1 + _m.pmf.rolling(n).sum() / _m.nmf.rolling(n).sum()))
    _m['mr'] = _m.pmf.rolling(n).sum() / _m.nmf.rolling(n).sum()
    _mfi['mfi'] = 100 * _m.mr / (1 + _m.mr)  # 同花顺自己给出的公式和实际用的公式不一样，真操蛋，浪费两个小时时间
    return _mfi


def pvt(df):
    """
    pvt	量价趋势指标	pvt
    如果设x=(今日收盘价—昨日收盘价)/昨日收盘价×当日成交量，
    那么当日PVT指标值则为从第一个交易日起每日X值的累加。
    """
    _pvt = pd.DataFrame()
    _pvt['date'] = df.date

    x = (df.close - df.close.shift(1)) / df.close.shift(1) * df.volume
    _pvt['pvt'] = x.expanding(1).sum()
    return _pvt


def wvad(df, n=24, m=6):
    """  # 算法是对的，同花顺计算wvad用的n=6
    威廉变异离散量	wvad(24,6)
    WVAD=N1日的∑ {(当日收盘价－当日开盘价)/(当日最高价－当日最低价)×成交量}
    MAWVAD=MA（WVAD，N2）
    """
    _wvad = pd.DataFrame()
    _wvad['date'] = df.date
    # _wvad['wvad'] = (np.true_divide((df.close - df.open), (df.high - df.low)) * df.volume).rolling(n).sum()
    _wvad['wvad'] = (np.true_divide((df.close - df.open), (df.high - df.low)) * df.volume).rolling(n).sum()
    _wvad['mawvad'] = _ma(_wvad.wvad, m)
    return _wvad


def cdp(df):
    """
    逆势操作	cdp
    CDP=(最高价+最低价+收盘价)/3  # 同花顺实际用的(H+L+2*c)/4
    AH=CDP+(前日最高价-前日最低价)
    NH=CDP×2-最低价
    NL=CDP×2-最高价
    AL=CDP-(前日最高价-前日最低价)
    """
    _cdp = pd.DataFrame()
    _cdp['date'] = df.date
    # _cdp['cdp'] = (df.high + df.low + df.close * 2).shift(1) / 4
    _cdp['cdp'] = df[['high', 'low', 'close', 'close']].shift().mean(axis=1)
    _cdp['ah'] = _cdp.cdp + (df.high.shift(1) - df.low.shift())
    _cdp['al'] = _cdp.cdp - (df.high.shift(1) - df.low.shift())
    _cdp['nh'] = _cdp.cdp * 2 - df.low.shift(1)
    _cdp['nl'] = _cdp.cdp * 2 - df.high.shift(1)
    return _cdp


def env(df, n=14):
    """
    ENV指标	ENV(14)
    Upper=MA(CLOSE，N)×1.06
    LOWER= MA(CLOSE，N)×0.94
    """
    _env = pd.DataFrame()
    _env['date'] = df.date
    _env['up'] = df.close.rolling(n).mean() * 1.06
    _env['low'] = df.close.rolling(n).mean() * 0.94
    return _env


def mike(df, n=12):
    """
    麦克指标	mike(12)
    初始价（TYP）=（当日最高价＋当日最低价＋当日收盘价）/3
    HV=N日内区间最高价
    LV=N日内区间最低价
    初级压力线（WR）=TYP×2-LV
    中级压力线（MR）=TYP+HV-LV
    强力压力线（SR）=2×HV-LV
    初级支撑线（WS）=TYP×2-HV
    中级支撑线（MS）=TYP-HV+LV
    强力支撑线（SS）=2×LV-HV
    """
    _mike = pd.DataFrame()
    _mike['date'] = df.date
    typ = df[['high', 'low', 'close']].mean(axis=1)
    hv = df.high.rolling(n).max()
    lv = df.low.rolling(n).min()
    _mike['wr'] = typ * 2 - lv
    _mike['mr'] = typ + hv - lv
    _mike['sr'] = 2 * hv - lv
    _mike['ws'] = typ * 2 - hv
    _mike['ms'] = typ - hv + lv
    _mike['ss'] = 2 * lv - hv
    return _mike


def vma(df, n=5):
    """
    量简单移动平均	VMA(5)	VMA=MA(volume,N)
    VOLUME表示成交量；N表示天数
    """
    _vma = pd.DataFrame()
    _vma['date'] = df.date
    _vma['vma'] = _ma(df.volume, n)
    return _vma


def vmacd(df, qn=12, sn=26, m=9):
    """
    量指数平滑异同平均	vmacd(12,26,9)
    今日EMA（N）=2/（N+1）×今日成交量+(N-1)/（N+1）×昨日EMA（N）
    DIFF= EMA（N1）- EMA（N2）
    DEA(DIF,M)= 2/(M+1)×DIF +[1-2/(M+1)]×DEA(REF(DIF,1),M)
    MACD（BAR）=2×（DIF-DEA）
    """
    _vmacd = pd.DataFrame()
    _vmacd['date'] = df.date
    _vmacd['diff'] = _ema(df.volume, qn) - _ema(df.volume, sn)
    _vmacd['dea'] = _ema(_vmacd['diff'], m)  # TODO: 不能用_vmacd.diff, 不知道为什么
    _vmacd['macd'] = (_vmacd['diff'] - _vmacd['dea'])
    return _vmacd


def vosc(df, n=12, m=26):
    """
    成交量震荡	vosc(12,26)
    VOSC=（MA（VOLUME,SHORT）- MA（VOLUME,LONG））/MA（VOLUME,SHORT）×100
    """
    _c = pd.DataFrame()
    _c['date'] = df['date']
    _c['osc'] = (_ma(df.volume, n) - _ma(df.volume, m)) / _ma(df.volume, n) * 100
    return _c


def tapi(df, n=6):
    """ # TODO: 由于get_k_data返回数据中没有amount，可以用get_h_data中amount，算法是正确的
    加权指数成交值	tapi(6)
    TAPI=每日成交总值/当日加权指数=a/PI；A表示每日的成交金额，PI表示当天的股价指数即指收盘价
    """
    _tapi = pd.DataFrame()
    # _tapi['date'] = df.date
    _tapi['tapi'] = df.amount / df.close
    _tapi['matapi'] = _ma(_tapi.tapi, n)
    return _tapi


def vstd(df, n=10):
    """
    成交量标准差	vstd(10)
    VSTD=STD（Volume,N）=[∑（Volume-MA(Volume，N)）^2/N]^0.5
    """
    _vstd = pd.DataFrame()
    _vstd['date'] = df.date
    _vstd['vstd'] = df.volume.rolling(n).std(ddof=1)
    return _vstd


def adtm(df, n=23, m=8):
    """
    动态买卖气指标	adtm(23,8)
    如果开盘价≤昨日开盘价，DTM=0
    如果开盘价＞昨日开盘价，DTM=(最高价-开盘价)和(开盘价-昨日开盘价)的较大值
    如果开盘价≥昨日开盘价，DBM=0
    如果开盘价＜昨日开盘价，DBM=(开盘价-最低价)
    STM=DTM在N日内的和
    SBM=DBM在N日内的和
    如果STM > SBM,ADTM=(STM-SBM)/STM
    如果STM < SBM , ADTM = (STM-SBM)/SBM
    如果STM = SBM,ADTM=0
    ADTMMA=MA(ADTM,M)
    """
    _adtm = pd.DataFrame()
    _adtm['date'] = df.date
    _m = pd.DataFrame()
    _m['cc'] = df.open - df.open.shift(1)
    _m['ho'] = df.high - df.open
    _m['ol'] = df.open - df.low
    _m['dtm'] = _m.apply(lambda x: max(x.ho, x.cc) if x.cc > 0 else 0, axis=1)
    _m['dbm'] = _m.apply(lambda x: x.ol if x.cc < 0 else 0, axis=1)
    _m['stm'] = _m.dtm.rolling(n).sum()
    _m['sbm'] = _m.dbm.rolling(n).sum()
    _m['ss'] = _m.stm - _m.sbm
    _adtm['adtm'] = _m.apply(lambda x: x.ss / x.stm if x.ss > 0 else (x.ss / x.sbm if x.ss < 0 else 0), axis=1)
    _adtm['adtmma'] = _ma(_adtm.adtm, m)
    return _adtm


def mi(df, n=12):
    """
    动量指标	mi(12)
    A=CLOSE-REF(CLOSE,N)
    MI=SMA(A,N,1)
    """
    _mi = pd.DataFrame()
    _mi['date'] = df.date
    _mi['mi'] = sma(df.close - df.close.shift(n), n)
    return _mi


def micd(df, n=3, m=10, k=20):
    """
    异同离差动力指数	micd(3,10,20)
    MI=CLOSE-ref(CLOSE,1)AMI=SMA(MI,N1,1)
    DIF=MA(ref(AMI,1),N2)-MA(ref(AMI,1),N3)
    MICD=SMA(DIF,10,1)
    """
    _micd = pd.DataFrame()
    _micd['date'] = df.date
    mi = df.close - df.close.shift(1)
    ami = sma(mi, n)
    dif = _ma(ami.shift(1), m) - _ma(ami.shift(1), k)
    _micd['micd'] = sma(dif, m)
    return _micd


def rc(df, n=50):
    """
    变化率指数	rc(50)
    RC=收盘价/REF（收盘价，N）×100
    ARC=EMA（REF（RC，1），N，1）
    """
    _rc = pd.DataFrame()
    _rc['date'] = df.date
    _rc['rc'] = df.close / df.close.shift(n) * 100
    _rc['arc'] = sma(_rc.rc.shift(1), n)
    return _rc


def rccd(df, n=59, m=21, k=28):
    """  # TODO: 计算结果错误和同花顺不同，检查不出来为什么
    异同离差变化率指数 rate of change convergence divergence	rccd(59,21,28)
    RC=收盘价/REF（收盘价，N）×100%
    ARC=EMA(REF(RC,1),N,1)
    DIF=MA(ref(ARC,1),N1)-MA MA(ref(ARC,1),N2)
    RCCD=SMA(DIF,N,1)
    """
    _rccd = pd.DataFrame()
    _rccd['date'] = df.date
    rc = df.close / df.close.shift(n) * 100
    arc = sma(rc.shift(), n)
    dif = _ma(arc.shift(), m) - _ma(arc.shift(), k)
    _rccd['rccd'] = sma(dif, n)
    return _rccd


def srmi(df, n=9):
    """
    SRMIMI修正指标	srmi(9)
    如果收盘价>N日前的收盘价，SRMI就等于（收盘价-N日前的收盘价）/收盘价
    如果收盘价<N日前的收盘价，SRMI就等于（收盘价-N日签的收盘价）/N日前的收盘价
    如果收盘价=N日前的收盘价，SRMI就等于0
    """
    _srmi = pd.DataFrame()
    _srmi['date'] = df.date
    _m = pd.DataFrame()
    _m['close'] = df.close
    _m['cp'] = df.close.shift(n)
    _m['cs'] = df.close - df.close.shift(n)
    _srmi['srmi'] = _m.apply(lambda x: x.cs/x.close if x.cs > 0 else (x.cs/x.cp if x.cs < 0 else 0), axis=1)
    return _srmi


def dptb(df, n=7):
    """
    大盘同步指标	dptb(7)
    DPTB=（统计N天中个股收盘价>开盘价，且指数收盘价>开盘价的天数或者个股收盘价<开盘价，且指数收盘价<开盘价）/N
    """
    ind = ts.get_k_data("sh000001", start=df.date.iloc[0], end=df.date.iloc[-1])
    sd = df.copy()
    sd.set_index('date', inplace=True)  # 可能出现停盘等情况，所以将date设为index
    ind.set_index('date', inplace=True)
    _dptb = pd.DataFrame(index=df.date)
    q = ind.close - ind.open
    _dptb['p'] = sd.close - sd.open
    _dptb['q'] = q
    _dptb['m'] = _dptb.apply(lambda x: 1 if (x.p > 0 and x.q > 0) or (x.p < 0 and x.q < 0) else np.nan, axis=1)
    _dptb['jdrs'] = _dptb.m.rolling(n).count() / n
    _dptb.drop(columns=['p', 'q', 'm'], inplace=True)
    _dptb.reset_index(inplace=True)
    return _dptb


def jdqs(df, n=20):
    """
    阶段强势指标	jdqs(20)
    JDQS=（统计N天中个股收盘价>开盘价，且指数收盘价<开盘价的天数）/（统计N天中指数收盘价<开盘价的天数）
    """
    ind = ts.get_k_data("sh000001", start=df.date.iloc[0], end=df.date.iloc[-1])
    sd = df.copy()
    sd.set_index('date', inplace=True)   # 可能出现停盘等情况，所以将date设为index
    ind.set_index('date', inplace=True)
    _jdrs = pd.DataFrame(index=df.date)
    q = ind.close - ind.open
    _jdrs['p'] = sd.close - sd.open
    _jdrs['q'] = q
    _jdrs['m'] = _jdrs.apply(lambda x: 1 if (x.p > 0 and x.q < 0) else np.nan, axis=1)
    q[q > 0] = np.nan
    _jdrs['t'] = q
    _jdrs['jdrs'] = _jdrs.m.rolling(n).count() / _jdrs.t.rolling(n).count()
    _jdrs.drop(columns=['p', 'q', 'm', 't'], inplace=True)
    _jdrs.reset_index(inplace=True)
    return _jdrs


def jdrs(df, n=20):
    """
    阶段弱势指标	jdrs(20)
    JDRS=（统计N天中个股收盘价<开盘价，且指数收盘价>开盘价的天数）/（统计N天中指数收盘价>开盘价的天数）
    """
    ind = ts.get_k_data("sh000001", start=df.date.iloc[0], end=df.date.iloc[-1])
    sd = df.copy()
    sd.set_index('date', inplace=True)
    ind.set_index('date', inplace=True)
    _jdrs = pd.DataFrame(index=df.date)
    q = ind.close - ind.open
    _jdrs['p'] = sd.close - sd.open
    _jdrs['q'] = q
    _jdrs['m'] = _jdrs.apply(lambda x: 1 if (x.p < 0 and x.q > 0) else np.nan, axis=1)
    q[q < 0] = np.nan
    _jdrs['t'] = q
    _jdrs['jdrs'] = _jdrs.m.rolling(n).count() / _jdrs.t.rolling(n).count()
    _jdrs.drop(columns=['p', 'q', 'm', 't'], inplace=True)
    _jdrs.reset_index(inplace=True)
    return _jdrs


def zdzb(df, n=125, m=5, k=20):
    """
    筑底指标	zdzb(125,5,20)
    A=（统计N1日内收盘价>=前收盘价的天数）/（统计N1日内收盘价<前收盘价的天数）
    B=MA（A,N2）
    D=MA（A，N3）
    """
    _zdzb = pd.DataFrame()
    _zdzb['date'] = df.date
    p = df.close - df.close.shift(1)
    q = p.copy()
    p[p < 0] = np.nan
    q[q >= 0] = np.nan
    _zdzb['a'] = p.rolling(n).count() / q.rolling(n).count()
    _zdzb['b'] = _zdzb.a.rolling(m).mean()
    _zdzb['d'] = _zdzb.a.rolling(k).mean()
    return _zdzb


def atr(df, n=14):
    """
    真实波幅	atr(14)
    TR:MAX(MAX((HIGH-LOW),ABS(REF(CLOSE,1)-HIGH)),ABS(REF(CLOSE,1)-LOW))
    ATR:MA(TR,N)
    """
    _atr = pd.DataFrame()
    _atr['date'] = df.date
    # _atr['tr'] = np.maximum(df.high - df.low, (df.close.shift(1) - df.low).abs())
    # _atr['tr'] = np.maximum.reduce([df.high - df.low, (df.close.shift(1) - df.high).abs(), (df.close.shift(1) - df.low).abs()])
    _atr['tr'] = np.vstack([df.high - df.low, (df.close.shift(1) - df.high).abs(), (df.close.shift(1) - df.low).abs()]).max(axis=0)
    _atr['atr'] = _atr.tr.rolling(n).mean()
    return _atr


def mass(df, n=9, m=25):
    """
    梅丝线	mass(9,25)
    AHL=MA(（H-L）,N1)
    BHL= MA（AHL，N1）
    MASS=SUM（AHL/BHL，N2）
    H：表示最高价；L：表示最低价
    """
    _mass = pd.DataFrame()
    _mass['date'] = df.date
    ahl = _ma((df.high - df.low), n)
    bhl = _ma(ahl, n)
    _mass['mass'] = (ahl / bhl).rolling(m).sum()
    return _mass


def vhf(df, n=28):
    """
    纵横指标	vhf(28)
    VHF=（N日内最大收盘价与N日内最小收盘价之前的差）/（N日收盘价与前收盘价差的绝对值之和）
    """
    _vhf = pd.DataFrame()
    _vhf['date'] = df.date
    _vhf['vhf'] = (df.close.rolling(n).max() - df.close.rolling(n).min()) / (df.close - df.close.shift(1)).abs().rolling(n).sum()
    return _vhf


def cvlt(df, n=10):
    """
    佳庆离散指标	cvlt(10)
    cvlt=（最高价与最低价的差的指数移动平均-前N日的最高价与最低价的差的指数移动平均）/前N日的最高价与最低价的差的指数移动平均
    """
    _cvlt = pd.DataFrame()
    _cvlt['date'] = df.date
    p = _ema(df.high.shift(n) - df.low.shift(n), n)
    _cvlt['cvlt'] = (_ema(df.high - df.low, n) - p) / p * 100
    return _cvlt


def up_n(df):
    """
    连涨天数	up_n	连续上涨天数，当天收盘价大于开盘价即为上涨一天 # 同花顺实际结果用收盘价-前一天收盘价
    """
    _up = pd.DataFrame()
    _up['date'] = df.date
    p = df.close - df.close.shift()
    p[p > 0] = 1
    p[p < 0] = 0
    m = []
    for k, g in itertools.groupby(p):
        t = 0
        for i in g:
            if k == 0:
                m.append(0)
            else:
                t += 1
                m.append(t)
    # _up['p'] = p
    _up['up'] = m
    return _up


def down_n(df):
    """
    连跌天数	down_n	连续下跌天数，当天收盘价小于开盘价即为下跌一天
    """
    _down = pd.DataFrame()
    _down['date'] = df.date
    p = df.close - df.close.shift()
    p[p > 0] = 0
    p[p < 0] = 1
    m = []
    for k, g in itertools.groupby(p):
        t = 0
        for i in g:
            if k == 0:
                m.append(0)
            else:
                t += 1
                m.append(t)
    _down['down'] = m
    return _down


def join_frame(d1, d2, column='date'):
    # 将两个DataFrame 按照datetime合并
    return d1.join(d2.set_index(column), on=column)


if __name__ == "__main__":
    import tushare as ts
    # data = ts.get_k_data("000063", start="2017-05-01")
    data = ts.get_k_data("601138", start="2017-05-01")
    # print(data)
    # maf = ma(data, n=[5, 10, 20])
    # 将均线合并到data中
    # print(join_frame(data, maf))

    # data = pd.DataFrame({"close": [1,2,3,4,5,6,7,8,9,0]})
    # print(ma(data))
    # mdf = md(data)
    # print(md(data, n=26))
    # print(join_frame(data, mdf))
    # emaf = ema(data)
    # print(ema(data, 5))
    # print(join_frame(data, emaf))
    # print(macd(data))
    # print(kdj(data))
    # print(vrsi(data, 6))
    # print(boll(data))
    # print(bbiboll(data))
    # print(wr(data))
    # print(bias(data))
    # print(asi(data))
    # print(vr_rate(data))
    # print(vr(data))
    # print(arbr(data))
    # print(dpo(data))
    # print(trix(data))
    # print(bbi(data))
    # print(ts.top_list(date="2019-01-17"))
    # print(mtm(data))
    # print(obv(data))
    # print(cci(data))
    # print(priceosc(data))
    # print(dbcd(data))
    # print(roc(data))
    # print(vroc(data))
    # print(cr(data))
    # print(psy(data))
    # print(wad(data))
    # print(mfi(data))
    # print(pvt(data))
    # print(wvad(data))
    # print(cdp(data))
    # print(env(data))
    # print(mike(data))
    # print(vr(data))
    # print(vma(data))
    # print(vmacd(data))
    # print(vosc(data))
    # print(tapi(data))
    # print(vstd(data))
    # print(adtm(data))
    # print(mi(data))
    # print(micd(data))
    # print(rc(data))
    print(rccd(data))
    # print(srmi(data))
    # print(dptb(data))
    # print(jdqs(data))
    # pd.set_option('display.max_rows', 1000)
    # print(jdrs(data))
    # print(join_frame(data, jdrs(data)))
    # print(data)
    # print(zdzb(data))
    # print(atr(data))
    # print(mass(data))
    # print(vhf(data))
    # print(cvlt(data))
    # print(up_n(data))
    # print(down_n(data))
