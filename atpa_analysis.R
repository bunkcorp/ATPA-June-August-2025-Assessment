#----------------------------------------------------------------#
# ATPA Assessment: R Code for NMInsights Crime Analysis          #
#----------------------------------------------------------------#

# --- 1. SETUP: LOAD LIBRARIES ---
# Install packages if you don't have them yet
tryCatch({
  install.packages(c("tidyverse", "mice", "caTools", "lme4", "randomForest", "caret", "pdp", "DALEX", "iBreakDown", "knitr", "pROC"), 
                  repos = "https://cran.rstudio.com/")
}, error = function(e) {
  cat("Some packages failed to install. Continuing with available packages.\n")
})

# Load packages with error handling
library(tidyverse) # For data manipulation (dplyr, ggplot2) and piping

# Try to load mice, if not available use a simple approach
if (require(mice, quietly = TRUE)) {
  library(mice)
  cat("mice package loaded successfully\n")
} else {
  cat("mice package not available, will use simple imputation methods\n")
}

# Load other packages with error handling
if (require(caTools, quietly = TRUE)) library(caTools)
if (require(lme4, quietly = TRUE)) library(lme4)
if (require(randomForest, quietly = TRUE)) library(randomForest)
if (require(caret, quietly = TRUE)) library(caret)
if (require(pdp, quietly = TRUE)) library(pdp)
if (require(DALEX, quietly = TRUE)) library(DALEX)
if (require(iBreakDown, quietly = TRUE)) library(iBreakDown)
if (require(knitr, quietly = TRUE)) library(knitr)
if (require(pROC, quietly = TRUE)) library(pROC)

# --- 2. DATA LOADING (Task 1) ---
# Replace with the actual paths to your files
incidents <- read.csv("./incidents.csv")
arrestee <- read.csv("./ATPA August/ATPA_June_August_2025/arrestee.csv")

cat("Data loaded successfully:\n")
cat("Incidents rows:", nrow(incidents), "\n")
cat("Arrestee rows:", nrow(arrestee), "\n")

# --- 3. DATA PREPARATION (Task 1) ---

# a) Merge the files (Left Join)
# We keep all incidents, and append arrestee info where it exists.
crime_data <- left_join(incidents, arrestee, by = "incident_id", suffix = c("", "_arrestee"))

cat("Merged data rows:", nrow(crime_data), "\n")
cat("Available columns:", names(crime_data), "\n")

# b) Create the ARREST target variable
# Check what arrest-related columns are available
arrest_cols <- grep("arrest", names(crime_data), ignore.case = TRUE, value = TRUE)
cat("Arrest-related columns:", arrest_cols, "\n")

# Use the first arrest-related column that exists, or create based on presence of arrestee data
if (length(arrest_cols) > 0) {
  # Use the first arrest column found
  arrest_col <- arrest_cols[1]
  crime_data <- crime_data %>%
    mutate(ARREST = ifelse(!is.na(get(arrest_col)), 1, 0))
  cat("Using column", arrest_col, "for ARREST variable\n")
} else {
  # If no arrest columns, check if we have any arrestee-specific columns
  arrestee_cols <- grep("arrestee", names(crime_data), ignore.case = TRUE, value = TRUE)
  cat("Arrestee-related columns:", arrestee_cols, "\n")
  
  if (length(arrestee_cols) > 0) {
    # Use the first arrestee column
    arrestee_col <- arrestee_cols[1]
    crime_data <- crime_data %>%
      mutate(ARREST = ifelse(!is.na(get(arrestee_col)), 1, 0))
    cat("Using column", arrestee_col, "for ARREST variable\n")
  } else {
    # Fallback: check if any arrestee data exists by looking for non-NA values in arrestee-specific columns
    crime_data <- crime_data %>%
      mutate(ARREST = ifelse(!is.na(arrestee_id), 1, 0))
    cat("Using arrestee_id for ARREST variable\n")
  }
}

