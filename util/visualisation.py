import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

def confusionMetrix(y_test, y_test_pred):
    # This function is not done!
    cfm = confusion_matrix(y_test, y_test_pred)
    s = np.sum(cfm)

    labels = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
    labels = np.array(labels).reshape(2, 2)

    # counts = cfm
    # normalisations = []
    # result = zip(labels, counts, normalisations)

    # sns.heatmap(cfm/s, annot=result, fmt='', cmap='Blues')
    pass