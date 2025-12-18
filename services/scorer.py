import re
from typing import List, Tuple

class ATSScorer:
    @staticmethod
    def extract_keywords(text: str) -> List[str]:
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        words = text.split()
        
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
            'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'should', 'could', 'may', 'might', 'must', 'can', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
        }
        
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        return keywords

    @classmethod
    def score_cv(cls, cv_text: str, job_description: str) -> Tuple[float, List[str], int]:
        cv_keywords = set(cls.extract_keywords(cv_text))
        jd_keywords = set(cls.extract_keywords(job_description))
        
        if not jd_keywords:
            return 0.0, [], 0
        
        matched = cv_keywords.intersection(jd_keywords)
        score = (len(matched) / len(jd_keywords)) * 100
        
        return round(score, 2), sorted(list(matched)), len(jd_keywords)