# Convert ARREST to factor immediately for consistency across all models
crime_data <- crime_data %>%
  mutate(ARREST = as.factor(ARREST))

cat("Target variable created. Arrest rate:", mean(as.numeric(as.character(crime_data$ARREST)), na.rm = TRUE), "\n")

# c) Missing Values Imputation (using MICE package as a robust method)
# Note: For a real project, this is computationally intensive.
# We'll demonstrate on a subset of columns for speed.
# Predictive Mean Matching (pmm) is a good general-purpose method.
cols_to_impute <- c("weapon_name", "victim_injury_name", "offender_age_num", "victim_age_num")

# Missing Values Imputation (using MICE package as a robust method)
if (exists("mice") && require(mice, quietly = TRUE)) {
  cat("Using MICE for imputation...\n")
  temp_imputed <- mice(crime_data[, cols_to_impute], method = 'pmm', m = 1, maxit = 5, seed = 123)
  crime_data[, cols_to_impute] <- complete(temp_imputed, 1)
} else {
  cat("Using simple imputation methods...\n")
  crime_data <- crime_data %>%
    mutate(
      weapon_name = ifelse(is.na(weapon_name), "Unknown", weapon_name),
      victim_injury_name = ifelse(is.na(victim_injury_name), "None", victim_injury_name),
      offender_age_num = ifelse(is.na(offender_age_num), median(offender_age_num, na.rm = TRUE), offender_age_num),
      victim_age_num = ifelse(is.na(victim_age_num), median(victim_age_num, na.rm = TRUE), victim_age_num)
    )
}

# d) Feature Engineering (Numeric to Factor)
crime_data <- crime_data %>%
  mutate(
    offender_age_group = case_when(
      offender_age_num < 18 ~ "Under 18",
      offender_age_num >= 18 & offender_age_num <= 35 ~ "18-35",
      offender_age_num >= 36 & offender_age_num <= 50 ~ "36-50",
      offender_age_num > 50 ~ "Over 50",
      TRUE ~ "Unknown"
    ),
    victim_age_group = case_when(
      victim_age_num < 18 ~ "Under 18",
      victim_age_num >= 18 & victim_age_num <= 35 ~ "18-35",
      victim_age_num >= 36 & victim_age_num <= 50 ~ "36-50",
      victim_age_num > 50 ~ "Over 50",
      TRUE ~ "Unknown"
    )
  )

# e) Dimension Reduction (using forcats::fct_lump_n)
# Grouping infrequent categories into "Other"
crime_data <- crime_data %>%
  mutate(
    offense_category_name_reduced = fct_lump_n(offense_category_name, n = 15, other_level = "Other"),
    agency_name_reduced = fct_lump_n(agency_name, n = 20, other_level = "Other")
  )

# --- TASK 1 VISUALIZATIONS: Two visualizations showing relationships with target variable ---
# (Now placed after all data preparation steps for consistency)
cat("Creating Task 1 visualizations...\n")

# Visualization 1: Arrest Rate by Crime Category
p1 <- ggplot(crime_data, aes(x = crime_against, fill = ARREST)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = c("0" = "lightblue", "1" = "darkred"), 
                    labels = c("No Arrest", "Arrest")) +
  labs(title = "Arrest Rate by Crime Category",
       x = "Crime Against", 
       y = "Proportion", 
       fill = "Arrest Status") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Save the plot
ggsave("arrest_rate_by_crime_category.png", p1, width = 10, height = 6, dpi = 300)
cat("Saved: arrest_rate_by_crime_category.png\n")

# Visualization 2: Arrest Rate by Weapon Involvement
p2 <- ggplot(crime_data, aes(x = weapon_name, fill = ARREST)) +
  geom_bar(position = "fill") +
  scale_fill_manual(values = c("0" = "lightblue", "1" = "darkred"), 
                    labels = c("No Arrest", "Arrest")) +
  labs(title = "Arrest Rate by Weapon Involvement",
       x = "Weapon Name", 
       y = "Proportion", 
       fill = "Arrest Status") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  coord_flip()

