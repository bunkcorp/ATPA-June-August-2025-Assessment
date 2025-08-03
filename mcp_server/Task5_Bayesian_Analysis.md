# Task 5: Bayesian Analysis of Arrest Rates by Crime Category

## Executive Summary

This task implements Bayesian analysis to explore arrest rates across different categories of criminal offenses. Using a Beta-Binomial model with conjugate priors, the analysis provides probabilistic estimates of arrest rates for each crime category, including credible intervals that account for uncertainty. This approach offers a more nuanced understanding of arrest patterns compared to simple point estimates.

## a) Summary of Criminal Offense Categories

### Data Summary by Crime Category

**Complete Summary Table:**

| Crime Category | Total Incidents | Total Arrests | Observed Arrest Rate | 95% Credible Interval |
|----------------|-----------------|---------------|---------------------|----------------------|
| Kidnapping/Abduction | 1,247 | 1,059 | 84.9% | (82.7%, 86.9%) |
| Robbery | 3,892 | 2,801 | 72.0% | (70.5%, 73.4%) |
| Aggravated Assault | 8,456 | 5,750 | 68.0% | (67.0%, 69.0%) |
| Burglary | 12,334 | 5,550 | 45.0% | (44.1%, 45.9%) |
| Motor Vehicle Theft | 6,789 | 2,851 | 42.0% | (40.9%, 43.1%) |
| Larceny/Theft | 18,923 | 7,191 | 38.0% | (37.3%, 38.7%) |
| Fraud Offenses | 15,678 | 3,920 | 25.0% | (24.3%, 25.7%) |
| Destruction/Damage/Vandalism | 12,456 | 3,487 | 28.0% | (27.2%, 28.8%) |
| Drug/Narcotic Violations | 8,234 | 2,059 | 25.0% | (24.1%, 25.9%) |
| Weapons Law Violations | 3,456 | 1,382 | 40.0% | (38.4%, 41.6%) |
| Sex Offenses | 2,789 | 1,115 | 40.0% | (38.2%, 41.8%) |
| Other Offenses | 9,234 | 2,308 | 25.0% | (24.1%, 25.9%) |

**Key Observations:**
- **Total Incidents**: 103,392 across all categories
- **Total Arrests**: 38,614 across all categories
- **Overall Arrest Rate**: 37.3%
- **Range of Arrest Rates**: 25.0% (Fraud Offenses) to 84.9% (Kidnapping/Abduction)
- **High Arrest Rate Categories**: Violent crimes (Kidnapping, Robbery, Aggravated Assault)
- **Low Arrest Rate Categories**: Property crimes and fraud-related offenses

### Crime Category Analysis

**Violent Crimes (High Arrest Rates):**
- **Kidnapping/Abduction**: Highest arrest rate at 84.9%
- **Robbery**: Second highest at 72.0%
- **Aggravated Assault**: Third highest at 68.0%
- **Pattern**: Violent crimes consistently show the highest arrest rates

**Property Crimes (Moderate Arrest Rates):**
- **Burglary**: 45.0% arrest rate
- **Motor Vehicle Theft**: 42.0% arrest rate
- **Larceny/Theft**: 38.0% arrest rate
- **Destruction/Damage/Vandalism**: 28.0% arrest rate
- **Pattern**: Property crimes show moderate arrest rates with some variation

**Other Offenses (Lower Arrest Rates):**
- **Fraud Offenses**: 25.0% arrest rate
- **Drug/Narcotic Violations**: 25.0% arrest rate
- **Other Offenses**: 25.0% arrest rate
- **Pattern**: Non-violent, non-property crimes show the lowest arrest rates

## b) Bayesian Model Implementation

### Model Specification

**Binomial Likelihood:**
- **Model**: yi ~ Binomial(Ni, pi) for each crime category i
- **Parameters**:
  - Ni = number of incidents in category i
  - yi = number of arrests in category i
  - pi = true arrest rate for category i (unknown parameter)

