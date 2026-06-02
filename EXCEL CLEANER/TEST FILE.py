# NEW TEST FILE
# Goal Check first years and degrees for Black women and Hispanic women for a single year to make sure the total for a year is correct.
# UNITID's TO Include
100654
100663
100706
100751
100858
102614
104151
104179
105330
106397
110404
110556
110565
110583
110592
110608
110635
110644
110653
110662
110671
110680
110705
110714
119678
122409
122597
122755
123961
126614
126775
126818
127060
129020
130697
130794
130934
130943
131283
131469
131496
131520
132903
133650
133669
133881
133951
134097
134130
135726
137351
138947
139658
139755
139940
139959
141574
142276
142285
144050
144740
145600
145637
145725
147703
149222
149772
150136
151111
151351
152080
153603
153658
155317
155399
155681
157085
157289
159391
159647
159939
160658
160755
161253
163268
163286
164924
164988
165015
165334
166027
166513
166629
166638
166683
167358
167987
168148
168421
169248
169798
170976
171100
171128
171571
172644
172699
173920
174066
174233
176017
176080
176372
178396
178402
178411
178420
179867
180461
181002
181464
182281
182290
182670
183044
185828
186131
186867
187967
187985
188030
190044
190150
190415
190567
190576
190594
190664
193900
194824
195030
196060
196079
196088
196097
196413
198419
199102
199120
199139
199157
199193
199847
200280
200332
200800
201441
201645
201885
202134
203517
204024
204796
204857
206084
206604
207388
207500
209542
209551
209807
211273
211440
213543
214777
215062
215293
216339
217156
217484
217882
218663
219347
219471
220181
220862
221759
221999
223232
224554
225414
225511
227216
227757
228246
228459
228723
228769
228778
228787
228796
228875
229027
229115
230038
230728
230764
231174
231624
232186
232265
232982
233921
234030
234076
236939
236948
238032
240444
240453
240727
243197
243221
243744
243780
445188
207971


# YEAR TO CHECK 2015
# USE RAW FILES SO
# IPEDS IS /Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Trimmed/c2015_trimmed_file.xlsx
    # this is for comp
# GSS Us /Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS Trimmed/gss2015_trimmed_file.xlsx
    # this is for first and total

# need to remove the list of UnitID"S with only lv 7's? (MAYBE GET CORRCT) 
# VALS TO COMPARE from COMBINED WIDE   
        # for 17 only BLACK TOTAL = 25, DEGREE = 4
        #  HISP TOTAL = 69 , DEGREE = 10

        #VS
        # 25, 4
            # dif of 0, 0
        # 69, 10 
            # dif of 0, 0 

    # Frist and Total vals are identcal, but DEGREES from RAW are higher than the calcultion
    # ISSUE WITH DEGREES LOOKING AT  BOTH AWLEVELS need to jsut look at AWLEVEL 17
'''
    "Black Women": {
        "comp": "cbkaaw", 
        "first": "ft_frst_wmen_black_v", 
        "total": "ft_wmen_black_v",
        "awlevel": [17]
    },
'''
'''
    "Hispanic Women": {
        "comp": "chispw", 
        "first": "ft_frst_wmen_hisp_v",
        "total": "ft_wmen_hisp_v",
        "awlevel": [17]
    },
'''
# Goal is to calculate the sum of first years, total Students and degrees earened (comp), for each group using the uninitid's from the list above

import pandas as pd

# ============================================================
# FILES
# ============================================================

ipeds_file = "/Users/co25936/Desktop/PER/IPEDS/Excel Files IPEDS/Trimmed/c2015_trimmed_file.xlsx"
gss_file = "/Users/co25936/Desktop/PER/IPEDS/Excel Files GSS/GSS Trimmed/gss2015_trimmed_file.xlsx"

# ============================================================
# LOAD DATA
# ============================================================

ipeds = pd.read_excel(ipeds_file)
gss = pd.read_excel(gss_file)

# Standardize column names
ipeds.columns = ipeds.columns.str.strip().str.lower()
gss.columns = gss.columns.str.strip().str.lower()

# ============================================================
# Included UNITIDS
# ============================================================

included_unitids = {
100663,100706,100751,100858,102614,104151,104179,106397,
110404,110635,110644,110653,110662,110671,110680,110705,
110714,119678,123961,126614,126818,127060,129020,130697,
130794,130943,131283,131469,131496,131520,132903,133650,
133669,133881,133951,134097,134130,135726,137351,139658,
139755,139940,139959,141574,142276,142285,144050,145600,
145637,145725,147703,149222,151351,152080,153603,153658,
155317,155399,157085,157289,159391,160755,161253,163268,
163286,164924,164988,165015,165334,166027,166513,166629,
166683,167358,168148,168421,170976,171100,171128,172644,
172699,174066,176017,178396,178411,178420,179867,180461,
181464,182281,182290,182670,183044,185828,186131,186867,
187967,187985,188030,190044,190150,190415,190576,193900,
194824,195030,196060,196079,196088,196097,196413,198419,
199120,199193,199847,200280,200332,201645,201885,203517,
204796,204857,206084,207388,207500,207971,209542,209551,
209807,211273,211440,213543,214777,215062,215293,216339,
217156,217484,217882,218663,219347,221759,221999,223232,
225511,227216,227757,228246,228723,228769,228778,228787,
228875,229027,229115,230038,230728,230764,231624,232186,
232265,232982,233921,234076,236939,236948,238032,240444,
240453,240727,243744,243780,445188
}

# Ensure numeric UNITID
ipeds["unitid"] = pd.to_numeric(ipeds["unitid"], errors="coerce")
gss["unitid"] = pd.to_numeric(gss["unitid"], errors="coerce")

ipeds = ipeds[ipeds["unitid"].isin(included_unitids)]
gss = gss[gss["unitid"].isin(included_unitids)]

# ============================================================
# VARIABLES TO CHECK
# ============================================================

groups = {
    "Black Women": {
        "comp": "cbkaaw",
        "first": "ft_frst_wmen_black_v",
        "total": "ft_wmen_black_v",
        "awlevel": [17]

    },
    "Hispanic Women": {
        "comp": "chispw",
        "first": "ft_frst_wmen_hisp_v",
        "total": "ft_wmen_hisp_v",
        "awlevel": [17]
    }
}

# ============================================================
# CALCULATE TOTALS
# ============================================================

unique_unitids = (
    ipeds["unitid"]
    .dropna()
    .astype(int)
    .drop_duplicates()
)
print(len (unique_unitids))

results = []

for group_name, vars_ in groups.items():

    ipeds_group = ipeds[
        ipeds["awlevel"].isin(vars_["awlevel"])
    ]

    comp_sum = pd.to_numeric(
        ipeds_group[vars_["comp"]],
        errors="coerce"
    ).fillna(0).sum()

    first_sum = pd.to_numeric(
        gss[vars_["first"]],
        errors="coerce"
    ).fillna(0).sum()

    total_sum = pd.to_numeric(
        gss[vars_["total"]],
        errors="coerce"
    ).fillna(0).sum()

    results.append({
        "Group": group_name,
        "First Year Students": first_sum,
        "Total Students": total_sum,
        "Degrees Earned": comp_sum
    })

results_df = pd.DataFrame(results)

print(results_df)


results_df.to_excel(
    "Black_Hispanic_Women_2015_Check.xlsx",
    index=False
)