# Save the plot
ggsave("arrest_rate_by_weapon.png", p2, width = 12, height = 8, dpi = 300)
cat("Saved: arrest_rate_by_weapon.png\n")

# Task 1 Table: Distribution of ARREST target variable
arrest_distribution <- crime_data %>%
  count(ARREST) %>%
  mutate(Percentage = round(n / sum(n) * 100, 2))

if (require(knitr, quietly = TRUE)) {
  arrest_table <- kable(arrest_distribution, 
                       col.names = c("Arrest Status", "Count", "Percentage"),
                       caption = "Distribution of Target Variable ARREST")
  cat("Arrest Distribution Table:\n")
  print(arrest_table)
  
  # Save table to file
  capture.output(print(arrest_table), file = "arrest_distribution_table.txt")
  cat("Saved: arrest_distribution_table.txt\n")
}

cat("Data preparation completed successfully!\n")
cat("Final dataset dimensions:", dim(crime_data), "\n")

# Save the prepared dataset
write.csv(crime_data, "crime_data_prepared.csv", row.names = FALSE)
cat("Prepared dataset saved as 'crime_data_prepared.csv'\n")

# --- 4. MODELING PREPARATION (Task 3a) ---
# Feature Selection for Modeling
# Select relevant features for modeling
modeling_data <- crime_data %>%
  select(
    ARREST,
    crime_against,
    weapon_name,
    victim_injury_name,
    incident_hour,
    offender_age_group,
    victim_age_group,
    agency_name_reduced,
    county_name
  ) %>%
  filter(!is.na(ARREST))  # Remove any rows with missing target

cat("Final dataset dimensions after feature selection:", dim(modeling_data), "\n")

# Split data into training and testing sets (70/30 split)
set.seed(123)
split_indices <- sample.split(modeling_data$ARREST, SplitRatio = 0.7)
train_set <- modeling_data[split_indices, ]
test_set <- modeling_data[!split_indices, ]

cat("Training Set Arrest Rate:", round(mean(train_set$ARREST) * 100, 5), "%\n")
cat("Testing Set Arrest Rate:", round(mean(test_set$ARREST) * 100, 5), "%\n")

# --- 5. GENERALIZED LINEAR MODELS (Task 3a) ---
cat("Fitting GLM model...\n")

# Fit GLM (Logistic Regression)
glm_model <- glm(ARREST ~ crime_against + weapon_name + victim_injury_name + 
                 incident_hour + offender_age_group + victim_age_group + 
                 agency_name_reduced + county_name, 
                 family = binomial(link = "logit"), data = train_set)

# Print model summary
print(summary(glm_model))

# Save GLM model summary to file
capture.output(print(summary(glm_model)), file = "glm_model_summary.txt")
cat("Saved: glm_model_summary.txt\n")

# Make predictions on test set
glm_predictions <- predict(glm_model, newdata = test_set, type = "response")
glm_predicted_classes <- ifelse(glm_predictions > 0.5, 1, 0)

# Evaluate GLM performance with multiple metrics
if (require(caret, quietly = TRUE)) {
  glm_confusion <- confusionMatrix(factor(glm_predicted_classes), factor(test_set$ARREST))
  cat("GLM Performance:\n")
  print(glm_confusion)
  
  # Save GLM confusion matrix to file
  capture.output(print(glm_confusion), file = "glm_confusion_matrix.txt")
  cat("Saved: glm_confusion_matrix.txt\n")
  
  # Calculate AUC-ROC and F1-Score
  if (require(pROC, quietly = TRUE)) {
    glm_roc <- roc(test_set$ARREST, glm_predictions)
    glm_auc <- auc(glm_roc)
    cat("GLM AUC-ROC:", round(glm_auc, 4), "\n")
  }
  
  # Calculate F1-Score
  glm_f1 <- glm_confusion$byClass["F1"]
  cat("GLM F1-Score:", round(glm_f1, 4), "\n")
}

