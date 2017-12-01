import pandas
import matplotlib.pyplot as plt

#files in project
import rgr

names=['name','fpts','cost','value']
nfdf = pandas.read_csv('nf.csv', names=names)
data = rgr.get_rg()


jdf = pandas.DataFrame()
for index, row in data.iterrows():
    p = row['player']
    if p == "Moe Harkless":
        p = "Maurice Harkless"
    if p == "Louis Williams":
        p = "Lou Williams"
    if p == "Larry Nance":
        p = "Larry Nance Jr."
    if p == "Dennis Smith Jr.":
        p = "Dennis Smith"
    for index2, row2 in nfdf.iterrows():
        p2 = row2['name']
        if p == p2:
            name = row2['name']
            fpts2 = row2['fpts']
            fpts = row['fpts']
            value2 = row2['value']
            value = row['value']
            posnum = row['posnum']
            floor = row['floor']
            ceil = row['ceil']
            
            entry = pandas.DataFrame([[name,posnum,fpts,fpts2,value,value2,ceil,floor]], columns=['name','posnum','fpts','fpts2','value', 'value2', 'ceil', 'floor'])
            jdf = jdf.append(entry)
        else:
            print p #TODO: figure out a way to add names that match >= 90% of characters 
            print p2  
#print kdf
jdf["fpts"] = jdf[['fpts','fpts2']].mean(axis=1)
jdf["value"] = jdf[['value','value2']].mean(axis=1)

print jdf


plt.scatter(x=jdf["fpts"], y=jdf["value"],c=jdf["posnum"], s=jdf['floor']*5)
#plt.plot(data["fpts"], data["value"], c='black')
#plt.colorbar()
for l, x, y, c in zip(jdf["name"], jdf["fpts"], jdf["value"], jdf["posnum"]):
    plt.annotate(l,
                 xy=(x,y), xytext=(20,20),
                 textcoords='offset points', ha='right',
                 va='bottom',
                 bbox=dict(boxstyle='round,pad=0.5',
                           fc=(c,1-c,1-c**2), alpha=0.5),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
plt.show()

"""

#swish projections          REQUIRED PAID
#numberfire projections     CHECK
#rotogrinder projections    CHECK! """

