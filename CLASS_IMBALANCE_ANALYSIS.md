# Class Imbalance Analysis
## ATPA Assessment - June to August 2025

---

## 📊 **Class Imbalance Overview**

### **Dataset Characteristics**
- **Total Incidents**: 26,955
- **Multiple Arrests (Positive Class)**: 1,465 (5.4%)
- **Single Arrests (Negative Class)**: 25,490 (94.6%)
- **Imbalance Ratio**: 17.4:1 (highly imbalanced)

### **Business Impact**
- **Rare Event Prediction**: Multiple arrests are rare but important events
- **Resource Allocation**: Identifying high-risk incidents is critical
- **Policy Development**: Understanding factors leading to multiple arrests

---

## ✅ **Techniques We Implemented**

### **1. Stratified Sampling**
```python
# Maintained class distribution in train/test splits
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
```

**Benefits:**
- Ensures both training and testing sets have same class distribution
- Prevents bias in model evaluation
- Maintains representativeness of rare events

### **2. AUC as Primary Metric**
```python
# Used ROC-AUC for model evaluation
train_auc = roc_auc_score(y_train, y_train_proba)
test_auc = roc_auc_score(y_test, y_test_proba)

# Used AUC for hyperparameter tuning
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(),
    param_grid=param_grid,
    scoring='roc_auc',
    cv=5
)
```

**Benefits:**
- Robust to class imbalance
- Measures discriminative ability
- Threshold-independent
- Range: 0.5 (random) to 1.0 (perfect)

### **3. Appropriate Metric Selection**
- **AUC**: Primary metric for model comparison
- **Accuracy**: Secondary metric (with caution)
- **Documentation**: Clear explanation of metric limitations

---

## ❌ **Missing Techniques (Enhancement Opportunities)**

### **1. Class Weights**

#### **What We Should Have Done:**
```python
# Random Forest with class weights
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced',  # Give more weight to minority class
    random_state=42
)

# Logistic Regression with class weights
lr_model = LogisticRegression(
    class_weight='balanced',
    random_state=42
)
```

#### **Benefits:**
- **Balanced Learning**: Model learns from both classes equally
- **Improved Sensitivity**: Better at identifying positive cases
- **Cost-Sensitive**: Accounts for different misclassification costs

### **2. Resampling Techniques**

#### **SMOTE (Synthetic Minority Over-sampling)**
```python
from imblearn.over_sampling import SMOTE

# Apply SMOTE to training data only
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
```

#### **Undersampling Majority Class**
```python
from imblearn.under_sampling import RandomUnderSampler

# Reduce majority class to balance dataset
rus = RandomUnderSampler(random_state=42)
X_train_resampled, y_train_resampled = rus.fit_resample(X_train, y_train)
```

#### **Combined Approach (SMOTEENN)**
```python
from imblearn.combine import SMOTEENN

# Combine SMOTE with Edited Nearest Neighbors
smoteenn = SMOTEENN(random_state=42)
X_train_resampled, y_train_resampled = smoteenn.fit_resample(X_train, y_train)
```

### **3. Threshold Optimization**

#### **ROC Curve Analysis**
```python
from sklearn.metrics import roc_curve

# Find optimal threshold
fpr, tpr, thresholds = roc_curve(y_test, y_test_proba)
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]

# Apply optimal threshold
y_pred_optimal = (y_test_proba >= optimal_threshold).astype(int)
```

#### **Precision-Recall Curve**
```python
from sklearn.metrics import precision_recall_curve

# Find threshold that maximizes F1-score
precision, recall, thresholds = precision_recall_curve(y_test, y_test_proba)
f1_scores = 2 * (precision * recall) / (precision + recall)
optimal_threshold = thresholds[np.argmax(f1_scores)]
```

### **4. Additional Metrics**

#### **Comprehensive Evaluation**
```python
from sklearn.metrics import classification_report, confusion_matrix

# Detailed classification report
print(classification_report(y_test, y_pred, target_names=['Single Arrest', 'Multiple Arrests']))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
```

#### **Business-Specific Metrics**
```python
# Calculate business-relevant metrics
sensitivity = cm[1,1] / (cm[1,0] + cm[1,1])  # True Positive Rate
specificity = cm[0,0] / (cm[0,0] + cm[0,1])  # True Negative Rate
precision = cm[1,1] / (cm[0,1] + cm[1,1])   # Positive Predictive Value
```

---

## 🎯 **Enhanced Implementation Strategy**

### **1. Task 3: Enhanced GLM**