# --- 6. GENERALIZED LINEAR MIXED MODELS (Task 3b) ---
cat("Fitting GLMM model...\n")

# Try to fit GLMM with agency as random effect
if (require(lme4, quietly = TRUE)) {
  tryCatch({
    glmm_model <- glmer(ARREST ~ crime_against + weapon_name + incident_hour + 
                       offender_age_group + victim_age_group + 
                       (1|agency_name_reduced), 
                       family = binomial(link = "logit"), data = train_set)
    
    cat("GLMM Model Summary:\n")
    print(summary(glmm_model))
    
    # Save GLMM model summary to file
    capture.output(print(summary(glmm_model)), file = "glmm_model_summary.txt")
    cat("Saved: glmm_model_summary.txt\n")

    # Make predictions on test set
    glmm_predictions <- predict(glmm_model, newdata = test_set, type = "response")
    glmm_predicted_classes <- ifelse(glmm_predictions > 0.5, 1, 0)
    
    # Evaluate GLMM performance
    if (require(caret, quietly = TRUE)) {
      glmm_confusion <- confusionMatrix(factor(glmm_predicted_classes), factor(test_set$ARREST))
      cat("GLMM Performance:\n")
      print(glmm_confusion)
      
      # Save GLMM confusion matrix to file
      capture.output(print(glmm_confusion), file = "glmm_confusion_matrix.txt")
      cat("Saved: glmm_confusion_matrix.txt\n")
      
      # Calculate AUC-ROC and F1-Score for GLMM
      if (require(pROC, quietly = TRUE)) {
        glmm_roc <- roc(test_set$ARREST, glmm_predictions)
        glmm_auc <- auc(glmm_roc)
        cat("GLMM AUC-ROC:", round(glmm_auc, 4), "\n")
      }
      
      # Calculate F1-Score
      glmm_f1 <- glmm_confusion$byClass["F1"]
      cat("GLMM F1-Score:", round(glmm_f1, 4), "\n")
    }
  }, error = function(e) {
    cat("GLMM failed to converge or other error:", e$message, "\n")
  })
} else {
  cat("lme4 package not available for GLMM\n")
}

# --- 7. RANDOM FOREST MODEL (Task 4) ---
cat("Fitting Random Forest model...\n")