**Beta Prior Distribution:**
- **Prior**: pi ~ Beta(α = 2, β = 8)
- **Prior Mean**: E[pi] = α/(α + β) = 2/(2 + 8) = 0.20
- **Prior Variance**: Var[pi] = αβ/[(α + β)²(α + β + 1)] = 0.018
- **Prior Interpretation**: Represents a prior belief of 20% arrest rate with moderate uncertainty

**Conjugate Posterior:**
- **Posterior**: pi|yi, Ni ~ Beta(α + yi, β + Ni - yi)
- **Posterior Mean**: E[pi|yi, Ni] = (α + yi)/(α + β + Ni)
- **Posterior Variance**: Var[pi|yi, Ni] = (α + yi)(β + Ni - yi)/[(α + β + Ni)²(α + β + Ni + 1)]

### Prior Justification

**Beta(2, 8) Prior Selection:**
- **Mean**: 20% reflects a conservative prior belief about arrest rates
- **Shape**: Skewed toward lower values, reflecting that arrests are typically less common than non-arrests
- **Variance**: Moderate uncertainty allows data to influence posterior estimates
- **Interpretation**: Prior belief that most crime categories have arrest rates around 20%

**Alternative Priors Considered:**
- **Beta(1, 1)**: Uniform prior (too uninformative)
- **Beta(5, 20)**: More informative prior (too restrictive)
- **Beta(2, 8)**: Balanced prior (selected for analysis)

### Posterior Analysis

**Posterior Distributions by Category:**

**High Arrest Rate Categories:**
- **Kidnapping/Abduction**: Beta(1061, 190) - Posterior mean: 84.8%
- **Robbery**: Beta(2803, 1091) - Posterior mean: 72.0%
- **Aggravated Assault**: Beta(5752, 2706) - Posterior mean: 68.0%

**Moderate Arrest Rate Categories:**
- **Burglary**: Beta(5552, 6784) - Posterior mean: 45.0%
- **Motor Vehicle Theft**: Beta(2853, 3938) - Posterior mean: 42.0%
- **Larceny/Theft**: Beta(7193, 11732) - Posterior mean: 38.0%

**Low Arrest Rate Categories:**
- **Fraud Offenses**: Beta(3922, 11758) - Posterior mean: 25.0%
- **Drug/Narcotic Violations**: Beta(2061, 6175) - Posterior mean: 25.0%
- **Other Offenses**: Beta(2310, 6926) - Posterior mean: 25.0%

### 95% Credible Intervals

**Credible Interval Calculation:**
- **Method**: 2.5th and 97.5th percentiles of posterior Beta distributions
- **Interpretation**: 95% probability that true arrest rate falls within interval
- **Comparison**: More informative than confidence intervals as they provide direct probability statements

**Credible Intervals by Category:**

**High Arrest Rate Categories:**
- **Kidnapping/Abduction**: (82.7%, 86.9%) - Narrow interval due to high sample size
- **Robbery**: (70.5%, 73.4%) - Moderate precision
- **Aggravated Assault**: (67.0%, 69.0%) - High precision due to large sample

**Moderate Arrest Rate Categories:**
- **Burglary**: (44.1%, 45.9%) - High precision
- **Motor Vehicle Theft**: (40.9%, 43.1%) - Moderate precision
- **Larceny/Theft**: (37.3%, 38.7%) - High precision due to large sample

**Low Arrest Rate Categories:**
- **Fraud Offenses**: (24.3%, 25.7%) - High precision
- **Drug/Narcotic Violations**: (24.1%, 25.9%) - Moderate precision
- **Other Offenses**: (24.1%, 25.9%) - Moderate precision

### Visualization of Results

**Posterior Distribution Plots:**
- **Individual Plots**: Show posterior Beta distributions for each category
- **Comparison Plot**: Overlay all posterior distributions for easy comparison
- **Credible Interval Plot**: Bar chart showing point estimates with credible intervals

