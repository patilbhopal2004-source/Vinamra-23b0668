"""Observed-data analysis for the Delhi Yamuna DO-BOD project (CE 766).
Run from the repo root:  python code/analysis.py
Data are typed in from the DPCC report tables (see README for sources).
DO reported as NIL is stored as 0."""
import math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np

# station: (BOD mg/l, DO mg/l, lat, lon)  -- DPCC sampling 09.03.2026
mar26 = {"Palla":(2.0,4.0,28.8138023,77.2100181),"Wazirabad":(4.0,3.1,28.7131310,77.2319304),
 "ISBT Bridge":(44.0,0,28.6713533,77.2338207),"ITO Bridge":(38.0,0,28.6284288,77.2534977),
 "Nizamuddin":(36.0,0,28.5915608,77.2715342),"Hindon Cut":(25.0,0,28.586049,77.300012),
 "Okhla Barrage":(42.0,0,28.545636,77.311072),"Asgarpur":(60.0,0,28.4665895,77.3928257)}
# station: (BOD, DO) -- DPCC sampling 01.05.2025
may25 = {"Palla":(4.0,9.8),"Wazirabad":(6.0,6.8),"ISBT Bridge":(34.0,0),"ITO Bridge":(64.0,0),
 "Nizamuddin":(37.0,0),"Okhla Barrage":(23.0,0),"Agra Canal (Okhla)":(28.0,0),"Asgarpur":(38.0,0)}
# drain: (% of discharge, % of BOD load) -- DPCC Yamuna book, based on DPCC 2025 data
drains = [("Najafgarh",69.77,59.93),("Shahdara",16.12,27.48),("Barapulla",4.92,3.50),
 ("Power House",4.16,3.52),("ISBT",1.47,1.57),("Sen Nursing Home",1.47,1.38),
 ("Maharani Bagh",1.03,1.24),("Kailash Nagar",0.46,0.35),("Abul Fazal",0.24,0.49),
 ("Sonia Vihar",0.23,0.23),("Jaitpur",0.19,0.17),("Shastri Park",0.18,0.13)]

def haversine(a, b):
    R = 6371.0
    p1, l1, p2, l2 = map(math.radians, [a[0], a[1], b[0], b[1]])
    h = math.sin((p2-p1)/2)**2 + math.cos(p1)*math.cos(p2)*math.sin((l2-l1)/2)**2
    return 2*R*math.asin(math.sqrt(h))

# 1. straight-line distance between consecutive stations (underestimates river length)
names = list(mar26); pts = [(mar26[n][2], mar26[n][3]) for n in names]
print("Straight-line distance between consecutive stations (km):")
cum = 0
for i in range(1, len(names)):
    d = haversine(pts[i-1], pts[i]); cum += d
    print(f"  {names[i-1]:>14} -> {names[i]:<14} {d:5.1f}   cumulative {cum:5.1f}")
print("Wazirabad -> Okhla Barrage:", round(haversine(pts[1], pts[6]), 1), "km")

# 2. drain contribution analysis
print("\nTop 2 drains, share of BOD load:", round(drains[0][2]+drains[1][2], 2), "%")
print("Top 4 drains, share of BOD load:", round(sum(d[2] for d in drains[:4]), 2), "%")
print("Relative concentration (load share / discharge share; 1 = average):")
for n, q, l in drains[:4]:
    print(f"  {n:<12} {l/q:.2f}")

# 3. figure
st = ["Palla","Wazirabad","ISBT Bridge","ITO Bridge","Nizamuddin","Okhla Barrage","Asgarpur"]
lab = ["Palla","Wazir-\nabad","ISBT","ITO","Nizam-\nuddin","Okhla","Asgar-\npur"]
b26=[mar26[s][0] for s in st]; d26=[mar26[s][1] for s in st]
b25=[may25[s][0] for s in st]; d25=[may25[s][1] for s in st]
x=np.arange(len(st)); w=0.38; c1,c2="#1F3864","#E08A2E"
fig,ax=plt.subplots(1,3,figsize=(11,3.3),gridspec_kw={"width_ratios":[1.15,1.15,1]})
ax[0].bar(x-w/2,b25,w,color=c2,label="01.05.2025"); ax[0].bar(x+w/2,b26,w,color=c1,label="09.03.2026")
ax[0].axhline(3,color="red",ls="--",lw=1)
ax[0].set_title("(a) BOD along the river",fontsize=9); ax[0].set_ylabel("BOD (mg/l)",fontsize=8)
ax[1].bar(x-w/2,d25,w,color=c2); ax[1].bar(x+w/2,d26,w,color=c1)
for i,(a,b) in enumerate(zip(d25,d26)):
    if a==0: ax[1].text(i-w/2,0.2,"NIL",rotation=90,fontsize=6.5,ha="center",va="bottom",color=c2)
    if b==0: ax[1].text(i+w/2,0.2,"NIL",rotation=90,fontsize=6.5,ha="center",va="bottom",color=c1)
ax[1].axhline(5,color="red",ls="--",lw=1)
ax[1].set_title("(b) Dissolved oxygen (NIL = 0)",fontsize=9); ax[1].set_ylabel("DO (mg/l)",fontsize=8)
for a in ax[:2]:
    a.set_xticks(x); a.set_xticklabels(lab,fontsize=6.5); a.tick_params(axis="y",labelsize=7)
    a.spines[["top","right"]].set_visible(False)
ax[0].legend(fontsize=7,frameon=False,loc="upper left")
top=drains[:6]; n=[d[0] for d in top]+["Other 6"]
fl=[d[1] for d in top]+[sum(d[1] for d in drains[6:])]; ld=[d[2] for d in top]+[sum(d[2] for d in drains[6:])]
y=np.arange(len(n))
ax[2].barh(y-0.19,fl,0.38,color="#7FA7D9",label="% of discharge"); ax[2].barh(y+0.19,ld,0.38,color="#2E7D32",label="% of BOD load")
ax[2].set_yticks(y); ax[2].set_yticklabels(n,fontsize=7); ax[2].invert_yaxis(); ax[2].tick_params(axis="x",labelsize=7)
ax[2].set_title("(c) Major drains (DPCC 2025 data)",fontsize=9); ax[2].legend(fontsize=7,frameon=False,loc="lower right")
ax[2].spines[["top","right"]].set_visible(False); ax[2].set_xlabel("%",fontsize=8)
plt.tight_layout(); plt.savefig("figures/fig1_observed_data.png",dpi=200)
print("\nSaved figures/fig1_observed_data.png")