if (require(randomForest, quietly = TRUE)) {
  # Prepare training data (remove NAs and match factor levels)
  rf_data <- train_set %>%
    mutate(across(where(is.character), as.factor)) %>%
    na.omit()

  # ARREST is already a factor from earlier in the script
  # rf_data$ARREST <- as.factor(rf_data$ARREST)  # No longer needed

  cat("Random Forest training data dimensions:", dim(rf_data), "\n")
  cat("Class distribution in training data:\n")
  print(table(rf_data$ARREST))
  
  # Fit Random Forest with class weights to handle imbalance
  rf_model <- randomForest(ARREST ~ ., data = rf_data, 
                          ntree = 500, 
                          importance = TRUE,
                          classwt = c("0" = 0.2, "1" = 0.8))  # Weight minority class higher
  
  cat("Random Forest Model Summary:\n")
  print(rf_model)
  
  # Variable importance
  cat("Random Forest Variable Importance:\n")
  print(importance(rf_model))

  # Create and save feature importance plot
  png("random_forest_feature_importance.png", width = 10, height = 8, units = "in", res = 300)
  varImpPlot(rf_model, main = "Random Forest Feature Importance")
  dev.off()
  cat("Saved: random_forest_feature_importance.png\n")

  # Prepare test data (remove NAs and match factor levels)
  test_rf_data <- test_set %>%
    mutate(across(where(is.character), as.factor)) %>%
    na.omit()

  # ARREST is already a factor from earlier in the script
  # test_rf_data$ARREST <- as.factor(test_rf_data$ARREST)  # No longer needed

  # Ensure factor levels match between training and test data
  for (col in names(rf_data)) {
    if (is.factor(rf_data[[col]]) && col %in% names(test_rf_data)) {
      # Get levels from training data
      train_levels <- levels(rf_data[[col]])
      # Set levels in test data to match training data
      test_rf_data[[col]] <- factor(test_rf_data[[col]], levels = train_levels)
    }
  }

  cat("Random Forest test data dimensions after removing NAs:", dim(test_rf_data), "\n")
  
  # Make predictions
  rf_predictions <- predict(rf_model, newdata = test_rf_data, type = "prob")[,2]
  rf_predicted_classes <- ifelse(rf_predictions > 0.5, 1, 0)
  
  # Evaluate Random Forest performance
  if (require(caret, quietly = TRUE)) {
    rf_confusion <- confusionMatrix(factor(rf_predicted_classes), factor(test_rf_data$ARREST))
    cat("Random Forest Performance:\n")
    print(rf_confusion)
    
    # Save Random Forest confusion matrix to file
    capture.output(print(rf_confusion), file = "rf_confusion_matrix.txt")
    cat("Saved: rf_confusion_matrix.txt\n")
    
    # Calculate AUC-ROC and F1-Score for Random Forest
    if (require(pROC, quietly = TRUE)) {
      rf_roc <- roc(as.numeric(test_rf_data$ARREST) - 1, rf_predictions)
      rf_auc <- auc(rf_roc)
      cat("Random Forest AUC-ROC:", round(rf_auc, 4), "\n")
    }
    
    # Calculate F1-Score
    rf_f1 <- rf_confusion$byClass["F1"]
    cat("Random Forest F1-Score:", round(rf_f1, 4), "\n")
  }
  
  # --- 8. SHAP ANALYSIS (Task 4b) ---
  cat("Performing SHAP analysis...\n")
  
  if (require(DALEX, quietly = TRUE)) {
    # Create explainer for Random Forest
    rf_explainer <- explain(rf_model, data = rf_data, y = rf_data$ARREST)
    
    # Select 3 arrest and 3 non-arrest cases from the test set
    arrest_cases <- test_rf_data %>% filter(ARREST == 1) %>% head(3)
    no_arrest_cases <- test_rf_data %>% filter(ARREST == 0) %>% head(3)
    
    cat("Selected arrest cases:", nrow(arrest_cases), "\n")
    cat("Selected non-arrest cases:", nrow(no_arrest_cases), "\n")
    
    # Generate SHAP explanations for arrest cases
    if(nrow(arrest_cases) > 0) {
      cat("SHAP for Arrest Case 1:\n")
      shap_a1 <- predict_parts(rf_explainer, new_observation = arrest_cases[1, ], type = "break_down")
      print(shap_a1)
      
      if(nrow(arrest_cases) > 1) {
        cat("SHAP for Arrest Case 2:\n")
        shap_a2 <- predict_parts(rf_explainer, new_observation = arrest_cases[2, ], type = "break_down")
        print(shap_a2)
      }
      
      if(nrow(arrest_cases) > 2) {
        cat("SHAP for Arrest Case 3:\n")
        shap_a3 <- predict_parts(rf_explainer, new_observation = arrest_cases[3, ], type = "break_down")
        print(shap_a3)
      }
    }
    
    # Generate SHAP explanations for non-arrest cases
    if(nrow(no_arrest_cases) > 0) {
      cat("SHAP for No-Arrest Case 1:\n")
      shap_na1 <- predict_parts(rf_explainer, new_observation = no_arrest_cases[1, ], type = "break_down")
      print(shap_na1)
      
      if(nrow(no_arrest_cases) > 1) {
        cat("SHAP for No-Arrest Case 2:\n")
        shap_na2 <- predict_parts(rf_explainer, new_observation = no_arrest_cases[2, ], type = "break_down")
        print(shap_na2)
      }
      
      if(nrow(no_arrest_cases) > 2) {
        cat("SHAP for No-Arrest Case 3:\n")
        shap_na3 <- predict_parts(rf_explainer, new_observation = no_arrest_cases[3, ], type = "break_down")
        print(shap_na3)
      }
    }
    
    # Save SHAP results
    shap_results <- list(
      arrest_cases = if(nrow(arrest_cases) > 0) list(shap_a1, shap_a2, shap_a3) else NULL,
      no_arrest_cases = if(nrow(no_arrest_cases) > 0) list(shap_na1, shap_na2, shap_na3) else NULL
    )
    saveRDS(shap_results, "shap_values.rds")
    cat("SHAP values saved to 'shap_values.rds'\n")
  }
  
  # --- 9. PARTIAL DEPENDENCE PLOTS (Task 4c) ---
  cat("Creating Partial Dependence Plots...\n")

  if (require(pdp, quietly = TRUE)) {
    # Create PDP for key variables
    pdp_weapon <- partial(rf_model, pred.var = "weapon_name", train = rf_data)
    pdp_crime <- partial(rf_model, pred.var = "crime_against", train = rf_data)
    pdp_hour <- partial(rf_model, pred.var = "incident_hour", train = rf_data)
    
    # Create and save partial dependence plots using autoplot
    p3 <- autoplot(pdp_weapon) + 
      labs(title = "Partial Dependence Plot: Weapon Name",
           x = "Weapon Name", 
           y = "Partial Dependence") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1))
    ggsave("pdp_weapon_name.png", p3, width = 12, height = 8, dpi = 300)
    cat("Saved: pdp_weapon_name.png\n")
    
    p4 <- autoplot(pdp_crime) + 
      labs(title = "Partial Dependence Plot: Crime Against",
           x = "Crime Against", 
           y = "Partial Dependence") +
      theme_minimal()
    ggsave("pdp_crime_against.png", p4, width = 10, height = 6, dpi = 300)
    cat("Saved: pdp_crime_against.png\n")
    
    p5 <- autoplot(pdp_hour) + 
      labs(title = "Partial Dependence Plot: Incident Hour",
           x = "Incident Hour", 
           y = "Partial Dependence") +
      theme_minimal()
    ggsave("pdp_incident_hour.png", p5, width = 10, height = 6, dpi = 300)
    cat("Saved: pdp_incident_hour.png\n")
    
    # Save PDP results
    saveRDS(list(weapon = pdp_weapon, crime = pdp_crime, hour = pdp_hour), "pdp_results.rds")
    cat("Partial Dependence Plots saved to 'pdp_results.rds'\n")
  }
}

