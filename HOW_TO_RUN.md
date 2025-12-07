# How to Run Exercise 2: Data Processing

## Fixed Errors
1. **Corrupted docstring** - Fixed malformed header with mixed code
2. **Duplicate code blocks** - Removed redundant file saving operations
3. **Missing exception handler** - Added proper except block for the final try statement
4. **Incomplete report** - Enhanced report with full data analysis summary
5. **Wrong HDFS API methods** - Fixed `mkdir()` → `makedirs()` and `open()` → `write()`

## Prerequisites
- Docker and Docker Compose installed
- Hadoop cluster must be running
- Exercise 1 must be completed first (to create employees.csv file)

## Quick Start

### 1. Start Hadoop Cluster
```bash
cd "/Users/dauvanmuoi/Downloads/D9 - Hadoop Introduction"
./setup.sh
```

### 2. Verify Cluster is Running
```bash
docker-compose ps
```
All services should show "Up" status.

### 3. Run Exercise 2
```bash
./run_exercise.sh 2
```

## Alternative: Run Directly
```bash
docker exec -it hadoop-python-client python /exercises/exercise2_data_processing.py
```

## Alternative: Interactive Mode
```bash
docker exec -it hadoop-python-client bash
python /exercises/exercise2_data_processing.py
```

## What the Exercise Does
1. **Reads CSV data** from HDFS (`/exercises/exercise1/employees.csv`)
2. **Calculates statistics** - mean, median, min, max for salary and age
3. **Filters data** - high salary employees (>$75K) and young employees (<30)
4. **Groups data** - salary by city and employees by age groups
5. **Saves results** to HDFS in multiple formats:
   - `high_salary_employees.csv` - Filtered employee data
   - `city_analysis.json` - City-wise salary analysis
   - `analysis_report.txt` - Comprehensive text report

## Expected Output Location
All results saved to: `/exercises/exercise2/` in HDFS

## View Results in HDFS
```bash
docker exec hadoop-namenode hdfs dfs -ls /exercises/exercise2/
docker exec hadoop-namenode hdfs dfs -cat /exercises/exercise2/analysis_report.txt
```

## Access HDFS Web UI
Open browser: http://localhost:9870

## Troubleshooting

### Error: "No such file or directory: employees.csv"
Run Exercise 1 first:
```bash
./run_exercise.sh 1
```

### Error: "Connection refused"
Restart Hadoop cluster:
```bash
docker-compose restart
```

### Error: "Directory already exists"
Normal if running multiple times - the script handles this.

## Cleanup
```bash
./cleanup.sh
```

## Summary of Code Changes
- Fixed corrupted header (lines 3-5)
- Removed duplicate save operations (removed 30 duplicate lines)
- Added missing exception handler for report generation
- Enhanced report with complete data summary
- **CRITICAL FIX**: Changed HDFS API calls:
  - `hdfs.mkdir()` → `hdfs.makedirs()`
  - `hdfs.open(path, 'wt')` → `hdfs.write(path, encoding='utf-8')`
  - `json.dump(dict, f)` → `json.dumps(dict)` then write as string

## Error Details
The original error was:
```
AttributeError: 'InsecureClient' object has no attribute 'mkdir'
AttributeError: 'InsecureClient' object has no attribute 'open'
```

This happened because the hdfs.InsecureClient library uses different method names than the original code assumed.
- Improved error messages

