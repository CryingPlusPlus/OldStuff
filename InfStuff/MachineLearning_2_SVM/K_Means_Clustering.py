import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

# KMeans algoritmus K Mittelpunkte machen random
# - abstände zu allen Punkten punkte clustern - mittelpunkte in den durchschnitt der Punkte machen -
# wiederholen bis sich die mittelpunkte nicht mehr verschieben

digits = load_digits()
data = scale(digits.data)  # features werden zwischen -1 und 1 gemacht

y = digits.target
k = len(np.unique(y))  # wieviele cluster es geben wird

samples, features = data.shape


def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y, estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))  # ist nicht super wichtig zu wissen was wa mcaht


clf = KMeans(n_clusters=k, init='k-means++', n_init=10)
# n_clusters = wie viele cluster;
# init = initialisierungsmethode... wie werden die cluster verteilt;
# n_init = wie oft soll initialisiert... der algorithmus nimmt das beste ergebnis


bench_k_means(clf, 'name', data)