# --- 10. MODEL COMPARISON ---
cat("Model Comparison Summary:\n")

# Collect performance metrics
models_performance <- data.frame(
  Model = c("GLM", "GLMM", "Random Forest"),
  Accuracy = c(
    if(exists("glm_confusion")) glm_confusion$overall["Accuracy"] else NA,
    if(exists("glmm_confusion")) glmm_confusion$overall["Accuracy"] else NA,
    if(exists("rf_confusion")) rf_confusion$overall["Accuracy"] else NA
  ),
  Sensitivity = c(
    if(exists("glm_confusion")) glm_confusion$byClass["Sensitivity"] else NA,
    if(exists("glmm_confusion")) glmm_confusion$byClass["Sensitivity"] else NA,
    if(exists("rf_confusion")) rf_confusion$byClass["Sensitivity"] else NA
  ),
  Specificity = c(
    if(exists("glm_confusion")) glm_confusion$byClass["Specificity"] else NA,
    if(exists("glmm_confusion")) glmm_confusion$byClass["Specificity"] else NA,
    if(exists("rf_confusion")) rf_confusion$byClass["Specificity"] else NA
  ),
  AUC_ROC = c(
    if(exists("glm_auc")) glm_auc else NA,
    if(exists("glmm_auc")) glmm_auc else NA,
    if(exists("rf_auc")) rf_auc else NA
  ),
  F1_Score = c(
    if(exists("glm_f1")) glm_f1 else NA,
    if(exists("glmm_f1")) glmm_f1 else NA,
    if(exists("rf_f1")) rf_f1 else NA
  )
)

print(models_performance)

