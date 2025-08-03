
# EXECUTIVE SUMMARY
## Crime Analysis for New Mexico Policy Decisions
### NMInsights Research Institute
---

## STATEMENT OF THE BUSINESS PROBLEM

NMInsights commissioned this analysis to understand patterns in criminal incidents that lead to arrests across New Mexico. The state consistently ranks among the highest in the U.S. for violent and property crime rates, making evidence-based policy recommendations critical for public safety improvements.

**Primary Research Questions:**
1. What characteristics of criminal incidents are most associated with arrests?
2. Which categories of criminal offenses are more likely to result in arrests?

This analysis examined 96,904 criminal incidents from 2023, of which 18,439 (19%) resulted in arrests - providing a realistic foundation for policy recommendations.

---

## KEY FINDINGS

### **1. Arrest Patterns Show Significant Variation by Crime Type**

Our Bayesian analysis revealed substantial differences in arrest rates across 24 crime categories:

**Highest Arrest Rates:**
- Drug/Narcotic Offenses: 57% arrest rate (5,149 incidents)
- Stolen Property Offenses: 47% arrest rate (707 incidents)  
- Assault Offenses: 41% arrest rate (23,550 incidents)

**Lowest Arrest Rates:**
- Motor Vehicle Theft: 3% arrest rate (7,482 incidents)
- Fraud Offenses: 2% arrest rate (6,104 incidents)
- Larceny/Theft: 10% arrest rate (27,614 incidents)

**Policy Insight:** The three most common crime types (Larceny, Assault, Property Damage) account for 66% of all incidents but show vastly different arrest patterns, suggesting opportunities for targeted intervention strategies.

### **2. Predictive Model Identifies Key Factors Influencing Arrests**

Our Random Forest model achieved 77% accuracy in predicting arrest outcomes, identifying the most important factors:

**Top Predictive Factors:**
1. **Offense Code** (25% importance): Specific crime type is the strongest predictor
2. **Court Case Flag** (24% importance): Cases with legal proceedings show higher arrest likelihood
3. **Offense Category** (21% importance): Broader crime classification matters significantly
4. **Law Enforcement Agency** (15% importance): Jurisdictional differences affect arrest patterns

**Policy Insight:** The model's strong performance (AUC = 0.86) demonstrates that arrest patterns are predictable, enabling proactive resource allocation and policy interventions.

### **3. Ethical Considerations Require Careful Implementation**

Our analysis identified potential bias risks that must be addressed:

**Identified Concerns:**
- Geographic disparities across law enforcement agencies
- Potential demographic impacts requiring fairness monitoring
- Data quality variations that could affect model reliability

**Recommended Safeguards:**
- Independent oversight board with community representation
- Regular bias audits across demographic and geographic groups
- Transparent reporting of model limitations and uncertainties

---

## RECOMMENDATIONS

### **Immediate Actions (0-3 months):**

1. **Focus Resources on High-Volume, Low-Arrest Categories**
   - Prioritize Larceny/Theft (27,614 incidents, 10% arrest rate)
   - Implement targeted Motor Vehicle Theft prevention (7,482 incidents, 3% arrest rate)
   - Develop specialized Fraud investigation units (6,104 incidents, 2% arrest rate)

2. **Standardize Arrest Documentation**
   - Implement consistent data collection across all 89 law enforcement agencies
   - Establish quality control measures for incident reporting
   - Create training programs for data accuracy improvement

### **Short-term Initiatives (3-12 months):**

1. **Deploy Predictive Analytics Pilot Program**
   - Begin with 3-5 law enforcement agencies showing highest data quality
   - Focus on resource allocation for Drug/Narcotic and Assault cases
   - Implement human oversight for all model-generated recommendations

2. **Establish Fairness Monitoring System**
   - Create automated bias detection for demographic and geographic groups
   - Develop community feedback mechanisms
   - Publish quarterly fairness and performance reports

### **Long-term Strategic Goals (1-3 years):**

1. **Statewide Implementation**
   - Scale successful pilot programs across all New Mexico jurisdictions
   - Integrate predictive analytics into daily law enforcement operations
   - Establish New Mexico as a model for evidence-based policing

2. **Policy Impact Measurement**
   - Track changes in arrest patterns following intervention implementation
   - Measure community trust and safety outcomes
   - Conduct independent evaluation of program effectiveness

---

## LIMITATIONS

**Data Limitations:**
- Analysis limited to 2023 data; long-term trends require multi-year analysis
- Missing data in some categories (up to 25% for certain variables)
- Potential reporting inconsistencies across 89 different law enforcement agencies

**Model Limitations:**
- Predictive accuracy of 77% means 23% of cases may be misclassified
- Model reflects historical patterns that may not represent future relationships
- Cannot capture all contextual factors influencing arrest decisions

**Implementation Considerations:**
- Model requires ongoing monitoring and retraining as crime patterns evolve
- Results should supplement, not replace, experienced law enforcement judgment
- Community engagement essential for successful policy implementation

**Ethical Constraints:**
- Model outputs must be regularly audited for bias and fairness
- Demographic variables require careful handling to prevent discrimination
- Privacy protection measures necessary for all data usage

---

## CONCLUSION

This analysis provides NMInsights with robust, evidence-based insights into New Mexico's crime and arrest patterns. The identification of significant variations in arrest rates across crime categories (from 2% to 57%) presents clear opportunities for targeted policy interventions.

The predictive model's strong performance (77% accuracy, 0.86 AUC) demonstrates that data-driven approaches can effectively support law enforcement resource allocation. However, successful implementation requires careful attention to ethical considerations, community engagement, and ongoing monitoring for bias and effectiveness.

**Success Metrics for Implementation:**
- Increase overall arrest rate from 19% to 25% within 2 years
- Reduce disparities in arrest rates across jurisdictions by 30%
- Maintain community trust scores above 75% in all pilot areas
- Achieve 90% data quality standards across all participating agencies

NMInsights is positioned to lead evidence-based criminal justice reform in New Mexico, providing policymakers with the tools needed to make informed decisions that enhance public safety while maintaining community trust and constitutional protections.

---

*This analysis was conducted following ASOP 41 Actuarial Communications standards and ATPA Module 1 ethical guidelines. All model limitations, assumptions, and uncertainties have been disclosed. Independent peer review is recommended before policy implementation.*

**Report prepared by:** ATPA Candidate  
**Date:** August 2025  
**For:** NMInsights Management Team  
