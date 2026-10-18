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

CATEGORIES = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]
SOURCES = [f"{LAST_NAME}-T{i}" for i in range(1, 6)]

# Generate individualized records from the seed and artist-letter positions.
records = []
for i in range(10):
    source = SOURCES[i % len(SOURCES)]
    category = CATEGORIES[i % len(CATEGORIES)]
    letter_value = ARTIST_POSITIONS[i % len(ARTIST_POSITIONS)]
    value = SEED_NUM * 3 + letter_value + (i * 2)
    records.append({
        "source": source,
        "category": category,
        "value": value
    })

# Include a repeated source/category record, as required by the appendix.
records.append(records[0].copy())

# Include additional measurements under multiple categories.
records.extend([
    {"source": SOURCES[0], "category": "VOLTAGE",
     "value": SEED_NUM * 4 + ARTIST_POSITIONS[1]},
    {"source": SOURCES[2], "category": "TEMPERATURE",
     "value": SEED_NUM * 5 + ARTIST_POSITIONS[2]},
])

print("=== APPENDIX 1: ENGINEERING TEST DATA ORGANIZER ===")
print("\n1. GENERATED TEST DATA")
for record in records:
    print(record)

organized = defaultdict(list)
for record in records:
    organized[(record["source"], record["category"])].append(record["value"])

print("\n2. ORGANIZED DATA (SOURCE / CATEGORY)")
for (source, category), values in sorted(organized.items()):
    print(f"{source} | {category}: {values}")

record_keys = [(r["source"], r["category"], r["value"]) for r in records]
counts = Counter(record_keys)
repeated = {key: count for key, count in counts.items() if count > 1}
distinct_records = sorted(set(record_keys))

print("\n3. REPEATED DATA")
print(repeated if repeated else "No repeated records found")
print(f"Distinct records: {len(distinct_records)}")
print(f"Total records: {len(records)}")

values = [record["value"] for record in records]
print("\n4. NUMERICAL SUMMARY")
print(f"Count: {len(values)}")
print(f"Minimum: {min(values)}")
print(f"Maximum: {max(values)}")
print(f"Average: {sum(values) / len(values):.2f}")

print("\n5. CATEGORICAL SUMMARY")
category_counts = Counter(record["category"] for record in records)
for category, count in sorted(category_counts.items()):
    print(f"{category}: {count} record(s)")

print("\n6. PROCESSED RESULTS (SORTED BY SOURCE, CATEGORY, VALUE)")
for record in sorted(records, key=lambda r: (r["source"], r["category"], r["value"])):
    print(record)

print("\n7. FINAL SUMMARY")
print(f"Test sources: {len(set(r['source'] for r in records))}")
print(f"Measurement categories: {len(set(r['category'] for r in records))}")
print(f"Total measurement records: {len(records)}")
print(f"Distinct records: {len(distinct_records)}")
print(f"Repeated record keys: {len(repeated)}")



# FINAL OUTPUT: FINAL ORGANIZED AND SUMMARIZED TEST DATASET

from collections import defaultdict

final_dataset = defaultdict(list)

# 1. Organize measurements by test source and category
for record in records:
    key = (record["source"], record["category"])
    final_dataset[key].append(record["value"])

# 2. Display the consolidated dataset with summaries
print("\n" + "=" * 65)
print("FINAL ORGANIZED AND SUMMARIZED TEST DATASET")
print("=" * 65)

for (source, category), measurements in sorted(final_dataset.items()):
    total = sum(measurements)
    count = len(measurements)
    average = total / count

    print(f"\nTest Source: {source}")
    print(f"Category: {category}")
    print(f"Measurements: {measurements}")
    print(f"Number of Measurements: {count}")
    print(f"Total: {total}")
    print(f"Minimum: {min(measurements)}")
    print(f"Maximum: {max(measurements)}")
    print(f"Average: {average:.2f}")

# 3. Overall dataset summary
all_values = [
    value
    for measurements in final_dataset.values()
    for value in measurements
]

print("\n" + "=" * 65)
print("OVERALL DATASET SUMMARY")
print("=" * 65)
print(f"Total Test Sources: {len(set(r['source'] for r in records))}")
print(f"Total Categories: {len(set(r['category'] for r in records))}")
print(f"Total Measurement Records: {len(records)}")
print(f"Distinct Source-Category Groups: {len(final_dataset)}")
print(f"Overall Minimum: {min(all_values)}")
print(f"Overall Maximum: {max(all_values)}")
print(f"Overall Average: {sum(all_values) / len(all_values):.2f}")
print(f"Overall Total: {sum(all_values)}")
print("=" * 65)