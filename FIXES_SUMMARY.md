# Exercise 2 - Error Fixes Summary

## Error Found in Terminal Output

```
AttributeError: 'InsecureClient' object has no attribute 'mkdir'
AttributeError: 'InsecureClient' object has no attribute 'open'
```

## Root Cause
The code was using incorrect HDFS API method names that don't exist in the `hdfs.InsecureClient` library.

## Fixes Applied

### 1. Wrong API Method Names
**BEFORE (Incorrect):**
```python
hdfs.mkdir('/exercises/exercise2/')
with hdfs.open('/exercises/exercise2/file.csv', 'wt') as f:
    f.write(content)
```

**AFTER (Correct):**
```python
hdfs.makedirs('/exercises/exercise2/')
with hdfs.write('/exercises/exercise2/file.csv', encoding='utf-8') as writer:
    writer.write(content)
```

### 2. JSON Handling
**BEFORE (Incorrect):**
```python
city_json = city_analysis.to_dict()
with hdfs.open('/path/file.json', 'wt') as f:
    json.dump(city_json, f, indent=2)
```

**AFTER (Correct):**
```python
city_json = json.dumps(city_analysis.to_dict(), indent=2)
with hdfs.write('/path/file.json', encoding='utf-8') as writer:
    writer.write(city_json)
```

## Correct HDFS API Reference

| Operation | Correct Method | Wrong Method |
|-----------|---------------|--------------|
| Create directory | `hdfs.makedirs(path)` | `hdfs.mkdir(path)` ❌ |
| Write file | `hdfs.write(path, encoding='utf-8')` | `hdfs.open(path, 'wt')` ❌ |
| Read file | `hdfs.read(path, encoding='utf-8')` | ✅ Already correct |
| Upload file | `hdfs.upload(hdfs_path, local_path)` | ✅ Already correct |
| List directory | `hdfs.list(path, status=True)` | ✅ Already correct |

## Test the Fix

Run the exercise again:
```bash
./run_exercise.sh 2
```

## Expected Success Output

```
Data loaded:
...
Statistical Summary:
...
Directory created: /exercises/exercise2/
File saved: /exercises/exercise2/high_salary_employees.csv
File saved: /exercises/exercise2/city_analysis.json
File saved: /exercises/exercise2/analysis_report.txt

Exercise 2 completed!
```

## Verify Results in HDFS

```bash
docker exec hadoop-namenode hdfs dfs -ls /exercises/exercise2/
docker exec hadoop-namenode hdfs dfs -cat /exercises/exercise2/analysis_report.txt
```

Or visit HDFS Web UI: http://localhost:9870

## All Fixed Issues
1. ✅ Corrupted docstring
2. ✅ Duplicate code blocks
3. ✅ Missing exception handler
4. ✅ Incomplete report content
5. ✅ **Wrong HDFS API methods** (main issue)

## Reference Files
- See `HOW_TO_RUN.md` for detailed running instructions
- See `exercise1_basic_operations.py` for correct API usage examples
- See `python-client/hdfs_demo.py` for comprehensive HDFS operations

