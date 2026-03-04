import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data of gurugram real Estate.csv')

#Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df=df.drop_duplicates()

#Numerical Columns Cleaning
df['price']=df['price'].astype(str).str.replace(',','').astype(float)
df['area']=df['area'].astype(str).str.replace(',','').astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',','').astype(int)

#Ctaegorical Columns Cleaning
df['status']=df['status'].str.strip().str.lower()
df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'approval by rera':True,' not approval by rera':False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()

df= df.drop_duplicates()
# print(df)
# print(df.info())

# Question 
# Question 1: Which is the costliest flat in the datasets
costliest_flat = df.loc[df["price"].idxmax()]
# print(costliest_flat)

# Question 2: Which locality has the highest average price?
print(df.groupby("locality")["price"].mean().sort_values(ascending=False))

# Question 3: Which locality has the highest rate per square foot?
print(df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False))

# Question 4: Ready-to-move vs Under-construction pricing
print(df.groupby("status")["price"].median())

# Question 5: Does RERA approval affect pricing?
print(df.groupby("rera_approval")["price"].median())

# Question 6: How does area impact price?
sns.scatterplot(x="area", y="price", data=df)
plt.show()

# Question 7: Which BHK configuration is most expensive?
print(df.groupby("bhk_count")["price"].mean())

# Question 8: Which property type is the costliest?
print(df.groupby("flat_type")["price"].mean())

# Question 9: Do certain builders price higher?
df.groupby("company_name")["price"].mean().sort_values(ascending=False)

# Question 10: Are larger homes more expensive per sqft?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()

df.to_excel("updated_gurugram_data.xlsx",index=False)