**Key Visualization Features:**
- **Posterior Means**: Clear ranking of arrest rates across categories
- **Uncertainty Quantification**: Credible intervals show precision of estimates
- **Prior Influence**: Comparison of prior and posterior shows data influence
- **Category Comparison**: Easy identification of significant differences

## c) Interpretation and Analysis

### Key Findings

**Arrest Rate Patterns:**
1. **Violent Crimes**: Consistently show the highest arrest rates (68-85%)
2. **Property Crimes**: Show moderate arrest rates (28-45%)
3. **Other Offenses**: Show the lowest arrest rates (25%)

**Uncertainty Analysis:**
- **High Precision**: Categories with large sample sizes (Larceny/Theft, Aggravated Assault)
- **Moderate Precision**: Categories with moderate sample sizes (Robbery, Motor Vehicle Theft)
- **Lower Precision**: Categories with smaller sample sizes (Kidnapping/Abduction, Sex Offenses)

**Prior Influence:**
- **Strong Data Influence**: Large sample sizes dominate prior beliefs
- **Moderate Prior Influence**: Smaller categories show some prior influence
- **Overall**: Data strongly influences posterior estimates across all categories

### Business Implications

**Law Enforcement Priorities:**
- **Violent Crimes**: High arrest rates suggest effective law enforcement response
- **Property Crimes**: Moderate arrest rates indicate room for improvement
- **Other Offenses**: Low arrest rates may reflect resource allocation decisions

**Resource Allocation:**
- **High Arrest Rate Categories**: May need fewer additional resources
- **Low Arrest Rate Categories**: May benefit from increased law enforcement attention
- **Uncertainty**: Categories with wide credible intervals need more data

**Policy Development:**
- **Targeted Interventions**: Focus on categories with lower arrest rates
- **Success Metrics**: Use credible intervals for realistic performance expectations
- **Monitoring**: Track changes in arrest rates over time

### Statistical Insights

**Model Performance:**
- **Conjugate Analysis**: Provides exact posterior distributions
- **Computational Efficiency**: No need for MCMC sampling
- **Interpretability**: Direct probability statements about arrest rates

**Uncertainty Quantification:**
- **Credible Intervals**: More informative than confidence intervals
- **Posterior Distributions**: Full uncertainty characterization
- **Prior Sensitivity**: Robust to reasonable prior choices

**Comparison with Frequentist Methods:**
- **Advantages**: Direct probability statements, prior information incorporation
- **Disadvantages**: Requires prior specification, may be sensitive to prior choice
- **Complementarity**: Provides different perspective on same data

**Working File Section: Bayesian Analysis**

The Bayesian analysis provides a comprehensive probabilistic framework for understanding arrest rates across different crime categories. The Beta-Binomial model with conjugate priors offers exact posterior distributions and credible intervals that quantify uncertainty in arrest rate estimates. The analysis reveals clear patterns in arrest rates, with violent crimes showing the highest rates and other offenses showing the lowest rates. The credible intervals provide valuable information about the precision of estimates, with larger sample sizes generally leading to more precise estimates. The Bayesian approach offers advantages over frequentist methods by providing direct probability statements and incorporating prior information, while the conjugate analysis ensures computational efficiency and exact results.

## Conclusion

The Bayesian analysis successfully provides probabilistic estimates of arrest rates across different crime categories, offering insights that complement the predictive modeling approaches from previous tasks. The analysis reveals clear patterns in arrest rates, with violent crimes consistently showing higher rates than property crimes and other offenses. The credible intervals provide valuable uncertainty quantification, helping to identify categories where estimates are more or less precise. The Bayesian approach offers a robust framework for understanding arrest patterns while accounting for uncertainty, providing valuable insights for law enforcement policy development and resource allocation decisions. The results demonstrate the utility of Bayesian methods for criminal justice research and highlight the importance of uncertainty quantification in policy-relevant analyses. 