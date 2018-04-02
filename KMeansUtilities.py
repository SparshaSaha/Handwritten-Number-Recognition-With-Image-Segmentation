
# coding: utf-8

# In[23]:


from sklearn.cluster import KMeans


# In[28]:


def get_clusters(points,k):
    kmeans = KMeans(n_clusters=2, random_state=0).fit(points)
    n=kmeans.labels_
    clusters=[[]for i in range(k)]
    for i in range(len(n)):
        clusters[n[i]].append(points[i])
    return clusters

