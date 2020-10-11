

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from dtreeplt import dtreeplt
  
#from sklearn.tree import export_graphviz
#import pydotplus



def splitdata_train_test(data, fraction_training):

  np.random.shuffle(data)
  split_index = int(fraction_training*len(data))
  return data[:split_index],data[split_index:]


def generate_features_targets(data):

  targets = data['class']
  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']
  # concentration in u filter
  features[:, 10] = data['petroR50_u']/data['petroR90_u']
  # concentration in r filter
  features[:, 11] = data['petroR50_r']/data['petroR90_r']
  # concentration in z filter
  features[:, 12] = data['petroR50_z']/data['petroR90_z']

  return features, targets


if __name__ == '__main__':
  data = np.load('galaxy_catalogue.npy')
  #filename="decision_tree.jpg"
    
#  predicted_class, actual_class = dtc_predict_actual(data)
  training_set,testing_set=splitdata_train_test(data,0.7)
  train_features,train_targets=generate_features_targets(training_set)
  test_features,test_targets=generate_features_targets(testing_set)
  dtc= DecisionTreeClassifier()
  dtc.fit(train_features,train_targets)
  #dot_data = export_graphviz(dtc, out_file=None,feature_names=['u - g', 'g - r', 'r - i', 'i - z','ecc','m4_u','m4_g','m4_r','m4_i','m4_z','conc1','conc2','conc3'])
  #graph = pydotplus.graph_from_dot_data(dot_data)
  #graph.write_jpg("decision_tree.jpg")
  #predictions= dtc.predict(test_features)
  dtree = dtreeplt(
    model=dtc,feature_names=['u - g', 'g - r', 'r - i', 'i - z','ecc','m4_u','m4_g','m4_r','m4_i','m4_z','flux_u','flux_r','flux_z'],target_names=['merger','elliptical','spiral'], filled=True)
  fig = dtree.view()
  fig.savefig('DTC.png')