#### **Improved Logistic Regression**
```python
# Enhanced logistic regression with class weights
lr_enhanced = LogisticRegression(
    class_weight='balanced',
    random_state=42,
    max_iter=1000
)

# Cross-validation with multiple metrics
from sklearn.model_selection import cross_validate

scoring = {
    'accuracy': 'accuracy',
    'auc': 'roc_auc',
    'f1': 'f1',
    'precision': 'precision',
    'recall': 'recall'
}

cv_results = cross_validate(
    lr_enhanced, X_train, y_train,
    cv=5, scoring=scoring, return_train_score=True
)
```

### **2. Task 4: Enhanced Random Forest**

#### **Improved Random Forest**
```python
# Enhanced Random Forest with class weights
rf_enhanced = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)

# SMOTE for training data
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

pipeline = Pipeline([
    ('smote', SMOTE(random_state=42)),
    ('classifier', rf_enhanced)
])

# Grid search with multiple metrics
param_grid = {
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [5, 10, 15],
    'classifier__min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    pipeline, param_grid,
    scoring=['roc_auc', 'f1', 'precision', 'recall'],
    refit='f1',  # Optimize for F1-score
    cv=5
)
```

### **3. Threshold Optimization**

#### **Comprehensive Threshold Analysis**
```python
def optimize_threshold(y_true, y_proba):
    """Find optimal threshold for imbalanced classification"""
    
    # ROC curve optimization
    fpr, tpr, thresholds_roc = roc_curve(y_true, y_proba)
    optimal_idx_roc = np.argmax(tpr - fpr)
    optimal_threshold_roc = thresholds_roc[optimal_idx_roc]
    
    # Precision-Recall optimization
    precision, recall, thresholds_pr = precision_recall_curve(y_true, y_proba)
    f1_scores = 2 * (precision * recall) / (precision + recall)
    optimal_threshold_pr = thresholds_pr[np.argmax(f1_scores)]
    
    # Business cost optimization
    # Assume cost of false negative (missing multiple arrest) is 10x false positive
    cost_fn = 10
    cost_fp = 1
    
    costs = []
    for threshold in thresholds_roc:
        y_pred = (y_proba >= threshold).astype(int)
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
        total_cost = fp * cost_fp + fn * cost_fn
        costs.append(total_cost)
    
    optimal_threshold_cost = thresholds_roc[np.argmin(costs)]
    
    return {
        'roc_optimal': optimal_threshold_roc,
        'pr_optimal': optimal_threshold_pr,
        'cost_optimal': optimal_threshold_cost
    }
```

---

## 📈 **Expected Improvements**

### **Performance Enhancements**
- **Sensitivity**: 20-40% improvement in detecting multiple arrests
- **F1-Score**: 15-30% improvement in balanced performance
- **Business Value**: Better identification of high-risk incidents

### **Model Robustness**
- **Generalization**: Better performance on rare events
- **Stability**: More consistent predictions across different thresholds
- **Interpretability**: Clearer feature importance for minority class

### **Business Impact**
- **Resource Allocation**: More accurate targeting of interventions
- **Risk Assessment**: Better identification of high-risk situations
- **Policy Development**: More reliable evidence for decision-making

---

## 🎯 **Recommendations for Future Implementation**

### **1. Immediate Enhancements**
- **Add class weights** to all classification models
- **Implement SMOTE** for training data augmentation
- **Optimize thresholds** for business-specific costs
- **Use F1-score** as primary optimization metric

### **2. Advanced Techniques**
- **Ensemble methods** combining multiple resampling approaches
- **Cost-sensitive learning** with domain-specific cost matrices
- **Anomaly detection** for rare event identification
- **Active learning** for targeted data collection

### **3. Evaluation Framework**
- **Multiple metrics** for comprehensive assessment
- **Business cost analysis** for threshold optimization
- **Cross-validation** with stratification
- **Holdout validation** for final assessment

---

## ✅ **Current Status Assessment**

### **What We Did Well:**
- ✅ **Identified the problem**: Clear documentation of class imbalance
- ✅ **Used appropriate metrics**: AUC for model evaluation
- ✅ **Stratified sampling**: Maintained class distribution
- ✅ **Documented limitations**: Honest assessment of challenges

### **What We Could Improve:**
- ❌ **Class weights**: Not implemented in models
- ❌ **Resampling**: No SMOTE or other techniques
- ❌ **Threshold optimization**: No business-specific tuning
- ❌ **Comprehensive metrics**: Limited F1-score analysis

### **Overall Grade: B+**
- **Good foundation** with appropriate metric selection
- **Missing advanced techniques** for severe imbalance
- **Clear documentation** of limitations and challenges
- **Room for improvement** in practical implementation

---

*Class imbalance analysis completed as part of ATPA Assessment - June to August 2025* 