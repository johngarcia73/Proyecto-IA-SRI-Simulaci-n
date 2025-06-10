import numpy as np

class ScoreNormalizer:
    def minmax_scale(self, scores):
        """Normalización Min-Max [0,1]"""
        if not scores:
            return scores
            
        min_val = min(scores)
        max_val = max(scores)
        
        if max_val - min_val < 1e-6:  # Evitar división por cero
            return [0.5] * len(scores)
            
        return [(s - min_val) / (max_val - min_val) for s in scores]
    
    def robust_scale(self, scores):
        """Escalado robusto usando IQR (menos sensible a outliers)"""
        if len(scores) < 4:
            return self.minmax_scale(scores)
            
        q75, q25 = np.percentile(scores, [75, 25])
        iqr = q75 - q25
        
        if iqr < 1e-6:
            return self.minmax_scale(scores)
            
        median = np.median(scores)
        return [(s - median) / iqr for s in scores]
    
    def softmax(self, scores):
        """Transformación Softmax para distribución de probabilidad"""
        exp_scores = np.exp(scores - np.max(scores))
        return list(exp_scores / exp_scores.sum())