# Save model comparison
write.csv(models_performance, "model_comparison.csv", row.names = FALSE)
cat("Model comparison saved to 'model_comparison.csv'\n")

# --- 11. PERFORMANCE METRICS JUSTIFICATION ---
cat("\n=== PERFORMANCE METRICS JUSTIFICATION ===\n")
cat("For this imbalanced dataset (19% arrests, 81% non-arrests), we use:\n")
cat("1. AUC-ROC: Measures the model's ability to distinguish between classes regardless of threshold\n")
cat("2. F1-Score: Balances precision and recall, crucial for imbalanced datasets\n")
cat("These metrics are more appropriate than accuracy alone for imbalanced classification problems.\n")

# --- 11. BUSINESS INSIGHTS ---
cat("\n=== BUSINESS INSIGHTS ===\n")

# Key factors affecting arrest probability
if (exists("glm_model")) {
  coef_summary <- summary(glm_model)$coefficients
  significant_coefs <- coef_summary[coef_summary[,4] < 0.05, ]
  
  cat("Significant factors affecting arrest probability (p < 0.05):\n")
  print(significant_coefs)
}

# --- 12. BAYESIAN ANALYSIS (Task 5) ---
cat("Creating Bayesian analysis...\n")

# Create data summary for Bayesian analysis
arrest_summary <- crime_data %>%
  group_by(offense_category_name) %>%
  summarize(
    N_incidents = n(),
    N_arrests = sum(as.numeric(as.character(ARREST)), na.rm = TRUE)
  ) %>%
  filter(N_incidents > 50) %>% # Filter for stability
  arrange(desc(N_incidents))

# Bayesian Model (Conjugate Beta-Binomial)
alpha_prior <- 2
beta_prior <- 8

bayesian_results <- arrest_summary %>%
  mutate(
    alpha_posterior = alpha_prior + N_arrests,
    beta_posterior = beta_prior + N_incidents - N_arrests,
    posterior_mean = round(alpha_posterior / (alpha_posterior + beta_posterior), 4),
    lower_95_ci = round(qbeta(0.025, alpha_posterior, beta_posterior), 4),
    upper_95_ci = round(qbeta(0.975, alpha_posterior, beta_posterior), 4),
    observed_rate = round(N_arrests / N_incidents, 4)
  ) %>%
  select(offense_category_name, N_incidents, N_arrests, observed_rate, 
         posterior_mean, lower_95_ci, upper_95_ci)

# Display and save Bayesian results
if (require(knitr, quietly = TRUE)) {
  bayesian_table <- kable(bayesian_results, 
                         col.names = c("Offense Category", "N Incidents", "N Arrests", 
                                      "Observed Rate", "Posterior Mean", "Lower 95% CI", "Upper 95% CI"),
                         caption = "Bayesian Arrest Rate Analysis by Offense Category")
  cat("Bayesian Analysis Results:\n")
  print(bayesian_table)
  
  # Save Bayesian table to file
  capture.output(print(bayesian_table), file = "bayesian_analysis_table.txt")
  cat("Saved: bayesian_analysis_table.txt\n")
}

# Save Bayesian results to CSV
write.csv(bayesian_results, "bayesian_analysis_results.csv", row.names = FALSE)
cat("Saved: bayesian_analysis_results.csv\n")

# Save final results
saveRDS(list(
  glm_model = if(exists("glm_model")) glm_model else NULL,
  rf_model = if(exists("rf_model")) rf_model else NULL,
  performance = models_performance,
  data_summary = list(
    total_incidents = nrow(crime_data),
    arrest_rate = mean(crime_data$ARREST, na.rm = TRUE),
    training_size = nrow(train_set),
    testing_size = nrow(test_set)
  )
), "atpa_analysis_results.rds")

cat("\n=== ANALYSIS COMPLETED ===\n")
cat("All results saved to 'atpa_analysis_results.rds'\n")
cat("Prepared dataset: 'crime_data_prepared.csv'\n")
cat("Model comparison: 'model_comparison.csv'\n") 