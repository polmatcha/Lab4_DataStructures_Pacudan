# Student-specific inputs
LAST_NAME = "Pacudan"
STUDENT_ID = "TUPM-26-1859"
FAVORITE_ARTIST = "The 1975"
SEED_NUM = int(STUDENT_ID[-1])  # 9

# Use alphabet positions from the artist's letters (A=1, ..., Z=26).
ARTIST_POSITIONS = [
    ord(char.upper()) - ord("A") + 1
    for char in FAVORITE_ARTIST
    if char.isalpha()
]

from collections import Counter, defaultdict

SUBJECTS = ["COMPUTER PROGRAMMING", "DIFFERENTIAL CALCULUS", "CHEMISTRY FOR ENGINEERS", "ETHICS", "PATHFIT"]
STUDENTS = [f"{LAST_NAME}-S{i}" for i in range(1, 6)]

records = []
for student_index, student in enumerate(STUDENTS):
    for subject_index, subject in enumerate(SUBJECTS):
        letter_value = ARTIST_POSITIONS[(student_index + subject_index) % len(ARTIST_POSITIONS)]
        score = 50 + (
            SEED_NUM * 7 + letter_value * 3 + student_index * 11 + subject_index * 7
        ) % 51
        records.append({
            "student": student,
            "subject": subject,
            "score": score
        })

# Required duplicate student-subject record.
records.append(records[0].copy())

# Required incomplete record (score is missing).
records.append({
    "student": STUDENTS[1],
    "subject": "ELECTRONICS",
    "score": None
})

def performance_category(score):
    if score is None:
        return "INCOMPLETE"
    if score >= 90:
        return "EXCELLENT"
    if score >= 80:
        return "VERY GOOD"
    if score >= 75:
        return "PASSED"
    return "NEEDS IMPROVEMENT"

print("=== APPENDIX 2: STUDENT PERFORMANCE DATA ANALYZER ===")
print("\n1. GENERATED PERFORMANCE RECORDS")
for record in records:
    print({**record, "category": performance_category(record["score"])})

organized = defaultdict(list)
for record in records:
    organized[(record["student"], record["subject"])].append(record["score"])

print("\n2. ORGANIZED STUDENT / SUBJECT DATA")
for key, scores in sorted(organized.items()):
    print(f"{key[0]} | {key[1]}: {scores}")

key_counts = Counter((r["student"], r["subject"], r["score"]) for r in records)
repeated = {key: count for key, count in key_counts.items() if count > 1}
incomplete = [r for r in records if r["score"] is None]
valid_records = [r for r in records if r["score"] is not None]

print("\n3. REPEATED AND INCOMPLETE RECORDS")
print(f"Repeated records: {repeated}")
print(f"Incomplete records: {incomplete}")

print("\n4. PERFORMANCE CATEGORIES")
category_counts = Counter(performance_category(r["score"]) for r in records)
for category, count in sorted(category_counts.items()):
    print(f"{category}: {count}")

print("\n5. STUDENT SUMMARIES")
for student in STUDENTS:
    scores = [r["score"] for r in valid_records if r["student"] == student]
    print(f"{student}: valid scores={len(scores)}, average={sum(scores)/len(scores):.2f}, "
          f"highest={max(scores)}, lowest={min(scores)}")

print("\n6. SUBJECT SUMMARIES")
for subject in SUBJECTS:
    scores = [r["score"] for r in valid_records if r["subject"] == subject]
    print(f"{subject}: valid scores={len(scores)}, average={sum(scores)/len(scores):.2f}")

print("\n7. ORDERED RESULTS (STUDENT, SUBJECT)")
for record in sorted(records, key=lambda r: (r["student"], r["subject"])):
    print({**record, "category": performance_category(record["score"])})

valid_scores = [r["score"] for r in valid_records]
print("\n8. FINAL PERFORMANCE REPORT")
print(f"Total records: {len(records)}")
print(f"Valid scores: {len(valid_scores)}")
print(f"Incomplete records: {len(incomplete)}")
print(f"Repeated record keys: {len(repeated)}")
print(f"Overall average: {sum(valid_scores)/len(valid_scores):.2f}")
print(f"Highest score: {max(valid_scores)}")
print(f"Lowest score: {min(valid_scores)}")
