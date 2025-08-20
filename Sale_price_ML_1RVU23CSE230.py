import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("F:/Sem-5/Fundamentals of Data Engineering/Labs/Lab-2/raw_data/sale_price.csv")

df['sale_price'] = df['sale_price'].replace('[\$,]', '', regex=True).astype(float)

df_grouped = df.groupby('customer_id').agg(
    total_purchase_amount=('sale_price', 'sum'),
    purchase_frequency=('sale_price', 'count'),
    avg_transaction_value=('sale_price', 'mean')
).reset_index()

df_grouped.fillna(0, inplace=True)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_grouped[['total_purchase_amount', 'purchase_frequency', 'avg_transaction_value']])

kmeans = KMeans(n_clusters=2, random_state=42)
df_grouped['cluster'] = kmeans.fit_predict(scaled_features)

vip_cluster = df_grouped.groupby('cluster')['total_purchase_amount'].mean().idxmax()
df_grouped['VIP_status'] = df_grouped['cluster'].apply(lambda x: 'VIP' if x == vip_cluster else 'Non-VIP')

df_enriched = df.merge(df_grouped[['customer_id', 'VIP_status']], on='customer_id', how='left')

df_enriched.to_csv("data_warehouse/enriched_vip_data.csv", index=False)